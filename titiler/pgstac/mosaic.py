"""TiTiler.PgSTAC custom Mosaic Backend and Custom STACReader."""

import json
from typing import Any, Dict, List, Optional, Tuple, Type, Union

import attr
import morecantile
from cachetools import TTLCache, cached
from cachetools.keys import hashkey
from cogeo_mosaic.backends import BaseBackend
from cogeo_mosaic.errors import NoAssetFoundError
from cogeo_mosaic.mosaic import MosaicJSON
from geojson_pydantic import Point, Polygon
from morecantile import TileMatrixSet
from psycopg2 import pool as psycopg2Pool
from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.errors import InvalidAssetName, PointOutsideBounds
from rio_tiler.io.base import BaseReader, MultiBaseReader
from rio_tiler.io.cogeo import COGReader
from rio_tiler.models import ImageData
from rio_tiler.mosaic import mosaic_reader
from rio_tiler.tasks import multi_values

from titiler.pgstac.settings import CacheSettings

cache_config = CacheSettings()


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

    def __attrs_post_init__(self) -> None:
        """Set reader spatial infos and list of valid assets."""
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


@attr.s
class PGSTACBackend(BaseBackend):
    """PgSTAC Mosaic Backend."""

    # Mosaic ID (hash)
    path: str = attr.ib()

    # Connection POOL to the database
    pool: psycopg2Pool = attr.ib()

    reader_options: Dict = attr.ib(factory=dict)

    # Because we are not using mosaicjson we are not limited to the WebMercator TMS
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    # default values for bounds
    bounds: Tuple[float, float, float, float] = attr.ib(default=(-180, -90, 180, 90))

    # !!! Warning: those should be set by the user ¡¡¡
    minzoom: int = attr.ib(default=0)
    maxzoom: int = attr.ib(default=30)

    # Use Custom STAC reader
    reader: Type[CustomSTACReader] = attr.ib(init=False, default=CustomSTACReader)

    # The reader is read-only, we can't pass mosaic_def to the init method
    mosaic_def: MosaicJSON = attr.ib(init=False)

    _backend_name = "PgSTAC"

    def __attrs_post_init__(self) -> None:
        """Post Init."""
        # Construct a FAKE mosaicJSON
        # mosaic_def has to be defined.
        # we set `tiles` to an empty list.
        self.mosaic_def = MosaicJSON(
            mosaicjson="0.0.2",
            name=self.path,
            bounds=self.bounds,
            minzoom=self.minzoom,
            maxzoom=self.maxzoom,
            tiles=[],
        )

    def write(self, overwrite: bool = True) -> None:
        """This method is not used but is required by the abstract class."""
        pass

    def update(self) -> None:
        """We overwrite the default method."""
        pass

    def _read(self) -> MosaicJSON:
        """This method is not used but is required by the abstract class."""
        pass

    def assets_for_tile(self, x: int, y: int, z: int, **kwargs: Any) -> List[Dict]:
        """Retrieve assets for tile."""
        bbox = self.tms.bounds(morecantile.Tile(x, y, z))
        return self.get_assets(Polygon.from_bounds(*bbox), **kwargs)

    def assets_for_point(self, lng: float, lat: float, **kwargs: Any) -> List[Dict]:
        """Retrieve assets for point."""
        # Point search is currently broken within PgSTAC
        # in order to return the correct result we need to make sure exitwhenfull and skipcovered options
        # are set to `False`
        # ref: https://github.com/stac-utils/pgstac/pull/52
        kwargs.update(**{"exitwhenfull": False, "skipcovered": False})
        return self.get_assets(Point(coordinates=(lng, lat)), **kwargs)

    @cached(
        TTLCache(maxsize=cache_config.maxsize, ttl=cache_config.ttl),
        key=lambda self, geom, **kwargs: hashkey(self.path, str(geom), **kwargs),
    )
    def get_assets(
        self,
        geom: Union[Point, Polygon],
        fields: Optional[Dict[str, Any]] = None,
        scan_limit: Optional[int] = None,
        items_limit: Optional[int] = None,
        time_limit: Optional[int] = None,
        exitwhenfull: Optional[bool] = None,
        skipcovered: Optional[bool] = None,
    ) -> List[Dict]:
        """Find assets."""
        fields = fields or {
            "include": ["assets", "id", "bbox"],
        }

        scan_limit = scan_limit or 10000
        items_limit = items_limit or 100
        time_limit = time_limit or 5
        exitwhenfull = True if exitwhenfull is None else exitwhenfull
        skipcovered = True if skipcovered is None else skipcovered

        conn = self.pool.getconn()
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM geojsonsearch(%s, %s, %s, %s, %s, %s, %s, %s);",
                        (
                            geom.json(exclude_none=True),
                            self.path,
                            json.dumps(fields),
                            scan_limit,
                            items_limit,
                            f"{time_limit} seconds",
                            exitwhenfull,
                            skipcovered,
                        ),
                    )
                    resp = cursor.fetchone()[0]
        finally:
            self.pool.putconn(conn)

        return resp.get("features", [])

    @property
    def _quadkeys(self) -> List[str]:
        return []

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        reverse: bool = False,
        scan_limit: Optional[int] = None,
        items_limit: Optional[int] = None,
        time_limit: Optional[int] = None,
        exitwhenfull: Optional[bool] = None,
        skipcovered: Optional[bool] = None,
        **kwargs: Any,
    ) -> Tuple[ImageData, List[str]]:
        """Get Tile from multiple observation."""
        mosaic_assets = self.assets_for_tile(
            tile_x,
            tile_y,
            tile_z,
            scan_limit=scan_limit,
            items_limit=items_limit,
            time_limit=time_limit,
            exitwhenfull=exitwhenfull,
            skipcovered=skipcovered,
        )

        if not mosaic_assets:
            raise NoAssetFoundError(
                f"No assets found for tile {tile_z}-{tile_x}-{tile_y}"
            )

        if reverse:
            mosaic_assets = list(reversed(mosaic_assets))

        def _reader(
            item: Dict[str, Any], x: int, y: int, z: int, **kwargs: Any
        ) -> ImageData:
            with self.reader(item, **self.reader_options) as src_dst:
                return src_dst.tile(x, y, z, **kwargs)

        return mosaic_reader(mosaic_assets, _reader, tile_x, tile_y, tile_z, **kwargs)

    def point(
        self,
        lon: float,
        lat: float,
        reverse: bool = False,
        scan_limit: Optional[int] = None,
        items_limit: Optional[int] = None,
        time_limit: Optional[int] = None,
        exitwhenfull: Optional[bool] = None,
        skipcovered: Optional[bool] = None,
        **kwargs: Any,
    ) -> List:
        """Get Point value from multiple observation."""
        mosaic_assets = self.assets_for_point(
            lon,
            lat,
            scan_limit=scan_limit,
            items_limit=items_limit,
            time_limit=time_limit,
            exitwhenfull=exitwhenfull,
            skipcovered=skipcovered,
        )
        if not mosaic_assets:
            raise NoAssetFoundError(f"No assets found for point ({lon},{lat})")

        if reverse:
            mosaic_assets = list(reversed(mosaic_assets))

        def _reader(
            item: Dict[str, Any], lon: float, lat: float, **kwargs: Any,
        ) -> Dict:
            with self.reader(item, **self.reader_options) as src_dst:
                return src_dst.point(lon, lat, **kwargs)

        if "allowed_exceptions" not in kwargs:
            kwargs.update({"allowed_exceptions": (PointOutsideBounds,)})

        return list(multi_values(mosaic_assets, _reader, lon, lat, **kwargs).items())
