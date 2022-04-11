"""Custom MosaicTiler Factory for PgSTAC Mosaic Backend."""

import os
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union
from urllib.parse import urlencode

import rasterio
from cogeo_mosaic.backends import BaseBackend
from geojson_pydantic import Feature, FeatureCollection
from morecantile import TileMatrixSet
from psycopg.rows import class_row
from rio_tiler.constants import MAX_THREADS
from rio_tiler.models import BandStatistics
from rio_tiler.utils import get_array_statistics

from titiler.core.dependencies import AssetsBidxExprParams, DefaultDependency
from titiler.core.factory import BaseTilerFactory, img_endpoint_params
from titiler.core.models.mapbox import TileJSON
from titiler.core.models.responses import MultiBaseStatisticsGeoJSON
from titiler.core.resources.enums import ImageType, OptionalHeader
from titiler.core.resources.responses import GeoJSONResponse
from titiler.core.utils import Timer
from titiler.mosaic.resources.enums import PixelSelectionMethod
from titiler.pgstac import model
from titiler.pgstac.dependencies import PathParams, PgSTACParams, SearchParams
from titiler.pgstac.mosaic import PGSTACBackend

from fastapi import Body, Depends, Path, Query

from starlette.requests import Request
from starlette.responses import Response


def _first_value(values: List[Any], default: Any = None):
    """Return the first not None value."""
    return next(filter(lambda x: x is not None, values), default)


