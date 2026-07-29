"""Benchmark items."""

import os

import httpx2 as httpx
import pytest

host = os.environ.get("HOST", "0.0.0.0")
port = os.environ.get("PORT", "8083")


@pytest.mark.parametrize(
    "tile",
    [
        "0/0/0",
        "1/1/1",
        "2/2/1",
        "3/5/0",
        "4/5/9",
        "5/16/5",
        "6/43/31",
    ],
)
def test_benchmark_tile(benchmark, tile):
    """Benchmark items endpoint."""

    def f(input_tile):
        response = httpx.get(
            f"http://{host}:{port}/collections/world/tiles/WebMercatorQuad/{input_tile}?assets=asset"
        )
        assert response.status_code == 200
        return response

    _ = httpx.get(f"http://{host}:{port}/collections/world/info")

    response = benchmark(f, tile)
    assert response.status_code == 200
