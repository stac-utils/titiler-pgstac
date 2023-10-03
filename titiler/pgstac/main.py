"""TiTiler+PgSTAC FastAPI application."""

import logging
import re
import warnings
from contextlib import asynccontextmanager
from typing import Dict, Generator, List, Optional
from urllib.parse import urlencode

import jinja2
from fastapi import Depends, FastAPI, Query
from psycopg import OperationalError, sql
from psycopg.rows import class_row
from psycopg_pool import PoolTimeout
from starlette.datastructures import QueryParams
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import NoMatchFound
from starlette.templating import Jinja2Templates
from typing_extensions import Annotated

from titiler.core.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from titiler.core.factory import AlgorithmFactory, MultiBaseTilerFactory, TMSFactory
from titiler.core.middleware import (
    CacheControlMiddleware,
    LoggerMiddleware,
    TotalTimeMiddleware,
)
from titiler.core.resources.enums import OptionalHeader
from titiler.mosaic.errors import MOSAIC_STATUS_CODES
from titiler.pgstac import __version__ as titiler_pgstac_version
from titiler.pgstac import model
from titiler.pgstac.db import close_db_connection, connect_to_db
from titiler.pgstac.dependencies import ItemPathParams, SearchParams, db_conn
from titiler.pgstac.factory import MosaicTilerFactory
from titiler.pgstac.reader import PgSTACReader
from titiler.pgstac.settings import ApiSettings, PostgresSettings

logging.getLogger("botocore.credentials").disabled = True
logging.getLogger("botocore.utils").disabled = True
logging.getLogger("rio-tiler").setLevel(logging.ERROR)

templates = Jinja2Templates(
    directory="",
    loader=jinja2.ChoiceLoader([jinja2.PackageLoader(__package__, "templates")]),
)  # type:ignore


postgres_settings = PostgresSettings()
settings = ApiSettings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI Lifespan."""
    # Create Connection Pool
    await connect_to_db(app, settings=postgres_settings)
    yield
    # Close the Connection Pool
    await close_db_connection(app)


app = FastAPI(
    title=settings.name,
    openapi_url="/api",
    docs_url="/api.html",
    description="""Dynamic Raster Tiler with PgSTAC backend.

---

**Documentation**: <a href="https://stac-utils.github.io/titiler-pgstac/" target="_blank">https://stac-utils.github.io/titiler-pgstac/</a>

**Source Code**: <a href="https://github.com/stac-utils/titiler-pgstac" target="_blank">https://github.com/stac-utils/titiler-pgstac</a>

