"""titiler.pgstac extensions."""

import warnings
from collections.abc import Callable
from typing import Annotated, Any
from urllib.parse import urlencode

import jinja2
import rasterio
from attrs import define, field
from fastapi import Depends, Query
from morecantile.models import crs_axis_inverted
from rasterio.crs import CRS
from rio_tiler.constants import WGS84_CRS
from rio_tiler.utils import CRS_to_urn
from starlette.datastructures import QueryParams
from starlette.requests import Request
from starlette.routing import NoMatchFound
from starlette.templating import Jinja2Templates

from titiler.core.factory import FactoryExtension, MultiBaseTilerFactory
from titiler.core.resources.enums import ImageType
from titiler.core.resources.responses import XMLResponse
from titiler.core.utils import (
    check_query_params,
    rio_crs_to_pyproj,
    tms_limits,
    tms_limits_to_xml,
    tms_to_xml,
)
from titiler.pgstac import model
from titiler.pgstac.errors import NoLayerFound
from titiler.pgstac.factory import MosaicTilerFactory, logger

jinja2_env = jinja2.Environment(
    autoescape=jinja2.select_autoescape(["xml"]),
    loader=jinja2.ChoiceLoader([jinja2.PackageLoader(__package__, "templates")]),
)
DEFAULT_TEMPLATES = Jinja2Templates(env=jinja2_env)


@define
class searchInfoExtension(FactoryExtension):
    """Add /info endpoint"""

    def register(self, factory: MosaicTilerFactory):  # type: ignore [override]  # noqa: C901
        """Register endpoint to the tiler factory."""

        @factory.router.get(
            "/info",
            responses={200: {"description": "Get Search query metadata."}},
            response_model=model.Info,
            response_model_exclude_none=True,
            operation_id=f"{factory.operation_prefix}getInfo",
        )
        def info(  # noqa: C901
            request: Request,
            search_id=Depends(factory.path_dependency),
            backend_params=Depends(factory.backend_dependency),
        ):
            """Get Search query metadata."""
            logger.info(
                f"opening data with backend: {factory.backend} and reader {factory.dataset_reader}"
            )
            with factory.backend(
                search_id,
                reader=factory.dataset_reader,
                **backend_params.as_dict(),
            ) as src_dst:
                search_info = src_dst.info()

            links: list[model.Link] = [
                model.Link(
                    rel="self",
                    title="Mosaic metadata",
                    href=factory.url_for(request, "info"),
                ),
            ]

            layers: list[tuple[str, str]] = []
            if renders := search_info.metadata.defaults_params:
                # List of dependencies a `/tile` URL should validate
                # Note: Those dependencies should only require Query() inputs
                tile_dependencies: list[Callable] = [
                    factory.layer_dependency,
                    factory.dataset_dependency,
                    factory.pixel_selection_dependency,
                    factory.process_dependency,
                    factory.colormap_dependency,
                    factory.render_dependency,
                    factory.assets_accessor_dependency,
                    factory.reader_dependency,
                    factory.backend_dependency,
                ]

                for name, values in renders.items():
                    if check_query_params(tile_dependencies, values):
                        layers.append((name, urlencode(values, doseq=True)))
                    else:
                        warnings.warn(
                            f"Cannot construct URL for layer `{name}`",
                            UserWarning,
                            stacklevel=2,
                        )

            try:
                tilejson_endpoint = factory.url_for(
                    request, "tilejson", tileMatrixSetId="{tileMatrixSetId}"
                )
                links.append(
                    model.Link(
                        title="TileJSON link (Template URL).",
                        rel="tilejson",
                        href=tilejson_endpoint,
                        templated=True,
                    ),
                )
                for layer, qs in layers:
                    links.append(
                        model.Link(
                            title=f"TileJSON link for `{layer}` layer (Template URL).",
                            rel="tilejson",
                            href=tilejson_endpoint + f"?{qs}",
                            templated=True,
                        ),
                    )

            except NoMatchFound:
                pass

            try:
                map_viewer_endpoint = factory.url_for(
                    request, "map_viewer", tileMatrixSetId="{tileMatrixSetId}"
                )
                links.append(
                    model.Link(
                        rel="map",
                        title="Map viewer link (Template URL).",
                        href=map_viewer_endpoint,
                        templated=True,
                    )
                )
                for layer, qs in layers:
                    links.append(
                        model.Link(
                            title=f"Map viewer link for `{layer}` layer (Template URL).",
                            rel="map",
                            href=map_viewer_endpoint + f"?{qs}",
                            templated=True,
                        ),
                    )

            except NoMatchFound:
                pass

            try:
                wmts_endpoint = factory.url_for(request, "wmts")
                links.append(
                    model.Link(
                        rel="wmts",
                        title="WMTS Capabilities link.",
                        href=wmts_endpoint,
                    )
                )

            except NoMatchFound:
                pass

            return model.Info(search=search_info, links=links)


