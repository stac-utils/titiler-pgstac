"""Test titiler.pgstac Mosaic endpoints."""

from unittest.mock import patch

import pytest
from rasterio.crs import CRS

from .conftest import mock_rasterio_open, parse_img

search_no_bbox = "8f5fb37ec266f4b84ec6aa4fe0453c59"
search_bbox = "5e86ce566b979e567370a6ad85aaa68a"


@pytest.mark.asyncio
async def test_register(app):
    """Register Search requests."""
    query = {"collections": ["noaa-emergency-response"], "filter-lang": "cql-json"}
    response = await app.post("/mosaic/register", json=query)
    assert response.status_code == 200
    resp = response.json()
    assert resp["searchid"] == search_no_bbox
    assert resp["links"]
    assert [link["rel"] for link in resp["links"]] == ["metadata", "tilejson"]

    query = {
        "collections": ["noaa-emergency-response"],
        "bbox": [-85.535, 36.137, -85.465, 36.179],
        "filter-lang": "cql-json",
    }
    response = await app.post("/mosaic/register", json=query)
    assert response.status_code == 200

    resp = response.json()
    assert resp["searchid"] == search_bbox
    assert resp["links"]
    assert [link["rel"] for link in resp["links"]] == ["metadata", "tilejson"]


@pytest.mark.asyncio
async def test_info(app):
    """Should return metadata about a search query."""
    response = await app.get(f"/mosaic/{search_no_bbox}/info")
    assert response.status_code == 200
    resp = response.json()
    assert resp["search"]
    assert resp["links"]
    search = resp["search"]
    assert search["search"] == {
        "collections": ["noaa-emergency-response"],
        "filter-lang": "cql-json",
    }
    assert search["metadata"] == {"type": "mosaic"}


