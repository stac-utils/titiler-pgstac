"""Custom MosaicTiler Factory for PgSTAC Mosaic Backend."""

import os
from dataclasses import dataclass, field
from typing import Callable, Dict, Optional, Type
from urllib.parse import urlencode

import rasterio
from cogeo_mosaic.backends import BaseBackend
from morecantile import TileMatrixSet
from rio_tiler.constants import MAX_THREADS

from titiler.core.dependencies import AssetsBidxExprParams, DefaultDependency, TMSParams
from titiler.core.factory import BaseTilerFactory, img_endpoint_params
from titiler.core.models.mapbox import TileJSON
from titiler.core.resources.enums import ImageType, OptionalHeader
from titiler.core.utils import Timer
from titiler.mosaic.resources.enums import PixelSelectionMethod
from titiler.pgstac.models import SearchQuery
from titiler.pgstac.mosaic import PGSTACBackend

from fastapi import Depends, Path, Query

from starlette.requests import Request
from starlette.responses import Response


def PathParams(searchid: str = Path(..., description="Search Id")) -> str:
    """SearcId"""
    return searchid


@dataclass
class PgSTACParams:
    """PgSTAC parameters."""

    scan_limit: Optional[int] = Query(
        None,
        description="Return as soon as we scan N items (defaults to 10000 in PgSTAC).",
    )
    items_limit: Optional[int] = Query(
        None,
        description="Return as soon as we have N items per geometry (defaults to 100 in PgSTAC).",
    )
    time_limit: Optional[int] = Query(
        None,
        description="Return after N seconds to avoid long requests (defaults to 5 in PgSTAC).",
    )
    exitwhenfull: Optional[bool] = Query(
        None,
        description="Return as soon as the geometry is fully covered (defaults to True in PgSTAC).",
    )
    skipcovered: Optional[bool] = Query(
        None,
        description="Skip any items that would show up completely under the previous items (defaults to True in PgSTAC).",
    )

    # Future dependencies class in titiler 0.4.0
    # Those 2 method enable dict unpacking `**PgSTACParams()`
    def keys(self):
        """Return keys."""
        return self.__dict__.keys()

    def __getitem__(self, key):
        """Return value."""
        return self.__dict__[key]


@dataclass
class MosaicTilerFactory(BaseTilerFactory):
    """Custom MosaicTiler for PgSTAC Mosaic Backend."""

    reader: BaseBackend = PGSTACBackend
    path_dependency: Callable[..., str] = PathParams
    layer_dependency: Type[DefaultDependency] = AssetsBidxExprParams

    # TileMatrixSet dependency
    tms_dependency: Callable[..., TileMatrixSet] = TMSParams

    backend_options: Dict = field(default_factory=dict)

    def register_routes(self) -> None:
        """This Method register routes to the router."""
        self._search_routes()
        self._tiles_routes()
        self._assets_routes()

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
            render_params=Depends(self.render_dependency),
            colormap=Depends(self.colormap_dependency),
            pixel_selection: PixelSelectionMethod = Query(
                PixelSelectionMethod.first, description="Pixel selection method."
            ),
            pgstac_params: PgSTACParams = Depends(),
            kwargs: Dict = Depends(self.additional_dependency),
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
                        pool=request.app.state.readpool,
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
                            threads=threads,
                            tilesize=tilesize,
                            **layer_params.kwargs,
                            **dataset_params.kwargs,
                            **pgstac_params,
                            **kwargs,
                        )
            timings.append(("dataread", round((t.elapsed - mosaic_read) * 1000, 2)))

            if not format:
                format = ImageType.jpeg if data.mask.all() else ImageType.png

            with Timer() as t:
                image = data.post_process(
                    in_range=render_params.rescale_range,
                    color_formula=render_params.color_formula,
                )
            timings.append(("postprocess", round(t.elapsed * 1000, 2)))

            with Timer() as t:
                content = image.render(
                    add_mask=render_params.return_mask,
                    img_format=format.driver,
                    colormap=colormap,
                    **format.profile,
                    **render_params.kwargs,
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
            render_params=Depends(self.render_dependency),  # noqa
            colormap=Depends(self.colormap_dependency),  # noqa
            pixel_selection: PixelSelectionMethod = Query(
                PixelSelectionMethod.first, description="Pixel selection method."
            ),  # noqa
            pgstac_params: PgSTACParams = Depends(),  # noqa
            kwargs: Dict = Depends(self.additional_dependency),  # noqa
        ):
            """Return TileJSON document for a SearchId."""
            pool = request.app.state.readpool
            conn = pool.getconn()
            try:
                with conn:
                    with conn.cursor() as cursor:
                        cursor.execute(
                            "SELECT * FROM searches WHERE hash=%s;", (searchid,),
                        )
                        r = cursor.fetchone()
                        fields = list(map(lambda x: x[0], cursor.description))
                        search_info = dict(zip(fields, r))
            finally:
                pool.putconn(conn)

            route_params = {
                "searchid": searchid,
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

            return {
                "bounds": search_info["search"].get("bbox", tms.bbox),
                "minzoom": minzoom if minzoom is not None else tms.minzoom,
                "maxzoom": maxzoom if maxzoom is not None else tms.maxzoom,
                "name": searchid,
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
                pool=request.app.state.readpool,
                tms=tms,
                **self.backend_options,
            ) as src_dst:
                return src_dst.assets_for_tile(x, y, z, **pgstac_params)

        @self.router.get(
            "/{searchid}/{lon},{lat}/assets",
            responses={200: {"description": "Return list of assets"}},
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
                searchid, pool=request.app.state.readpool, **self.backend_options,
            ) as src_dst:
                return src_dst.assets_for_point(lon, lat, **pgstac_params)

    def _search_routes(self) -> None:
        """register search routes."""

        @self.router.post(
            "/register", responses={200: {"description": "Register a Search."}},
        )
        def register_search(request: Request, body: SearchQuery):
            """Register a Search query."""
            pool = request.app.state.writepool
            conn = pool.getconn()

            try:
                with conn:
                    with conn.cursor() as cursor:
                        cursor.execute(
                            "SELECT * FROM search_query(%s);",
                            (body.json(exclude_none=True),),
                        )
                        r = cursor.fetchone()
                        fields = list(map(lambda x: x[0], cursor.description))
                        search_info = dict(zip(fields, r))
            finally:
                pool.putconn(conn)

            searchid = search_info["hash"]
            return {
                "searchid": searchid,
                "metadata": self.url_for(request, "info_search", searchid=searchid),
                "tiles": self.url_for(request, "tilejson", searchid=searchid),
            }

        @self.router.get(
            "/{searchid}/info",
            responses={200: {"description": "Get Search query metadata."}},
        )
        def info_search(request: Request, searchid=Depends(self.path_dependency)):
            """Get Search query metadata."""
            pool = request.app.state.readpool
            conn = pool.getconn()
            try:
                with conn:
                    with conn.cursor() as cursor:
                        cursor.execute(
                            "SELECT * FROM searches WHERE hash=%s;", (searchid,),
                        )
                        r = cursor.fetchone()
                        fields = list(map(lambda x: x[0], cursor.description))
                        search_info = dict(zip(fields, r))
            finally:
                pool.putconn(conn)

            return search_info