@define
class wmtsExtensionMosaic(FactoryExtension):
    """WMTS Extension for MosaicTilerFactory."""

    # Geographic Coordinate Reference System.
    crs: CRS = field(default=WGS84_CRS)

    templates: Jinja2Templates = field(default=DEFAULT_TEMPLATES)

    def register(self, factory: MosaicTilerFactory):  # type: ignore [override] # noqa: C901
        """Register endpoint to the tiler factory."""

        @factory.router.get(
            "/WMTSCapabilities.xml",
            response_class=XMLResponse,
            operation_id=f"{factory.operation_prefix}getWMTS",
        )
        def wmts(  # noqa: C901
            request: Request,
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
            use_epsg: Annotated[
                bool,
                Query(
                    description="Use EPSG code, not opengis.net, for the ows:SupportedCRS in the TileMatrixSet (set to True to enable ArcMap compatability)"
                ),
            ] = False,
            src_path=Depends(factory.path_dependency),
            backend_params=Depends(factory.backend_dependency),
            reader_params=Depends(factory.reader_dependency),
            env=Depends(factory.environment_dependency),
        ):
            """OGC WMTS endpoint."""
            qs_key_to_remove = [
                "tile_format",
                "tile_scale",
                "service",
                "use_epsg",
                "request",
            ]

            with rasterio.Env(**env):
                with factory.backend(
                    src_path,
                    reader=factory.dataset_reader,
                    reader_options=reader_params.as_dict(),
                    **backend_params.as_dict(),
                ) as src_dst:
                    bounds = src_dst.get_geographic_bounds(self.crs)
                    search_info = src_dst.info()

            # List of dependencies a `/tile` URL should validate
            # Note: Those dependencies should only require Query() inputs
            tile_dependencies: list[Callable] = [
                factory.backend_dependency,
                factory.reader_dependency,
                factory.assets_accessor_dependency,
                factory.layer_dependency,
                factory.dataset_dependency,
                factory.pixel_selection_dependency,
                factory.tile_dependency,
                factory.process_dependency,
                factory.colormap_dependency,
                factory.render_dependency,
            ]

            renders: list[dict[str, Any]] = []

            # LAYERS from mosaic metadata
            if render_metadata := search_info.metadata.defaults_params:
                for name, values in render_metadata.items():
                    if check_query_params(tile_dependencies, values):
                        renders.append(
                            {
                                "name": name,
                                "query_string": urlencode(values, doseq=True)
                                if values
                                else None,
                            }
                        )
                    else:
                        warnings.warn(
                            f"Cannot construct URL for layer `{name}`",
                            UserWarning,
                            stacklevel=2,
                        )

            # LAYER from query-parameters
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
                renders.append({"name": "default", "query_string": qs})

            if not renders:
                raise NoLayerFound(
                    "Could not find any valid layers in metadata or construct one from Query Parameters."
                )

            tileMatrixSet = []
            for tms_id in factory.supported_tms.list():
                tms = factory.supported_tms.get(tms_id)
                try:
                    with rasterio.Env(**env):
                        with factory.backend(
                            src_path,
                            tms=tms,
                            reader=factory.dataset_reader,
                            reader_options=reader_params.as_dict(),
                            **backend_params.as_dict(),
                        ) as src_dst:
                            tms_minzoom = src_dst.minzoom
                            tms_maxzoom = src_dst.maxzoom

                            _limits = tms_limits(
                                tms,
                                bounds,
                                zooms=(tms_minzoom, tms_maxzoom),
                                geographic_crs=self.crs,
                            )

                    if use_epsg:
                        supported_crs = f"EPSG:{tms.crs.to_epsg()}"
                    else:
                        supported_crs = tms.crs.srs

                    tileMatrixSet.append(
                        {
                            "id": tms_id,
                            "tilematrix": tms_to_xml(tms, tms_minzoom, tms_maxzoom),
                            "crs": supported_crs,
                            "limits": tms_limits_to_xml(_limits),
                        }
                    )
                except Exception as e:  # noqa
                    pass

            bbox_crs_type = "WGS84BoundingBox"
            bbox_crs_uri = "urn:ogc:def:crs:OGC:2:84"
            if self.crs != WGS84_CRS:
                bbox_crs_type = "BoundingBox"
                bbox_crs_uri = CRS_to_urn(self.crs)  # type: ignore
                # WGS88BoundingBox is always xy ordered, but BoundingBox must match the CRS order
                proj_crs = rio_crs_to_pyproj(self.crs)
                if crs_axis_inverted(proj_crs):
                    # match the bounding box coordinate order to the CRS
                    bounds = [bounds[1], bounds[0], bounds[3], bounds[2]]

            layers: list[dict[str, Any]] = []
            for tilematrix in tileMatrixSet:
                route_params = {
                    "z": "{TileMatrix}",
                    "x": "{TileCol}",
                    "y": "{TileRow}",
                    "scale": tile_scale,
                    "format": tile_format.value,
                    "tileMatrixSetId": tilematrix["id"],
                }
                for render in renders:
                    layers.append(
                        {
                            "is_default": False,
                            "title": render["name"],
                            "identifier": f"{render['name']}_{tilematrix['id']}",
                            "tms_identifier": tilematrix["id"],
                            "limits": tilematrix["limits"],
                            "tiles_url": factory.url_for(
                                request, "tile", **route_params
                            ),
                            "query_string": render["query_string"],
                            "bounds": bounds,
                        }
                    )

            return self.templates.TemplateResponse(
                request,
                name="wmts.xml",
                context={
                    "layers": layers,
                    "tileMatrixSets": tileMatrixSet,
                    "bbox_crs_type": bbox_crs_type,
                    "bbox_crs_uri": bbox_crs_uri,
                    "media_type": tile_format.mediatype,
                },
                media_type="application/xml",
            )


