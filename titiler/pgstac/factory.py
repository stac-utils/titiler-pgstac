"""Custom MosaicTiler Factory for PgSTAC Mosaic Backend."""

import os
import re
import warnings
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

import jinja2
import rasterio
from attrs import define, field
from cogeo_mosaic.errors import MosaicNotFoundError
from fastapi import Body, Depends, FastAPI, HTTPException, Path, Query
from fastapi.dependencies.utils import get_dependant, request_params_to_args
from geojson_pydantic import Feature, FeatureCollection
from morecantile import TileMatrixSets
from morecantile import tms as morecantile_tms
from morecantile.models import crs_axis_inverted
from psycopg import errors as pgErrors
from psycopg import sql
from psycopg.rows import class_row, dict_row
from pydantic import Field
from rio_tiler.constants import MAX_THREADS, WGS84_CRS
from rio_tiler.mosaic.methods.base import MosaicMethodBase
from rio_tiler.types import ColorMapType
from rio_tiler.utils import CRS_to_uri
from starlette.datastructures import QueryParams
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response
from starlette.routing import NoMatchFound
from starlette.templating import Jinja2Templates
from typing_extensions import Annotated

from titiler.core.algorithm import BaseAlgorithm
from titiler.core.algorithm import algorithms as available_algorithms
from titiler.core.dependencies import (
    AssetsBidxExprParams,
    ColorMapParams,
    CoordCRSParams,
    CRSParams,
    DatasetParams,
    DefaultDependency,
    DstCRSParams,
    HistogramParams,
    ImageRenderingParams,
    PartFeatureParams,
    StatisticsParams,
    TileParams,
)
from titiler.core.factory import BaseFactory, img_endpoint_params
from titiler.core.models.mapbox import TileJSON
from titiler.core.models.OGC import TileSet, TileSetList
from titiler.core.models.responses import MultiBaseStatisticsGeoJSON
from titiler.core.resources.enums import ImageType, MediaType, OptionalHeader
from titiler.core.resources.responses import GeoJSONResponse, JSONResponse, XMLResponse
from titiler.core.utils import render_image
from titiler.mosaic.factory import PixelSelectionParams
from titiler.mosaic.models.responses import Point
from titiler.pgstac import model
from titiler.pgstac.backend import PGSTACBackend
from titiler.pgstac.dependencies import BackendParams, PgSTACParams, SearchParams
from titiler.pgstac.errors import ReadOnlyPgSTACError
from titiler.pgstac.reader import SimpleSTACReader

MOSAIC_THREADS = int(os.getenv("MOSAIC_CONCURRENCY", MAX_THREADS))
MOSAIC_STRICT_ZOOM = str(os.getenv("MOSAIC_STRICT_ZOOM", False)).lower() in [
    "true",
    "yes",
]


def _first_value(values: List[Any], default: Any = None):
    """Return the first not None value."""
    return next(filter(lambda x: x is not None, values), default)


jinja2_env = jinja2.Environment(
    loader=jinja2.ChoiceLoader(
        [
            jinja2.PackageLoader(__package__, "templates"),
            jinja2.PackageLoader("titiler.core", "templates"),
        ]
    ),
)
DEFAULT_TEMPLATES = Jinja2Templates(env=jinja2_env)


def check_query_params(
    *, dependencies: List[Callable], query_params: Union[QueryParams, Dict]
) -> None:
    """Check QueryParams for Query dependency.

    1. `get_dependant` is used to get the query-parameters required by the `callable`
    2. we use `request_params_to_args` to construct arguments needed to call the `callable`
    3. we call the `callable` and catch any errors

    Important: We assume the `callable` in not a co-routine

    """
    for dependency in dependencies:
        dep = get_dependant(path="", call=dependency)
        if dep.query_params:
            # call the dependency with the query-parameters values
            query_values, _ = request_params_to_args(dep.query_params, query_params)
            _ = dependency(**query_values)

    return


