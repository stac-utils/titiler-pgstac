"""test custom reader."""

import json
import os

import pystac

from titiler.pgstac.reader import PgSTACReader, SimpleSTACReader

DATA_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
item = os.path.join(DATA_DIR, "20200307aC0853900w361030.json")
asset_url = os.path.join(DATA_DIR, "20200307aC0853900w361030n.tif")

with open(item, "r") as f:
    pystac_item = pystac.Item.from_dict(json.load(f))


def test_pgstac_reader():
    """Test PgSTACReader."""
    with PgSTACReader(pystac_item) as stac:
        assert stac.assets == ["cog"]
        assert stac._get_asset_info("cog")
        assert stac.tile(4293, 6424, 14, assets="cog")

        assert stac._get_asset_info("vrt://cog?bands=1")
        assert stac.tile(4293, 6424, 14, assets="vrt://cog?bands=1")


def test_pgstac_simple_reader():
    """Test simple Dict STACReader."""
    stac_dict = {
        "id": "20200307aC0853900w361030",
        "collection": "noaa-emergency-response",
        "bbox": [-85.6501, 36.1499, -85.6249, 36.1751],
        "assets": {"cog": {"href": asset_url}},
    }
    with SimpleSTACReader(stac_dict) as stac:
        assert stac.assets == ["cog"]
        assert stac._get_asset_info("cog")
        assert stac.tile(4293, 6424, 14, assets="cog")

        assert stac._get_asset_info("vrt://cog?bands=1")
        assert stac.tile(4293, 6424, 14, assets="vrt://cog?bands=1")
