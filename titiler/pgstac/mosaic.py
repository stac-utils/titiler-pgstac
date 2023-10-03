"""TiTiler.PgSTAC custom Mosaic Backend and Custom STACReader."""

import json
from typing import Any, Dict, List, Optional, Tuple, Type

import attr
import rasterio
from cachetools import TTLCache, cached
from cachetools.keys import hashkey
from cogeo_mosaic.backends import BaseBackend
from cogeo_mosaic.errors import MosaicNotFoundError, NoAssetFoundError
from cogeo_mosaic.mosaic import MosaicJSON
from geojson_pydantic import Point, Polygon
from geojson_pydantic.geometries import Geometry, parse_geometry_obj
from morecantile import Tile, TileMatrixSet
from psycopg import errors as pgErrors
from psycopg_pool import ConnectionPool
from rasterio.crs import CRS
from rasterio.warp import transform, transform_bounds, transform_geom
from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import InvalidAssetName, PointOutsideBounds
from rio_tiler.io import Reader
from rio_tiler.io.base import BaseReader, MultiBaseReader
from rio_tiler.models import ImageData
from rio_tiler.mosaic import mosaic_reader
from rio_tiler.tasks import multi_values
from rio_tiler.types import AssetInfo, BBox

from titiler.pgstac.settings import CacheSettings, RetrySettings
from titiler.pgstac.utils import retry

cache_config = CacheSettings()
retry_config = RetrySettings()


@attr.s
class CustomSTACReader(MultiBaseReader):
    """Simplified STAC Reader.

    Inputs should be in form of:
    {
        "id": "IAMASTACITEM",
        "collection": "mycollection",
        "bbox": (0, 0, 10, 10),
        "assets": {
            "COG": {
                "href": "https://somewhereovertherainbow.io/cog.tif"
            }
        }
    }

    """

    input: Dict[str, Any] = attr.ib()
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib()
    maxzoom: int = attr.ib()

    reader: Type[BaseReader] = attr.ib(default=Reader)
    reader_options: Dict = attr.ib(factory=dict)

    ctx: Any = attr.ib(default=rasterio.Env)

    def __attrs_post_init__(self) -> None:
        """Set reader spatial infos and list of valid assets."""
        self.bounds = self.input["bbox"]
        self.crs = WGS84_CRS  # Per specification STAC items are in WGS84
        self.assets = list(self.input["assets"])

    @minzoom.default
    def _minzoom(self):
        return self.tms.minzoom

    @maxzoom.default
    def _maxzoom(self):
        return self.tms.maxzoom

    def _get_asset_info(self, asset: str) -> AssetInfo:
        """Validate asset names and return asset's url.

        Args:
            asset (str): STAC asset name.

        Returns:
            str: STAC asset href.

        """
        if asset not in self.assets:
            raise InvalidAssetName(
                f"{asset} is not valid. Should be one of {self.assets}"
            )

        asset_info = self.input["assets"][asset]
        info = AssetInfo(
            url=asset_info["href"],
            env={},
        )

        if header_size := asset_info.get("file:header_size"):
            info["env"]["GDAL_INGESTED_BYTES_AT_OPEN"] = header_size

        if bands := asset_info.get("raster:bands"):
            stats = [
                (b["statistics"]["minimum"], b["statistics"]["maximum"])
                for b in bands
                if {"minimum", "maximum"}.issubset(b.get("statistics", {}))
            ]
            if len(stats) == len(bands):
                info["dataset_statistics"] = stats

        return info