@dataclass
class MosaicTilerFactory(BaseTilerFactory):
    """Custom MosaicTiler for PgSTAC Mosaic Backend."""

    reader: Type[BaseBackend] = PGSTACBackend
    path_dependency: Callable[..., str] = PathParams
    layer_dependency: Type[DefaultDependency] = AssetsBidxExprParams

    # Search dependency
    search_dependency: Callable[
        ..., Tuple[model.PgSTACSearch, model.Metadata]
    ] = SearchParams

    backend_options: Dict = field(default_factory=dict)

    # Add/Remove some endpoints
    add_statistics: bool = False

    def register_routes(self) -> None:
        """This Method register routes to the router."""
        self._search_routes()
        self._tiles_routes()
        self._assets_routes()
        if self.add_statistics:
            self._statistics_routes()

    def _tiles_routes(self) -> None:
        """register tiles routes."""

        @self.router.get("/tiles/{searchid}/{z}/{x}/{y}", **img_endpoint_params)
        @self.router.get(
            "/tiles/{searchid}/{z}/{x}/{y}.{format}", **img_endpoint_params
        )
        @self.router.get(
            "/tiles/{searchid}/{z}/{x}/{y}@{scale}x", **img_endpoint_params
        )
        @self.router.get(
            "/tiles/{searchid}/{z}/{x}/{y}@{scale}x.{format}", **img_endpoint_params
        )
        @self.router.get(
            "/tiles/{searchid}/{TileMatrixSetId}/{z}/{x}/{y}", **img_endpoint_params
        )
        @self.router.get(
            "/tiles/{searchid}/{TileMatrixSetId}/{z}/{x}/{y}.{format}",
            **img_endpoint_params,
        )
        @self.router.get(
            "/tiles/{searchid}/{TileMatrixSetId}/{z}/{x}/{y}@{scale}x",
            **img_endpoint_params,
        )
        @self.router.get(
            "/tiles/{searchid}/{TileMatrixSetId}/{z}/{x}/{y}@{scale}x.{format}",
            **img_endpoint_params,
        )
        def tile(
            request: Request,
            searchid=Depends(self.path_dependency),
            z: int = Path(..., ge=0, le=30, description="Tile's zoom level"),
            x: int = Path(..., description="Tile's column"),
            y: int = Path(..., description="Tile's row"),
            tms: TileMatrixSet = Depends(self.tms_dependency),
            scale: int = Query(
                1, gt=0, lt=4, description="Tile size scale. 1=256x256, 2=512x512..."
            ),
            format: ImageType = Query(
                None, description="Output image type. Default is auto."
            ),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection: PixelSelectionMethod = Query(
                PixelSelectionMethod.first, description="Pixel selection method."
            ),
            postprocess_params=Depends(self.process_dependency),
            colormap=Depends(self.colormap_dependency),
            render_params=Depends(self.render_dependency),
            tile_buffer: Optional[float] = Query(
                None,
                gt=0,
                alias="buffer",
                title="Tile buffer.",
                description="Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * tile_buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).",
            ),
            pgstac_params: PgSTACParams = Depends(),
        ):
            """Create map tile."""
            timings = []
            headers: Dict[str, str] = {}

            tilesize = scale * 256

            threads = int(os.getenv("MOSAIC_CONCURRENCY", MAX_THREADS))
            with Timer() as t:
                with rasterio.Env(**self.gdal_config):
                    with self.reader(
                        searchid,
                        pool=request.app.state.dbpool,
                        tms=tms,
                        **self.backend_options,
                    ) as src_dst:
                        mosaic_read = t.from_start
                        timings.append(("mosaicread", round(mosaic_read * 1000, 2)))

                        data, _ = src_dst.tile(
                            x,
                            y,
                            z,
                            pixel_selection=pixel_selection.method(),
                            tilesize=tilesize,
                            threads=threads,
                            tile_buffer=tile_buffer,
                            **layer_params,
                            **dataset_params,
                            **pgstac_params,
                        )
            timings.append(("dataread", round((t.elapsed - mosaic_read) * 1000, 2)))

            if not format:
                format = ImageType.jpeg if data.mask.all() else ImageType.png

            with Timer() as t:
                image = data.post_process(**postprocess_params)
            timings.append(("postprocess", round(t.elapsed * 1000, 2)))

            with Timer() as t:
                content = image.render(
                    img_format=format.driver,
                    colormap=colormap,
                    **format.profile,
                    **render_params,
                )
            timings.append(("format", round(t.elapsed * 1000, 2)))

            if OptionalHeader.server_timing in self.optional_headers:
                headers["Server-Timing"] = ", ".join(
                    [f"{name};dur={time}" for (name, time) in timings]
                )

            if OptionalHeader.x_assets in self.optional_headers:
                ids = [x["id"] for x in data.assets]
                headers["X-Assets"] = ",".join(ids)

            return Response(content, media_type=format.mediatype, headers=headers)

        @self.router.get(
            "/{searchid}/tilejson.json",
            response_model=TileJSON,
            responses={200: {"description": "Return a tilejson"}},
            response_model_exclude_none=True,
        )
        @self.router.get(
            "/{searchid}/{TileMatrixSetId}/tilejson.json",
            response_model=TileJSON,
            responses={200: {"description": "Return a tilejson"}},
            response_model_exclude_none=True,
        )
        def tilejson(
            request: Request,
            searchid=Depends(self.path_dependency),
            tms: TileMatrixSet = Depends(self.tms_dependency),
            tile_format: Optional[ImageType] = Query(
                None, description="Output image type. Default is auto."
            ),
            tile_scale: int = Query(
                1, gt=0, lt=4, description="Tile size scale. 1=256x256, 2=512x512..."
            ),
            minzoom: Optional[int] = Query(
                None, description="Overwrite default minzoom."
            ),
            maxzoom: Optional[int] = Query(
                None, description="Overwrite default maxzoom."
            ),
            layer_params=Depends(self.layer_dependency),  # noqa
            dataset_params=Depends(self.dataset_dependency),  # noqa
            pixel_selection: PixelSelectionMethod = Query(
                PixelSelectionMethod.first, description="Pixel selection method."
            ),  # noqa
            postprocess_params=Depends(self.process_dependency),  # noqa
            colormap=Depends(self.colormap_dependency),  # noqa
            render_params=Depends(self.render_dependency),  # noqa
            tile_buffer: Optional[float] = Query(  # noqa
                None,
                gt=0,
                alias="buffer",
                title="Tile buffer.",
                description="Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * tile_buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).",
            ),
            pgstac_params: PgSTACParams = Depends(),  # noqa
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
                        raise KeyError(f"search {searchid} not found")

            route_params = {
                "searchid": search_info.id,
                "z": "{z}",
                "x": "{x}",
                "y": "{y}",
                "scale": tile_scale,
                "TileMatrixSetId": tms.identifier,
            }
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

    def _assets_routes(self):
        """Register assets routes."""

        @self.router.get(
            "/{searchid}/{z}/{x}/{y}/assets",
            responses={200: {"description": "Return list of assets"}},
        )
        @self.router.get(
            "/{searchid}/{TileMatrixSetId}/{z}/{x}/{y}/assets",
            responses={200: {"description": "Return list of assets"}},
            response_model=List[Dict],
        )
        def assets_for_tile(
            request: Request,
            searchid=Depends(self.path_dependency),
            z: int = Path(..., ge=0, le=30, description="Tiles's zoom level"),
            x: int = Path(..., description="Tiles's column"),
            y: int = Path(..., description="Tiles's row"),
            tms: TileMatrixSet = Depends(self.tms_dependency),
            pgstac_params: PgSTACParams = Depends(),
        ):
            """Return a list of assets which overlap a given tile"""
            with self.reader(
                searchid,
                pool=request.app.state.dbpool,
                tms=tms,
                **self.backend_options,
            ) as src_dst:
                return src_dst.assets_for_tile(x, y, z, **pgstac_params)

        @self.router.get(
            "/{searchid}/{lon},{lat}/assets",
            responses={200: {"description": "Return list of assets"}},
            response_model=List[Dict],
        )
        def assets_for_point(
            request: Request,
            searchid=Depends(self.path_dependency),
            lon: float = Path(..., description="Longitude"),
            lat: float = Path(..., description="Latitude"),
            pgstac_params: PgSTACParams = Depends(),
        ):
            """Return a list of assets for a given point."""
            with self.reader(
                searchid,
                pool=request.app.state.dbpool,
                **self.backend_options,
            ) as src_dst:
                return src_dst.assets_for_point(lon, lat, **pgstac_params)

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
            request: Request,
            geojson: Union[FeatureCollection, Feature] = Body(
                ..., description="GeoJSON Feature or FeatureCollection."
            ),
            searchid=Depends(self.path_dependency),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection: PixelSelectionMethod = Query(
                PixelSelectionMethod.first, description="Pixel selection method."
            ),
            max_size: int = Query(1024, description="Maximum image size to read onto."),
            stats_params=Depends(self.stats_dependency),
            histogram_params=Depends(self.histogram_dependency),
            pgstac_params: PgSTACParams = Depends(),
        ):
            """Get Statistics from a geojson feature or featureCollection."""
            threads = int(os.getenv("MOSAIC_CONCURRENCY", MAX_THREADS))

            with rasterio.Env(**self.gdal_config):
                with self.reader(
                    searchid,
                    pool=request.app.state.dbpool,
                    **self.backend_options,
                ) as src_dst:
                    if isinstance(geojson, FeatureCollection):
                        for feature in geojson:
                            data, _ = src_dst.feature(
                                feature.dict(exclude_none=True),
                                pixel_selection=pixel_selection.method(),
                                threads=threads,
                                max_size=max_size,
                                **layer_params,
                                **dataset_params,
                                **pgstac_params,
                            )

                            stats = get_array_statistics(
                                data.as_masked(),
                                **stats_params,
                                **histogram_params,
                            )

                        feature.properties = feature.properties or {}
                        feature.properties.update(
                            {
                                "statistics": {
                                    f"{data.band_names[ix]}": BandStatistics(
                                        **stats[ix]
                                    )
                                    for ix in range(len(stats))
                                }
                            }
                        )

                    else:  # simple feature
                        data, _ = src_dst.feature(
                            geojson.dict(exclude_none=True),
                            pixel_selection=pixel_selection.method(),
                            threads=threads,
                            max_size=max_size,
                            **layer_params,
                            **dataset_params,
                            **pgstac_params,
                        )
                        stats = get_array_statistics(
                            data.as_masked(),
                            **stats_params,
                            **histogram_params,
                        )

                        geojson.properties = geojson.properties or {}
                        geojson.properties.update(
                            {
                                "statistics": {
                                    f"{data.band_names[ix]}": BandStatistics(
                                        **stats[ix]
                                    )
                                    for ix in range(len(stats))
                                }
                            }
                        )

            return geojson
