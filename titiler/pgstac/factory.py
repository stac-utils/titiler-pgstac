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
    Set,
    Tuple,
    Type,
    Union,
)
from urllib.parse import urlencode

import rasterio
from attrs import define, field
from cogeo_mosaic.errors import MosaicNotFoundError
from fastapi import Body, Depends, FastAPI, Path, Query
from geojson_pydantic import Feature, FeatureCollection
from morecantile import TileMatrixSets
from morecantile import tms as morecantile_tms
from morecantile.models import crs_axis_inverted
from psycopg import errors as pgErrors
from psycopg import sql
from psycopg.rows import class_row, dict_row
from pydantic import Field
from rio_tiler.constants import MAX_THREADS, WGS84_CRS
from rio_tiler.utils import CRS_to_urn
from starlette.datastructures import QueryParams
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import NoMatchFound
from starlette.templating import Jinja2Templates
from typing_extensions import Annotated

from titiler.core.dependencies import (
    AssetsBidxExprParams,
    CoordCRSParams,
    DefaultDependency,
    DstCRSParams,
    HistogramParams,
    PartFeatureParams,
    StatisticsParams,
)
from titiler.core.factory import DEFAULT_TEMPLATES, img_endpoint_params
from titiler.core.models.mapbox import TileJSON
from titiler.core.models.responses import MultiBaseStatisticsGeoJSON
from titiler.core.resources.enums import ImageType, MediaType, OptionalHeader
from titiler.core.resources.responses import GeoJSONResponse, XMLResponse
from titiler.core.utils import check_query_params, render_image
from titiler.mosaic.factory import MosaicTilerFactory as BaseFactory
from titiler.pgstac import model
from titiler.pgstac.backend import PGSTACBackend
from titiler.pgstac.dependencies import BackendParams, PgSTACParams, SearchParams
from titiler.pgstac.errors import NoLayerFound, ReadOnlyPgSTACError
from titiler.pgstac.reader import SimpleSTACReader

MOSAIC_THREADS = int(os.getenv("MOSAIC_CONCURRENCY", MAX_THREADS))
MOSAIC_STRICT_ZOOM = str(os.getenv("MOSAIC_STRICT_ZOOM", False)).lower() in [
    "true",
    "yes",
]


def _first_value(values: List[Any], default: Any = None):
    """Return the first not None value."""
    return next(filter(lambda x: x is not None, values), default)


