"""titiler.pgstac extensions."""

from dataclasses import dataclass
from typing import List

from cogeo_mosaic.errors import MosaicNotFoundError
from fastapi import Depends
from psycopg.rows import class_row
from starlette.requests import Request
from starlette.routing import NoMatchFound

from titiler.core.factory import FactoryExtension
from titiler.pgstac import model
from titiler.pgstac.factory import MosaicTilerFactory


@dataclass
class searchInfoExtension(FactoryExtension):
    """Add /info endpoint"""

    def register(self, factory: MosaicTilerFactory):
        """Register endpoint to the tiler factory."""

        @factory.router.get(
            "/{search_id}/info",
            responses={200: {"description": "Get Search query metadata."}},
            response_model=model.Info,
            response_model_exclude_none=True,
        )
        def info_search(request: Request, search_id=Depends(factory.path_dependency)):
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
                    href=factory.url_for(
                        request, "info_search", search_id=search_info.id
                    ),
                ),
                model.Link(
                    title="Link for TileJSON (Template URL)",
                    rel="tilejson",
                    href=factory.url_for(request, "tilejson", search_id=search_info.id),
                ),
            ]

            try:
                links.append(
                    model.Link(
                        rel="map",
                        title="Link for Map viewer (Template URL)",
                        href=factory.url_for(
                            request, "map_viewer", search_id=search_info.id
                        ),
                    )
                )
            except NoMatchFound:
                pass

            try:
                links.append(
                    model.Link(
                        rel="wmts",
                        title="Link for WMTS (Template URL)",
                        href=factory.url_for(request, "wmts", search_id=search_info.id),
                    )
                )
            except NoMatchFound:
                pass

            return model.Info(search=search_info, links=links)
