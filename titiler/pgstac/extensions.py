"""titiler.pgstac extensions."""

import warnings
from dataclasses import dataclass
from typing import List, Tuple
from urllib.parse import urlencode

from cogeo_mosaic.errors import MosaicNotFoundError
from fastapi import Depends
from psycopg.rows import class_row
from starlette.datastructures import QueryParams
from starlette.requests import Request
from starlette.routing import NoMatchFound

from titiler.core.factory import FactoryExtension
from titiler.pgstac import model
from titiler.pgstac.factory import MosaicTilerFactory, check_query_params


@dataclass
class searchInfoExtension(FactoryExtension):
    """Add /info endpoint"""

    def register(self, factory: MosaicTilerFactory):  # noqa: C901
        """Register endpoint to the tiler factory."""

        @factory.router.get(
            "/info",
            responses={200: {"description": "Get Search query metadata."}},
            response_model=model.Info,
            response_model_exclude_none=True,
        )
        def info_search(  # noqa: C901
            request: Request, search_id=Depends(factory.path_dependency)
        ):
            """Get Search query metadata."""
            with request.app.state.dbpool.connection() as conn:
                with conn.cursor(row_factory=class_row(model.Search)) as cursor:
                    cursor.execute(
                        "SELECT * FROM searches WHERE hash=%s;",
                        (search_id,),
                    )
                    search_info = cursor.fetchone()

            if not search_info:
                raise MosaicNotFoundError(f"SearchId `{search_id}` not found")

            links: List[model.Link] = [
                model.Link(
                    rel="self",
                    title="Mosaic metadata",
                    href=factory.url_for(request, "info_search"),
                ),
            ]

            layers: List[Tuple[str, str]] = []
            if search_info.metadata.defaults:
                # List of dependencies a `/tile` URL should validate
                # Note: Those dependencies should only require Query() inputs
                tile_dependencies = [
                    factory.layer_dependency,
                    factory.dataset_dependency,
                    factory.pixel_selection_dependency,
                    factory.process_dependency,
                    factory.rescale_dependency,
                    factory.colormap_dependency,
                    factory.render_dependency,
                    factory.pgstac_dependency,
                    factory.reader_dependency,
                    factory.backend_dependency,
                ]

                for name, values in search_info.metadata.defaults.items():
                    query_string = urlencode(values, doseq=True)
                    try:
                        check_query_params(
                            dependencies=tile_dependencies,
                            query_params=QueryParams(query_string),
                        )
                    except Exception as e:
                        warnings.warn(
                            f"Cannot construct URL for layer `{name}`: {repr(e)}",
                            UserWarning,
                            stacklevel=2,
                        )
                        continue
                    layers.append((name, query_string))

            try:
                tilejson_endpoint = factory.url_for(request, "tilejson")
                links.append(
                    model.Link(
                        title="TileJSON link (Template URL)",
                        rel="tilejson",
                        href=tilejson_endpoint,
                    ),
                )
                for layer, qs in layers:
                    links.append(
                        model.Link(
                            title=f"TileJSON link for `{layer}` layer",
                            rel="tilejson",
                            href=tilejson_endpoint + f"?{qs}",
                        ),
                    )

            except NoMatchFound:
                pass

            try:
                map_viewer_endpoint = factory.url_for(request, "map_viewer")
                links.append(
                    model.Link(
                        rel="map",
                        title="Map viewer link (Template URL)",
                        href=map_viewer_endpoint,
                    )
                )
                for layer, qs in layers:
                    links.append(
                        model.Link(
                            title=f"Map viewer link for `{layer}` layer",
                            rel="map",
                            href=map_viewer_endpoint + f"?{qs}",
                        ),
                    )

            except NoMatchFound:
                pass

            try:
                wmts_endpoint = factory.url_for(request, "wmts")
                links.append(
                    model.Link(
                        rel="wmts",
                        title="WMTS link (Template URL)",
                        href=wmts_endpoint,
                    )
                )
                for _layer, qs in layers:
                    links.append(
                        model.Link(
                            title=f"WMTS link for `{layer}` layer",
                            rel="wmts",
                            href=wmts_endpoint + f"?{qs}",
                        ),
                    )

            except NoMatchFound:
                pass

            return model.Info(search=search_info, links=links)
