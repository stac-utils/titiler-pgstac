"""Test middlewares."""

from typing import cast
from unittest import mock
from urllib.parse import quote

import pytest
from starlette.types import Receive, Scope, Send

from titiler.pgstac.middleware import StripNulMiddleware


@pytest.mark.asyncio
async def test_strip_nul_middleware_with_nuls(app) -> None:
    """Test nul byte stripping middleware with nul bytes."""
    app_mock = mock.AsyncMock()
    core_scope = {
        "type": "http",
    }
    path_with_nul = "/path/with-{}/nul".format("\x00")
    path_with_escaped_nul = "/path/with-{}/nul".format(quote("\x00"))
    await StripNulMiddleware(app_mock)(
        cast(
            Scope,
            {
                **core_scope,
                "path": path_with_nul,
                "query_string": "param=query-with-{}-nul".format(quote("\x00")).encode(
                    "utf-8"
                ),
                "raw_path": path_with_escaped_nul.encode("utf-8"),
            },
        ),
        cast(Receive, None),
        cast(Send, None),
    )
    path_without_null = "/path/with-/nul"
    app_mock.assert_called_once_with(
        {
            **core_scope,
            "path": path_without_null,
            "query_string": "param=query-with--nul".encode("utf-8"),
            "raw_path": path_without_null.encode("utf-8"),
        },
        None,
        None,
    )


@pytest.mark.asyncio
async def test_strip_nul_middleware_without_nuls(app) -> None:
    """Test nul byte stripping middleware without any nul butes."""
    app_mock = mock.AsyncMock()
    path = "/path/without/nul"
    core_scope = {
        "type": "http",
        "path": path,
        "query_string": "param=query-without-nul".encode("utf-8"),
        "raw_path": path.encode("utf-8"),
    }
    await StripNulMiddleware(app_mock)(
        cast(
            Scope,
            core_scope,
        ),
        cast(Receive, None),
        cast(Send, None),
    )
    app_mock.assert_called_once_with(
        core_scope,
        None,
        None,
    )
