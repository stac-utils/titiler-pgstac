"""titiler-pgstac Middleware."""

import re
from typing import Final, cast
from urllib.parse import quote

from starlette.types import ASGIApp, Receive, Scope, Send

_encoding: Final[str] = "utf-8"
_nul: Final[str] = "\x00"


class StripNulMiddleware:
    r"""
    Postgres cannot handle NUL bytes. If left unhandled \x00 will first cause problems
    when JSON is passed to SQL, as JSON escapes \x00 to \u0000 but does not escape the
    \ escape character. If this character _is_ escaped then Postgres will report
    "PostgreSQL text fields cannot contain NUL (0x00) bytes".
    This class presumes that no legitimate API client will intentionally submit NUL bytes
    and simply strips them from all parameters.
    """

    def __init__(
        self,
        app: ASGIApp,
    ) -> None:
        """Strip NUL Middleware."""
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        """Remove NUL bytes from path and query string."""
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        scope["path"] = re.sub(
            _nul, "", scope["path"]
        )  # nul in path is URL-unescaped at this point
        for property in ["query_string", "raw_path"]:
            scope[property] = re.sub(
                quote(_nul),
                "",
                cast(bytes, scope[property]).decode(
                    _encoding
                ),  # nul in these properties is URL-escaped
            ).encode(_encoding)

        await self.app(scope, receive, send)
