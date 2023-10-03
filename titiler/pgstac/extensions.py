"""titiler-pgstac Extension."""

import re
import warnings
from dataclasses import dataclass
from typing import Generator, List, Optional
from urllib.parse import urlencode

from cogeo_mosaic.errors import MosaicNotFoundError
from fastapi import Depends, Query
from psycopg import sql
from psycopg.rows import class_row
from starlette.datastructures import QueryParams
from starlette.requests import Request
from starlette.routing import NoMatchFound
from typing_extensions import Annotated

from titiler.core.factory import BaseTilerFactory, FactoryExtension
from titiler.pgstac import model
from titiler.pgstac.dependencies import db_conn


@dataclass
class searchRegisterExtension(FactoryExtension):
    """Add /register and /list endpoints."""

    def register(self, factory: BaseTilerFactory):
        """Register endpoint to the tiler factory."""

        @factory.router.post(
            "/register",
            responses={200: {"description": "Register a Search."}},
            response_model=model.RegisterResponse,
            response_model_exclude_none=True,
        )
        def register_search(
            request: Request,
            search_query=Depends(factory.search_dependency),
            connection=Depends(db_conn),
        ):
            """Register a Search query."""
            search, metadata = search_query

            with connection.cursor(row_factory=class_row(model.Search)) as cursor:
                cursor.execute(
                    "SELECT * FROM search_query(%s, _metadata => %s);",
                    (
                        search.model_dump_json(by_alias=True, exclude_none=True),
                        metadata.model_dump_json(exclude_none=True),
                    ),
                )
                search_info = cursor.fetchone()

            links: List[model.Link] = [
                model.Link(
                    rel="metadata",
                    title="Mosaic metadata",
                    href=factory.url_for(
                        request, "info_search", searchid=search_info.id
                    ),
                ),
                model.Link(
                    rel="tilejson",
                    title="Link for TileJSON",
                    href=factory.url_for(request, "tilejson", searchid=search_info.id),
                ),
            ]

            try:
                links.append(
                    model.Link(
                        rel="map",
                        title="Link for Map viewer",
                        href=factory.url_for(
                            request, "map_viewer", searchid=search_info.id
                        ),
                    )
                )
            except NoMatchFound:
                pass

            try:
                links.append(
                    model.Link(
                        rel="wmts",
                        title="Link for WMTS",
                        href=factory.url_for(request, "wmts", searchid=search_info.id),
                    )
                )
            except NoMatchFound:
                pass

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
                        factory.check_query_params(
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

                    links.append(
                        model.Link(
                            title=f"TileJSON link for `{name}` layer.",
                            rel="tilejson",
                            href=factory.url_for(
                                request,
                                "tilejson",
                                searchid=search_info.id,
                            )
                            + f"?{query_string}",
                        )
                    )

            return model.RegisterResponse(searchid=search_info.id, links=links)


@dataclass
class searchInfoExtension(FactoryExtension):
    """Add /info endpoints."""

    def register(self, factory: BaseTilerFactory):
        """Register endpoint to the tiler factory."""

        @factory.router.get(
            "/{searchid}/info",
            responses={200: {"description": "Get Search query metadata."}},
            response_model=model.Info,
            response_model_exclude_none=True,
        )
        def info_search(
            request: Request,
            searchid=Depends(factory.path_dependency),
            connection=Depends(db_conn),
        ):
            """Get Search query metadata."""
            with connection.cursor(row_factory=class_row(model.Search)) as cursor:
                cursor.execute(
                    "SELECT * FROM searches WHERE hash=%s;",
                    (searchid,),
                )
                search_info = cursor.fetchone()

            if not search_info:
                raise MosaicNotFoundError(f"SearchId `{searchid}` not found")

            links: List[model.Link] = [
                model.Link(
                    rel="self",
                    title="Mosaic metadata",
                    href=factory.url_for(
                        request, "info_search", searchid=search_info.id
                    ),
                ),
                model.Link(
                    title="Link for TileJSON",
                    rel="tilejson",
                    href=factory.url_for(request, "tilejson", searchid=search_info.id),
                ),
            ]

            try:
                links.append(
                    model.Link(
                        rel="map",
                        title="Link for Map viewer",
                        href=factory.url_for(
                            request, "map_viewer", searchid=search_info.id
                        ),
                    )
                )
            except NoMatchFound:
                pass

            try:
                links.append(
                    model.Link(
                        rel="wmts",
                        title="Link for WMTS",
                        href=factory.url_for(request, "wmts", searchid=search_info.id),
                    )
                )
            except NoMatchFound:
                pass

            if search_info.metadata.defaults:
                for name, values in search_info.metadata.defaults.items():
                    links.append(
                        model.Link(
                            title=f"TileJSON link for `{name}` layer.",
                            rel="tilejson",
                            href=factory.url_for(
                                request,
                                "tilejson",
                                searchid=search_info.id,
                            )
                            + f"?{urlencode(values, doseq=True)}",
                        )
                    )

            return model.Info(search=search_info, links=links)


@dataclass
class searchListExtension(FactoryExtension):
    """Add search /list endpoint."""

    def register(self, factory: BaseTilerFactory):  # noqa: C901
        """Register endpoint to the tiler factory."""

        @factory.router.get(
            "/list",
            responses={200: {"description": "List Mosaics in PgSTAC."}},
            response_model=model.Infos,
            response_model_exclude_none=True,
        )
        def list_mosaic(  # noqa: C901
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
            connection=Depends(db_conn),
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

            with connection.cursor() as cursor:
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
                    href=factory.url_for(request, "list_mosaic") + f"?{qs}",
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
                        href=factory.url_for(request, "list_mosaic") + f"?{qs}",
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
                        href=factory.url_for(request, "list_mosaic") + f"?{qs}",
                    ),
                )

            def _create_links(searchid: str) -> List[model.Link]:
                links = [
                    model.Link(
                        rel="tilejson",
                        href=factory.url_for(request, "tilejson", searchid=searchid),
                    ),
                ]

                try:
                    links.append(
                        model.Link(
                            rel="metadata",
                            href=factory.url_for(
                                request, "info_search", searchid=searchid
                            ),
                        ),
                    )
                except NoMatchFound:
                    pass

                return links

            return model.Infos(
                searches=[
                    model.Info(search=search, links=_create_links(search.id))
                    for search in searches_info
                ],
                links=links,
                context=model.Context(
                    returned=len(searches_info),
                    matched=nb_items,
                    limit=limit,
                ),
            )
