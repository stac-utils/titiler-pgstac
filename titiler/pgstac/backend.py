"""TiTiler.PgSTAC custom Mosaic Backend and Custom STACReader."""

import json
import logging
from threading import Lock
from typing import Any

import attr
from cachetools import TTLCache, cached
from cachetools.keys import hashkey
from geojson_pydantic import Point, Polygon
from geojson_pydantic.geometries import Geometry
from morecantile import Tile, TileMatrixSet
from psycopg import errors as pgErrors
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from rasterio.crs import CRS
from rasterio.warp import transform, transform_bounds
from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.mosaic.backend import BaseBackend
from rio_tiler.types import BBox

from titiler.pgstac.errors import MosaicNotFoundError
from titiler.pgstac.model import Search
from titiler.pgstac.reader import SimpleSTACReader
from titiler.pgstac.settings import CacheSettings, PgstacSettings, RetrySettings
from titiler.pgstac.utils import retry


def _first_value(values: list[Any], default: Any = None):
    """Return the first not None value."""
    return next(filter(lambda x: x is not None, values), default)


cache_config = CacheSettings()
pgstac_config = PgstacSettings()
retry_config = RetrySettings()
ttl_cache = TTLCache(maxsize=cache_config.maxsize, ttl=cache_config.ttl)  # type: ignore

logger = logging.getLogger(__name__)


@attr.s
class PGSTACBackend(BaseBackend):
    """PgSTAC Mosaic Backend."""

    # Mosaic ID (hash)
    input: str = attr.ib()

    # Connection POOL to the database
    pool: ConnectionPool = attr.ib()

    # Because we are not using mosaicjson we are not limited to the WebMercator TMS
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    # Use Custom STAC reader (outside init)
    reader: type[SimpleSTACReader] = attr.ib(default=SimpleSTACReader)
    reader_options: dict = attr.ib(factory=dict)

    # default values for bounds
    crs: CRS = attr.ib(default=WGS84_CRS)

    _backend_name = "PgSTAC"

    @property
    def minzoom(self) -> int:  # type: ignore [override]
        """Return minzoom."""
        info = self.info()
        return (
            info.metadata.minzoom
            if info.metadata.minzoom is not None
            else self.tms.minzoom
        )

    @property
    def maxzoom(self) -> int:  # type: ignore [override]
        """Return maxzoom."""
        info = self.info()
        return (
            info.metadata.maxzoom
            if info.metadata.maxzoom is not None
            else self.tms.maxzoom
        )

    @property
    def bounds(self) -> BBox:  # type: ignore [override]
        """Return mosaic BBox."""
        info = self.info()
        return _first_value(
            [info.input_search.get("bbox"), info.metadata.bounds],
            self.tms.bbox,
        )

    # in PgSTAC backend assets are STAC Items as dict
    def asset_name(self, asset: dict) -> str:
        """Get asset name."""
        return f"{asset['collection']}/{asset['id']}"

    def assets_for_tile(self, x: int, y: int, z: int, **kwargs: Any) -> list[dict]:
        """Retrieve assets for tile."""
        bbox = self.tms.bounds(Tile(x, y, z))
        return self.get_assets(Polygon.from_bounds(*bbox), **kwargs)

    def assets_for_point(
        self,
        lng: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        **kwargs: Any,
    ) -> list[dict]:
        """Retrieve assets for point."""
        # Point search is currently broken within PgSTAC
        # in order to return the correct result we need to make sure exitwhenfull and skipcovered options
        # are set to `False`
        # ref: https://github.com/stac-utils/pgstac/pull/52
        kwargs.update(**{"exitwhenfull": False, "skipcovered": False})

        if coord_crs != WGS84_CRS:
            xs, ys = transform(coord_crs, WGS84_CRS, [lng], [lat])
            lng, lat = xs[0], ys[0]

        return self.get_assets(
            Point(
                type="Point",
                coordinates=(lng, lat),  # type: ignore
            ),
            **kwargs,
        )

    def assets_for_bbox(
        self,
        xmin: float,
        ymin: float,
        xmax: float,
        ymax: float,
        coord_crs: CRS = WGS84_CRS,
        **kwargs: Any,
    ) -> list[dict]:
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
        ttl_cache,
        key=lambda self, geom, **kwargs: hashkey(self.input, str(geom), **kwargs),
        lock=Lock(),
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
        fields: dict[str, Any] | None = None,
        scan_limit: int | None = None,
        items_limit: int | None = None,
        time_limit: int | None = None,
        exitwhenfull: bool | None = None,
        skipcovered: bool | None = None,
    ) -> list[dict]:
        """Find assets."""
        fields = fields or {
            "include": ["assets", "id", "bbox", "collection"],
        }

        scan_limit = scan_limit or pgstac_config.scan_limit
        items_limit = items_limit or pgstac_config.items_limit
        time_limit = time_limit or pgstac_config.time_limit
        exitwhenfull = (
            pgstac_config.exitwhenfull if exitwhenfull is None else exitwhenfull
        )
        skipcovered = pgstac_config.skipcovered if skipcovered is None else skipcovered

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
                    resp = cursor.fetchone()[0]  # type: ignore

                except (pgErrors.RaiseException, pgErrors.NotNullViolation) as e:
                    # Catch Invalid SearchId and raise specific Error
                    if f"Search with Query Hash {self.input} Not Found" in str(
                        e
                    ) or 'null value in column "search" of relation "searches"' in str(
                        e
                    ):
                        raise MosaicNotFoundError(
                            f"SearchId `{self.input}` not found"
                        ) from e
                    else:
                        raise e

        features = resp.get("features", [])

        logger.info(f"found {len(features)} assets")
        return features

    @cached(  # type: ignore
        ttl_cache,
        key=lambda self: hashkey(self.input, "info"),
        lock=Lock(),
    )
    def info(self) -> Search:  # type: ignore
        """Custom pgSTAC Mosaic info."""
        with self.pool.connection() as conn:
            with conn.cursor(row_factory=class_row(Search)) as cursor:
                cursor.execute(
                    "SELECT * FROM searches WHERE hash=%s;",
                    (self.input,),
                )
                search_info = cursor.fetchone()

        if not search_info:
            raise MosaicNotFoundError(f"SearchId `{self.input}` not found")

        return search_info
