"""Optional Prometheus metrics for the default application."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING
from weakref import WeakSet

from prometheus_client import Counter, Histogram
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_fastapi_instrumentator.metrics import Info

if TYPE_CHECKING:
    from fastapi import FastAPI

_INSTRUMENTED_APPS: WeakSet[FastAPI] = WeakSet()

_ROUTE_RULES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^/$"), "landing"),
    (re.compile(r"^/conformance$"), "conformance"),
    (re.compile(r"^/searches/register$"), "register_search"),
    (re.compile(r"^/searches/?$"), "list_searches"),
    (re.compile(r"^/searches/[^/]+/info$"), "search_info"),
    (re.compile(r"/tiles(/|$)"), "tiles"),
    (re.compile(r"/point/"), "point"),
    (re.compile(r"/items/"), "item"),
    (re.compile(r"^/collections/"), "collection"),
    (re.compile(r"^/searches/"), "search"),
    (re.compile(r"^/external"), "external"),
    (re.compile(r"^/tileMatrixSets"), "tms"),
    (re.compile(r"^/algorithms"), "algorithms"),
    (re.compile(r"^/colorMaps"), "colormaps"),
]


def resolve_operation(route: str | None) -> str:
    """Map a request to a low-cardinality operation label."""
    if not route or route == "none":
        return "unknown"

    for pattern, operation in _ROUTE_RULES:
        if pattern.search(route):
            return operation

    return "other"


REQUESTS = Counter(
    "titiler_pgstac_http_requests_total",
    "Total HTTP requests by operation.",
    labelnames=("operation", "method", "status"),
)
LATENCY = Histogram(
    "titiler_pgstac_http_request_duration_seconds",
    "HTTP request latency by operation.",
    labelnames=("operation", "method"),
    buckets=(0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10, float("inf")),
)


def record_service_metrics(info: Info) -> None:
    """Record request count and latency using low-cardinality operation labels."""
    route = info.request.scope.get("route")
    route_path = getattr(route, "path", None)
    operation = resolve_operation(route_path)

    REQUESTS.labels(operation, info.method, info.modified_status).inc()
    LATENCY.labels(operation, info.method).observe(info.modified_duration)


def instrument_app(app: FastAPI, endpoint: str = "/metrics") -> None:
    """Instrument a FastAPI app and expose Prometheus metrics."""
    if app in _INSTRUMENTED_APPS:
        return

    (
        Instrumentator(
            should_group_status_codes=True,
            should_ignore_untemplated=True,
            excluded_handlers=[r"^/healthz$", rf"^{re.escape(endpoint)}$"],
        )
        .add(record_service_metrics)
        .instrument(app)
        .expose(app, endpoint=endpoint, include_in_schema=False)
    )

    _INSTRUMENTED_APPS.add(app)
