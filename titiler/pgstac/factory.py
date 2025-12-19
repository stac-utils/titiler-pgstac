"""Custom MosaicTiler Factory for PgSTAC Mosaic Backend."""

import logging
import os
import re
import warnings
from collections.abc import Callable, Generator
from enum import Enum
from urllib.parse import urlencode

from attrs import define
from fastapi import Depends, FastAPI, Query
from psycopg import errors as pgErrors
from psycopg import sql
from psycopg.rows import class_row, dict_row
from rio_tiler.constants import MAX_THREADS
from starlette.datastructures import QueryParams
from starlette.requests import Request
from starlette.routing import NoMatchFound
from typing_extensions import Annotated

from titiler.core.dependencies import AssetsBidxExprParams, DefaultDependency
from titiler.core.utils import check_query_params
from titiler.mosaic.factory import MosaicTilerFactory as BaseFactory
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

logger = logging.getLogger(__name__)


@define(kw_only=True)
class MosaicTilerFactory(BaseFactory):
    """Custom MosaicTiler for PgSTAC Mosaic Backend."""

    path_dependency: Callable[..., str]

    backend: type[PGSTACBackend] = PGSTACBackend
    backend_dependency: type[DefaultDependency] = BackendParams

    # Rasterio Dataset Options (nodata, unscale, resampling, reproject)
    dataset_reader: type[SimpleSTACReader] = SimpleSTACReader

    # Backend.get_assets() Options
    assets_accessor_dependency: type[DefaultDependency] = PgSTACParams

    # Assets/Indexes/Expression Dependencies
    layer_dependency: type[DefaultDependency] = AssetsBidxExprParams

    def register_routes(self) -> None:
        """Custom: remove `self.info()."""
        self.tilesets()
        self.tile()
        if self.add_viewer:
            self.map_viewer()
        self.tilejson()
        self.point()
        self.assets()

        if self.add_part:
            self.part()

        if self.add_statistics:
            self.statistics()

        if self.add_ogc_maps:
            self.ogc_maps()


def add_search_register_route(  # noqa: C901
    app: FastAPI,
    *,
    prefix: str = "",
    search_dependency: Callable[
        ..., tuple[model.PgSTACSearch, model.Metadata]
    ] = SearchParams,
    tile_dependencies: list[Callable] | None = None,
    tags: list[str | Enum] | None = None,
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

        links: list[model.Link] = []

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
                    title="WMTS Capabilities link.",
                    href=str(
                        app.url_path_for(
                            "wmts",
                            search_id=search_info.id,
                        ).make_absolute_url(base_url=base_url)
                    ),
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
    tags: list[str | Enum] | None = None,
):
    """Add PgSTAC Search (of type mosaic) listing route."""
    name = prefix.replace("/", ".")
    operation_prefix = f"{name}." if name else ""

    @app.get(
        f"{prefix}/",
        responses={200: {"description": "List Mosaics in PgSTAC."}},
        response_model=model.Infos,
        response_model_exclude_none=True,
        tags=tags,
        operation_id=f"{operation_prefix}getMosaicList",
    )
    @app.get(
        f"{prefix}/list",
        responses={200: {"description": "List Mosaics in PgSTAC."}},
        response_model=model.Infos,
        response_model_exclude_none=True,
        tags=tags,
        operation_id=f"{operation_prefix}getMosaicList-deprecated",
        deprecated=True,
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
            str | None,
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
            search_links: list[model.Link] = []
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
