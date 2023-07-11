"""TiTiler+PgSTAC FastAPI application."""

import logging
import re
from fastapi import FastAPI, Query
from fastapi.openapi.utils import get_openapi
from http.client import HTTP_PORT, HTTPS_PORT
from psycopg import OperationalError
from psycopg_pool import PoolTimeout
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware as _CORSMiddleware
from starlette.types import ASGIApp, Receive, Scope, Send
from titiler.core.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from titiler.core.factory import AlgorithmFactory, MultiBaseTilerFactory, TMSFactory
from titiler.core.middleware import (
    CacheControlMiddleware,
    LoggerMiddleware,
    TotalTimeMiddleware,
)
from titiler.core.resources.enums import OptionalHeader
from titiler.mosaic.errors import MOSAIC_STATUS_CODES
from typing import Dict, Tuple, List

from titiler.pgstac import __version__ as titiler_pgstac_version
from titiler.pgstac.db import close_db_connection, connect_to_db
from titiler.pgstac.dependencies import ItemPathParams
from titiler.pgstac.factory import MosaicTilerFactory
from titiler.pgstac.reader import PgSTACReader
from titiler.pgstac.settings import ApiSettings

logging.getLogger("botocore.credentials").disabled = True
logging.getLogger("botocore.utils").disabled = True
logging.getLogger("rio-tiler").setLevel(logging.ERROR)

settings = ApiSettings()

app = FastAPI(title=settings.name, version=titiler_pgstac_version)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="TiTiler PgSTAC",
        version=titiler_pgstac_version,
        description="A lightweight STAC API implementation using PostgreSQL as a backend.",
        routes=app.routes,
        openapi_version="3.0.1",
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


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


class ProxyHeaderMiddleware:
    """
    Account for forwarding headers when deriving base URL.

    Prioritise standard Forwarded header, look for non-standard X-Forwarded-* if missing.
    Default to what can be derived from the URL if no headers provided.
    Middleware updates the host header that is interpreted by starlette when deriving Request.base_url.
    """

    def __init__(self, app: ASGIApp):
        """Create proxy header middleware."""
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """Call from stac-fastapi framework."""
        if scope["type"] == "http":
            proto, domain, port = self._get_forwarded_url_parts(scope)
            scope["scheme"] = proto
            if domain is not None:
                port_suffix = ""
                if port is not None:
                    if (proto == "http" and port != HTTP_PORT) or (
                            proto == "https" and port != HTTPS_PORT
                    ):
                        port_suffix = f":{port}"
                scope["headers"] = self._replace_header_value_by_name(
                    scope,
                    "host",
                    f"{domain}{port_suffix}",
                )
        await self.app(scope, receive, send)

    def _get_forwarded_url_parts(self, scope: Scope) -> Tuple[str]:
        proto = scope.get("scheme", "http")
        header_host = self._get_header_value_by_name(scope, "host")
        if header_host is None:
            domain, port = scope.get("server")
        else:
            header_host_parts = header_host.split(":")
            if len(header_host_parts) == 2:
                domain, port = header_host_parts
            else:
                domain = header_host_parts[0]
                port = None
        forwarded = self._get_header_value_by_name(scope, "forwarded")
        if forwarded is not None:
            parts = forwarded.split(";")
            for part in parts:
                if len(part) > 0 and re.search("=", part):
                    key, value = part.split("=")
                    if key == "proto":
                        proto = value
                    elif key == "host":
                        host_parts = value.split(":")
                        domain = host_parts[0]
                        try:
                            port = int(host_parts[1]) if len(host_parts) == 2 else None
                        except ValueError:
                            # ignore ports that are not valid integers
                            pass
        else:
            proto = self._get_header_value_by_name(scope, "x-forwarded-proto", proto)
            port_str = self._get_header_value_by_name(scope, "x-forwarded-port", port)
            try:
                port = int(port_str) if port_str is not None else None
            except ValueError:
                # ignore ports that are not valid integers
                pass

        return (proto, domain, port)

    def _get_header_value_by_name(
            self, scope: Scope, header_name: str, default_value: str = None
    ) -> str:
        headers = scope["headers"]
        candidates = [
            value.decode() for key, value in headers if key.decode() == header_name
        ]
        return candidates[0] if len(candidates) == 1 else default_value

    @staticmethod
    def _replace_header_value_by_name(
            scope: Scope, header_name: str, new_value: str
    ) -> List[Tuple[str]]:
        return [
            (name, value)
            for name, value in scope["headers"]
            if name.decode() != header_name
        ] + [(str.encode(header_name), str.encode(new_value))]


app.add_middleware(CacheControlMiddleware, cachecontrol=settings.cachecontrol)
app.add_middleware(ProxyHeaderMiddleware)
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
