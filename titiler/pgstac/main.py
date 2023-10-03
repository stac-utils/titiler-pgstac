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
from titiler.pgstac.dependencies import ItemPathParams
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
    router_prefix="/mosaic",
    add_statistics=True,
    add_viewer=True,
    add_mosaic_list=True,
    add_part=True,
)
app.include_router(mosaic.router, tags=["Mosaic"], prefix="/mosaic")

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
                "href": mosaic.url_for(request, "list_mosaic"),
                "type": "application/json",
                "rel": "data",
            },
            {
                "title": "Mosaic Metadata (template URL)",
                "href": mosaic.url_for(request, "info_search", searchid="{searchid}"),
                "type": "application/json",
                "rel": "data",
            },
            {
                "title": "Mosaic viewer (template URL)",
                "href": mosaic.url_for(request, "map_viewer", searchid="{searchid}"),
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
