"""Test titiler.pgstac search endpoints."""

from unittest.mock import patch

from .conftest import mock_rasterio_open, parse_img

search_no_bbox = "d7f31eb5c11b1b7fa46990ef2de7b136"
search_bbox = "ef44755ef0ecfe9a3be58b6e94ebc264"


def test_register(app):
    """Register Search requests."""
    query = {"collections": ["noaa-emergency-response"], "filter-lang": "cql-json"}
    response = app.post("/register", json=query)
    assert response.status_code == 200

    resp = response.json()
    assert resp["searchid"] == search_no_bbox
    assert resp["metadata"]
    assert resp["tiles"]

    query = {
        "collections": ["noaa-emergency-response"],
        "bbox": [-85.535, 36.137, -85.465, 36.179],
        "filter-lang": "cql-json",
    }
    response = app.post("/register", json=query)
    assert response.status_code == 200

    resp = response.json()
    assert resp["searchid"] == search_bbox
    assert resp["metadata"]
    assert resp["tiles"]


def test_info(app):
    """Should return metadata about a search query."""
    response = app.get(f"/{search_no_bbox}/info")
    assert response.status_code == 200
    resp = response.json()

    assert "hash" in resp
    assert resp["search"] == {
        "collections": ["noaa-emergency-response"],
        "filter-lang": "cql-json",
    }
    assert resp["metadata"] == {}


def test_assets_for_point(app):
    """Get assets for a Point."""
    response = app.get(f"/{search_no_bbox}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    # make sure we can find assets when having both bbox and geometry
    response = app.get(f"/{search_bbox}/-85.5,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # no assets found outside the mosaic bbox
    response = app.get(f"/{search_bbox}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0


def test_assets_for_tile(app):
    """Get assets for a Tile."""
    response = app.get(f"/{search_no_bbox}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    # make sure we can find assets when having both bbox and geometry
    response = app.get(f"/{search_bbox}/15/8601/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # no assets found outside the query bbox
    response = app.get(f"/{search_bbox}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0


def test_tilejson(app):
    """Create TileJSON."""
    response = app.get(f"/{search_no_bbox}/tilejson.json")
    assert response.status_code == 400

    response = app.get(f"/{search_no_bbox}/tilejson.json?assets=cog")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert resp["name"] == search_no_bbox
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 24
    assert round(resp["bounds"][0]) == -180
    assert "?assets=cog" in resp["tiles"][0]

    response = app.get(
        f"/{search_no_bbox}/tilejson.json?assets=cog&scan_limit=100&items_limit=1&time_limit=2&exitwhenfull=False&skipcovered=False"
    )
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert (
        "?assets=cog&scan_limit=100&items_limit=1&time_limit=2&exitwhenfull=False&skipcovered=False"
        in resp["tiles"][0]
    )

    response = app.get(f"/{search_no_bbox}/tilejson.json?expression=cog")
    assert response.status_code == 200
    resp = response.json()
    assert "?expression=cog" in resp["tiles"][0]

    response = app.get(f"/{search_no_bbox}/tilejson.json?expression=cog")
    assert response.status_code == 200
    resp = response.json()
    assert "?expression=cog" in resp["tiles"][0]

    response = app.get(f"/{search_no_bbox}/WorldCRS84Quad/tilejson.json?assets=cog")
    assert response.status_code == 200
    resp = response.json()
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 17
    assert resp["bounds"] == [-180.0, -90.0, 180.0, 90.0]
    assert "?assets=cog" in resp["tiles"][0]

    response = app.get(f"/{search_no_bbox}/tilejson.json?assets=cog&tile_format=png")
    assert response.status_code == 200
    resp = response.json()
    assert ".png?assets=cog" in resp["tiles"][0]

    response = app.get(f"/{search_bbox}/tilejson.json?assets=cog")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert resp["name"] == search_bbox
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 24
    assert resp["bounds"] == [-85.535, 36.137, -85.465, 36.179]
    assert "?assets=cog" in resp["tiles"][0]


@patch("rio_tiler.io.cogeo.rasterio")
def test_tiles(rio, app):
    """Create tiles."""
    rio.open = mock_rasterio_open

    z, x, y = 15, 8589, 12849

    # missing assets
    response = app.get(f"/tiles/{search_no_bbox}/{z}/{x}/{y}")
    assert response.status_code == 400

    response = app.get(f"/tiles/{search_no_bbox}/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = app.get(f"/tiles/{search_no_bbox}/{z}/{x}/{y}.png?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256

    # tile is outside mosaic bbox, it should return 404 (NoAssetFoundError)
    response = app.get(f"/tiles/{search_bbox}/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 404


@patch("rio_tiler.io.cogeo.rasterio")
def test_cql2(rio, app):
    """Test with cql2."""
    rio.open = mock_rasterio_open

    query = {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        }
    }
    response = app.post("/register", json=query)
    assert response.status_code == 200
    resp = response.json()
    assert resp["metadata"]
    assert resp["tiles"]

    cql2_id = resp["searchid"]

    response = app.get(f"/{cql2_id}/info")
    assert response.status_code == 200
    resp = response.json()
    assert "hash" in resp
    assert resp["search"] == {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        }
    }
    assert resp["metadata"] == {}

    response = app.get(f"/{cql2_id}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    response = app.get(f"/{cql2_id}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    response = app.get(f"/{cql2_id}/tilejson.json?assets=cog")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert resp["name"] == cql2_id
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 24
    assert round(resp["bounds"][0]) == -180
    assert "?assets=cog" in resp["tiles"][0]

    z, x, y = 15, 8589, 12849
    response = app.get(f"/tiles/{cql2_id}/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256


@patch("rio_tiler.io.cogeo.rasterio")
def test_cql2_with_geometry(rio, app):
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
    response = app.post("/register", json=query)
    assert response.status_code == 200
    resp = response.json()
    assert resp["metadata"]
    assert resp["tiles"]

    cql2_id = resp["searchid"]

    response = app.get(f"/{cql2_id}/info")
    assert response.status_code == 200
    resp = response.json()
    assert "hash" in resp
    assert resp["metadata"] == {}

    # make sure we can find assets when having both geometry filter and geometry
    response = app.get(f"/{cql2_id}/15/8601/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # point is outside the geometry filter
    response = app.get(f"/{cql2_id}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0

    # make sure we can find assets when having both geometry filter and geometry
    response = app.get(f"/{cql2_id}/15/8601/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # tile is outside the geometry filter
    response = app.get(f"/{cql2_id}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0

    # tile is outside the geometry filter
    z, x, y = 15, 8589, 12849
    response = app.get(f"/tiles/{cql2_id}/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 404


def test_query_with_metadata(app):
    """Test with cql2."""
    query = {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        },
        "metadata": {"name": "mymosaic", "minzoom": 1, "maxzoom": 2},
    }

    response = app.post("/register", json=query)
    assert response.status_code == 200
    resp = response.json()
    assert resp["metadata"]
    assert resp["tiles"]

    cql2_id = resp["searchid"]

    response = app.get(f"/{cql2_id}/info")
    assert response.status_code == 200
    resp = response.json()
    assert "hash" in resp
    assert resp["search"] == {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        }
    }
    assert resp["metadata"] == {"name": "mymosaic", "minzoom": 1, "maxzoom": 2}
