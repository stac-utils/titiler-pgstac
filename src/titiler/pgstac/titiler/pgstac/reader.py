"""Simplified STAC reader."""

from typing import Any, Dict, Type

import attr
from morecantile import TileMatrixSet
from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.errors import InvalidAssetName
from rio_tiler.io.base import BaseReader, MultiBaseReader
from rio_tiler.io.cogeo import COGReader


@attr.s
class CustomSTACReader(MultiBaseReader):
    """Simplified STAC Reader.

    Items should be in form of:
    {
        "id": "IAMASTACITEM",
        "bbox": (0, 0, 10, 10),
        "assets": {
            "COG": {
                "href": "https://somewhereovertherainbow.io/cog.tif"
            }
        }

    }

    """

    item: Dict[str, Any] = attr.ib()
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)
    reader: Type[BaseReader] = attr.ib(default=COGReader)
    reader_options: Dict = attr.ib(factory=dict)

    def __attrs_post_init__(self):
        """Fetch STAC Item and get list of valid assets."""
        self.bounds = self.item["bbox"]
        self.assets = list(self.item["assets"])

        if self.minzoom is None:
            self.minzoom = self.tms.minzoom

        if self.maxzoom is None:
            self.maxzoom = self.tms.maxzoom

    def _get_asset_url(self, asset: str) -> str:
        """Validate asset names and return asset's url.

        Args:
            asset (str): STAC asset name.

        Returns:
            str: STAC asset href.

        """
        if asset not in self.assets:
            raise InvalidAssetName(f"{asset} is not valid")

        return self.item["assets"][asset]["href"]
