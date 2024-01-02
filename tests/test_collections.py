"""Test titiler.pgstac Mosaic endpoints."""

import io
from unittest.mock import patch

import rasterio
from rasterio.crs import CRS

from .conftest import mock_rasterio_open, parse_img

collection_id = "noaa-emergency-response"


def test_assets_for_point_collections(app):
    """Get assets for a Point."""
    response = app.get(f"/collections/{collection_id}/-85.5,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2
    assert list(resp[0]) == ["id", "bbox", "assets", "collection"]
    assert resp[0]["id"] == "20200307aC0853130w361030"
    assert resp[1]["id"] == "20200307aC0853000w361030"

    # with coord-crs
    response = app.get(
        f"/collections/{collection_id}/-9517816.46282489,4322990.432036275/assets",
        params={"coord_crs": "epsg:3857"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # CollectionId not found
    response = app.get(
        "/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/-85.5,36.1624/assets"
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "CollectionId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_assets_for_tile_collections(app):
    """Get assets for a Tile."""
    response = app.get(f"/collections/{collection_id}/tiles/15/8589/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets", "collection"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

    response = app.get(f"/collections/{collection_id}/tiles/15/8601/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    response = app.get(
        f"/collections/{collection_id}/tiles/WebMercatorQuad/15/8601/12849/assets"
    )
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # With WGS1994Quad TMS
    response = app.get(
        f"/collections/{collection_id}/tiles/WGS1984Quad/14/8601/4901/assets"
    )
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 4

    response = app.get(f"/collections/{collection_id}/tiles/15/8601/12849/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # CollectionId not found
    response = app.get(
        "/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/tiles/15/8589/12849/assets"
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "CollectionId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_tilejson_collections(app):
    """Create TileJSON."""
    response = app.get(f"/collections/{collection_id}/tilejson.json")
    assert response.status_code == 400

    response = app.get(f"/collections/{collection_id}/tilejson.json?assets=cog")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert resp["name"] == f"Mosaic for '{collection_id}' Collection"
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 24
    assert round(resp["bounds"][0]) == -180
    assert "?assets=cog" in resp["tiles"][0]

    response = app.get(
        f"/collections/{collection_id}/tilejson.json?assets=cog&scan_limit=100&items_limit=1&time_limit=2&exitwhenfull=False&skipcovered=False"
    )
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert (
        "?assets=cog&scan_limit=100&items_limit=1&time_limit=2&exitwhenfull=False&skipcovered=False"
        in resp["tiles"][0]
    )

    response = app.get(f"/collections/{collection_id}/tilejson.json?expression=cog")
    assert response.status_code == 200
    resp = response.json()
    assert "?expression=cog" in resp["tiles"][0]

    response = app.get(f"/collections/{collection_id}/tilejson.json?expression=cog")
    assert response.status_code == 200
    resp = response.json()
    assert "?expression=cog" in resp["tiles"][0]

    response = app.get(
        f"/collections/{collection_id}/WorldCRS84Quad/tilejson.json?assets=cog"
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 23
    for xc, yc in zip(resp["bounds"], [-180.0, -90.0, 180.0, 90.0]):
        assert round(xc, 5) == round(yc, 5)
    assert "?assets=cog" in resp["tiles"][0]

    response = app.get(
        f"/collections/{collection_id}/tilejson.json?assets=cog&tile_format=png"
    )
    assert response.status_code == 200
    resp = response.json()
    assert ".png?assets=cog" in resp["tiles"][0]

    # CollectionId not found
    response = app.get(
        "/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/tilejson.json?assets=cog"
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "CollectionId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


@patch("rio_tiler.io.rasterio.rasterio")
def test_tiles_collections(rio, app):
    """Create tiles."""
    rio.open = mock_rasterio_open

    z, x, y = 15, 8589, 12849

    # missing assets
    response = app.get(f"/collections/{collection_id}/tiles/{z}/{x}/{y}")
    assert response.status_code == 400

    response = app.get(f"/collections/{collection_id}/tiles/{z}/{x}/{y}?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = app.get(
        f"/collections/{collection_id}/tiles/{z}/{x}/{y}?assets=cog&buffer=0.5"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 257
    assert meta["height"] == 257

    response = app.get(f"/collections/{collection_id}/tiles/{z}/{x}/{y}.png?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = app.get(
        f"/collections/{collection_id}/tiles/WebMercatorQuad/{z}/{x}/{y}.tif?assets=cog"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["crs"] == CRS.from_epsg(3857)
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = app.get(
        f"/collections/{collection_id}/tiles/WorldCRS84Quad/18/137421/78424.tif?assets=cog"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["crs"] == CRS.from_epsg(4326)
    assert meta["width"] == 256
    assert meta["height"] == 256

    # CollectionId not found
    response = app.get(
        "/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/tiles/0/0/0?assets=cog"
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "CollectionId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_wmts_collections(app):
    """Create wmts document."""
    # missing assets
    response = app.get(f"/collections/{collection_id}/WMTSCapabilities.xml")
    assert response.status_code == 400
    assert (
        response.json()["detail"]
        == "assets must be defined either via expression or assets options."
    )

    response = app.get(f"/collections/{collection_id}/WMTSCapabilities.xml?assets=cog")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/xml"

    # Validate it's a good WMTS
    with rasterio.open(io.BytesIO(response.content)) as src:
        assert src.crs == "epsg:3857"
        assert src.profile["driver"] == "WMTS"

    response = app.get(
        f"/collections/{collection_id}/WorldCRS84Quad/WMTSCapabilities.xml?assets=cog"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/xml"

    # Validate it's a good WMTS
    with rasterio.open(io.BytesIO(response.content)) as src:
        assert src.crs == "OGC:CRS84"
        assert src.profile["driver"] == "WMTS"


@patch("rio_tiler.io.rasterio.rasterio")
def test_statistics_collections(rio, app):
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

    response = app.post(
        f"/collections/{collection_id}/statistics", json=feat, params={"max_size": 1024}
    )
    assert response.status_code == 400

    response = app.post(
        f"/collections/{collection_id}/statistics",
        json=feat,
        params={"assets": "cog", "max_size": 1024},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    assert response.json()["features"][0]["properties"]["statistics"]["cog_b1"]

    response = app.post(
        f"/collections/{collection_id}/statistics",
        json=feat["features"][0],
        params={"assets": "cog", "max_size": 1024},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    assert response.json()["properties"]["statistics"]["cog_b1"]

    # CollectionId not found
    response = app.post(
        "/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/statistics",
        json=feat,
        params={"assets": "cog", "max_size": 1024},
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "CollectionId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_map_collection(app):
    """test /map endpoint."""
    response = app.get(f"/collections/{collection_id}/map")
    assert response.status_code == 400

    response = app.get(f"/collections/{collection_id}/map", params={"assets": "cog"})
    assert response.status_code == 200


@patch("rio_tiler.io.rasterio.rasterio")
def test_feature_collection(rio, app):
    """Get feature image."""
    rio.open = mock_rasterio_open

    feat = {
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

    response = app.post(
        f"/collections/{collection_id}/feature", json=feat, params={"max_size": 1024}
    )
    assert response.status_code == 400

    response = app.post(
        f"/collections/{collection_id}/feature",
        json=feat,
        params={"assets": "cog", "max_size": 1024},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 725
    assert meta["height"] == 591
    assert meta["count"] == 4

    response = app.post(
        f"/collections/{collection_id}/feature.jpeg",
        json=feat,
        params={"assets": "cog", "max_size": 1024},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 725
    assert meta["height"] == 591
    assert meta["count"] == 3

    response = app.post(
        f"/collections/{collection_id}/feature/300x400.jpeg",
        json=feat,
        params={"assets": "cog", "max_size": 1024},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 300
    assert meta["height"] == 400
    assert meta["count"] == 3

    response = app.post(
        f"/collections/{collection_id}/feature/300x400.tif",
        json=feat,
        params={"assets": "cog", "max_size": 1024},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["crs"] == "epsg:4326"

    response = app.post(
        f"/collections/{collection_id}/feature/300x400.tif",
        json=feat,
        params={"assets": "cog", "max_size": 1024, "dst_crs": "epsg:3857"},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["crs"] == "epsg:3857"


@patch("rio_tiler.io.rasterio.rasterio")
def test_bbox_collection(rio, app):
    """Get bbox image."""
    rio.open = mock_rasterio_open

    bbox = [
        -85.64546585083008,
        36.157904740240866,
        -85.63568115234375,
        36.16587374136926,
    ]
    str_bbox = ",".join(map(str, bbox))
    response = app.get(
        f"/collections/{collection_id}/bbox/{str_bbox}.png", params={"max_size": 1024}
    )
    assert response.status_code == 400

    response = app.get(
        f"/collections/{collection_id}/bbox/{str_bbox}.png",
        params={"assets": "cog", "max_size": 1024},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 725
    assert meta["height"] == 591
    assert meta["count"] == 4

    response = app.get(
        f"/collections/{collection_id}/bbox/{str_bbox}.jpeg",
        params={"assets": "cog", "max_size": 1024},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 725
    assert meta["height"] == 591
    assert meta["count"] == 3

    response = app.get(
        f"/collections/{collection_id}/bbox/{str_bbox}/300x400.jpeg",
        params={"assets": "cog", "max_size": 1024},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 300
    assert meta["height"] == 400
    assert meta["count"] == 3

    response = app.get(
        f"/collections/{collection_id}/bbox/{str_bbox}.tif",
        params={"assets": "cog", "max_size": 1024},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["crs"] == "epsg:4326"

    response = app.get(
        f"/collections/{collection_id}/bbox/{str_bbox}.tif",
        params={"assets": "cog", "max_size": 1024, "dst_crs": "epsg:3857"},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["crs"] == "epsg:3857"


def test_query_point_collections(app):
    """Get values for a Point."""
    response = app.get(
        f"/collections/{collection_id}/-85.5,36.1624/values", params={"assets": "cog"}
    )

    assert response.status_code == 200
    resp = response.json()

    values = resp["values"]
    assert len(values) == 2
    assert values[0][0] == [
        "https://noaa-eri-pds.s3.us-east-1.amazonaws.com/2020_Nashville_Tornado/20200307a_RGB/20200307aC0853130w361030n.tif"
    ]
    assert values[0][2] == ["cog_b1", "cog_b2", "cog_b3"]

    # with coord-crs
    response = app.get(
        f"/collections/{collection_id}/-9517816.46282489,4322990.432036275/values",
        params={"assets": "cog", "coord_crs": "epsg:3857"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert len(resp["values"]) == 2

    # CollectionId not found
    response = app.get(
        "/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/-85.5,36.1624/values",
        params={"assets": "cog"},
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "CollectionId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"

    # at a point with no assets
    response = app.get(
        f"/collections/{collection_id}/-86.0,-35.0/values", params={"assets": "cog"}
    )

    assert response.status_code == 204  # (no content)
