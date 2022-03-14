"""Custom STAC reader."""

from typing import Dict, Optional, Set, Type

import attr
import pystac
from morecantile import TileMatrixSet
from rasterio.crs import CRS
from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import InvalidAssetName, MissingAssets
from rio_tiler.io import BaseReader, COGReader, MultiBaseReader
from rio_tiler.io.stac import DEFAULT_VALID_TYPE, _get_assets


@attr.s
class PgSTACReader(MultiBaseReader):
    """Custom STAC Reader."""

    input: pystac.Item = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)

    geographic_crs: CRS = attr.ib(default=WGS84_CRS)

    include_assets: Optional[Set[str]] = attr.ib(default=None)
    exclude_assets: Optional[Set[str]] = attr.ib(default=None)

    include_asset_types: Set[str] = attr.ib(default=DEFAULT_VALID_TYPE)
    exclude_asset_types: Optional[Set[str]] = attr.ib(default=None)

    reader: Type[BaseReader] = attr.ib(default=COGReader)
    reader_options: Dict = attr.ib(factory=dict)

    fetch_options: Dict = attr.ib(factory=dict)

    def __attrs_post_init__(self):
        """Fetch STAC Item and get list of valid assets."""
        self.bounds = self.input.bbox
        self.crs = WGS84_CRS

        self.assets = list(
            _get_assets(
                self.input,
                include=self.include_assets,
                exclude=self.exclude_assets,
                include_asset_types=self.include_asset_types,
                exclude_asset_types=self.exclude_asset_types,
            )
        )
        if not self.assets:
            raise MissingAssets("No valid asset found")

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

        return self.input.assets[asset].get_absolute_href()
