"""FastAPI application using PGStac."""

from fastapi import FastAPI
from stac_fastapi.pgstac.config import Settings as pgStacSettings
from stac_fastapi.pgstac.db import close_db_connection, connect_to_db
from starlette.middleware.cors import CORSMiddleware
from titiler.core.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from titiler.mosaic.errors import MOSAIC_STATUS_CODES
from titiler.pgstac.factory import MosaicTilerFactory
from titiler.pgstac.settings import ApiSettings
from titiler.pgstac.version import __version__ as titiler_pgstac_version

settings = ApiSettings()
pg_settings = pgStacSettings()

app = FastAPI(title=settings.name, version=titiler_pgstac_version,)
app.state.settings = pg_settings


@app.on_event("startup")
async def startup_event():
    """Connect to database on startup."""
    await connect_to_db(app)


@app.on_event("shutdown")
async def shutdown_event():
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
        allow_methods=["GET"],
        allow_headers=["*"],
    )


mosaic = MosaicTilerFactory()
app.include_router(mosaic.router)


@app.get("/healthz", description="Health Check", tags=["Health Check"])
def ping():
    """Health check."""
    return {"ping": "pong!"}
