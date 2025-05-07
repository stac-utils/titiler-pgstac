"""Test titiler.pgstac Mosaic endpoints."""

import io
from unittest.mock import patch

import rasterio
from rasterio.crs import CRS

from .conftest import mock_rasterio_open, parse_img

collection_id = "noaa-emergency-response"


def test_assets_for_point_collections(app):
    """Get assets for a Point."""
    response = app.get(f"/collections/{collection_id}/point/-85.5,36.1624/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2
    assert list(resp[0]) == ["id", "bbox", "assets", "collection"]
    assert resp[0]["id"] == "20200307aC0853130w361030"
    assert resp[1]["id"] == "20200307aC0853000w361030"

    # with coord-crs
    response = app.get(
        f"/collections/{collection_id}/point/-9517816.46282489,4322990.432036275/assets",
        params={"coord_crs": "epsg:3857"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 2

    # CollectionId not found
    response = app.get(
        "/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/point/-85.5,36.1624/assets"
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "CollectionId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_assets_for_tile_collections(app):
    """Get assets for a Tile."""
    response = app.get(
        f"/collections/{collection_id}/tiles/WebMercatorQuad/15/8589/12849/assets"
    )
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert list(resp[0]) == ["id", "bbox", "assets", "collection"]
    assert resp[0]["id"] == "20200307aC0853900w361030"

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

    # CollectionId not found
    response = app.get(
        "/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/tiles/WebMercatorQuad/15/8589/12849/assets"
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "CollectionId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_assets_for_bbox_collections(app):
    """Get assets for a Point."""

    bbox = [-86.0, 36.0, -85.0, 37.0]
    str_bbox = ",".join(map(str, bbox))

    response = app.get(f"/collections/{collection_id}/bbox/{str_bbox}/assets")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 61

    bbox = [-9573476, 4300621, -9462156, 4439106]
    str_bbox = ",".join(map(str, bbox))

    # with coord-crs
    response = app.get(
        f"/collections/{collection_id}/bbox/{str_bbox}/assets",
        params={"coord_crs": "epsg:3857"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 61

    # CollectionId not found
    response = app.get(
        f"/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/bbox/{str_bbox}/assets"
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "CollectionId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_tilejson_collections(app):
    """Create TileJSON."""
    response = app.get(f"/collections/{collection_id}/WebMercatorQuad/tilejson.json")
    assert response.status_code == 400

    response = app.get(
        f"/collections/{collection_id}/WebMercatorQuad/tilejson.json?assets=cog"
    )
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert resp["name"] == f"Mosaic for '{collection_id}' Collection"
    assert resp["minzoom"] == 0
    assert resp["maxzoom"] == 24
    assert round(resp["bounds"][0]) == -180
    assert "?assets=cog" in resp["tiles"][0]

    response = app.get(
        f"/collections/{collection_id}/WebMercatorQuad/tilejson.json?assets=cog&scan_limit=100&items_limit=1&time_limit=2&exitwhenfull=False&skipcovered=False"
    )
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    resp = response.json()
    assert (
        "?assets=cog&scan_limit=100&items_limit=1&time_limit=2&exitwhenfull=False&skipcovered=False"
        in resp["tiles"][0]
    )

    response = app.get(
        f"/collections/{collection_id}/WebMercatorQuad/tilejson.json?expression=cog"
    )
    assert response.status_code == 200
    resp = response.json()
    assert "?expression=cog" in resp["tiles"][0]

    response = app.get(
        f"/collections/{collection_id}/WebMercatorQuad/tilejson.json?expression=cog"
    )
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
        f"/collections/{collection_id}/WebMercatorQuad/tilejson.json?assets=cog&tile_format=png"
    )
    assert response.status_code == 200
    resp = response.json()
    assert ".png?assets=cog" in resp["tiles"][0]

    # CollectionId not found
    response = app.get(
        "/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/WebMercatorQuad/tilejson.json?assets=cog"
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
    response = app.get(
        f"/collections/{collection_id}/tiles/WebMercatorQuad/{z}/{x}/{y}"
    )
    assert response.status_code == 400

    response = app.get(
        f"/collections/{collection_id}/tiles/WebMercatorQuad/{z}/{x}/{y}?assets=cog"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = app.get(
        f"/collections/{collection_id}/tiles/WebMercatorQuad/{z}/{x}/{y}?assets=cog&buffer=0.5"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 257
    assert meta["height"] == 257

    response = app.get(
        f"/collections/{collection_id}/tiles/WebMercatorQuad/{z}/{x}/{y}.png?assets=cog"
    )
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
        "/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/tiles/WebMercatorQuad/0/0/0?assets=cog"
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "CollectionId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"


def test_wmts_collections(app):
    """Create wmts document."""
    # missing assets
    response = app.get(
        f"/collections/{collection_id}/WebMercatorQuad/WMTSCapabilities.xml"
    )
    assert response.status_code == 400
    assert (
        response.json()["detail"]
        == "Could not find any valid layers in metadata or construct one from Query Parameters."
    )

    response = app.get(
        f"/collections/{collection_id}/WebMercatorQuad/WMTSCapabilities.xml?assets=cog"
    )
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
    response = app.get(f"/collections/{collection_id}/WebMercatorQuad/map.html")
    assert response.status_code == 400

    response = app.get(
        f"/collections/{collection_id}/WebMercatorQuad/map.html",
        params={"assets": "cog"},
    )
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
        f"/collections/{collection_id}/point/-85.5,36.1624", params={"assets": "cog"}
    )

    assert response.status_code == 200
    resp = response.json()
    values = resp["values"]
    assert len(values) == 2
    assert values[0][0] == "noaa-emergency-response/20200307aC0853130w361030"
    assert values[0][2] == ["cog_b1", "cog_b2", "cog_b3"]
    assert values[1][0] == "noaa-emergency-response/20200307aC0853000w361030"

    # with coord-crs
    response = app.get(
        f"/collections/{collection_id}/point/-9517816.46282489,4322990.432036275",
        params={"assets": "cog", "coord_crs": "epsg:3857"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert len(resp["values"]) == 2

    # CollectionId not found
    response = app.get(
        "/collections/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/point/-85.5,36.1624",
        params={"assets": "cog"},
    )
    assert response.status_code == 404
    resp = response.json()
    assert resp["detail"] == "CollectionId `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` not found"

    # at a point with no assets
    response = app.get(
        f"/collections/{collection_id}/point/-86.0,-35.0", params={"assets": "cog"}
    )

    assert response.status_code == 204  # (no content)


def test_collections_render(app, tmp_path):
    """Create wmts document."""
    response = app.get(
        "/collections/MAXAR_BayofBengal_Cyclone_Mocha_May_23/WebMercatorQuad/WMTSCapabilities.xml"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/xml"

    wmts = tmp_path / "WMTSCapabilities.xml"
    with open(wmts, "wb") as f:
        f.write(response.content)

    # Validate it's a good WMTS
    with rasterio.open(wmts) as src:
        assert not src.crs
        assert src.profile["driver"] == "WMTS"
        assert len(src.subdatasets) == 3
        assert ["color", "visual", "visualr"] == [
            s.split(",layer=")[1] for s in src.subdatasets
        ]
        with rasterio.open(src.subdatasets[0]) as sub:
            assert sub.crs == CRS.from_epsg(3857)
            assert sub.profile["driver"] == "WMTS"

    response = app.get("/collections/MAXAR_BayofBengal_Cyclone_Mocha_May_23/info")
    assert response.status_code == 200
    assert len(response.json()["links"]) == 10  # self, tilejson (4), map (4), wmts (1)


def test_collections_additional_parameters(app):
    """Check that additional parameter work."""
    # bbox
    response = app.get(
        "/collections/noaa-emergency-response/info",
        params={"bbox": "-87.0251,36.1749,-86.9999,36.2001"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["search"]["search"]["bbox"] == [-87.0251, 36.1749, -86.9999, 36.2001]
    assert resp["search"]["metadata"]["bounds"] == [
        -87.0251,
        36.1749,
        -86.9999,
        36.2001,
    ]

    # ids
    response = app.get(
        "/collections/noaa-emergency-response/info",
        params={"ids": "20200307aC0853130w361030"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["search"]["search"]["ids"] == ["20200307aC0853130w361030"]

    response = app.get(
        "/collections/noaa-emergency-response/point/-85.5,36.1624/assets",
        params={"ids": "20200307aC0853130w361030"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 1
    assert resp[0]["id"] == "20200307aC0853130w361030"

    # datetime
    response = app.get(
        "/collections/noaa-emergency-response/info",
        params={"datetime": "2020-03-07T00:00:00Z"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["search"]["search"]["datetime"] == "2020-03-07T00:00:00Z"

    response = app.get(
        "/collections/noaa-emergency-response/info",
        params={"datetime": "../2020-03-07T00:00:00Z"},
    )
    assert response.status_code == 200
    resp = response.json()
    assert resp["search"]["search"]["datetime"] == "../2020-03-07T00:00:00Z"