# NOTE: Maybe add this in titiler.extensions.wmts
@define
class wmtsExtensionSTAC(FactoryExtension):
    """WMTS Extension for STAC TilerFactory with support of Render extension."""

    # Geographic Coordinate Reference System.
    crs: CRS = field(default=WGS84_CRS)

    templates: Jinja2Templates = field(default=DEFAULT_TEMPLATES)

    def register(self, factory: MultiBaseTilerFactory):  # type: ignore [override] # noqa: C901
        """Register extension's endpoints."""

        @factory.router.get(
            "/WMTSCapabilities.xml",
            response_class=XMLResponse,
            operation_id=f"{factory.operation_prefix}getWMTS",
        )
        def wmts(  # noqa: C901
            request: Request,
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
            use_epsg: Annotated[
                bool,
                Query(
                    description="Use EPSG code, not opengis.net, for the ows:SupportedCRS in the TileMatrixSet (set to True to enable ArcMap compatability)"
                ),
            ] = False,
            src_path=Depends(factory.path_dependency),
            reader_params=Depends(factory.reader_dependency),
            # NOTE: We don't have endpoint dependencies to enable layers from render metadata
            env=Depends(factory.environment_dependency),
        ):
            """OGC WMTS endpoint."""
            qs_key_to_remove = [
                "tile_format",
                "tile_scale",
                "service",
                "use_epsg",
                "request",
            ]

            with rasterio.Env(**env):
                with factory.reader(src_path, **reader_params.as_dict()) as src_dst:
                    bounds = src_dst.get_geographic_bounds(self.crs)
                    stac_renders = src_dst.item.properties.get("renders", {})

            # List of dependencies a `/tile` URL should validate
            # Note: Those dependencies should only require Query() inputs
            tile_dependencies: list[Callable] = [
                factory.reader_dependency,
                factory.tile_dependency,
                factory.layer_dependency,
                factory.dataset_dependency,
                factory.process_dependency,
                factory.colormap_dependency,
                factory.render_dependency,
            ]

            renders: list[dict[str, Any]] = []

            # Check Renders
            for name, values in stac_renders.items():
                if check_query_params(tile_dependencies, values):
                    renders.append(
                        {
                            "name": name,
                            "query_string": urlencode(values, doseq=True)
                            if values
                            else None,
                        }
                    )
                else:
                    warnings.warn(
                        f"Cannot construct URL for layer `{name}`",
                        UserWarning,
                        stacklevel=2,
                    )

            # LAYER from query-parameters
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
            # 2. if there is no layers (from STAC Render metadata) we raise the caught error
            # 3. if there no errors we then add a default `layer` to the layers stack
            if check_query_params(tile_dependencies, QueryParams(qs)):
                renders.append({"name": "default", "query_string": qs})

            if not renders:
                raise NoLayerFound(
                    "Could not find any valid layers in metadata or construct one from Query Parameters."
                )

            tileMatrixSet: list[dict[str, Any]] = []
            for tms_id in factory.supported_tms.list():
                tms = factory.supported_tms.get(tms_id)
                try:
                    with rasterio.Env(**env):
                        with factory.reader(
                            src_path,
                            tms=tms,
                            **reader_params.as_dict(),
                        ) as src_dst:
                            tms_minzoom = src_dst.minzoom
                            tms_maxzoom = src_dst.maxzoom

                            _limits = tms_limits(
                                tms,
                                bounds,
                                zooms=(tms_minzoom, tms_maxzoom),
                                geographic_crs=self.crs,
                            )

                    if use_epsg:
                        supported_crs = f"EPSG:{tms.crs.to_epsg()}"
                    else:
                        supported_crs = tms.crs.srs

                    tileMatrixSet.append(
                        {
                            "id": tms_id,
                            "tilematrix": tms_to_xml(tms, tms_minzoom, tms_maxzoom),
                            "crs": supported_crs,
                            "limits": tms_limits_to_xml(_limits),
                        }
                    )
                except Exception as e:  # noqa
                    pass

            bbox_crs_type = "WGS84BoundingBox"
            bbox_crs_uri = "urn:ogc:def:crs:OGC:2:84"
            if self.crs != WGS84_CRS:
                bbox_crs_type = "BoundingBox"
                bbox_crs_uri = CRS_to_urn(self.crs)  # type: ignore
                # WGS88BoundingBox is always xy ordered, but BoundingBox must match the CRS order
                proj_crs = rio_crs_to_pyproj(self.crs)
                if crs_axis_inverted(proj_crs):
                    # match the bounding box coordinate order to the CRS
                    bounds = [bounds[1], bounds[0], bounds[3], bounds[2]]

            layers: list[dict[str, Any]] = []
            for tilematrix in tileMatrixSet:
                route_params = {
                    "z": "{TileMatrix}",
                    "x": "{TileCol}",
                    "y": "{TileRow}",
                    "scale": tile_scale,
                    "format": tile_format.value,
                    "tileMatrixSetId": tilematrix["id"],
                }
                for render in renders:
                    layers.append(
                        {
                            "is_default": False,
                            "title": render["name"],
                            "identifier": f"{render['name']}_{tilematrix['id']}",
                            "tms_identifier": tilematrix["id"],
                            "limits": tilematrix["limits"],
                            "tiles_url": factory.url_for(
                                request, "tile", **route_params
                            ),
                            "query_string": render["query_string"],
                            "bounds": bounds,
                        }
                    )

            return self.templates.TemplateResponse(
                request,
                name="wmts.xml",
                context={
                    "layers": layers,
                    "tileMatrixSets": tileMatrixSet,
                    "bbox_crs_type": bbox_crs_type,
                    "bbox_crs_uri": bbox_crs_uri,
                    "media_type": tile_format.mediatype,
                },
                media_type="application/xml",
            )
