"""TiTiler+PgSTAC FastAPI application."""

import logging
from contextlib import asynccontextmanager
from typing import Dict, Literal, Optional

import jinja2
import rasterio
from fastapi import FastAPI, Path, Query
from psycopg import OperationalError
from psycopg.rows import dict_row
from psycopg_pool import PoolTimeout
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from typing_extensions import Annotated

from titiler.core import __version__ as titiler_version
from titiler.core.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from titiler.core.factory import (
    AlgorithmFactory,
    ColorMapFactory,
    MultiBaseTilerFactory,
    TilerFactory,
    TMSFactory,
)
from titiler.core.middleware import (
    CacheControlMiddleware,
    LoggerMiddleware,
    TotalTimeMiddleware,
)
from titiler.core.models.OGC import Conformance, Landing
from titiler.core.resources.enums import MediaType, OptionalHeader
from titiler.core.templating import create_html_response
from titiler.core.utils import accept_media_type, update_openapi
from titiler.mosaic.errors import MOSAIC_STATUS_CODES
from titiler.pgstac import __version__ as titiler_pgstac_version
from titiler.pgstac.db import close_db_connection, connect_to_db
from titiler.pgstac.dependencies import (
    AssetIdParams,
    CollectionIdParams,
    ItemIdParams,
    SearchIdParams,
)
from titiler.pgstac.errors import PGSTAC_STATUS_CODES
from titiler.pgstac.extensions import searchInfoExtension
from titiler.pgstac.factory import (
    MosaicTilerFactory,
    add_search_list_route,
    add_search_register_route,
)
from titiler.pgstac.reader import PgSTACReader
from titiler.pgstac.settings import ApiSettings

logging.getLogger("botocore.credentials").disabled = True
logging.getLogger("botocore.utils").disabled = True
logging.getLogger("rio-tiler").setLevel(logging.ERROR)

jinja2_env = jinja2.Environment(
    loader=jinja2.ChoiceLoader(
        [
            jinja2.PackageLoader(__package__, "templates"),
            jinja2.PackageLoader("titiler.core.templating", "html"),
        ]
    ),
)
templates = Jinja2Templates(env=jinja2_env)