---
    """,
    version=titiler_pgstac_version,
    root_path=settings.root_path,
    lifespan=lifespan,
)

add_exception_handlers(app, DEFAULT_STATUS_CODES)
add_exception_handlers(app, MOSAIC_STATUS_CODES)


# Set all CORS enabled origins
if settings.cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
    )

app.add_middleware(CacheControlMiddleware, cachecontrol=settings.cachecontrol)
if settings.debug:
    app.add_middleware(TotalTimeMiddleware)
    app.add_middleware(LoggerMiddleware)

if settings.debug:
    optional_headers = [OptionalHeader.server_timing, OptionalHeader.x_assets]
else:
    optional_headers = []

###############################################################################
# MOSAIC Endpoints
mosaic = MosaicTilerFactory(
    optional_headers=optional_headers,
    router_prefix="/mosaic/{search_id}",
    add_statistics=True,
    add_viewer=True,
    add_part=True,
)
app.include_router(mosaic.router, tags=["Mosaic"], prefix="/mosaic/{search_id}")

###############################################################################
# STAC Item Endpoints
stac = MultiBaseTilerFactory(
    reader=PgSTACReader,
    path_dependency=ItemPathParams,
    optional_headers=optional_headers,
    router_prefix="/collections/{collection_id}/items/{item_id}",
    add_viewer=True,
)
app.include_router(
    stac.router, tags=["Item"], prefix="/collections/{collection_id}/items/{item_id}"
)

###############################################################################
# Tiling Schemes Endpoints
tms = TMSFactory()
app.include_router(tms.router, tags=["Tiling Schemes"])

###############################################################################
# Algorithms Endpoints
algorithms = AlgorithmFactory()
app.include_router(algorithms.router, tags=["Algorithms"])


###############################################################################
# Health Check Endpoint
@app.get("/healthz", description="Health Check", tags=["Health Check"])
def ping(
    timeout: int = Query(1, description="Timeout getting SQL connection from the pool.")
) -> Dict:
    """Health check."""
    try:
        with app.state.dbpool.connection(timeout) as conn:
            conn.execute("SELECT 1")
            db_online = True
    except (OperationalError, PoolTimeout):
        db_online = False

    return {"database_online": db_online}


###############################################################################
# Landing Page
@app.get("/", response_class=HTMLResponse)
def landing(request: Request):
    """Get landing page."""
    data = {
        "title": "TiTiler-PgSTACr",
        "links": [
            {
                "title": "Landing page",
                "href": str(request.url_for("landing")),
                "type": "text/html",
                "rel": "self",
            },
            {
                "title": "the API definition (JSON)",
                "href": str(request.url_for("openapi")),
                "type": "application/vnd.oai.openapi+json;version=3.0",
                "rel": "service-desc",
            },
            {
                "title": "the API documentation",
                "href": str(request.url_for("swagger_ui_html")),
                "type": "text/html",
                "rel": "service-doc",
            },
            {
                "title": "Mosaic List (JSON)",
                "href": app.url_path_for("list_mosaic"),
                "type": "application/json",
                "rel": "data",
            },
            {
                "title": "Mosaic Metadata (template URL)",
                "href": mosaic.url_for(request, "info_search"),
                "type": "application/json",
                "rel": "data",
            },
            {
                "title": "Mosaic viewer (template URL)",
                "href": mosaic.url_for(request, "map_viewer"),
                "type": "text/html",
                "rel": "data",
            },
            {
                "title": "TiTiler-PgSTAC Documentation (external link)",
                "href": "https://stac-utils.github.io/titiler-pgstac/",
                "type": "text/html",
                "rel": "doc",
            },
            {
                "title": "TiTiler-PgSTAC source code (external link)",
                "href": "https://github.com/stac-utils/titiler-pgstac",
                "type": "text/html",
                "rel": "doc",
            },
        ],
    }

    urlpath = request.url.path
    crumbs = []
    baseurl = str(request.base_url).rstrip("/")

    crumbpath = str(baseurl)
    for crumb in urlpath.split("/"):
        crumbpath = crumbpath.rstrip("/")
        part = crumb
        if part is None or part == "":
            part = "Home"
        crumbpath += f"/{crumb}"
        crumbs.append({"url": crumbpath.rstrip("/"), "part": part.capitalize()})

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "response": data,
            "template": {
                "api_root": baseurl,
                "params": request.query_params,
                "title": "TiTiler-PgSTAC",
            },
            "crumbs": crumbs,
            "url": str(request.url),
            "baseurl": baseurl,
            "urlpath": str(request.url.path),
            "urlparams": str(request.url.query),
        },
    )


###############################################################################
# Register Mosaic
@app.post(
    "/mosaic/register",
    responses={200: {"description": "Register a Search."}},
    response_model=model.RegisterResponse,
    response_model_exclude_none=True,
    tags=["Mosaic"],
)
def register_search(
    request: Request,
    search_query=Depends(SearchParams),
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
            href=mosaic.url_for(request, "info_search").replace(
                "{search_id}", search_info.id
            ),
        ),
        model.Link(
            rel="tilejson",
            title="Link for TileJSON",
            href=mosaic.url_for(request, "tilejson").replace(
                "{search_id}", search_info.id
            ),
        ),
    ]

    try:
        links.append(
            model.Link(
                rel="map",
                title="Link for Map viewer",
                href=mosaic.url_for(request, "map_viewer").replace(
                    "{search_id}", search_info.id
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
                href=mosaic.url_for(request, "wmts").replace(
                    "{search_id}", search_info.id
                ),
            )
        )
    except NoMatchFound:
        pass

    if search_info.metadata.defaults:
        # List of dependencies a `/tile` URL should validate
        # Note: Those dependencies should only require Query() inputs
        tile_dependencies = [
            mosaic.layer_dependency,
            mosaic.dataset_dependency,
            mosaic.pixel_selection_dependency,
            mosaic.process_dependency,
            mosaic.rescale_dependency,
            mosaic.colormap_dependency,
            mosaic.render_dependency,
            mosaic.pgstac_dependency,
            mosaic.reader_dependency,
            mosaic.backend_dependency,
        ]

        for name, values in search_info.metadata.defaults.items():
            query_string = urlencode(values, doseq=True)
            try:
                mosaic.check_query_params(
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
                    href=mosaic.url_for(
                        request,
                        "tilejson",
                    ).replace("{search_id}", search_info.id)
                    + f"?{query_string}",
                )
            )

    return model.RegisterResponse(searchid=search_info.id, links=links)


###############################################################################
# List Mosaic
@app.get(
    "/mosaic/list",
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
        cursor.execute(sql.SQL(" ").join(query), {"limit": limit, "offset": offset})
        searches_info = cursor.fetchall()

    qs = QueryParams({**request.query_params, "limit": limit, "offset": offset})
    links = [
        model.Link(
            rel="self",
            href=app.url_path_for("list_mosaic") + f"?{qs}",
        ),
    ]

    if len(searches_info) < nb_items:
        next_token = offset + len(searches_info)
        qs = QueryParams({**request.query_params, "limit": limit, "offset": next_token})
        links.append(
            model.Link(
                rel="next",
                href=app.url_path_for("list_mosaic") + f"?{qs}",
            ),
        )

    if offset > 0:
        prev_token = offset - limit if (offset - limit) > 0 else 0
        qs = QueryParams({**request.query_params, "limit": limit, "offset": prev_token})
        links.append(
            model.Link(
                rel="prev",
                href=app.url_path_for("list_mosaic") + f"?{qs}",
            ),
        )

    def _create_links(searchid: str) -> List[model.Link]:
        links = [
            model.Link(
                rel="tilejson",
                href=mosaic.url_for(request, "tilejson").replace(
                    "{search_id}", searchid
                ),
            ),
        ]

        try:
            links.append(
                model.Link(
                    rel="metadata",
                    href=mosaic.url_for(request, "info_search").replace(
                        "{search_id}", searchid
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