@define(kw_only=True)
class MosaicTilerFactory(BaseFactory):
    """Custom MosaicTiler for PgSTAC Mosaic Backend."""

    path_dependency: Callable[..., str]

    backend: Type[PGSTACBackend] = PGSTACBackend
    backend_dependency: Type[DefaultDependency] = BackendParams

    # Backend.get_assets() Options
    assets_accessor_dependency: Type[DefaultDependency] = PgSTACParams

    # Rasterio Dataset Options (nodata, unscale, resampling, reproject)
    dataset_reader: Type[SimpleSTACReader] = SimpleSTACReader

    # Assets/Indexes/Expression Dependencies
    layer_dependency: Type[DefaultDependency] = AssetsBidxExprParams

    # Statistics/Histogram Dependencies
    stats_dependency: Type[DefaultDependency] = StatisticsParams
    histogram_dependency: Type[DefaultDependency] = HistogramParams

    # Crop endpoints Dependencies
    # WARNINGS: `/bbox` and `/feature` endpoints should be used carefully because
    # each request might need to open/read a lot of files if the user decide to
    # submit large bbox/geojson. This will also depends on the STAC Items resolution.
    img_part_dependency: Type[DefaultDependency] = PartFeatureParams

    supported_tms: TileMatrixSets = morecantile_tms

    templates: Jinja2Templates = DEFAULT_TEMPLATES

    render_func: Callable[..., Tuple[bytes, str]] = render_image

    optional_headers: List[OptionalHeader] = field(factory=list)

    # Add/Remove some endpoints
    add_viewer: bool = False
    add_statistics: bool = False
    add_part: bool = False

    conforms_to: Set[str] = field(
        factory=lambda: {
            # https://docs.ogc.org/is/20-057/20-057.html#toc30
            "http://www.opengis.net/spec/ogcapi-tiles-1/1.0/req/tileset",
            # https://docs.ogc.org/is/20-057/20-057.html#toc34
            "http://www.opengis.net/spec/ogcapi-tiles-1/1.0/req/tilesets-list",
            # https://docs.ogc.org/is/20-057/20-057.html#toc65
            "http://www.opengis.net/spec/ogcapi-tiles-1/1.0/req/core",
            "http://www.opengis.net/spec/ogcapi-tiles-1/1.0/req/png",
            "http://www.opengis.net/spec/ogcapi-tiles-1/1.0/req/jpeg",
            "http://www.opengis.net/spec/ogcapi-tiles-1/1.0/req/tiff",
        }
    )

    def register_routes(self) -> None:
        """This Method register routes to the router."""
        self.tilesets()
        self.tile()
        if self.add_viewer:
            self.map_viewer()
        self.tilejson()
        self.wmts()
        self.point()
        self.assets()

        if self.add_part:
            self.part()

        if self.add_statistics:
            self.statistics()

    def tilejson(self) -> None:
        """register tiles routes."""

        @self.router.get(
            "/{tileMatrixSetId}/tilejson.json",
            response_model=TileJSON,
            responses={200: {"description": "Return a tilejson"}},
            response_model_exclude_none=True,
            operation_id=f"{self.operation_prefix}getTileJSON",
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
            assets_accessor_params=Depends(self.assets_accessor_dependency),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
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

    def wmts(self):  # noqa: C901
        """Add wmts endpoint."""

        @self.router.get(
            "/{tileMatrixSetId}/WMTSCapabilities.xml",
            response_class=XMLResponse,
            operation_id=f"{self.operation_prefix}getWMTS",
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
                self.assets_accessor_dependency,
                self.layer_dependency,
                self.dataset_dependency,
                self.pixel_selection_dependency,
                self.tile_dependency,
                self.process_dependency,
                self.render_dependency,
                self.reader_dependency,
                self.backend_dependency,
            ]

            layers: List[Dict[str, Any]] = []

            # LAYERS from mosaic metadata
            if renders := search_info.metadata.defaults_params:
                for name, values in renders.items():
                    if check_query_params(tile_dependencies, values):
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
                    else:
                        warnings.warn(
                            f"Cannot construct URL for layer `{name}`",
                            UserWarning,
                            stacklevel=2,
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
            qs = urlencode(
                [
                    (key, value)
                    for (key, value) in request.query_params._list
                    if key.lower() not in qs_key_to_remove
                ],
                doseq=True,
            )

            # Checking if we can construct a valid tile URL
            # 1. we use `check_query_params` to validate the query-parameter
            # 2. if there is no layers (from mosaic metadata) we raise the caught error
            # 3. if there no errors we then add a default `layer` to the layers stack
            if check_query_params(tile_dependencies, QueryParams(qs)):
                layers.append(
                    {
                        "titler": search_info.metadata.name or search_id,
                        "name": "default",
                        "tiles_url": tiles_url,
                        "query_string": qs if qs else None,
                        "bounds": bounds,
                    }
                )

            if not layers:
                raise NoLayerFound(
                    "Could not find any valid layers in metadata or construct one from Query Parameters."
                )

            bbox_crs_type = "WGS84BoundingBox"
            bbox_crs_uri = "urn:ogc:def:crs:OGC:2:84"
            if tms.rasterio_geographic_crs != WGS84_CRS:
                bbox_crs_type = "BoundingBox"
                bbox_crs_uri = CRS_to_urn(tms.rasterio_geographic_crs)
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
            operation_id=f"{self.operation_prefix}postStatisticsForGeoJSON",
        )
        def geojson_statistics(
            geojson: Annotated[
                Union[FeatureCollection, Feature],
                Body(description="GeoJSON Feature or FeatureCollection."),
            ],
            search_id=Depends(self.path_dependency),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            assets_accessor_params=Depends(self.assets_accessor_dependency),
            coord_crs=Depends(CoordCRSParams),
            dst_crs=Depends(DstCRSParams),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            image_params=Depends(self.img_part_dependency),
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
                    for feature in fc.features:
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
                            **assets_accessor_params.as_dict(),
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
            operation_id=f"{self.operation_prefix}getDataForBoundingBoxWithFormat",
            **img_endpoint_params,
        )
        @self.router.get(
            "/bbox/{minx},{miny},{maxx},{maxy}/{width}x{height}.{format}",
            operation_id=f"{self.operation_prefix}getDataForBoundingBoxWithSizesAndFormat",
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
                Field(
                    description="Default will be automatically defined if the output image needs a mask (png) or not (jpeg)."
                ),
            ] = None,
            backend_params=Depends(self.backend_dependency),
            assets_accessor_params=Depends(self.assets_accessor_dependency),
            reader_params=Depends(self.reader_dependency),
            coord_crs=Depends(CoordCRSParams),
            dst_crs=Depends(DstCRSParams),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            image_params=Depends(self.img_part_dependency),
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
                        **assets_accessor_params.as_dict(),
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
                headers["X-Assets"] = ",".join(assets)

            return Response(content, media_type=media_type, headers=headers)

        @self.router.post(
            "/feature",
            operation_id=f"{self.operation_prefix}postDataForGeoJSON",
            **img_endpoint_params,
        )
        @self.router.post(
            "/feature.{format}",
            operation_id=f"{self.operation_prefix}postDataForGeoJSONWithFormat",
            **img_endpoint_params,
        )
        @self.router.post(
            "/feature/{width}x{height}.{format}",
            operation_id=f"{self.operation_prefix}postDataForGeoJSONWithSizesAndFormat",
            **img_endpoint_params,
        )
        def feature_image(
            geojson: Annotated[Union[Feature], Body(description="GeoJSON Feature.")],
            search_id=Depends(self.path_dependency),
            format: Annotated[
                ImageType,
                Field(
                    description="Default will be automatically defined if the output image needs a mask (png) or not (jpeg)."
                ),
            ] = None,
            backend_params=Depends(self.backend_dependency),
            assets_accessor_params=Depends(self.assets_accessor_dependency),
            reader_params=Depends(self.reader_dependency),
            coord_crs=Depends(CoordCRSParams),
            dst_crs=Depends(DstCRSParams),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            image_params=Depends(self.img_part_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
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
                        **assets_accessor_params.as_dict(),
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
                headers["X-Assets"] = ",".join(assets)

            return Response(content, media_type=media_type, headers=headers)


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

    name = prefix.replace("/", ".")
    operation_prefix = f"{name}." if name else ""

    @app.post(
        f"{prefix}/register",
        responses={200: {"description": "Register a Virtual Mosaic (PgSTAC Search)."}},
        response_model=model.RegisterResponse,
        response_model_exclude_none=True,
        tags=tags,
        operation_id=f"{operation_prefix}Register",
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
                if check_query_params(tile_dependencies, values):
                    links.append(
                        model.Link(
                            title=f"TileJSON link for `{name}` layer (Template URL).",
                            rel="tilejson",
                            href=f"{tilejson_endpoint}?{urlencode(values, doseq=True)}",
                            templated=True,
                        )
                    )
                else:
                    warnings.warn(
                        f"Cannot construct URL for layer `{name}`",
                        UserWarning,
                        stacklevel=2,
                    )

        return model.RegisterResponse(id=search_info.id, links=links)


def add_search_list_route(  # noqa: C901
    app: FastAPI,
    *,
    prefix: str = "",
    tags: Optional[List[str]] = None,
):
    """Add PgSTAC Search (of type mosaic) listing route."""

    name = prefix.replace("/", ".")
    operation_prefix = f"{name}." if name else ""

    @app.get(
        f"{prefix}/list",
        responses={200: {"description": "List Mosaics in PgSTAC."}},
        response_model=model.Infos,
        response_model_exclude_none=True,
        tags=tags,
        operation_id=f"{operation_prefix}getMosaicList",
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
