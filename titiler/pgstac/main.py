"""TiTiler+PgSTAC FastAPI application."""

import logging
from typing import Dict

from titiler.core.dependencies import TileMatrixSetName, TMSParams
from titiler.core.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from titiler.core.factory import MultiBaseTilerFactory, TMSFactory
from titiler.core.middleware import (
    CacheControlMiddleware,
    LoggerMiddleware,
    TotalTimeMiddleware,
)
from titiler.core.resources.enums import OptionalHeader
from titiler.mosaic.errors import MOSAIC_STATUS_CODES
from titiler.pgstac.db import close_db_connection, connect_to_db
from titiler.pgstac.dependencies import ItemPathParams
from titiler.pgstac.factory import MosaicTilerFactory
from titiler.pgstac.reader import PgSTACReader
from titiler.pgstac.settings import ApiSettings
from titiler.pgstac.version import __version__ as titiler_pgstac_version

from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

logging.getLogger("botocore.credentials").disabled = True
logging.getLogger("botocore.utils").disabled = True
logging.getLogger("rio-tiler").setLevel(logging.ERROR)

settings = ApiSettings()

app = FastAPI(title=settings.name, version=titiler_pgstac_version)


@app.on_event("startup")
async def startup_event() -> None:
    """Connect to database on startup."""
    await connect_to_db(app)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """Close database connection."""
    await close_db_connection(app)


add_exception_handlers(app, DEFAULT_STATUS_CODES)
add_exception_handlers(app, MOSAIC_STATUS_CODES)


# Set all CORS enabled origins
if settings.cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST"],
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


mosaic = MosaicTilerFactory(
    optional_headers=optional_headers, router_prefix="/mosaic", add_statistics=True
)
app.include_router(mosaic.router, tags=["Mosaic"], prefix="/mosaic")

stac = MultiBaseTilerFactory(
    reader=PgSTACReader,
    path_dependency=ItemPathParams,
    optional_headers=optional_headers,
    router_prefix="/stac",
)
app.include_router(stac.router, tags=["Items"], prefix="/stac")

tms = TMSFactory(supported_tms=TileMatrixSetName, tms_dependency=TMSParams)
app.include_router(tms.router, tags=["TileMatrixSets"])


@app.get("/healthz", description="Health Check", tags=["Health Check"])
def ping() -> Dict:
    """Health check."""
    return {"ping": "pong!"}
