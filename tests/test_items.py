"""Test titiler.pgstac Item endpoints."""

from unittest.mock import patch

import pystac

from titiler.pgstac.dependencies import get_stac_item

from .conftest import mock_rasterio_open


def test_get_stac_item(app):
    """test get_stac_item."""
    item = get_stac_item(
        app.app.state.dbpool, "noaa-emergency-response", "20200307aC0853900w361030"
    )
    assert isinstance(item, pystac.Item)
    assert item.id == "20200307aC0853900w361030"
    assert item.collection_id == "noaa-emergency-response"


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

    response = app.get(
        "/collections/noaa-emergency-response/items/20200307aC0853900w361030/tilejson.json",
        params={
            "assets": "cog",
        },
    )
    assert response.status_code == 200
    resp = response.json()
    assert (
        "collections/noaa-emergency-response/items/20200307aC0853900w361030/tiles/WebMercatorQuad"
        in resp["tiles"][0]
    )

    response = app.get(
        "/collections/noaa-emergency-response/items/20200307aC0853900w361030/WGS1984Quad/tilejson.json",
        params={
            "assets": "cog",
        },
    )
    assert response.status_code == 200
    resp = response.json()
    assert (
        "collections/noaa-emergency-response/items/20200307aC0853900w361030/tiles/WGS1984Quad"
        in resp["tiles"][0]
    )