@pytest.mark.asyncio
async def test_assets_for_point(app):
    """Get assets for a Point."""
    response = await app.get(f"/mosaic/{search_no_bbox}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    # make sure we can find assets when having both bbox and geometry
    response = await app.get(f"/mosaic/{search_bbox}/-85.5,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # no assets found outside the mosaic bbox
    response = await app.get(f"/mosaic/{search_bbox}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0


@pytest.mark.asyncio
async def test_assets_for_tile(app):
    """Get assets for a Tile."""
    response = await app.get(f"/mosaic/{search_no_bbox}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    # make sure we can find assets when having both bbox and geometry
    response = await app.get(f"/mosaic/{search_bbox}/15/8601/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # no assets found outside the query bbox
    response = await app.get(f"/mosaic/{search_bbox}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0


@pytest.mark.asyncio
async def test_tilejson(app):
    """Create TileJSON."""
    response = await app.get(f"/mosaic/{search_no_bbox}/tilejson.json")
    assert response.status_code == 400

    response = await app.get(f"/mosaic/{search_no_bbox}/tilejson.json?assets=cog")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert resp["name"] == search_no_bbox
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 24
    assert round(resp["bounds"][0]) == -180
    assert "?assets=cog" in resp["tiles"][0]

    response = await app.get(
        f"/mosaic/{search_no_bbox}/tilejson.json?assets=cog&scan_limit=100&items_limit=1&time_limit=2&exitwhenfull=False&skipcovered=False"
    )
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert (
        "?assets=cog&scan_limit=100&items_limit=1&time_limit=2&exitwhenfull=False&skipcovered=False"
        in resp["tiles"][0]
    )

    response = await app.get(f"/mosaic/{search_no_bbox}/tilejson.json?expression=cog")
    assert response.status_code == 200
    resp = response.json()
    assert "?expression=cog" in resp["tiles"][0]

    response = await app.get(f"/mosaic/{search_no_bbox}/tilejson.json?expression=cog")
    assert response.status_code == 200
    resp = response.json()
    assert "?expression=cog" in resp["tiles"][0]

    response = await app.get(
        f"/mosaic/{search_no_bbox}/WorldCRS84Quad/tilejson.json?assets=cog"
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 17
    assert resp["bounds"] == [-180.0, -90.0, 180.0, 90.0]
    assert "?assets=cog" in resp["tiles"][0]

    response = await app.get(
        f"/mosaic/{search_no_bbox}/tilejson.json?assets=cog&tile_format=png"
    )
    assert response.status_code == 200
    resp = response.json()
    assert ".png?assets=cog" in resp["tiles"][0]

    response = await app.get(f"/mosaic/{search_bbox}/tilejson.json?assets=cog")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert resp["name"] == search_bbox
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 24
    assert resp["bounds"] == [-85.535, 36.137, -85.465, 36.179]
    assert "?assets=cog" in resp["tiles"][0]


@patch("rio_tiler.io.cogeo.rasterio")
@pytest.mark.asyncio
async def test_tiles(rio, app):
    """Create tiles."""
    rio.open = mock_rasterio_open

    z, x, y = 15, 8589, 12849

    # missing assets
    response = await app.get(f"/mosaic/tiles/{search_no_bbox}/{z}/{x}/{y}")
    assert response.status_code == 400

    response = await app.get(f"/mosaic/tiles/{search_no_bbox}/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = await app.get(
        f"/mosaic/tiles/{search_no_bbox}/{z}/{x}/{y}?assets=cog&buffer=0.5"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 257
    assert meta["height"] == 257

    response = await app.get(
        f"/mosaic/tiles/{search_no_bbox}/{z}/{x}/{y}.png?assets=cog"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256

    # tile is outside mosaic bbox, it should return 404 (NoAssetFoundError)
    response = await app.get(f"/mosaic/tiles/{search_bbox}/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 404

    response = await app.get(
        f"/mosaic/tiles/{search_no_bbox}/WebMercatorQuad/{z}/{x}/{y}.tif?assets=cog"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["crs"] == CRS.from_epsg(3857)
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = await app.get(
        f"/mosaic/tiles/{search_no_bbox}/WorldCRS84Quad/18/137421/78424.tif?assets=cog"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["crs"] == CRS.from_epsg(4326)
    assert meta["width"] == 256
    assert meta["height"] == 256


@patch("rio_tiler.io.cogeo.rasterio")
@pytest.mark.asyncio
async def test_cql2(rio, app):
    """Test with cql2."""
    rio.open = mock_rasterio_open

    query = {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        }
    }
    response = await app.post("/mosaic/register", json=query)
    assert response.status_code == 200
    resp = response.json()
    assert resp["searchid"]
    assert resp["links"]

    cql2_id = resp["searchid"]

    response = await app.get(f"/mosaic/{cql2_id}/info")
    assert response.status_code == 200
    resp = response.json()
    assert resp["search"]
    assert resp["links"]
    search = resp["search"]
    assert search["search"] == {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        }
    }
    assert search["metadata"] == {"type": "mosaic"}

    response = await app.get(f"/mosaic/{cql2_id}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    response = await app.get(f"/mosaic/{cql2_id}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    response = await app.get(f"/mosaic/{cql2_id}/tilejson.json?assets=cog")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert resp["name"] == cql2_id
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 24
    assert round(resp["bounds"][0]) == -180
    assert "?assets=cog" in resp["tiles"][0]

    z, x, y = 15, 8589, 12849
    response = await app.get(f"/mosaic/tiles/{cql2_id}/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256


@patch("rio_tiler.io.cogeo.rasterio")
@pytest.mark.asyncio
async def test_cql2_with_geometry(rio, app):
    """Test with cql2 with geometry filter."""
    rio.open = mock_rasterio_open
    # Filter with geometry
    query = {
        "filter": {
            "op": "and",
            "args": [
                {
                    "op": "=",
                    "args": [{"property": "collection"}, "noaa-emergency-response"],
                },
                {
                    "op": "s_intersects",
                    "args": [
                        {"property": "geometry"},
                        {
                            "coordinates": [
                                [
                                    [-85.535, 36.137],
                                    [-85.535, 36.179],
                                    [-85.465, 36.179],
                                    [-85.465, 36.137],
                                    [-85.535, 36.137],
                                ]
                            ],
                            "type": "Polygon",
                        },
                    ],
                },
            ],
        }
    }
    response = await app.post("/mosaic/register", json=query)
    assert response.status_code == 200
    resp = response.json()
    assert resp["searchid"]
    assert resp["links"]

    cql2_id = resp["searchid"]

    response = await app.get(f"/mosaic/{cql2_id}/info")
    assert response.status_code == 200
    resp = response.json()
    assert resp["search"]
    assert resp["links"]
    search = resp["search"]
    assert search["metadata"] == {"type": "mosaic"}

    # make sure we can find assets when having both geometry filter and geometry
    response = await app.get(f"/mosaic/{cql2_id}/15/8601/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # point is outside the geometry filter
    response = await app.get(f"/mosaic/{cql2_id}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0

    # make sure we can find assets when having both geometry filter and geometry
    response = await app.get(f"/mosaic/{cql2_id}/15/8601/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # tile is outside the geometry filter
    response = await app.get(f"/mosaic/{cql2_id}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0

    # tile is outside the geometry filter
    z, x, y = 15, 8589, 12849
    response = await app.get(f"/mosaic/tiles/{cql2_id}/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_query_with_metadata(app):
    """Test with cql2."""
    query = {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        },
        "metadata": {"name": "mymosaic", "minzoom": 1, "maxzoom": 2},
    }

    response = await app.post("/mosaic/register", json=query)
    assert response.status_code == 200
    resp = response.json()
    assert resp["searchid"]
    assert resp["links"]

    cql2_id = resp["searchid"]

    response = await app.get(f"/mosaic/{cql2_id}/info")
    assert response.status_code == 200
    resp = response.json()
    assert resp["search"]
    assert resp["links"]
    search = resp["search"]
    assert search["search"] == {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        }
    }
    assert search["metadata"] == {
        "type": "mosaic",
        "name": "mymosaic",
        "minzoom": 1,
        "maxzoom": 2,
    }