settings = ApiSettings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI Lifespan."""
    # Create Connection Pool
    await connect_to_db(app)
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

# Fix OpenAPI response header for OGC Common compatibility
update_openapi(app)

ERRORS = {**DEFAULT_STATUS_CODES, **MOSAIC_STATUS_CODES, **PGSTAC_STATUS_CODES}
add_exception_handlers(app, ERRORS)


# Set all CORS enabled origins
if settings.cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
    )

app.add_middleware(
    CacheControlMiddleware,
    cachecontrol=settings.cachecontrol,
    exclude_path=settings.cachecontrol_exclude_paths,
)

optional_headers = []
if settings.debug:
    app.add_middleware(TotalTimeMiddleware)
    app.add_middleware(LoggerMiddleware)

    optional_headers = [OptionalHeader.server_timing, OptionalHeader.x_assets]

    @app.get("/collections", include_in_schema=False, tags=["DEBUG"])
    async def list_collections(request: Request):
        """list collections."""
        with request.app.state.dbpool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cursor:
                cursor.execute("SELECT * FROM pgstac.all_collections();")
                r = cursor.fetchone()
                cols = r.get("all_collections", [])
                return [col["id"] for col in cols]

    @app.get("/collections/{collection_id}", include_in_schema=False, tags=["DEBUG"])
    async def get_collection(request: Request, collection_id: str = Path()):
        """get collection."""
        with request.app.state.dbpool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cursor:
                cursor.execute(
                    "SELECT * FROM get_collection(%s);",
                    (collection_id,),
                )
                r = cursor.fetchone()
                return r.get("get_collection") or {}

    @app.get("/pgstac", include_in_schema=False, tags=["DEBUG"])
    def pgstac_info(request: Request) -> Dict:
        """Retrieve PgSTAC Info."""
        with request.app.state.dbpool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cursor:
                cursor.execute("SELECT pgstac.readonly()")
                pgstac_readonly = cursor.fetchone()["readonly"]

                cursor.execute("SELECT pgstac.get_version();")
                pgstac_version = cursor.fetchone()["get_version"]

        return {
            "pgstac_version": pgstac_version,
            "pgstac_readonly": pgstac_readonly,
        }


TITILER_CONFORMS_TO = {
    "http://www.opengis.net/spec/ogcapi-common-1/1.0/req/core",
    "http://www.opengis.net/spec/ogcapi-common-1/1.0/req/landing-page",
    "http://www.opengis.net/spec/ogcapi-common-1/1.0/req/oas30",
    "http://www.opengis.net/spec/ogcapi-common-1/1.0/req/html",
    "http://www.opengis.net/spec/ogcapi-common-1/1.0/req/json",
}

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

add_search_list_route(app, prefix="/searches", tags=["STAC Search"])

add_search_register_route(
    app,
    prefix="/searches",
    tile_dependencies=[
        searches.layer_dependency,
        searches.dataset_dependency,
        searches.pixel_selection_dependency,
        searches.process_dependency,
        searches.render_dependency,
        searches.assets_accessor_dependency,
        searches.reader_dependency,
        searches.backend_dependency,
    ],
    tags=["STAC Search"],
)

TITILER_CONFORMS_TO.update(searches.conforms_to)

###############################################################################
# STAC COLLECTION Endpoints
collection = MosaicTilerFactory(
    path_dependency=CollectionIdParams,
    optional_headers=optional_headers,
    router_prefix="/collections/{collection_id}",
    add_statistics=True,
    add_viewer=True,
    add_part=True,
    extensions=[
        searchInfoExtension(),
    ],
)
app.include_router(
    collection.router, tags=["STAC Collection"], prefix="/collections/{collection_id}"
)
TITILER_CONFORMS_TO.update(collection.conforms_to)

###############################################################################
# STAC Item Endpoints
stac = MultiBaseTilerFactory(
    reader=PgSTACReader,
    path_dependency=ItemIdParams,
    router_prefix="/collections/{collection_id}/items/{item_id}",
    add_viewer=True,
)
app.include_router(
    stac.router,
    tags=["STAC Item"],
    prefix="/collections/{collection_id}/items/{item_id}",
)
TITILER_CONFORMS_TO.update(stac.conforms_to)

###############################################################################
# STAC Assets Endpoints
if settings.enable_assets_endpoints:
    asset = TilerFactory(
        path_dependency=AssetIdParams,
        router_prefix="/collections/{collection_id}/items/{item_id}/assets/{asset_id}",
        add_viewer=True,
    )
    app.include_router(
        asset.router,
        tags=["STAC Asset"],
        prefix="/collections/{collection_id}/items/{item_id}/assets/{asset_id}",
    )
    TITILER_CONFORMS_TO.update(asset.conforms_to)

###############################################################################
# External Dataset Endpoints
if settings.enable_external_dataset_endpoints:
    external_cog = TilerFactory(router_prefix="/external", add_viewer=True)
    app.include_router(
        external_cog.router,
        tags=["External Dataset"],
        prefix="/external",
    )
    TITILER_CONFORMS_TO.update(external_cog.conforms_to)

###############################################################################
# Tiling Schemes Endpoints
tms = TMSFactory()
app.include_router(tms.router, tags=["Tiling Schemes"])
TITILER_CONFORMS_TO.update(tms.conforms_to)

###############################################################################
# Algorithms Endpoints
algorithms = AlgorithmFactory()
app.include_router(algorithms.router, tags=["Algorithms"])
TITILER_CONFORMS_TO.update(algorithms.conforms_to)

###############################################################################
# Colormaps endpoints
cmaps = ColorMapFactory()
app.include_router(
    cmaps.router,
    tags=["ColorMaps"],
)
TITILER_CONFORMS_TO.update(cmaps.conforms_to)


###############################################################################
# Health Check Endpoint
@app.get("/healthz", description="Health Check", tags=["Health Check"])
def ping(
    timeout: int = Query(
        1, description="Timeout getting SQL connection from the pool."
    ),
) -> Dict:
    """Health check."""
    try:
        with app.state.dbpool.connection(timeout) as conn:
            conn.execute("SELECT 1")
            db_online = True
    except (OperationalError, PoolTimeout):
        db_online = False

    return {
        "database_online": db_online,
        "versions": {
            "titiler": titiler_version,
            "titiler.pgstac": titiler_pgstac_version,
            "rasterio": rasterio.__version__,
            "gdal": rasterio.__gdal_version__,
            "proj": rasterio.__proj_version__,
            "geos": rasterio.__geos_version__,
        },
    }


@app.get(
    "/",
    response_model=Landing,
    response_model_exclude_none=True,
    responses={
        200: {
            "content": {
                "text/html": {},
                "application/json": {},
            }
        },
    },
    tags=["OGC Common"],
)
def landing(
    request: Request,
    f: Annotated[
        Optional[Literal["html", "json"]],
        Query(
            description="Response MediaType. Defaults to endpoint's default or value defined in `accept` header."
        ),
    ] = None,
):
    """TiTiler landing page."""
    baseurl = str(request.base_url).rstrip("/")

    data = {
        "title": "TiTiler-PgSTAC",
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
                "title": "Conformance Declaration",
                "href": str(request.url_for("conformance")),
                "type": "text/html",
                "rel": "http://www.opengis.net/def/rel/ogc/1.0/conformance",
            },
            {
                "title": "PgSTAC Virtual Mosaic list (JSON)",
                "href": baseurl + app.url_path_for("list_searches"),
                "type": "application/json",
                "rel": "data",
            },
            {
                "title": "PgSTAC Virtual Mosaic viewer (template URL)",
                "href": baseurl
                + app.url_path_for(
                    "map_viewer",
                    search_id="{search_id}",
                    tileMatrixSetId="{tileMatrixSetId}",
                ),
                "type": "text/html",
                "rel": "data",
                "templated": True,
            },
            {
                "title": "PgSTAC Collection viewer (template URL)",
                "href": baseurl
                + app.url_path_for(
                    "map_viewer",
                    collection_id="{collection_id}",
                    tileMatrixSetId="{tileMatrixSetId}",
                ),
                "type": "text/html",
                "rel": "data",
                "templated": True,
            },
            {
                "title": "PgSTAC Item viewer (template URL)",
                "href": baseurl
                + app.url_path_for(
                    "map_viewer",
                    collection_id="{collection_id}",
                    item_id="{item_id}",
                    tileMatrixSetId="{tileMatrixSetId}",
                ),
                "type": "text/html",
                "rel": "data",
                "templated": True,
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

    output_type: Optional[MediaType]
    if f:
        output_type = MediaType[f]
    else:
        accepted_media = [MediaType.html, MediaType.json]
        output_type = accept_media_type(
            request.headers.get("accept", ""), accepted_media
        )

    if output_type == MediaType.html:
        return create_html_response(
            request,
            data,
            "landing",
            templates=templates,
            title="TiTiler-PgSTAC",
        )

    return data


@app.get(
    "/conformance",
    response_model=Conformance,
    response_model_exclude_none=True,
    responses={
        200: {
            "content": {
                "text/html": {},
                "application/json": {},
            }
        },
    },
    tags=["OGC Common"],
)
def conformance(
    request: Request,
    f: Annotated[
        Optional[Literal["html", "json"]],
        Query(
            description="Response MediaType. Defaults to endpoint's default or value defined in `accept` header."
        ),
    ] = None,
):
    """Conformance classes.

    Called with `GET /conformance`.

    Returns:
        Conformance classes which the server conforms to.

    """
    data = {"conformsTo": sorted(TITILER_CONFORMS_TO)}

    output_type: Optional[MediaType]
    if f:
        output_type = MediaType[f]
    else:
        accepted_media = [MediaType.html, MediaType.json]
        output_type = accept_media_type(
            request.headers.get("accept", ""), accepted_media
        )

    if output_type == MediaType.html:
        return create_html_response(
            request,
            data,
            "conformance",
            templates=templates,
            title="Conformance",
        )

    return data
