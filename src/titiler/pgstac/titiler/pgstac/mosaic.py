"""STACAPI Backend."""

from typing import Any, Coroutine, Dict, List, Tuple, Type, Union

import asyncpg
import attr
import morecantile
from buildpg import render
from cogeo_mosaic.backends import BaseBackend
from cogeo_mosaic.errors import NoAssetFoundError
from cogeo_mosaic.mosaic import MosaicJSON
from geojson_pydantic import Point, Polygon
from morecantile import TileMatrixSet
from morecantile.utils import bbox_to_feature
from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.models import ImageData

from titiler.pgstac.compat import AsyncReader, async_mosaic_reader
from titiler.pgstac.reader import CustomSTACReader

async_reader = type("AsyncReader", (AsyncReader,), {"reader": CustomSTACReader})


@attr.s
class STACAPIBackend(BaseBackend):
    """PGSTAC Api Mosaic Backend."""

    path: str = attr.ib()
    pool: asyncpg.pool = attr.ib()

    reader_options: Dict = attr.ib(factory=dict)

    # Because we are not using mosaicjson we are not limited to the WebMercator TMS
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    # default values for bounds and zoom
    bounds: Tuple[float, float, float, float] = attr.ib(
        init=False, default=(-180, -90, 180, 90)
    )

    # !!! Warning: those should be set by the user ¡¡¡
    minzoom: int = attr.ib(default=0)
    maxzoom: int = attr.ib(default=30)

    reader: Type[AsyncReader] = attr.ib(init=False, default=async_reader)

    # The reader is read-only, we can't pass mosaic_def to the init method
    mosaic_def: MosaicJSON = attr.ib(init=False)

    _backend_name = "STACFastAPI"

    def __attrs_post_init__(self):
        """Post Init."""
        # Construct a FAKE mosaicJSON
        # mosaic_def has to be defined.
        # we set `tiles` to an empty list.
        self.mosaic_def = MosaicJSON(
            mosaicjson="0.0.2",
            name=self.path,
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

    async def assets_for_tile(self, x: int, y: int, z: int) -> List[Dict]:
        """Retrieve assets for tile."""
        bbox = self.tms.bounds(morecantile.Tile(x, y, z))
        return await self.get_assets(
            Polygon(coordinates=bbox_to_feature(*bbox)["coordinates"])
        )

    async def assets_for_point(self, lng: float, lat: float) -> List[Dict]:
        """Retrieve assets for point."""
        return await self.get_assets(Point(coordinates=(0, 0)))

    # TODO: add LRU cache
    async def get_assets(self, geom: Union[Point, Polygon]) -> List[Dict]:
        """Find assets."""
        async with self.pool.acquire() as conn:
            q, p = render(
                """
                SELECT * FROM items_for_geom(:mosaicid::text, :geom::text::jsonb);
                """,
                mosaicid=self.path,
                geom=geom.json(exclude_none=True),
            )
            items = await conn.fetchval(q, *p)
        return items.get("features", [])

    @property
    def _quadkeys(self) -> List[str]:
        return []

    async def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        reverse: bool = False,
        **kwargs: Any,
    ) -> Tuple[ImageData, List[str]]:
        """Get Tile from multiple observation."""
        mosaic_assets = await self.assets_for_tile(tile_x, tile_y, tile_z)
        if not mosaic_assets:
            raise NoAssetFoundError(
                f"No assets found for tile {tile_z}-{tile_x}-{tile_y}"
            )

        if reverse:
            mosaic_assets = list(reversed(mosaic_assets))

        async def _reader(
            item_id: str, x: int, y: int, z: int, **kwargs: Any
        ) -> Coroutine[Any, Any, ImageData]:
            item = list(filter(lambda x: x["id"] == item_id, mosaic_assets))[0]
            async with self.reader(item, **self.reader_options) as src_dst:
                return await src_dst.tile(x, y, z, **kwargs)

        ids = [assets["id"] for assets in mosaic_assets]
        return await async_mosaic_reader(ids, _reader, tile_x, tile_y, tile_z, **kwargs)

    async def point(
        self, lon: float, lat: float, reverse: bool = False, **kwargs: Any,
    ) -> List:
        """Get Point value from multiple observation."""
        raise NotImplementedError
        # mosaic_assets = await self.assets_for_point(lon, lat)
        # if not mosaic_assets:
        #     raise NoAssetFoundError(f"No assets found for point ({lon},{lat})")

        # if reverse:
        #     mosaic_assets = list(reversed(mosaic_assets))

        # def _reader(item_id: str, lon: float, lat: float, **kwargs) -> Dict:
        #     item = list(filter(lambda x: x["id"] == item_id, mosaic_assets))[0]
        #     with self.reader(item_id, item=item, **self.reader_options) as src_dst:
        #         return src_dst.point(lon, lat, **kwargs)

        # if "allowed_exceptions" not in kwargs:
        #     kwargs.update({"allowed_exceptions": (PointOutsideBounds,)})

        # ids = [assets["id"] for assets in mosaic_assets]
        # return list(multi_values(ids, _reader, lon, lat, **kwargs).items())
