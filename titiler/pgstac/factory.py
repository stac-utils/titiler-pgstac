"""Custom MosaicTiler Factory for PgSTAC Mosaic Backend."""

import os
import re
import sys
from dataclasses import dataclass
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    List,
    Literal,
    Optional,
    Tuple,
    Type,
    Union,
)
from urllib.parse import urlencode

import rasterio
from cogeo_mosaic.backends import BaseBackend
from cogeo_mosaic.errors import MosaicNotFoundError
from fastapi import Body, Depends, HTTPException, Path, Query
from geojson_pydantic import Feature, FeatureCollection
from psycopg import sql
from psycopg.rows import class_row
from pydantic import conint
from rio_tiler.constants import MAX_THREADS, WGS84_CRS
from rio_tiler.mosaic.methods.base import MosaicMethodBase
from starlette.datastructures import QueryParams
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

from titiler.core.dependencies import (
    AssetsBidxExprParams,
    CoordCRSParams,
    DefaultDependency,
    HistogramParams,
    StatisticsParams,
)
from titiler.core.factory import BaseTilerFactory, img_endpoint_params
from titiler.core.models.mapbox import TileJSON
from titiler.core.models.responses import MultiBaseStatisticsGeoJSON
from titiler.core.resources.enums import ImageType, MediaType, OptionalHeader
from titiler.core.resources.responses import GeoJSONResponse, XMLResponse
from titiler.mosaic.factory import PixelSelectionParams
from titiler.pgstac import model
from titiler.pgstac.dependencies import (
    BackendParams,
    PathParams,
    PgSTACParams,
    SearchParams,
    TileParams,
)
from titiler.pgstac.mosaic import PGSTACBackend

if sys.version_info >= (3, 9):
    from typing import Annotated  # pylint: disable=no-name-in-module
else:
    from typing_extensions import Annotated


def _first_value(values: List[Any], default: Any = None):
    """Return the first not None value."""
    return next(filter(lambda x: x is not None, values), default)


