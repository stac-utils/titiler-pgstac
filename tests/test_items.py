"""Test titiler.pgstac Item endpoints."""

from unittest.mock import patch

from .conftest import mock_rasterio_open


@patch("rio_tiler.io.rasterio.rasterio")
def test_stac_items(rio, app):
    """test STAC items endpoints."""
    rio.open = mock_rasterio_open

    response = app.get(
        "/collections/noaa-emergency-response/items/20200307aC0853900w361030/info",
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["cog"]

    response = app.get(
        "/collections/noaa-emergency-response/items/20200307aC0853900w361/info",
    )
    assert response.status_code == 404
    assert (
        "No item '20200307aC0853900w361' found in 'noaa-emergency-response' collection"
        in response.json()["detail"]
    )

    response = app.get(
        "/collections/noaa-emergency-response/items/20200307aC0853900w361030/asset_statistics",
        params={
            "assets": "cog",
        },
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["cog"]