@define(kw_only=True)
class MosaicTilerFactory(BaseFactory):
    """Custom MosaicTiler for PgSTAC Mosaic Backend."""

    path_dependency: Callable[..., str]

    backend: Type[PGSTACBackend] = PGSTACBackend
    backend_dependency: Type[DefaultDependency] = BackendParams

    dataset_reader: Type[SimpleSTACReader] = SimpleSTACReader
    reader_dependency: Type[DefaultDependency] = DefaultDependency

    # Assets/Indexes/Expression Dependencies
    layer_dependency: Type[DefaultDependency] = AssetsBidxExprParams

    # Rasterio Dataset Options (nodata, unscale, resampling, reproject)
    dataset_dependency: Type[DefaultDependency] = DatasetParams

    # Tile/Tilejson/WMTS Dependencies
    tile_dependency: Type[DefaultDependency] = TileParams

    # Post Processing Dependencies (algorithm)
    process_dependency: Callable[..., Optional[BaseAlgorithm]] = (
        available_algorithms.dependency
    )

    # Image rendering Dependencies
    colormap_dependency: Callable[..., Optional[ColorMapType]] = ColorMapParams
    render_dependency: Type[DefaultDependency] = ImageRenderingParams

    # Mosaic Dependency
    pixel_selection_dependency: Callable[..., MosaicMethodBase] = PixelSelectionParams

    # GDAL ENV dependency
    environment_dependency: Callable[..., Dict] = field(default=lambda: {})

    # Statistics/Histogram Dependencies
    stats_dependency: Type[DefaultDependency] = StatisticsParams
    histogram_dependency: Type[DefaultDependency] = HistogramParams

    # Crop endpoints Dependencies
    # WARNINGS: `/bbox` and `/feature` endpoints should be used carefully because
    # each request might need to open/read a lot of files if the user decide to
    # submit large bbox/geojson. This will also depends on the STAC Items resolution.
    img_part_dependency: Type[DefaultDependency] = PartFeatureParams

    pgstac_dependency: Type[DefaultDependency] = PgSTACParams

    supported_tms: TileMatrixSets = morecantile_tms

    templates: Jinja2Templates = DEFAULT_TEMPLATES

    render_func: Callable[..., Tuple[bytes, str]] = render_image

    optional_headers: List[OptionalHeader] = field(factory=list)

    # Add/Remove some endpoints
    add_viewer: bool = False
    add_statistics: bool = False
    add_part: bool = False

    def register_routes(self) -> None:
        """This Method register routes to the router."""
        self.tilesets()
        self.assets_tile()
        self.tile()
        if self.add_viewer:
            self.map_viewer()
        self.tilejson()
        self.wmts()
        self.point()
        self.assets_point()

        if self.add_part:
            self.part()

        if self.add_statistics:
            self.statistics()

    ############################################################################
    # /tileset
    ############################################################################
    def tilesets(self):
        """Register OGC tilesets endpoints."""

        @self.router.get(
            "/tiles",
            response_model=TileSetList,
            response_class=JSONResponse,
            response_model_exclude_none=True,
            responses={
                200: {
                    "content": {
                        "application/json": {},
                    }
                }
            },
            summary="Retrieve a list of available raster tilesets for the specified dataset.",
        )
        async def tileset_list(
            request: Request,
            search_id=Depends(self.path_dependency),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            crs=Depends(CRSParams),
            env=Depends(self.environment_dependency),
        ):
            """Retrieve a list of available raster tilesets for the specified dataset."""
            with rasterio.Env(**env):
                with self.backend(
                    search_id,
                    reader=self.dataset_reader,
                    reader_options=reader_params.as_dict(),
                    **backend_params.as_dict(),
                ) as src_dst:
                    bounds = src_dst.get_geographic_bounds(crs or WGS84_CRS)

            collection_bbox = {
                "lowerLeft": [bounds[0], bounds[1]],
                "upperRight": [bounds[2], bounds[3]],
                "crs": CRS_to_uri(crs or WGS84_CRS),
            }

            qs = [
                (key, value)
                for (key, value) in request.query_params._list
                if key.lower() not in ["crs"]
            ]
            query_string = f"?{urlencode(qs)}" if qs else ""

            tilesets = []
            for tms in self.supported_tms.list():
                tileset = {
                    "title": f"tileset tiled using {tms} TileMatrixSet",
                    "dataType": "map",
                    "crs": self.supported_tms.get(tms).crs,
                    "boundingBox": collection_bbox,
                    "links": [
                        {
                            "href": self.url_for(
                                request, "tileset", tileMatrixSetId=tms
                            )
                            + query_string,
                            "rel": "self",
                            "type": "application/json",
                            "title": f"Tileset tiled using {tms} TileMatrixSet",
                        },
                        {
                            "href": self.url_for(
                                request,
                                "tile",
                                tileMatrixSetId=tms,
                                z="{z}",
                                x="{x}",
                                y="{y}",
                            )
                            + query_string,
                            "rel": "tile",
                            "title": "Templated link for retrieving Raster tiles",
                        },
                    ],
                }

                try:
                    tileset["links"].append(
                        {
                            "href": str(
                                request.url_for("tilematrixset", tileMatrixSetId=tms)
                            ),
                            "rel": "http://www.opengis.net/def/rel/ogc/1.0/tiling-schemes",
                            "type": "application/json",
                            "title": f"Definition of '{tms}' tileMatrixSet",
                        }
                    )
                except NoMatchFound:
                    pass

                tilesets.append(tileset)

            data = TileSetList.model_validate({"tilesets": tilesets})
            return data

        @self.router.get(
            "/tiles/{tileMatrixSetId}",
            response_model=TileSet,
            response_class=JSONResponse,
            response_model_exclude_none=True,
            responses={200: {"content": {"application/json": {}}}},
            summary="Retrieve the raster tileset metadata for the specified dataset and tiling scheme (tile matrix set).",
        )
        async def tileset(
            request: Request,
            tileMatrixSetId: Annotated[
                Literal[tuple(self.supported_tms.list())],
                Path(
                    description="Identifier selecting one of the TileMatrixSetId supported."
                ),
            ],
            search_id=Depends(self.path_dependency),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Retrieve the raster tileset metadata for the specified dataset and tiling scheme (tile matrix set)."""
            tms = self.supported_tms.get(tileMatrixSetId)
            with rasterio.Env(**env):
                with self.backend(
                    search_id,
                    tms=tms,
                    reader=self.dataset_reader,
                    reader_options=reader_params.as_dict(),
                    **backend_params.as_dict(),
                ) as src_dst:
                    bounds = src_dst.get_geographic_bounds(tms.rasterio_geographic_crs)
                    minzoom = src_dst.minzoom
                    maxzoom = src_dst.maxzoom

                    collection_bbox = {
                        "lowerLeft": [bounds[0], bounds[1]],
                        "upperRight": [bounds[2], bounds[3]],
                        "crs": CRS_to_uri(tms.rasterio_geographic_crs),
                    }

                    tilematrix_limit = []
                    for zoom in range(minzoom, maxzoom + 1, 1):
                        matrix = tms.matrix(zoom)
                        ulTile = tms.tile(bounds[0], bounds[3], int(matrix.id))
                        lrTile = tms.tile(bounds[2], bounds[1], int(matrix.id))
                        minx, maxx = (min(ulTile.x, lrTile.x), max(ulTile.x, lrTile.x))
                        miny, maxy = (min(ulTile.y, lrTile.y), max(ulTile.y, lrTile.y))
                        tilematrix_limit.append(
                            {
                                "tileMatrix": matrix.id,
                                "minTileRow": max(miny, 0),
                                "maxTileRow": min(maxy, matrix.matrixHeight),
                                "minTileCol": max(minx, 0),
                                "maxTileCol": min(maxx, matrix.matrixWidth),
                            }
                        )

            qs = list(request.query_params._list)
            query_string = f"?{urlencode(qs)}" if qs else ""

            links = [
                {
                    "href": self.url_for(
                        request,
                        "tileset",
                        tileMatrixSetId=tileMatrixSetId,
                    ),
                    "rel": "self",
                    "type": "application/json",
                    "title": f"Tileset tiled using {tileMatrixSetId} TileMatrixSet",
                },
                {
                    "href": self.url_for(
                        request,
                        "tile",
                        tileMatrixSetId=tileMatrixSetId,
                        z="{z}",
                        x="{x}",
                        y="{y}",
                    )
                    + query_string,
                    "rel": "tile",
                    "title": "Templated link for retrieving Raster tiles",
                    "templated": True,
                },
            ]
            try:
                links.append(
                    {
                        "href": str(
                            request.url_for(
                                "tilematrixset", tileMatrixSetId=tileMatrixSetId
                            )
                        ),
                        "rel": "http://www.opengis.net/def/rel/ogc/1.0/tiling-schemes",
                        "type": "application/json",
                        "title": f"Definition of '{tileMatrixSetId}' tileMatrixSet",
                    }
                )
            except NoMatchFound:
                pass

            if self.add_viewer:
                links.append(
                    {
                        "href": self.url_for(
                            request,
                            "map_viewer",
                            tileMatrixSetId=tileMatrixSetId,
                        )
                        + query_string,
                        "type": "text/html",
                        "rel": "data",
                        "title": f"Map viewer for '{tileMatrixSetId}' tileMatrixSet",
                    }
                )

            # TODO: add render links

            data = TileSet.model_validate(
                {
                    "title": f"tileset tiled using {tileMatrixSetId} TileMatrixSet",
                    "dataType": "map",
                    "crs": tms.crs,
                    "boundingBox": collection_bbox,
                    "links": links,
                    "tileMatrixSetLimits": tilematrix_limit,
                }
            )

            return data

    def tile(self) -> None:
        """register tiles routes."""

        @self.router.get("/tiles/{tileMatrixSetId}/{z}/{x}/{y}", **img_endpoint_params)
        @self.router.get(
            "/tiles/{tileMatrixSetId}/{z}/{x}/{y}.{format}",
            **img_endpoint_params,
        )
        @self.router.get(
            "/tiles/{tileMatrixSetId}/{z}/{x}/{y}@{scale}x",
            **img_endpoint_params,
        )
        @self.router.get(
            "/tiles/{tileMatrixSetId}/{z}/{x}/{y}@{scale}x.{format}",
            **img_endpoint_params,
        )
        def tile(
            z: Annotated[
                int,
                Path(
                    description="Identifier (Z) selecting one of the scales defined in the TileMatrixSet and representing the scaleDenominator the tile.",
                ),
            ],
            x: Annotated[
                int,
                Path(
                    description="Column (X) index of the tile on the selected TileMatrix. It cannot exceed the MatrixHeight-1 for the selected TileMatrix.",
                ),
            ],
            y: Annotated[
                int,
                Path(
                    description="Row (Y) index of the tile on the selected TileMatrix. It cannot exceed the MatrixWidth-1 for the selected TileMatrix.",
                ),
            ],
            tileMatrixSetId: Annotated[  # type: ignore
                Literal[tuple(self.supported_tms.list())],
                Path(
                    description="Identifier selecting one of the TileMatrixSetId supported."
                ),
            ],
            scale: Annotated[
                int,
                Field(
                    gt=0, le=4, description="Tile size scale. 1=256x256, 2=512x512..."
                ),
            ] = 1,
            format: Annotated[
                Optional[ImageType],
                "Default will be automatically defined if the output image needs a mask (png) or not (jpeg).",
            ] = None,
            search_id=Depends(self.path_dependency),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pgstac_params=Depends(self.pgstac_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            tile_params=Depends(self.tile_dependency),
            post_process=Depends(self.process_dependency),
            colormap=Depends(self.colormap_dependency),
            render_params=Depends(self.render_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Create map tile."""
            scale = scale or 1

            tms = self.supported_tms.get(tileMatrixSetId)
            with rasterio.Env(**env):
                with self.backend(
                    search_id,
                    tms=tms,
                    reader=self.dataset_reader,
                    reader_options=reader_params.as_dict(),
                    **backend_params.as_dict(),
                ) as src_dst:
                    if MOSAIC_STRICT_ZOOM and (
                        z < src_dst.minzoom or z > src_dst.maxzoom
                    ):
                        raise HTTPException(
                            400,
                            f"Invalid ZOOM level {z}. Should be between {src_dst.minzoom} and {src_dst.maxzoom}",
                        )

                    image, assets = src_dst.tile(
                        x,
                        y,
                        z,
                        tilesize=scale * 256,
                        pixel_selection=pixel_selection,
                        threads=MOSAIC_THREADS,
                        **tile_params.as_dict(),
                        **layer_params.as_dict(),
                        **dataset_params.as_dict(),
                        **pgstac_params.as_dict(),
                    )

            if post_process:
                image = post_process(image)

            content, media_type = self.render_func(
                image,
                output_format=format,
                colormap=colormap,
                **render_params.as_dict(),
            )

            headers: Dict[str, str] = {}
            if OptionalHeader.x_assets in self.optional_headers:
                ids = [x["id"] for x in assets]
                headers["X-Assets"] = ",".join(ids)

            return Response(content, media_type=media_type, headers=headers)

    def tilejson(self) -> None:
        """register tiles routes."""

        @self.router.get(
            "/{tileMatrixSetId}/tilejson.json",
            response_model=TileJSON,
            responses={200: {"description": "Return a tilejson"}},
            response_model_exclude_none=True,
        )
        def tilejson(
            request: Request,
            tileMatrixSetId: Annotated[  # type: ignore
                Literal[tuple(self.supported_tms.list())],
                Path(
                    description="Identifier selecting one of the TileMatrixSetId supported."
                ),
            ],
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
            search_id=Depends(self.path_dependency),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pgstac_params=Depends(self.pgstac_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            tile_params=Depends(self.tile_dependency),
            post_process=Depends(self.process_dependency),
            colormap=Depends(self.colormap_dependency),
            render_params=Depends(self.render_dependency),
        ):
            """Return TileJSON document for a search_id."""
            with request.app.state.dbpool.connection() as conn:
                with conn.cursor(row_factory=class_row(model.Search)) as cursor:
                    cursor.execute(
                        "SELECT * FROM searches WHERE hash=%s;",
                        (search_id,),
                    )
                    search_info = cursor.fetchone()
                    if not search_info:
                        raise MosaicNotFoundError(f"SearchId `{search_id}` not found")

            route_params = {
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
                tiles_url += f"?{urlencode(qs, doseq=True)}"

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

    def map_viewer(self):  # noqa: C901
        """Register /map endpoint."""

        @self.router.get("/{tileMatrixSetId}/map", response_class=HTMLResponse)
        def map_viewer(
            request: Request,
            tileMatrixSetId: Annotated[
                Literal[tuple(self.supported_tms.list())],
                Path(
                    description="Identifier selecting one of the TileMatrixSetId supported."
                ),
            ],
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
            search_id=Depends(self.path_dependency),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pgstac_params=Depends(self.pgstac_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            tile_params=Depends(self.tile_dependency),
            post_process=Depends(self.process_dependency),
            colormap=Depends(self.colormap_dependency),
            render_params=Depends(self.render_dependency),
        ):
            """Return a simple map viewer."""
            tilejson_url = self.url_for(
                request,
                "tilejson",
                tileMatrixSetId=tileMatrixSetId,
            )
            if request.query_params._list:
                tilejson_url += f"?{urlencode(request.query_params._list, doseq=True)}"

            tms = self.supported_tms.get(tileMatrixSetId)
            return self.templates.TemplateResponse(
                request,
                name="map.html",
                context={
                    "tilejson_endpoint": tilejson_url,
                    "tms": tms,
                    "resolutions": [matrix.cellSize for matrix in tms],
                },
                media_type="text/html",
            )

    def wmts(self):  # noqa: C901
        """Add wmts endpoint."""

        @self.router.get(
            "/{tileMatrixSetId}/WMTSCapabilities.xml",
            response_class=XMLResponse,
        )
        def wmts(  # noqa: C901
            request: Request,
            tileMatrixSetId: Annotated[
                Literal[tuple(self.supported_tms.list())],
                Path(
                    description="Identifier selecting one of the TileMatrixSetId supported."
                ),
            ],
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
            use_epsg: Annotated[
                bool,
                Query(
                    description="Use EPSG code, not opengis.net, for the ows:SupportedCRS in the TileMatrixSet (set to True to enable ArcMap compatability)"
                ),
            ] = False,
            search_id=Depends(self.path_dependency),
        ):
            """OGC WMTS endpoint."""
            with request.app.state.dbpool.connection() as conn:
                with conn.cursor(row_factory=class_row(model.Search)) as cursor:
                    cursor.execute(
                        "SELECT * FROM searches WHERE hash=%s;",
                        (search_id,),
                    )
                    search_info = cursor.fetchone()
                    if not search_info:
                        raise MosaicNotFoundError(f"SearchId `{search_id}` not found")

            route_params = {
                "z": "{TileMatrix}",
                "x": "{TileCol}",
                "y": "{TileRow}",
                "scale": tile_scale,
                "format": tile_format.value,
                "tileMatrixSetId": tileMatrixSetId,
            }

            tiles_url = self.url_for(request, "tile", **route_params)

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

            if use_epsg:
                supported_crs = f"EPSG:{tms.crs.to_epsg()}"
            else:
                supported_crs = tms.crs.srs

            # List of dependencies a `/tile` URL should validate
            # Note: Those dependencies should only require Query() inputs
            tile_dependencies = [
                self.layer_dependency,
                self.dataset_dependency,
                self.pixel_selection_dependency,
                self.tile_dependency,
                self.process_dependency,
                self.render_dependency,
                self.pgstac_dependency,
                self.reader_dependency,
                self.backend_dependency,
            ]

            layers: List[Dict[str, Any]] = []

            # LAYERS from mosaic metadata
            if renders := search_info.metadata.defaults_params:
                for name, values in renders.items():
                    try:
                        check_query_params(
                            dependencies=tile_dependencies,  # type: ignore
                            query_params=values,
                        )
                    except Exception as e:
                        warnings.warn(
                            f"Cannot construct URL for layer `{name}`: {repr(e)}",
                            UserWarning,
                            stacklevel=2,
                        )
                        continue

                    layers.append(
                        {
                            "titler": search_info.metadata.name or search_id,
                            "name": name,
                            "tiles_url": tiles_url,
                            "query_string": urlencode(values, doseq=True)
                            if values
                            else None,
                            "bounds": bounds,
                        }
                    )

            # LAYER from query-parameters
            qs_key_to_remove = [
                "tilematrixsetid",
                "tile_format",
                "tile_scale",
                "minzoom",
                "maxzoom",
                "service",
                "use_epsg",
                "request",
            ]
            qs = [
                (key, value)
                for (key, value) in request.query_params._list
                if key.lower() not in qs_key_to_remove
            ]

            # Checking if we can construct a valid tile URL
            # 1. we use `check_query_params` to validate the query-parameter
            # 2. if there is no layers (from mosaic metadata) we raise the caught error
            # 3. if there no errors we then add a default `layer` to the layers stack
            try:
                check_query_params(
                    dependencies=tile_dependencies,  # type: ignore
                    query_params=QueryParams(qs),
                )
            except Exception as e:
                if not layers:
                    raise e
            else:
                layers.append(
                    {
                        "titler": search_info.metadata.name or search_id,
                        "name": "default",
                        "tiles_url": tiles_url,
                        "query_string": urlencode(qs, doseq=True) if qs else None,
                        "bounds": bounds,
                    }
                )

            bbox_crs_type = "WGS84BoundingBox"
            bbox_crs_uri = "urn:ogc:def:crs:OGC:2:84"
            if tms.rasterio_geographic_crs != WGS84_CRS:
                bbox_crs_type = "BoundingBox"
                bbox_crs_uri = CRS_to_uri(tms.rasterio_geographic_crs)
                # WGS88BoundingBox is always xy ordered, but BoundingBox must match the CRS order
                if crs_axis_inverted(tms.geographic_crs):
                    # match the bounding box coordinate order to the CRS
                    bounds = [bounds[1], bounds[0], bounds[3], bounds[2]]

            return self.templates.TemplateResponse(
                request,
                name="wmts.xml",
                context={
                    "tileMatrixSetId": tms.id,
                    "tileMatrix": tileMatrix,
                    "supported_crs": supported_crs,
                    "bbox_crs_type": bbox_crs_type,
                    "bbox_crs_uri": bbox_crs_uri,
                    "layers": layers,
                    "media_type": tile_format.mediatype,
                },
                media_type=MediaType.xml.value,
            )

    def assets_tile(self):
        """Register assets routes."""

        @self.router.get(
            "/tiles/{tileMatrixSetId}/{z}/{x}/{y}/assets",
            responses={200: {"description": "Return list of assets"}},
            response_model=List[Dict],
        )
        def assets_for_tile(
            tileMatrixSetId: Annotated[
                Literal[tuple(self.supported_tms.list())],
                Path(
                    description="Identifier selecting one of the TileMatrixSetId supported."
                ),
            ],
            z: Annotated[
                int,
                Path(
                    description="Identifier (Z) selecting one of the scales defined in the TileMatrixSet and representing the scaleDenominator the tile.",
                ),
            ],
            x: Annotated[
                int,
                Path(
                    description="Column (X) index of the tile on the selected TileMatrix. It cannot exceed the MatrixHeight-1 for the selected TileMatrix.",
                ),
            ],
            y: Annotated[
                int,
                Path(
                    description="Row (Y) index of the tile on the selected TileMatrix. It cannot exceed the MatrixWidth-1 for the selected TileMatrix.",
                ),
            ],
            search_id=Depends(self.path_dependency),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            pgstac_params=Depends(self.pgstac_dependency),
        ):
            """Return a list of assets which overlap a given tile"""
            tms = self.supported_tms.get(tileMatrixSetId)
            with self.backend(
                search_id,
                tms=tms,
                reader=self.dataset_reader,
                reader_options=reader_params.as_dict(),
                **backend_params.as_dict(),
            ) as src_dst:
                return src_dst.assets_for_tile(
                    x,
                    y,
                    z,
                    **pgstac_params.as_dict(),
                )

    def assets_point(self):
        """Register assets routes."""

        @self.router.get(
            "/point/{lon},{lat}/assets",
            responses={200: {"description": "Return list of assets"}},
            response_model=List[Dict],
        )
        def assets_for_point(
            lon: Annotated[float, Path(description="Longitude")],
            lat: Annotated[float, Path(description="Latitude")],
            search_id=Depends(self.path_dependency),
            coord_crs=Depends(CoordCRSParams),
            pgstac_params=Depends(self.pgstac_dependency),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
        ):
            """Return a list of assets for a given point."""
            with self.backend(
                search_id,
                reader=self.dataset_reader,
                reader_options=reader_params.as_dict(),
                **backend_params.as_dict(),
            ) as src_dst:
                return src_dst.assets_for_point(
                    lon,
                    lat,
                    coord_crs=coord_crs or WGS84_CRS,
                    **pgstac_params.as_dict(),
                )

    def statistics(self):
        """Register /statistics endpoint."""

        @self.router.post(
            "/statistics",
            response_model=MultiBaseStatisticsGeoJSON,
            response_model_exclude_none=True,
            response_class=GeoJSONResponse,
            responses={
                200: {
                    "content": {"application/geo+json": {}},
                    "description": "Return statistics for geojson features.",
                }
            },
        )
        def geojson_statistics(
            geojson: Annotated[
                Union[FeatureCollection, Feature],
                Body(description="GeoJSON Feature or FeatureCollection."),
            ],
            search_id=Depends(self.path_dependency),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            coord_crs=Depends(CoordCRSParams),
            dst_crs=Depends(DstCRSParams),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            image_params=Depends(self.img_part_dependency),
            pgstac_params=Depends(self.pgstac_dependency),
            post_process=Depends(self.process_dependency),
            stats_params=Depends(self.stats_dependency),
            histogram_params=Depends(self.histogram_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Get Statistics from a geojson feature or featureCollection."""
            fc = geojson
            if isinstance(fc, Feature):
                fc = FeatureCollection(type="FeatureCollection", features=[geojson])

            with rasterio.Env(**env):
                with self.backend(
                    search_id,
                    reader=self.dataset_reader,
                    reader_options=reader_params.as_dict(),
                    **backend_params.as_dict(),
                ) as src_dst:
                    for feature in fc:
                        shape = feature.model_dump(exclude_none=True)

                        image, _ = src_dst.feature(
                            shape,
                            shape_crs=coord_crs or WGS84_CRS,
                            dst_crs=dst_crs,
                            pixel_selection=pixel_selection,
                            threads=MOSAIC_THREADS,
                            align_bounds_with_dataset=True,
                            **image_params.as_dict(),
                            **layer_params.as_dict(),
                            **dataset_params.as_dict(),
                            **pgstac_params.as_dict(),
                        )

                        coverage_array = image.get_coverage_array(
                            shape,
                            shape_crs=coord_crs or WGS84_CRS,
                        )

                        if post_process:
                            image = post_process(image)

                        stats = image.statistics(
                            **stats_params.as_dict(),
                            hist_options=histogram_params.as_dict(),
                            coverage=coverage_array,
                        )

                        feature.properties = feature.properties or {}
                        feature.properties.update({"statistics": stats})

            return fc.features[0] if isinstance(geojson, Feature) else fc

    def part(self):  # noqa: C901
        """Register /bbox and /feature endpoint."""

        # GET endpoints
        @self.router.get(
            "/bbox/{minx},{miny},{maxx},{maxy}.{format}",
            **img_endpoint_params,
        )
        @self.router.get(
            "/bbox/{minx},{miny},{maxx},{maxy}/{width}x{height}.{format}",
            **img_endpoint_params,
        )
        def bbox_image(
            minx: Annotated[float, Path(description="Bounding box min X")],
            miny: Annotated[float, Path(description="Bounding box min Y")],
            maxx: Annotated[float, Path(description="Bounding box max X")],
            maxy: Annotated[float, Path(description="Bounding box max Y")],
            search_id=Depends(self.path_dependency),
            format: Annotated[
                ImageType,
                "Default will be automatically defined if the output image needs a mask (png) or not (jpeg).",
            ] = None,
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            coord_crs=Depends(CoordCRSParams),
            dst_crs=Depends(DstCRSParams),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            image_params=Depends(self.img_part_dependency),
            pgstac_params=Depends(self.pgstac_dependency),
            post_process=Depends(self.process_dependency),
            colormap=Depends(self.colormap_dependency),
            render_params=Depends(self.render_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Create image from a bbox."""
            with rasterio.Env(**env):
                with self.backend(
                    search_id,
                    reader=self.dataset_reader,
                    reader_options=reader_params.as_dict(),
                    **backend_params.as_dict(),
                ) as src_dst:
                    image, assets = src_dst.part(
                        [minx, miny, maxx, maxy],
                        dst_crs=dst_crs,
                        bounds_crs=coord_crs or WGS84_CRS,
                        pixel_selection=pixel_selection,
                        **layer_params.as_dict(),
                        **image_params.as_dict(),
                        **dataset_params.as_dict(),
                    )
                    dst_colormap = getattr(src_dst, "colormap", None)

            if post_process:
                image = post_process(image)

            content, media_type = self.render_func(
                image,
                output_format=format,
                colormap=colormap or dst_colormap,
                **render_params.as_dict(),
            )

            headers: Dict[str, str] = {}
            if OptionalHeader.x_assets in self.optional_headers:
                ids = [x["id"] for x in assets]
                headers["X-Assets"] = ",".join(ids)

            return Response(content, media_type=media_type, headers=headers)

        @self.router.post(
            "/feature",
            **img_endpoint_params,
        )
        @self.router.post(
            "/feature.{format}",
            **img_endpoint_params,
        )
        @self.router.post(
            "/feature/{width}x{height}.{format}",
            **img_endpoint_params,
        )
        def feature_image(
            geojson: Annotated[Union[Feature], Body(description="GeoJSON Feature.")],
            search_id=Depends(self.path_dependency),
            format: Annotated[
                ImageType,
                "Default will be automatically defined if the output image needs a mask (png) or not (jpeg).",
            ] = None,
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            coord_crs=Depends(CoordCRSParams),
            dst_crs=Depends(DstCRSParams),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            image_params=Depends(self.img_part_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            pgstac_params=Depends(self.pgstac_dependency),
            post_process=Depends(self.process_dependency),
            colormap=Depends(self.colormap_dependency),
            render_params=Depends(self.render_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Create image from a geojson feature."""
            with rasterio.Env(**env):
                with self.backend(
                    search_id,
                    reader=self.dataset_reader,
                    reader_options=reader_params.as_dict(),
                    **backend_params.as_dict(),
                ) as src_dst:
                    image, assets = src_dst.feature(
                        geojson.model_dump(exclude_none=True),
                        dst_crs=dst_crs,
                        shape_crs=coord_crs or WGS84_CRS,
                        pixel_selection=pixel_selection,
                        threads=MOSAIC_THREADS,
                        **layer_params.as_dict(),
                        **image_params.as_dict(),
                        **dataset_params.as_dict(),
                        **pgstac_params.as_dict(),
                    )

            if post_process:
                image = post_process(image)

            content, media_type = self.render_func(
                image,
                output_format=format,
                colormap=colormap,
                **render_params.as_dict(),
            )

            headers: Dict[str, str] = {}
            if OptionalHeader.x_assets in self.optional_headers:
                ids = [x["id"] for x in assets]
                headers["X-Assets"] = ",".join(ids)

            return Response(content, media_type=media_type, headers=headers)

    def point(self):
        """Register point values endpoint."""

        @self.router.get(
            "/point/{lon},{lat}",
            response_model=Point,
            response_class=JSONResponse,
            responses={200: {"description": "Return a value for a point"}},
        )
        def point(
            lon: Annotated[float, Path(description="Longitude")],
            lat: Annotated[float, Path(description="Latitude")],
            search_id=Depends(self.path_dependency),
            coord_crs=Depends(CoordCRSParams),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pgstac_params=Depends(self.pgstac_dependency),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Get Point value for a Mosaic."""
            with rasterio.Env(**env):
                with self.backend(
                    search_id,
                    reader=self.dataset_reader,
                    reader_options=reader_params.as_dict(),
                    **backend_params.as_dict(),
                ) as src_dst:
                    values = src_dst.point(
                        lon,
                        lat,
                        coord_crs=coord_crs or WGS84_CRS,
                        threads=MOSAIC_THREADS,
                        **layer_params.as_dict(),
                        **dataset_params.as_dict(),
                        **pgstac_params.as_dict(),
                    )

            return {
                "coordinates": [lon, lat],
                "values": [
                    (src, pts.data.tolist(), pts.band_names) for src, pts in values
                ],
            }


def add_search_register_route(  # noqa: C901
    app: FastAPI,
    *,
    prefix: str = "",
    search_dependency: Callable[
        ..., Tuple[model.PgSTACSearch, model.Metadata]
    ] = SearchParams,
    tile_dependencies: Optional[List[Callable]] = None,
    tags: Optional[List[str]] = None,
):
    """add `/register` route"""

    tile_dependencies = tile_dependencies or []

    @app.post(
        f"{prefix}/register",
        responses={200: {"description": "Register a Virtual Mosaic (PgSTAC Search)."}},
        response_model=model.RegisterResponse,
        response_model_exclude_none=True,
        tags=tags,
    )
    def register_search(request: Request, search_query=Depends(search_dependency)):
        """Register a Search query."""
        search, metadata = search_query

        with request.app.state.dbpool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cursor:
                try:
                    cursor.execute("SELECT pgstac.readonly()")
                    if cursor.fetchone()["readonly"]:
                        raise ReadOnlyPgSTACError(
                            "PgSTAC instance is set to `read-only`, cannot register search query."
                        )

                # before pgstac 0.8.2, the read-only mode didn't exist
                except pgErrors.UndefinedFunction:
                    conn.rollback()
                    pass

                cursor.row_factory = class_row(model.Search)
                cursor.execute(
                    "SELECT * FROM search_query(%s, _metadata => %s);",
                    (
                        search.model_dump_json(by_alias=True, exclude_none=True),
                        metadata.model_dump_json(exclude_none=True),
                    ),
                )
                search_info = cursor.fetchone()

        links: List[model.Link] = []

        base_url = str(request.base_url)

        try:
            links.append(
                model.Link(
                    rel="metadata",
                    title="Mosaic metadata",
                    href=str(
                        app.url_path_for(
                            "info",
                            search_id=search_info.id,
                        ).make_absolute_url(base_url=base_url)
                    ),
                ),
            )
        except NoMatchFound:
            pass

        tilejson_endpoint = None
        try:
            tilejson_endpoint = str(
                app.url_path_for(
                    "tilejson",
                    search_id=search_info.id,
                    tileMatrixSetId="{tileMatrixSetId}",
                ).make_absolute_url(base_url=base_url)
            )

            links.append(
                model.Link(
                    rel="tilejson",
                    title="Link for TileJSON (Template URL)",
                    href=tilejson_endpoint,
                    templated=True,
                )
            )
        except NoMatchFound:
            pass

        try:
            links.append(
                model.Link(
                    rel="map",
                    title="Link for Map viewer (Template URL)",
                    href=str(
                        app.url_path_for(
                            "map_viewer",
                            search_id=search_info.id,
                            tileMatrixSetId="{tileMatrixSetId}",
                        ).make_absolute_url(base_url=base_url)
                    ),
                    templated=True,
                )
            )
        except NoMatchFound:
            pass

        try:
            links.append(
                model.Link(
                    rel="wmts",
                    title="Link for WMTS (Template URL)",
                    href=str(
                        app.url_path_for(
                            "wmts",
                            search_id=search_info.id,
                            tileMatrixSetId="{tileMatrixSetId}",
                        ).make_absolute_url(base_url=base_url)
                    ),
                    templated=True,
                )
            )
        except NoMatchFound:
            pass

        if renders := search_info.metadata.defaults_params:
            for name, values in renders.items():
                try:
                    check_query_params(
                        dependencies=tile_dependencies,
                        query_params=values,
                    )
                except Exception as e:
                    warnings.warn(
                        f"Cannot construct URL for layer `{name}`: {repr(e)}",
                        UserWarning,
                        stacklevel=2,
                    )
                    continue

                links.append(
                    model.Link(
                        title=f"TileJSON link for `{name}` layer (Template URL).",
                        rel="tilejson",
                        href=f"{tilejson_endpoint}?{urlencode(values, doseq=True)}",
                        templated=True,
                    )
                )

        return model.RegisterResponse(id=search_info.id, links=links)


def add_search_list_route(  # noqa: C901
    app: FastAPI,
    *,
    prefix: str = "",
    tags: Optional[List[str]] = None,
):
    """Add PgSTAC Search (of type mosaic) listing route."""

    @app.get(
        f"{prefix}/list",
        responses={200: {"description": "List Mosaics in PgSTAC."}},
        response_model=model.Infos,
        response_model_exclude_none=True,
        tags=tags,
    )
    def list_searches(  # noqa: C901
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
        """List a PgSTAC Searches."""
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
                parts = re.match("^(?P<dir>[+-]?)(?P<prop>.*)$", s.lstrip()).groupdict()  # type:ignore

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

        base_url = str(request.base_url)
        list_endpoint = str(
            app.url_path_for("list_searches").make_absolute_url(base_url=base_url)
        )

        qs = QueryParams({**request.query_params, "limit": limit, "offset": offset})
        links = [
            model.Link(rel="self", href=f"{list_endpoint}?{qs}"),
        ]

        if len(searches_info) < nb_items:
            next_token = offset + len(searches_info)
            qs = QueryParams(
                {**request.query_params, "limit": limit, "offset": next_token}
            )
            links.append(
                model.Link(rel="next", href=f"{list_endpoint}?{qs}"),
            )

        if offset > 0:
            prev_token = offset - limit if (offset - limit) > 0 else 0
            qs = QueryParams(
                {**request.query_params, "limit": limit, "offset": prev_token}
            )
            links.append(
                model.Link(rel="prev", href=f"{list_endpoint}?{qs}"),
            )

        tilejson_endpoint = None
        try:
            tilejson_endpoint = str(
                app.url_path_for(
                    "tilejson",
                    search_id="{search_id}",
                    tileMatrixSetId="{tileMatrixSetId}",
                ).make_absolute_url(base_url=base_url)
            )
        except NoMatchFound:
            pass

        mosaic_info_endpoint = None
        try:
            mosaic_info_endpoint = str(
                app.url_path_for("info", search_id="{search_id}").make_absolute_url(
                    base_url=base_url
                )
            )
        except NoMatchFound:
            pass

        searches = []
        for search in searches_info:
            search_links: List[model.Link] = []
            if mosaic_info_endpoint:
                search_links.append(
                    model.Link(
                        rel="metadata",
                        title="Mosaic metadata",
                        href=mosaic_info_endpoint.replace("{search_id}", search.id),
                    ),
                )

            if tilejson_endpoint:
                search_links.append(
                    model.Link(
                        rel="tilejson",
                        title="Link for TileJSON (Template URL)",
                        href=tilejson_endpoint.replace("{search_id}", search.id),
                        templated=True,
                    ),
                )

            searches.append(model.Info(search=search, links=search_links))

        return model.Infos(
            searches=searches,
            links=links,
            context=model.Context(
                returned=len(searches_info),
                matched=nb_items,
                limit=limit,
            ),
        )