@dataclass
class MosaicTilerFactory(BaseTilerFactory):
    """Custom MosaicTiler for PgSTAC Mosaic Backend."""

    reader: Type[BaseBackend] = PGSTACBackend
    path_dependency: Callable[..., str] = PathParams
    layer_dependency: Type[DefaultDependency] = AssetsBidxExprParams

    # Statistics/Histogram Dependencies
    stats_dependency: Type[DefaultDependency] = StatisticsParams
    histogram_dependency: Type[DefaultDependency] = HistogramParams

    # Search dependency
    search_dependency: Callable[
        ..., Tuple[model.PgSTACSearch, model.Metadata]
    ] = SearchParams

    pixel_selection_dependency: Callable[..., MosaicMethodBase] = PixelSelectionParams

    backend_dependency: Type[DefaultDependency] = BackendParams

    # Add/Remove some endpoints
    add_statistics: bool = False

    add_viewer: bool = False

    add_mosaic_list: bool = False

    def register_routes(self) -> None:
        """This Method register routes to the router."""
        self._search_routes()
        if self.add_mosaic_list:
            self._search_list_routes()

        # NOTE: `assets` route HAVE TO be registered before `tiles` routes
        self._assets_routes()

        self._tiles_routes()
        self._tilejson_routes()
        self._wmts_routes()

        if self.add_statistics:
            self._statistics_routes()

        if self.add_viewer:
            self._map_routes()

    def _tiles_routes(self) -> None:
        """register tiles routes."""

        @self.router.get("/{searchid}/tiles/{z}/{x}/{y}", **img_endpoint_params)
        @self.router.get(
            "/{searchid}/tiles/{z}/{x}/{y}.{format}", **img_endpoint_params
        )
        @self.router.get(
            "/{searchid}/tiles/{z}/{x}/{y}@{scale}x", **img_endpoint_params
        )
        @self.router.get(
            "/{searchid}/tiles/{z}/{x}/{y}@{scale}x.{format}", **img_endpoint_params
        )
        @self.router.get(
            "/{searchid}/tiles/{tileMatrixSetId}/{z}/{x}/{y}", **img_endpoint_params
        )
        @self.router.get(
            "/{searchid}/tiles/{tileMatrixSetId}/{z}/{x}/{y}.{format}",
            **img_endpoint_params,
        )
        @self.router.get(
            "/{searchid}/tiles/{tileMatrixSetId}/{z}/{x}/{y}@{scale}x",
            **img_endpoint_params,
        )
        @self.router.get(
            "/{searchid}/tiles/{tileMatrixSetId}/{z}/{x}/{y}@{scale}x.{format}",
            **img_endpoint_params,
        )
        def tile(
            searchid=Depends(self.path_dependency),
            tile=Depends(TileParams),
            tileMatrixSetId: Annotated[  # type: ignore
                Literal[tuple(self.supported_tms.list())],
                f"Identifier selecting one of the TileMatrixSetId supported (default: '{self.default_tms}')",
            ] = self.default_tms,
            scale: Annotated[  # type: ignore
                Optional[conint(gt=0, le=4)],
                "Tile size scale. 1=256x256, 2=512x512...",
            ] = None,
            format: Annotated[
                ImageType,
                "Default will be automatically defined if the output image needs a mask (png) or not (jpeg).",
            ] = None,
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            buffer: Annotated[
                Optional[float],
                Query(
                    gt=0,
                    title="Tile buffer.",
                    description="Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).",
                ),
            ] = None,
            post_process=Depends(self.process_dependency),
            rescale=Depends(self.rescale_dependency),
            color_formula: Annotated[
                Optional[str],
                Query(
                    title="Color Formula",
                    description="rio-color formula (info: https://github.com/mapbox/rio-color)",
                ),
            ] = None,
            colormap=Depends(self.colormap_dependency),
            render_params=Depends(self.render_dependency),
            pgstac_params: PgSTACParams = Depends(),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Create map tile."""
            threads = int(os.getenv("MOSAIC_CONCURRENCY", MAX_THREADS))

            scale = scale or 1

            strict_zoom = str(os.getenv("MOSAIC_STRICT_ZOOM", False)).lower() in [
                "true",
                "yes",
            ]

            tms = self.supported_tms.get(tileMatrixSetId)
            with rasterio.Env(**env):
                with self.reader(
                    searchid,
                    tms=tms,
                    reader_options={**reader_params},
                    **backend_params,
                ) as src_dst:

                    if strict_zoom and (
                        tile.z < src_dst.minzoom or tile.z > src_dst.maxzoom
                    ):
                        raise HTTPException(
                            400,
                            f"Invalid ZOOM level {tile.z}. Should be between {src_dst.minzoom} and {src_dst.maxzoom}",
                        )

                    image, assets = src_dst.tile(
                        tile.x,
                        tile.y,
                        tile.z,
                        tilesize=scale * 256,
                        buffer=buffer,
                        pixel_selection=pixel_selection,
                        threads=threads,
                        **layer_params,
                        **dataset_params,
                        **pgstac_params,
                    )

            if post_process:
                image = post_process(image)

            if rescale:
                image.rescale(rescale)

            if color_formula:
                image.apply_color_formula(color_formula)

            if colormap:
                image = image.apply_colormap(colormap)

            if not format:
                format = ImageType.jpeg if image.mask.all() else ImageType.png

            content = image.render(
                img_format=format.driver,
                **format.profile,
                **render_params,
            )

            headers: Dict[str, str] = {}
            if OptionalHeader.x_assets in self.optional_headers:
                ids = [x["id"] for x in assets]
                headers["X-Assets"] = ",".join(ids)

            return Response(content, media_type=format.mediatype, headers=headers)

    def _tilejson_routes(self) -> None:
        """register tiles routes."""

        @self.router.get(
            "/{searchid}/tilejson.json",
            response_model=TileJSON,
            responses={200: {"description": "Return a tilejson"}},
            response_model_exclude_none=True,
        )
        @self.router.get(
            "/{searchid}/{tileMatrixSetId}/tilejson.json",
            response_model=TileJSON,
            responses={200: {"description": "Return a tilejson"}},
            response_model_exclude_none=True,
        )
        def tilejson(
            request: Request,
            searchid=Depends(self.path_dependency),
            tileMatrixSetId: Annotated[  # type: ignore
                Literal[tuple(self.supported_tms.list())],
                f"Identifier selecting one of the TileMatrixSetId supported (default: '{self.default_tms}')",
            ] = self.default_tms,
            tile_format: Annotated[
                Optional[ImageType],
                Query(
                    description="Default will be automatically defined if the output image needs a mask (png) or not (jpeg).",
                ),
            ] = None,
            tile_scale: Annotated[
                Optional[int],
                Query(
                    gt=0, lt=4, description="Tile size scale. 1=256x256, 2=512x512..."
                ),
            ] = None,
            minzoom: Annotated[
                Optional[int],
                Query(description="Overwrite default minzoom."),
            ] = None,
            maxzoom: Annotated[
                Optional[int],
                Query(description="Overwrite default maxzoom."),
            ] = None,
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            buffer: Annotated[
                Optional[float],
                Query(
                    gt=0,
                    title="Tile buffer.",
                    description="Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).",
                ),
            ] = None,
            post_process=Depends(self.process_dependency),
            rescale=Depends(self.rescale_dependency),
            color_formula: Annotated[
                Optional[str],
                Query(
                    title="Color Formula",
                    description="rio-color formula (info: https://github.com/mapbox/rio-color)",
                ),
            ] = None,
            colormap=Depends(self.colormap_dependency),
            render_params=Depends(self.render_dependency),
            pgstac_params: PgSTACParams = Depends(),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
        ):
            """Return TileJSON document for a SearchId."""
            with request.app.state.dbpool.connection() as conn:
                with conn.cursor(row_factory=class_row(model.Search)) as cursor:
                    cursor.execute(
                        "SELECT * FROM searches WHERE hash=%s;",
                        (searchid,),
                    )
                    search_info = cursor.fetchone()
                    if not search_info:
                        raise MosaicNotFoundError(f"SearchId `{searchid}` not found")

            route_params = {
                "searchid": search_info.id,
                "z": "{z}",
                "x": "{x}",
                "y": "{y}",
                "tileMatrixSetId": tileMatrixSetId,
            }
            if tile_scale:
                route_params["scale"] = tile_scale
            if tile_format:
                route_params["format"] = tile_format.value

            tiles_url = self.url_for(request, "tile", **route_params)

            qs_key_to_remove = [
                "tilematrixsetid",
                "tile_format",
                "tile_scale",
                "minzoom",
                "maxzoom",
            ]
            qs = [
                (key, value)
                for (key, value) in request.query_params._list
                if key.lower() not in qs_key_to_remove
            ]
            if qs:
                tiles_url += f"?{urlencode(qs)}"

            tms = self.supported_tms.get(tileMatrixSetId)
            minzoom = _first_value([minzoom, search_info.metadata.minzoom], tms.minzoom)
            maxzoom = _first_value([maxzoom, search_info.metadata.maxzoom], tms.maxzoom)
            bounds = _first_value(
                [search_info.input_search.get("bbox"), search_info.metadata.bounds],
                tms.bbox,
            )
            return {
                "bounds": bounds,
                "minzoom": minzoom,
                "maxzoom": maxzoom,
                "name": search_info.metadata.name or search_info.id,
                "tiles": [tiles_url],
            }

    def _map_routes(self):  # noqa: C901
        """Register /map endpoint."""

        @self.router.get("/{searchid}/map", response_class=HTMLResponse)
        @self.router.get(
            "/{searchid}/{tileMatrixSetId}/map", response_class=HTMLResponse
        )
        def map_viewer(
            request: Request,
            searchid=Depends(self.path_dependency),
            tileMatrixSetId: Annotated[
                Literal[tuple(self.supported_tms.list())],
                f"Identifier selecting one of the TileMatrixSetId supported (default: '{self.default_tms}')",
            ] = self.default_tms,
            tile_format: Annotated[
                Optional[ImageType],
                Query(
                    description="Default will be automatically defined if the output image needs a mask (png) or not (jpeg).",
                ),
            ] = None,
            tile_scale: Annotated[
                Optional[int],
                Query(
                    gt=0, lt=4, description="Tile size scale. 1=256x256, 2=512x512..."
                ),
            ] = None,
            minzoom: Annotated[
                Optional[int],
                Query(description="Overwrite default minzoom."),
            ] = None,
            maxzoom: Annotated[
                Optional[int],
                Query(description="Overwrite default maxzoom."),
            ] = None,
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            buffer: Annotated[
                Optional[float],
                Query(
                    gt=0,
                    title="Tile buffer.",
                    description="Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).",
                ),
            ] = None,
            post_process=Depends(self.process_dependency),
            rescale=Depends(self.rescale_dependency),
            color_formula: Annotated[
                Optional[str],
                Query(
                    title="Color Formula",
                    description="rio-color formula (info: https://github.com/mapbox/rio-color)",
                ),
            ] = None,
            colormap=Depends(self.colormap_dependency),
            render_params=Depends(self.render_dependency),
            pgstac_params: PgSTACParams = Depends(),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Return a simple map viewer."""
            tilejson_url = self.url_for(
                request, "tilejson", searchid=searchid, tileMatrixSetId=tileMatrixSetId
            )
            if request.query_params._list:
                tilejson_url += f"?{urlencode(request.query_params._list)}"

            tms = self.supported_tms.get(tileMatrixSetId)
            return self.templates.TemplateResponse(
                name="map.html",
                context={
                    "request": request,
                    "tilejson_endpoint": tilejson_url,
                    "tms": tms,
                    "resolutions": [tms._resolution(matrix) for matrix in tms],
                },
                media_type="text/html",
            )

    def _wmts_routes(self):  # noqa: C901
        """Add wmts endpoint."""

        @self.router.get("/{searchid}/WMTSCapabilities.xml", response_class=XMLResponse)
        @self.router.get(
            "/{searchid}/{tileMatrixSetId}/WMTSCapabilities.xml",
            response_class=XMLResponse,
        )
        def wmts(
            request: Request,
            searchid=Depends(self.path_dependency),
            tileMatrixSetId: Annotated[
                Literal[tuple(self.supported_tms.list())],
                f"Identifier selecting one of the TileMatrixSetId supported (default: '{self.default_tms}')",
            ] = self.default_tms,
            src_path=Depends(self.path_dependency),
            tile_format: Annotated[
                ImageType,
                Query(description="Output image type. Default is png."),
            ] = ImageType.png,
            tile_scale: Annotated[
                int,
                Query(
                    gt=0, lt=4, description="Tile size scale. 1=256x256, 2=512x512..."
                ),
            ] = 1,
            minzoom: Annotated[
                Optional[int],
                Query(description="Overwrite default minzoom."),
            ] = None,
            maxzoom: Annotated[
                Optional[int],
                Query(description="Overwrite default maxzoom."),
            ] = None,
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            buffer: Annotated[
                Optional[float],
                Query(
                    gt=0,
                    title="Tile buffer.",
                    description="Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).",
                ),
            ] = None,
            post_process=Depends(self.process_dependency),
            rescale=Depends(self.rescale_dependency),
            color_formula: Annotated[
                Optional[str],
                Query(
                    title="Color Formula",
                    description="rio-color formula (info: https://github.com/mapbox/rio-color)",
                ),
            ] = None,
            colormap=Depends(self.colormap_dependency),
            render_params=Depends(self.render_dependency),
            pgstac_params: PgSTACParams = Depends(),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """OGC WMTS endpoint."""
            with request.app.state.dbpool.connection() as conn:
                with conn.cursor(row_factory=class_row(model.Search)) as cursor:
                    cursor.execute(
                        "SELECT * FROM searches WHERE hash=%s;",
                        (searchid,),
                    )
                    search_info = cursor.fetchone()
                    if not search_info:
                        raise MosaicNotFoundError(f"SearchId `{searchid}` not found")

            route_params = {
                "searchid": searchid,
                "z": "{TileMatrix}",
                "x": "{TileCol}",
                "y": "{TileRow}",
                "scale": tile_scale,
                "format": tile_format.value,
                "tileMatrixSetId": tileMatrixSetId,
            }
            tiles_url = self.url_for(request, "tile", **route_params)

            qs_key_to_remove = [
                "tilematrixsetid",
                "tile_format",
                "tile_scale",
                "minzoom",
                "maxzoom",
                "service",
                "request",
            ]
            qs = [
                (key, value)
                for (key, value) in request.query_params._list
                if key.lower() not in qs_key_to_remove
            ]
            if qs:
                tiles_url += f"?{urlencode(qs)}"

            tms = self.supported_tms.get(tileMatrixSetId)
            minzoom = _first_value([minzoom, search_info.metadata.minzoom], tms.minzoom)
            maxzoom = _first_value([maxzoom, search_info.metadata.maxzoom], tms.maxzoom)
            bounds = _first_value(
                [search_info.input_search.get("bbox"), search_info.metadata.bounds],
                tms.bbox,
            )

            tileMatrix = []
            for zoom in range(minzoom, maxzoom + 1):  # type: ignore
                matrix = tms.matrix(zoom)
                tm = f"""
                        <TileMatrix>
                            <ows:Identifier>{matrix.id}</ows:Identifier>
                            <ScaleDenominator>{matrix.scaleDenominator}</ScaleDenominator>
                            <TopLeftCorner>{matrix.pointOfOrigin[0]} {matrix.pointOfOrigin[1]}</TopLeftCorner>
                            <TileWidth>{matrix.tileWidth}</TileWidth>
                            <TileHeight>{matrix.tileHeight}</TileHeight>
                            <MatrixWidth>{matrix.matrixWidth}</MatrixWidth>
                            <MatrixHeight>{matrix.matrixHeight}</MatrixHeight>
                        </TileMatrix>"""
                tileMatrix.append(tm)

            return self.templates.TemplateResponse(
                "wmts.xml",
                {
                    "request": request,
                    "tiles_endpoint": tiles_url,
                    "bounds": bounds,
                    "tileMatrix": tileMatrix,
                    "tms": tms,
                    "title": "Mosaic",
                    "layer_name": "mosaic",
                    "media_type": tile_format.mediatype,
                },
                media_type=MediaType.xml.value,
            )

    def _assets_routes(self):
        """Register assets routes."""

        @self.router.get(
            "/{searchid}/tiles/{z}/{x}/{y}/assets",
            responses={200: {"description": "Return list of assets"}},
        )
        @self.router.get(
            "/{searchid}/tiles/{tileMatrixSetId}/{z}/{x}/{y}/assets",
            responses={200: {"description": "Return list of assets"}},
            response_model=List[Dict],
        )
        def assets_for_tile(
            searchid=Depends(self.path_dependency),
            tile=Depends(TileParams),
            tileMatrixSetId: Annotated[
                Literal[tuple(self.supported_tms.list())],
                f"Identifier selecting one of the TileMatrixSetId supported (default: '{self.default_tms}')",
            ] = self.default_tms,
            pgstac_params: PgSTACParams = Depends(),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
        ):
            """Return a list of assets which overlap a given tile"""
            tms = self.supported_tms.get(tileMatrixSetId)
            with self.reader(
                searchid,
                tms=tms,
                reader_options={**reader_params},
                **backend_params,
            ) as src_dst:
                return src_dst.assets_for_tile(tile.x, tile.y, tile.z, **pgstac_params)

        @self.router.get(
            "/{searchid}/{lon},{lat}/assets",
            responses={200: {"description": "Return list of assets"}},
            response_model=List[Dict],
        )
        def assets_for_point(
            lon: Annotated[float, Path(description="Longitude")],
            lat: Annotated[float, Path(description="Latitude")],
            searchid=Depends(self.path_dependency),
            coord_crs=Depends(CoordCRSParams),
            pgstac_params: PgSTACParams = Depends(),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
        ):
            """Return a list of assets for a given point."""
            with self.reader(
                searchid,
                reader_options={**reader_params},
                **backend_params,
            ) as src_dst:
                return src_dst.assets_for_point(
                    lon,
                    lat,
                    coord_crs=coord_crs or WGS84_CRS,
                    **pgstac_params,
                )

    def _search_routes(self) -> None:
        """register search routes."""

        @self.router.post(
            "/register",
            responses={200: {"description": "Register a Search."}},
            response_model=model.RegisterResponse,
            response_model_exclude_none=True,
        )
        def register_search(
            request: Request, search_query=Depends(self.search_dependency)
        ):
            """Register a Search query."""
            search, metadata = search_query

            with request.app.state.dbpool.connection() as conn:
                with conn.cursor(row_factory=class_row(model.Search)) as cursor:
                    cursor.execute(
                        "SELECT * FROM search_query(%s, _metadata => %s);",
                        (
                            search.json(by_alias=True, exclude_none=True),
                            metadata.json(exclude_none=True),
                        ),
                    )
                    search_info = cursor.fetchone()

            return model.RegisterResponse(
                searchid=search_info.id,
                links=[
                    model.Link(
                        rel="metadata",
                        href=self.url_for(
                            request, "info_search", searchid=search_info.id
                        ),
                    ),
                    model.Link(
                        rel="tilejson",
                        href=self.url_for(request, "tilejson", searchid=search_info.id),
                    ),
                ],
            )

        @self.router.get(
            "/{searchid}/info",
            responses={200: {"description": "Get Search query metadata."}},
            response_model=model.Info,
            response_model_exclude_none=True,
        )
        def info_search(request: Request, searchid=Depends(self.path_dependency)):
            """Get Search query metadata."""
            with request.app.state.dbpool.connection() as conn:
                with conn.cursor(row_factory=class_row(model.Search)) as cursor:
                    cursor.execute(
                        "SELECT * FROM searches WHERE hash=%s;",
                        (searchid,),
                    )
                    search_info = cursor.fetchone()

            if not search_info:
                raise MosaicNotFoundError(f"SearchId `{searchid}` not found")

            return model.Info(
                search=search_info,
                links=[
                    model.Link(
                        rel="self",
                        href=self.url_for(
                            request, "info_search", searchid=search_info.id
                        ),
                    ),
                    model.Link(
                        rel="tilejson",
                        href=self.url_for(request, "tilejson", searchid=search_info.id),
                    ),
                ],
            )

    def _search_list_routes(self) -> None:
        """Add mosaic listing route."""

        @self.router.get(
            "/list",
            responses={200: {"description": "List Mosaics in PgSTAC."}},
            response_model=model.Infos,
            response_model_exclude_none=True,
        )
        def list_mosaic(
            request: Request,
            limit: Annotated[
                int,
                Query(
                    ge=1,
                    le=1000,
                    description="Page size limit",
                ),
            ] = 10,
            offset: Annotated[
                int,
                Query(
                    ge=0,
                    description="Page offset",
                ),
            ] = 0,
            sortby: Annotated[
                Optional[str],
                Query(
                    description="Sort the response items by a property (ascending (default) or descending).",
                ),
            ] = None,
        ):
            """List a Search query."""
            # Default filter to only return `metadata->type == 'mosaic'`
            mosaic_filter = sql.SQL("metadata->>'type' = 'mosaic'")

            # additional metadata property filter passed in query-parameters
            # <propname>=val - filter for a metadata property. Multiple property filters are ANDed together.
            qs_key_to_remove = ["limit", "offset", "sortby"]
            additional_filter = [
                sql.SQL("metadata->>{key} = {value}").format(
                    key=sql.Literal(key), value=sql.Literal(value)
                )
                for (key, value) in request.query_params.items()
                if key.lower() not in qs_key_to_remove
            ]
            filters = [
                sql.SQL("WHERE"),
                sql.SQL("AND ").join([mosaic_filter, *additional_filter]),
            ]

            def parse_sort_by(sortby: str) -> Generator[sql.Composable, None, None]:
                """Parse SortBy expression."""
                for s in sortby.split(","):
                    parts = re.match(
                        "^(?P<dir>[+-]?)(?P<prop>.*)$", s.lstrip()
                    ).groupdict()  # type:ignore

                    prop = parts["prop"]
                    if parts["prop"] in ["lastused", "usecount"]:
                        prop = sql.Identifier(prop)
                    else:
                        prop = sql.SQL("metadata->>{}").format(sql.Literal(prop))

                    if parts["dir"] == "-":
                        order = sql.SQL("{} DESC").format(prop)
                    else:
                        order = sql.SQL("{} ASC").format(prop)

                    yield order

            # sortby=[+|-]PROP - sort the response items by a property (ascending (default) or descending).
            order_by = []
            if sortby:
                sort_expr = list(parse_sort_by(sortby))
                if sort_expr:
                    order_by = [
                        sql.SQL("ORDER BY"),
                        sql.SQL(", ").join(sort_expr),
                    ]

            with request.app.state.dbpool.connection() as conn:
                with conn.cursor() as cursor:
                    # Get Total Number of searches rows
                    query = [
                        sql.SQL("SELECT count(*) FROM searches"),
                        *filters,
                    ]
                    cursor.execute(sql.SQL(" ").join(query))
                    nb_items = int(cursor.fetchone()[0])

                    # Get rows
                    cursor.row_factory = class_row(model.Search)
                    query = [
                        sql.SQL("SELECT * FROM searches"),
                        *filters,
                        *order_by,
                        sql.SQL("LIMIT %(limit)s OFFSET %(offset)s"),
                    ]
                    cursor.execute(
                        sql.SQL(" ").join(query), {"limit": limit, "offset": offset}
                    )
                    searches_info = cursor.fetchall()

            qs = QueryParams({**request.query_params, "limit": limit, "offset": offset})
            links = [
                model.Link(
                    rel="self",
                    href=self.url_for(request, "list_mosaic") + f"?{qs}",
                ),
            ]

            if len(searches_info) < nb_items:
                next_token = offset + len(searches_info)
                qs = QueryParams(
                    {**request.query_params, "limit": limit, "offset": next_token}
                )
                links.append(
                    model.Link(
                        rel="next",
                        href=self.url_for(request, "list_mosaic") + f"?{qs}",
                    ),
                )

            if offset > 0:
                prev_token = offset - limit if (offset - limit) > 0 else 0
                qs = QueryParams(
                    {**request.query_params, "limit": limit, "offset": prev_token}
                )
                links.append(
                    model.Link(
                        rel="prev",
                        href=self.url_for(request, "list_mosaic") + f"?{qs}",
                    ),
                )

            return model.Infos(
                searches=[
                    model.Info(
                        search=search,
                        links=[
                            model.Link(
                                rel="metadata",
                                href=self.url_for(
                                    request, "info_search", searchid=search.id
                                ),
                            ),
                            model.Link(
                                rel="tilejson",
                                href=self.url_for(
                                    request, "tilejson", searchid=search.id
                                ),
                            ),
                        ],
                    )
                    for search in searches_info
                ],
                links=links,
                context=model.Context(
                    returned=len(searches_info),
                    matched=nb_items,
                    limit=limit,
                ),
            )

    def _statistics_routes(self):
        """Register /statistics endpoint."""

        @self.router.post(
            "/{searchid}/statistics",
            response_model=MultiBaseStatisticsGeoJSON,
            response_model_exclude_none=True,
            response_class=GeoJSONResponse,
            responses={
                200: {
                    "content": {"application/json": {}},
                    "description": "Return statistics for geojson features.",
                }
            },
        )
        def geojson_statistics(
            geojson: Annotated[
                Union[FeatureCollection, Feature],
                Body(description="GeoJSON Feature or FeatureCollection."),
            ],
            searchid=Depends(self.path_dependency),
            coord_crs=Depends(CoordCRSParams),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            max_size: Annotated[
                int, Query(description="Maximum image size to read onto.")
            ] = 1024,
            stats_params=Depends(self.stats_dependency),
            histogram_params=Depends(self.histogram_dependency),
            pgstac_params: PgSTACParams = Depends(),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Get Statistics from a geojson feature or featureCollection."""
            fc = geojson
            if isinstance(fc, Feature):
                fc = FeatureCollection(type="FeatureCollection", features=[geojson])

            threads = int(os.getenv("MOSAIC_CONCURRENCY", MAX_THREADS))

            with rasterio.Env(**env):
                with self.reader(
                    searchid,
                    reader_options={**reader_params},
                    **backend_params,
                ) as src_dst:
                    for feature in fc:
                        data, _ = src_dst.feature(
                            feature.dict(exclude_none=True),
                            shape_crs=coord_crs or WGS84_CRS,
                            pixel_selection=pixel_selection,
                            threads=threads,
                            max_size=max_size,
                            **layer_params,
                            **dataset_params,
                            **pgstac_params,
                        )

                        stats = data.statistics(
                            **stats_params, hist_options={**histogram_params}
                        )

                        feature.properties = feature.properties or {}
                        feature.properties.update({"statistics": stats})

            return fc.features[0] if isinstance(geojson, Feature) else fc
