"""Test titiler.pgstac Item endpoints."""

from unittest.mock import patch

import pytest

from .conftest import mock_rasterio_open


@patch("rio_tiler.io.cogeo.rasterio")
@pytest.mark.asyncio
async def test_stac_items(rio, app):
    """test STAC items endpoints."""
    rio.open = mock_rasterio_open

    response = await app.get(
        "/stac/info",
        params={
            "collection": "noaa-emergency-response",
            "item": "20200307aC0853900w361030",
        },
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["cog"]

    response = await app.get(
        "/stac/info",
        params={
            "collection": "noaa-emergency-response",
            "item": "20200307aC0853900w361",
        },
    )
    assert response.status_code == 404
    assert (
        "No item '20200307aC0853900w361' found in 'noaa-emergency-response' collection"
        in response.json()["detail"]
    )

    response = await app.get(
        "/stac/asset_statistics",
        params={
            "collection": "noaa-emergency-response",
            "item": "20200307aC0853900w361030",
            "assets": "cog",
        },
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["cog"]
