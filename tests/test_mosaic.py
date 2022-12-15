"""Test titiler.pgstac Mosaic endpoints."""

import io
from datetime import datetime
from unittest.mock import patch

import rasterio
from rasterio.crs import CRS

from .conftest import mock_rasterio_open, parse_img

search_no_bbox = "8f5fb37ec266f4b84ec6aa4fe0453c59"
search_bbox = "5e86ce566b979e567370a6ad85aaa68a"


def test_register(app):
    """Register Search requests."""
    query = {"collections": ["noaa-emergency-response"], "filter-lang": "cql-json"}
    response = app.post("/mosaic/register", json=query)
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
    response = app.post("/mosaic/register", json=query)
    assert response.status_code == 200

    resp = response.json()
    assert resp["searchid"] == search_bbox
    assert resp["links"]
    assert [link["rel"] for link in resp["links"]] == ["metadata", "tilejson"]


def test_info(app):
    """Should return metadata about a search query."""
    response = app.get(f"/mosaic/{search_no_bbox}/info")
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

    response = app.get("/mosaic/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/info")
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "SearchId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_assets_for_point(app):
    """Get assets for a Point."""
    response = app.get(f"/mosaic/{search_no_bbox}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets", "collection"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    # make sure we can find assets when having both bbox and geometry
    response = app.get(f"/mosaic/{search_bbox}/-85.5,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # no assets found outside the mosaic bbox
    response = app.get(f"/mosaic/{search_bbox}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0

    # searchId not found
    response = app.get("/mosaic/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/-85.5,36.1624/assets")
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "SearchId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_assets_for_tile(app):
    """Get assets for a Tile."""
    response = app.get(f"/mosaic/{search_no_bbox}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets", "collection"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    # make sure we can find assets when having both bbox and geometry
    response = app.get(f"/mosaic/{search_bbox}/15/8601/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # no assets found outside the query bbox
    response = app.get(f"/mosaic/{search_bbox}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0

    # searchId not found
    response = app.get("/mosaic/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/15/8589/12849/assets")
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "SearchId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_tilejson(app):
    """Create TileJSON."""
    response = app.get(f"/mosaic/{search_no_bbox}/tilejson.json")
    assert response.status_code == 400

    response = app.get(f"/mosaic/{search_no_bbox}/tilejson.json?assets=cog")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert resp["name"] == search_no_bbox
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 24
    assert round(resp["bounds"][0]) == -180
    assert "?assets=cog" in resp["tiles"][0]

    response = app.get(
        f"/mosaic/{search_no_bbox}/tilejson.json?assets=cog&scan_limit=100&items_limit=1&time_limit=2&exitwhenfull=False&skipcovered=False"
    )
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert (
        "?assets=cog&scan_limit=100&items_limit=1&time_limit=2&exitwhenfull=False&skipcovered=False"
        in resp["tiles"][0]
    )

    response = app.get(f"/mosaic/{search_no_bbox}/tilejson.json?expression=cog")
    assert response.status_code == 200
    resp = response.json()
    assert "?expression=cog" in resp["tiles"][0]

    response = app.get(f"/mosaic/{search_no_bbox}/tilejson.json?expression=cog")
    assert response.status_code == 200
    resp = response.json()
    assert "?expression=cog" in resp["tiles"][0]

    response = app.get(
        f"/mosaic/{search_no_bbox}/WorldCRS84Quad/tilejson.json?assets=cog"
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 17
    assert resp["bounds"] == [-180.0, -90.0, 180.0, 90.0]
    assert "?assets=cog" in resp["tiles"][0]

    response = app.get(
        f"/mosaic/{search_no_bbox}/tilejson.json?assets=cog&tile_format=png"
    )
    assert response.status_code == 200
    resp = response.json()
    assert ".png?assets=cog" in resp["tiles"][0]

    response = app.get(f"/mosaic/{search_bbox}/tilejson.json?assets=cog")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert resp["name"] == search_bbox
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 24
    assert resp["bounds"] == [-85.535, 36.137, -85.465, 36.179]
    assert "?assets=cog" in resp["tiles"][0]

    # searchId not found
    response = app.get("/mosaic/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/info?assets=cog")
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "SearchId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


@patch("rio_tiler.io.rasterio.rasterio")
def test_tiles(rio, app):
    """Create tiles."""
    rio.open = mock_rasterio_open

    z, x, y = 15, 8589, 12849

    # missing assets
    response = app.get(f"/mosaic/{search_no_bbox}/tiles/{z}/{x}/{y}")
    assert response.status_code == 400

    response = app.get(f"/mosaic/{search_no_bbox}/tiles/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = app.get(
        f"/mosaic/{search_no_bbox}/tiles/{z}/{x}/{y}?assets=cog&buffer=0.5"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 257
    assert meta["height"] == 257

    response = app.get(f"/mosaic/{search_no_bbox}/tiles/{z}/{x}/{y}.png?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256

    # tile is outside mosaic bbox, it should return 404 (NoAssetFoundError)
    response = app.get(f"/mosaic/{search_bbox}/tiles/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 404

    response = app.get(
        f"/mosaic/{search_no_bbox}/tiles/WebMercatorQuad/{z}/{x}/{y}.tif?assets=cog"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["crs"] == CRS.from_epsg(3857)
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = app.get(
        f"/mosaic/{search_no_bbox}/tiles/WorldCRS84Quad/18/137421/78424.tif?assets=cog"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["crs"] == CRS.from_epsg(4326)
    assert meta["width"] == 256
    assert meta["height"] == 256

    # searchId not found
    response = app.get(
        "/mosaic/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/tiles/0/0/0?assets=cog"
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "SearchId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_wmts(app):
    """Create wmts document."""
    # missing assets
    response = app.get(f"/mosaic/{search_no_bbox}/WMTSCapabilities.xml")
    assert response.status_code == 400
    assert (
        response.json()["detail"]
        == "assets must be defined either via expression or assets options."
    )

    response = app.get(f"/mosaic/{search_no_bbox}/WMTSCapabilities.xml?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/xml"

    # Validate it's a good WMTS
    with rasterio.open(io.BytesIO(response.content)) as src:
        assert src.crs == "epsg:3857"
        assert src.profile["driver"] == "WMTS"

    response = app.get(
        f"/mosaic/{search_no_bbox}/WorldCRS84Quad/WMTSCapabilities.xml?assets=cog"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/xml"

    # Validate it's a good WMTS
    with rasterio.open(io.BytesIO(response.content)) as src:
        assert src.crs == "OGC:CRS84"
        assert src.profile["driver"] == "WMTS"


@patch("rio_tiler.io.rasterio.rasterio")
def test_cql2(rio, app):
    """Test with cql2."""
    rio.open = mock_rasterio_open

    query = {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        }
    }
    response = app.post("/mosaic/register", json=query)
    assert response.status_code == 200
    resp = response.json()
    assert resp["searchid"]
    assert resp["links"]

    cql2_id = resp["searchid"]

    response = app.get(f"/mosaic/{cql2_id}/info")
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

    response = app.get(f"/mosaic/{cql2_id}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets", "collection"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    response = app.get(f"/mosaic/{cql2_id}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets", "collection"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    response = app.get(f"/mosaic/{cql2_id}/tilejson.json?assets=cog")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert resp["name"] == cql2_id
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 24
    assert round(resp["bounds"][0]) == -180
    assert "?assets=cog" in resp["tiles"][0]

    z, x, y = 15, 8589, 12849
    response = app.get(f"/mosaic/{cql2_id}/tiles/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256


@patch("rio_tiler.io.rasterio.rasterio")
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
    response = app.post("/mosaic/register", json=query)
    assert response.status_code == 200
    resp = response.json()
    assert resp["searchid"]
    assert resp["links"]

    cql2_id = resp["searchid"]

    response = app.get(f"/mosaic/{cql2_id}/info")
    assert response.status_code == 200
    resp = response.json()
    assert resp["search"]
    assert resp["links"]
    search = resp["search"]
    assert search["metadata"] == {"type": "mosaic"}

    # make sure we can find assets when having both geometry filter and geometry
    response = app.get(f"/mosaic/{cql2_id}/15/8601/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # point is outside the geometry filter
    response = app.get(f"/mosaic/{cql2_id}/-85.6358,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0

    # make sure we can find assets when having both geometry filter and geometry
    response = app.get(f"/mosaic/{cql2_id}/15/8601/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # tile is outside the geometry filter
    response = app.get(f"/mosaic/{cql2_id}/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 0

    # tile is outside the geometry filter
    z, x, y = 15, 8589, 12849
    response = app.get(f"/mosaic/{cql2_id}/tiles/{z}/{x}/{y}?assets=cog")
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

    response = app.post("/mosaic/register", json=query)
    assert response.status_code == 200
    resp = response.json()
    assert resp["searchid"]
    assert resp["links"]

    cql2_id = resp["searchid"]

    response = app.get(f"/mosaic/{cql2_id}/info")
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

    response = app.get(f"/mosaic/{cql2_id}/tilejson.json?assets=cog")
    assert response.status_code == 200
    resp = response.json()
    assert resp["minzoom"] == 1
    assert resp["maxzoom"] == 2


@patch("rio_tiler.io.rasterio.rasterio")
def test_statistics(rio, app):
    """Get Stats."""
    rio.open = mock_rasterio_open

    feat = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [-85.64065933227539, 36.16587374136926],
                            [-85.64546585083008, 36.161716102717804],
                            [-85.64443588256836, 36.158043338486344],
                            [-85.64083099365234, 36.157904740240866],
                            [-85.63679695129393, 36.15901351934466],
                            [-85.6358528137207, 36.161577510965],
                            [-85.63568115234375, 36.16441859292501],
                            [-85.63902854919434, 36.16511152412467],
                            [-85.64065933227539, 36.16587374136926],
                        ]
                    ],
                },
            }
        ],
    }

    response = app.post(f"/mosaic/{search_no_bbox}/statistics", json=feat)
    assert response.status_code == 400

    response = app.post(
        f"/mosaic/{search_no_bbox}/statistics", json=feat, params={"assets": "cog"}
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    assert response.json()["features"][0]["properties"]["statistics"]["cog_b1"]

    response = app.post(
        f"/mosaic/{search_no_bbox}/statistics",
        json=feat["features"][0],
        params={"assets": "cog"},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    assert response.json()["properties"]["statistics"]["cog_b1"]

    # searchId not found
    response = app.post(
        "/mosaic/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/statistics",
        json=feat,
        params={"assets": "cog"},
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "SearchId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_mosaic_list(app):
    """Test list mosaic."""
    response = app.get("/mosaic/list")
    assert response.status_code == 200
    resp = response.json()
    assert ["searches", "links", "context"] == list(resp)
    assert resp["context"] == {"returned": 5, "limit": 10, "matched": 5}
    assert len(resp["searches"]) == 5
    assert len(resp["links"]) == 1

    response = app.get("/mosaic/list?limit=1")
    assert response.status_code == 200
    resp = response.json()
    assert ["searches", "links", "context"] == list(resp)
    assert resp["context"] == {"returned": 1, "limit": 1, "matched": 5}
    assert len(resp["searches"]) == 1
    assert len(resp["links"]) == 2

    response = app.get("/mosaic/list?limit=1&offset=1")
    assert response.status_code == 200
    resp = response.json()
    assert ["searches", "links", "context"] == list(resp)
    assert resp["context"] == {"returned": 1, "limit": 1, "matched": 5}
    assert len(resp["searches"]) == 1
    assert len(resp["links"]) == 3

    query = {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        },
        "metadata": {"data": "noaa", "num": 2},
    }
    response = app.post("/mosaic/register", json=query)

    query = {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        },
        "metadata": {"data": "noaa", "num": 1},
    }
    response = app.post("/mosaic/register", json=query)

    query = {
        "filter": {
            "op": "=",
            "args": [{"property": "collection"}, "noaa-emergency-response"],
        },
        "metadata": {"data": "noaa", "num": 3},
    }
    response = app.post("/mosaic/register", json=query)

    response = app.get("/mosaic/list?data=noaa")
    assert response.status_code == 200
    resp = response.json()
    assert ["searches", "links", "context"] == list(resp)
    assert resp["context"] == {"returned": 3, "limit": 10, "matched": 3}
    assert len(resp["searches"]) == 3
    assert [s["search"]["metadata"]["num"] for s in resp["searches"]] == [2, 1, 3]

    response = app.get("/mosaic/list?data=noaa&sortby=%2Bnum")
    assert response.status_code == 200
    resp = response.json()
    assert [s["search"]["metadata"]["num"] for s in resp["searches"]] == [1, 2, 3]

    response = app.get("/mosaic/list?data=noaa&sortby=num")
    assert response.status_code == 200
    resp = response.json()
    assert [s["search"]["metadata"]["num"] for s in resp["searches"]] == [1, 2, 3]

    response = app.get("/mosaic/list?data=noaa&sortby=-num")
    assert response.status_code == 200
    resp = response.json()
    assert [s["search"]["metadata"]["num"] for s in resp["searches"]] == [3, 2, 1]

    response = app.get("/mosaic/list?sortby=lastused")
    assert response.status_code == 200
    resp = response.json()
    assert resp["context"] == {"returned": 8, "limit": 10, "matched": 8}
    dates = [
        datetime.strptime(s["search"]["lastused"][0:-6], "%Y-%m-%dT%H:%M:%S.%f")
        for s in resp["searches"]
    ]
    assert dates[0] < dates[-1]

    response = app.get("/mosaic/list?sortby=-lastused")
    assert response.status_code == 200
    resp = response.json()
    assert resp["context"] == {"returned": 8, "limit": 10, "matched": 8}
    dates = [
        datetime.strptime(s["search"]["lastused"][0:-6], "%Y-%m-%dT%H:%M:%S.%f")
        for s in resp["searches"]
    ]
    assert dates[0] > dates[-1]
