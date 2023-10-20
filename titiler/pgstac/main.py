"""TiTiler+PgSTAC FastAPI application."""

import logging
from contextlib import asynccontextmanager
from typing import Dict

import jinja2
from fastapi import FastAPI, Query
from psycopg import OperationalError
from psycopg_pool import PoolTimeout
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

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
from titiler.pgstac.db import close_db_connection, connect_to_db
from titiler.pgstac.dependencies import CollectionIdParams, ItemIdParams, SearchIdParams
from titiler.pgstac.extensions import searchInfoExtension
from titiler.pgstac.factory import (
    MosaicTilerFactory,
    add_search_list_route,
    add_search_register_route,
)
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
# STAC Search Endpoints
searches = MosaicTilerFactory(
    path_dependency=SearchIdParams,
    optional_headers=optional_headers,
    router_prefix="/searches/{search_id}",
    add_statistics=True,
    add_viewer=True,
    add_part=True,
    extensions=[
        searchInfoExtension(),
    ],
)
app.include_router(
    searches.router, tags=["STAC Search"], prefix="/searches/{search_id}"
)

add_search_register_route(
    app,
    prefix="/searches",
    tile_dependencies=[
        searches.layer_dependency,
        searches.dataset_dependency,
        searches.pixel_selection_dependency,
        searches.process_dependency,
        searches.rescale_dependency,
        searches.colormap_dependency,
        searches.render_dependency,
        searches.pgstac_dependency,
        searches.reader_dependency,
        searches.backend_dependency,
    ],
    tags=["STAC Search"],
)
add_search_list_route(app, prefix="/searches", tags=["STAC Search"])

###############################################################################
# STAC COLLECTION Endpoints
collection = MosaicTilerFactory(
    path_dependency=CollectionIdParams,
    optional_headers=optional_headers,
    router_prefix="/collections/{collection_id}",
    add_statistics=True,
    add_viewer=True,
    add_part=True,
)
app.include_router(
    collection.router, tags=["STAC Collection"], prefix="/collections/{collection_id}"
)

###############################################################################
# STAC Item Endpoints
stac = MultiBaseTilerFactory(
    reader=PgSTACReader,
    path_dependency=ItemIdParams,
    optional_headers=optional_headers,
    router_prefix="/collections/{collection_id}/items/{item_id}",
    add_viewer=True,
)
app.include_router(
    stac.router,
    tags=["STAC Item"],
    prefix="/collections/{collection_id}/items/{item_id}",
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
                "title": "PgSTAC Virtual Mosaic list (JSON)",
                "href": app.url_path_for("list_searches"),
                "type": "application/json",
                "rel": "data",
            },
            {
                "title": "PgSTAC Virtual Mosaic viewer (template URL)",
                "href": app.url_path_for("map_viewer", search_id="{search_id}"),
                "type": "text/html",
                "rel": "data",
            },
            {
                "title": "PgSTAC Collection viewer (template URL)",
                "href": app.url_path_for("map_viewer", collection_id="{collection_id}"),
                "type": "text/html",
                "rel": "data",
            },
            {
                "title": "PgSTAC Item viewer (template URL)",
                "href": app.url_path_for(
                    "map_viewer", collection_id="{collection_id}", item_id="{item_id}"
                ),
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