@attr.s
class PGSTACBackend(BaseBackend):
    """PgSTAC Mosaic Backend."""

    # Mosaic ID (hash)
    input: str = attr.ib()

    # Connection POOL to the database
    pool: ConnectionPool = attr.ib()

    # Because we are not using mosaicjson we are not limited to the WebMercator TMS
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib()
    maxzoom: int = attr.ib()

    # Use Custom STAC reader (outside init)
    reader: Type[CustomSTACReader] = attr.ib(init=False, default=CustomSTACReader)
    reader_options: Dict = attr.ib(factory=dict)

    # default values for bounds
    bounds: BBox = attr.ib(default=(-180, -90, 180, 90))

    crs: CRS = attr.ib(default=WGS84_CRS)
    geographic_crs: CRS = attr.ib(default=WGS84_CRS)

    # The reader is read-only (outside init)
    mosaic_def: MosaicJSON = attr.ib(init=False)

    _backend_name = "PgSTAC"

    def __attrs_post_init__(self) -> None:
        """Post Init."""
        # Construct a FAKE mosaicJSON
        # mosaic_def has to be defined.
        # we set `tiles` to an empty list.
        self.mosaic_def = MosaicJSON(
            mosaicjson="0.0.3",
            name=self.input,
            bounds=self.bounds,
            minzoom=self.minzoom,
            maxzoom=self.maxzoom,
            tiles={},
        )

    @minzoom.default
    def _minzoom(self):
        return self.tms.minzoom

    @maxzoom.default
    def _maxzoom(self):
        return self.tms.maxzoom

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
        bbox = self.tms.bounds(Tile(x, y, z))
        return self.get_assets(Polygon.from_bounds(*bbox), **kwargs)

    def assets_for_point(
        self,
        lng: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        **kwargs: Any,
    ) -> List[Dict]:
        """Retrieve assets for point."""
        # Point search is currently broken within PgSTAC
        # in order to return the correct result we need to make sure exitwhenfull and skipcovered options
        # are set to `False`
        # ref: https://github.com/stac-utils/pgstac/pull/52
        kwargs.update(**{"exitwhenfull": False, "skipcovered": False})

        if coord_crs != WGS84_CRS:
            xs, ys = transform(coord_crs, WGS84_CRS, [lng], [lat])
            lng, lat = xs[0], ys[0]

        return self.get_assets(Point(type="Point", coordinates=(lng, lat)), **kwargs)

    def assets_for_bbox(
        self,
        xmin: float,
        ymin: float,
        xmax: float,
        ymax: float,
        coord_crs: CRS = WGS84_CRS,
        **kwargs: Any,
    ) -> List[Dict]:
        """Retrieve assets for bbox."""
        if coord_crs != WGS84_CRS:
            xmin, ymin, xmax, ymax = transform_bounds(
                coord_crs,
                WGS84_CRS,
                xmin,
                ymin,
                xmax,
                ymax,
            )

        return self.get_assets(Polygon.from_bounds(xmin, ymin, xmax, ymax), **kwargs)

    @cached(  # type: ignore
        TTLCache(maxsize=cache_config.maxsize, ttl=cache_config.ttl),
        key=lambda self, geom, **kwargs: hashkey(self.input, str(geom), **kwargs),
    )
    @retry(
        tries=retry_config.retry,
        delay=retry_config.delay,
        exceptions=(
            pgErrors.OperationalError,
            pgErrors.InterfaceError,
        ),
    )
    def get_assets(
        self,
        geom: Geometry,
        fields: Optional[Dict[str, Any]] = None,
        scan_limit: Optional[int] = None,
        items_limit: Optional[int] = None,
        time_limit: Optional[int] = None,
        exitwhenfull: Optional[bool] = None,
        skipcovered: Optional[bool] = None,
    ) -> List[Dict]:
        """Find assets."""
        fields = fields or {
            "include": ["assets", "id", "bbox", "collection"],
        }

        scan_limit = scan_limit or 10000
        items_limit = items_limit or 100
        time_limit = time_limit or 5
        exitwhenfull = True if exitwhenfull is None else exitwhenfull
        skipcovered = True if skipcovered is None else skipcovered

        with self.pool.connection() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(
                        "SELECT * FROM geojsonsearch(%s, %s, %s, %s, %s, %s, %s, %s);",
                        (
                            geom.model_dump_json(exclude_none=True),
                            self.input,
                            json.dumps(fields),
                            scan_limit,
                            items_limit,
                            f"{time_limit} seconds",
                            exitwhenfull,
                            skipcovered,
                        ),
                    )
                    resp = cursor.fetchone()[0]

                except pgErrors.RaiseException as e:
                    # Catch Invalid SearchId and raise specific Error
                    if f"Search with Query Hash {self.input} Not Found" in str(e):
                        raise MosaicNotFoundError(
                            f"SearchId `{self.input}` not found"
                        ) from e
                    else:
                        raise e

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
            with self.reader(item, tms=self.tms, **self.reader_options) as src_dst:
                return src_dst.tile(x, y, z, **kwargs)

        return mosaic_reader(mosaic_assets, _reader, tile_x, tile_y, tile_z, **kwargs)

    def point(
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
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
            coord_crs=coord_crs,
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
            item: Dict[str, Any],
            lon: float,
            lat: float,
            coord_crs=coord_crs,
            **kwargs: Any,
        ) -> Dict:
            with self.reader(item, **self.reader_options) as src_dst:
                return src_dst.point(lon, lat, coord_crs=coord_crs, **kwargs)

        if "allowed_exceptions" not in kwargs:
            kwargs.update({"allowed_exceptions": (PointOutsideBounds,)})

        return list(multi_values(mosaic_assets, _reader, lon, lat, **kwargs).items())

    def part(
        self,
        bbox: BBox,
        dst_crs: Optional[CRS] = None,
        bounds_crs: CRS = WGS84_CRS,
        reverse: bool = False,
        scan_limit: Optional[int] = None,
        items_limit: Optional[int] = None,
        time_limit: Optional[int] = None,
        exitwhenfull: Optional[bool] = None,
        skipcovered: Optional[bool] = None,
        **kwargs: Any,
    ) -> Tuple[ImageData, List[str]]:
        """Create an Image from multiple items for a bbox."""
        xmin, ymin, xmax, ymax = bbox

        mosaic_assets = self.assets_for_bbox(
            xmin,
            ymin,
            xmax,
            ymax,
            coord_crs=bounds_crs,
            scan_limit=scan_limit,
            items_limit=items_limit,
            time_limit=time_limit,
            exitwhenfull=exitwhenfull,
            skipcovered=skipcovered,
        )

        if not mosaic_assets:
            raise NoAssetFoundError("No assets found for bbox input")

        if reverse:
            mosaic_assets = list(reversed(mosaic_assets))

        def _reader(item: Dict[str, Any], bbox: BBox, **kwargs: Any) -> ImageData:
            with self.reader(item, **self.reader_options) as src_dst:
                return src_dst.part(bbox, **kwargs)

        return mosaic_reader(
            mosaic_assets,
            _reader,
            bbox,
            bounds_crs=bounds_crs,
            dst_crs=dst_crs or bounds_crs,
            **kwargs,
        )

    def feature(
        self,
        shape: Dict,
        dst_crs: Optional[CRS] = None,
        shape_crs: CRS = WGS84_CRS,
        max_size: int = 1024,
        reverse: bool = False,
        scan_limit: Optional[int] = None,
        items_limit: Optional[int] = None,
        time_limit: Optional[int] = None,
        exitwhenfull: Optional[bool] = None,
        skipcovered: Optional[bool] = None,
        **kwargs: Any,
    ) -> Tuple[ImageData, List[str]]:
        """Create an Image from multiple items for a GeoJSON feature."""
        if "geometry" in shape:
            shape = shape["geometry"]

        # PgSTAC needs geometry in WGS84
        shape_wgs84 = shape
        if shape_crs != WGS84_CRS:
            shape_wgs84 = transform_geom(shape_crs, WGS84_CRS, shape)

        mosaic_assets = self.get_assets(
            parse_geometry_obj(shape_wgs84),
            scan_limit=scan_limit,
            items_limit=items_limit,
            time_limit=time_limit,
            exitwhenfull=exitwhenfull,
            skipcovered=skipcovered,
        )

        if not mosaic_assets:
            raise NoAssetFoundError("No assets found for Geometry")

        if reverse:
            mosaic_assets = list(reversed(mosaic_assets))

        def _reader(item: Dict[str, Any], shape: Dict, **kwargs: Any) -> ImageData:
            with self.reader(item, **self.reader_options) as src_dst:
                return src_dst.feature(shape, **kwargs)

        return mosaic_reader(
            mosaic_assets,
            _reader,
            shape,
            shape_crs=shape_crs,
            dst_crs=dst_crs or shape_crs,
            max_size=max_size,
            **kwargs,
        )
