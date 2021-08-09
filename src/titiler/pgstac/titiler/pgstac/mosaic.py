"""STACAPI Backend."""

import json
from typing import Any, Dict, List, Optional, Tuple, Type, Union

import attr
import morecantile
from cogeo_mosaic.backends import BaseBackend
from cogeo_mosaic.errors import NoAssetFoundError
from cogeo_mosaic.mosaic import MosaicJSON
from geojson_pydantic import Point, Polygon
from morecantile import TileMatrixSet
from morecantile.utils import bbox_to_feature
from psycopg2 import pool as psycopg2Pool
from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.errors import PointOutsideBounds
from rio_tiler.models import ImageData
from rio_tiler.mosaic import mosaic_reader
from rio_tiler.tasks import multi_values

from titiler.pgstac.reader import CustomSTACReader


@attr.s
class STACAPIBackend(BaseBackend):
    """PGSTAC Api Mosaic Backend."""

    path: str = attr.ib()
    pool: psycopg2Pool = attr.ib()

    reader_options: Dict = attr.ib(factory=dict)

    # Because we are not using mosaicjson we are not limited to the WebMercator TMS
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    # default values for bounds and zoom
    bounds: Tuple[float, float, float, float] = attr.ib(default=(-180, -90, 180, 90))

    # !!! Warning: those should be set by the user ¡¡¡
    minzoom: int = attr.ib(default=0)
    maxzoom: int = attr.ib(default=30)

    reader: Type[CustomSTACReader] = attr.ib(init=False, default=CustomSTACReader)

    # The reader is read-only, we can't pass mosaic_def to the init method
    mosaic_def: MosaicJSON = attr.ib(init=False)

    _backend_name = "PgSTAC"

    def __attrs_post_init__(self):
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

    def write(self, overwrite: bool = True):
        """This method is not used but is required by the abstract class."""
        pass

    def update(self):
        """We overwrite the default method."""
        pass

    def _read(self) -> MosaicJSON:
        """This method is not used but is required by the abstract class."""
        pass

    def assets_for_tile(self, x: int, y: int, z: int, **kwargs: Any) -> List[Dict]:
        """Retrieve assets for tile."""
        bbox = self.tms.bounds(morecantile.Tile(x, y, z))
        return self.get_assets(
            Polygon(coordinates=bbox_to_feature(*bbox)["coordinates"]), **kwargs
        )

    def assets_for_point(self, lng: float, lat: float, **kwargs: Any) -> List[Dict]:
        """Retrieve assets for point."""
        return self.get_assets(Point(coordinates=(0, 0)), **kwargs)

    # TODO: add LRU cache
    def get_assets(
        self,
        geom: Union[Point, Polygon],
        fields: Optional[Dict[str, Any]] = None,
        scan_limit: int = 10000,
        items_limit: int = 100,
        time_limit: int = 5,
        skipcovered: bool = True,
    ) -> List[Dict]:
        """Find assets."""
        fields = fields or {
            "includes": ["assets", "id", "bbox"],
        }

        conn = self.pool.getconn()
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM geojsonsearch(%s, %s, %s, %s, %s, %s, %s);",
                        (
                            geom.json(exclude_none=True),
                            self.path,
                            json.dumps(fields),
                            scan_limit,
                            items_limit,
                            f"{time_limit} seconds",
                            skipcovered,
                        ),
                    )
                    items = cursor.fetchone()[0]
        finally:
            self.pool.putconn(conn)

        return items.get("features", [])

    @property
    def _quadkeys(self) -> List[str]:
        return []

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        reverse: bool = False,
        scan_limit: int = 10000,
        items_limit: int = 100,
        time_limit: int = 5,
        skipcovered: bool = True,
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
            skipcovered=skipcovered,
        )
        if not mosaic_assets:
            raise NoAssetFoundError(
                f"No assets found for tile {tile_z}-{tile_x}-{tile_y}"
            )

        if reverse:
            mosaic_assets = list(reversed(mosaic_assets))

        def _reader(item_id: str, x: int, y: int, z: int, **kwargs: Any) -> ImageData:
            item = list(filter(lambda x: x["id"] == item_id, mosaic_assets))[0]
            with self.reader(item, **self.reader_options) as src_dst:
                return src_dst.tile(x, y, z, **kwargs)

        ids = [assets["id"] for assets in mosaic_assets]
        return mosaic_reader(ids, _reader, tile_x, tile_y, tile_z, **kwargs)

    def point(
        self,
        lon: float,
        lat: float,
        reverse: bool = False,
        scan_limit: int = 10000,
        items_limit: int = 100,
        time_limit: int = 5,
        skipcovered: bool = True,
        **kwargs: Any,
    ) -> List:
        """Get Point value from multiple observation."""
        mosaic_assets = self.assets_for_point(
            lon,
            lat,
            scan_limit=scan_limit,
            items_limit=items_limit,
            time_limit=time_limit,
            skipcovered=skipcovered,
        )
        if not mosaic_assets:
            raise NoAssetFoundError(f"No assets found for point ({lon},{lat})")

        if reverse:
            mosaic_assets = list(reversed(mosaic_assets))

        def _reader(item_id: str, lon: float, lat: float, **kwargs) -> Dict:
            item = list(filter(lambda x: x["id"] == item_id, mosaic_assets))[0]
            with self.reader(item_id, item=item, **self.reader_options) as src_dst:
                return src_dst.point(lon, lat, **kwargs)

        if "allowed_exceptions" not in kwargs:
            kwargs.update({"allowed_exceptions": (PointOutsideBounds,)})

        ids = [assets["id"] for assets in mosaic_assets]
        return list(multi_values(ids, _reader, lon, lat, **kwargs).items())
