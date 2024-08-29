"""test external cog and asset endpoints."""

from unittest.mock import patch

from .conftest import mock_rasterio_open


@patch("rio_tiler.io.rasterio.rasterio")
def test_cog_assets(rio, app):
    """test STAC Assets endpoints."""
    rio.open = mock_rasterio_open

    response = app.get(
        "/collections/noaa-emergency-response/items/20200307aC0853900w361030/assets/cog/info",
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["bounds"]

    response = app.get(
        "/collections/noaa-emergency-response/items/20200307aC0853900w361030/assets/cog/WebMercatorQuad/tilejson.json",
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["tilejson"]


def test_external_cog(app):
    """test external cog endpoints."""
    response = app.get(
        "/external/info",
        params={"url": "tests/fixtures/20200307aC0853900w361030n.tif"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["bounds"]

    response = app.get(
        "/external/WebMercatorQuad/tilejson.json",
        params={"url": "tests/fixtures/20200307aC0853900w361030n.tif"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["tilejson"]
