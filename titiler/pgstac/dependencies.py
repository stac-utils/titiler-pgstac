"""titiler-pgstac dependencies."""

import warnings
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

import morecantile
import pystac
from cachetools import TTLCache, cached
from cachetools.keys import hashkey
from cogeo_mosaic.errors import MosaicNotFoundError
from fastapi import HTTPException, Path, Query
from geojson_pydantic.types import BBox
from psycopg import errors as pgErrors
from psycopg.rows import class_row, dict_row
from psycopg_pool import ConnectionPool
from starlette.requests import Request
from typing_extensions import Annotated

from titiler.core.dependencies import DefaultDependency
from titiler.pgstac import model
from titiler.pgstac.errors import ReadOnlyPgSTACError
from titiler.pgstac.settings import CacheSettings, RetrySettings
from titiler.pgstac.utils import retry

cache_config = CacheSettings()
retry_config = RetrySettings()


def SearchIdParams(
    search_id: Annotated[
        str,
        Path(description="PgSTAC Search Identifier (Hash)"),
    ],
) -> str:
    """search_id"""
    return search_id


@cached(  # type: ignore
    TTLCache(maxsize=cache_config.maxsize, ttl=cache_config.ttl),
    key=lambda pool, collection_id, ids, bbox, datetime: hashkey(
        collection_id,
        str(ids),
        str(bbox),
        datetime,
    ),
)
@retry(
    tries=retry_config.retry,
    delay=retry_config.delay,
    exceptions=(
        pgErrors.OperationalError,
        pgErrors.InterfaceError,
    ),
)
def get_collection_id(
    pool: ConnectionPool,
    collection_id: str,
    ids: Optional[List[str]] = None,
    bbox: Optional[BBox] = None,
    datetime: Optional[str] = None,
) -> str:  # noqa: C901
    """Get Search Id for a Collection."""
    search = model.PgSTACSearch(
        collections=[collection_id],
        ids=ids,
        bbox=bbox,
        datetime=datetime,
    )

    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                "SELECT * FROM pgstac.get_collection(%s);",
                (collection_id,),
            )
            collection = cursor.fetchone()["get_collection"]
            if not collection:
                raise MosaicNotFoundError(f"CollectionId `{collection_id}` not found")

            collection_bbox = collection["extent"]["spatial"].get(
                "bbox", [[-180, -90, 180, 90]]
            )
            metadata = model.Metadata(
                name=f"Mosaic for '{collection_id}' Collection",
                bounds=bbox or collection_bbox[0],
            )

            # item-assets https://github.com/stac-extensions/item-assets
            if "item_assets" in collection:
                metadata.assets = list(collection["item_assets"])

            # render https://github.com/stac-extensions/render
            if "renders" in collection:
                renders = {}
                for name, render in collection["renders"].items():
                    try:
                        # `title` is not a parameter expected by titiler-pgstac
                        _ = render.pop("title", None)

                        # TODO: add support for tilematrixset
                        _ = render.pop("tilematrixsets", None)

                        # `minmax_zoom` is not a parameter expected by titiler-pgstac
                        zooms = render.pop("minmax_zoom", None)
                        if zooms and len(zooms) == 2:
                            render["minzoom"] = zooms[0]
                            render["maxzoom"] = zooms[1]

                        renders[name] = render

                    except Exception as e:
                        warnings.warn(
                            f"Invalid render `{name}`: {repr(e)}",
                            UserWarning,
                            stacklevel=2,
                        )
                        continue

                metadata.defaults = renders

            # TODO: adapt Mosaic Backend to accept Search object directly
            # we technically don't need to register the search request for /collections
            try:
                cursor.execute("SELECT pgstac.readonly()")
                if cursor.fetchone()["readonly"]:
                    raise ReadOnlyPgSTACError(
                        "PgSTAC instance is set to `read-only`, cannot register search query."
                    )

            # before pgstac 0.8.2, the read-only mode didn't exist
            except pgErrors.UndefinedFunction:
                conn.rollback()
                pass

            cursor.row_factory = class_row(model.Search)
            cursor.execute(
                "SELECT * FROM search_query(%s, _metadata => %s);",
                (
                    search.model_dump_json(by_alias=True, exclude_none=True),
                    metadata.model_dump_json(exclude_none=True),
                ),
            )
            search_info: model.Search = cursor.fetchone()

    return search_info.id


def CollectionIdParams(
    request: Request,
    collection_id: Annotated[
        str,
        Path(description="STAC Collection Identifier"),
    ],
    ids: Annotated[
        Optional[str],
        Query(
            description="Array of Item ids",
            json_schema_extra={
                "example": "item1,item2",
            },
        ),
    ] = None,
    bbox: Annotated[
        Optional[str],
        Query(
            description="Filters items intersecting this bounding box",
            json_schema_extra={
                "example": "-175.05,-85.05,175.05,85.05",
            },
        ),
    ] = None,
    datetime: Annotated[
        Optional[str],
        Query(
            description="""Filters items that have a temporal property that intersects this value.\n
Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.""",
            openapi_examples={
                "datetime": {"value": "2018-02-12T23:20:50Z"},
                "closed-interval": {
                    "value": "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
                },
                "open-interval-from": {"value": "2018-02-12T00:00:00Z/.."},
                "open-interval-to": {"value": "../2018-03-18T12:31:12Z"},
            },
        ),
    ] = None,
) -> str:
    """Collection endpoints Parameters"""
    return get_collection_id(
        request.app.state.dbpool,
        collection_id=collection_id,
        ids=ids.split(",") if ids else None,
        bbox=list(map(float, bbox.split(","))) if bbox else None,
        datetime=datetime,
    )


def SearchParams(
    body: model.RegisterMosaic,
) -> Tuple[model.PgSTACSearch, model.Metadata]:
    """Search parameters."""
    search = body.model_dump(
        exclude_none=True,
        exclude={"metadata"},
        by_alias=True,
    )
    return model.PgSTACSearch(**search), body.metadata


@dataclass(init=False)
class BackendParams(DefaultDependency):
    """backend parameters."""

    pool: ConnectionPool = field(init=False)

    def __init__(self, request: Request):
        """Initialize BackendParams

        Note: Because we don't want `pool` to appear in the documentation we use a dataclass with a custom `__init__` method.
        FastAPI will use the `__init__` method but will exclude Request in the documentation making `pool` an invisible dependency.
        """
        self.pool = request.app.state.dbpool


@dataclass
class PgSTACParams(DefaultDependency):
    """PgSTAC parameters."""

    scan_limit: Annotated[
        Optional[int],
        Query(
            description="Return as soon as we scan N items (defaults to 10000 in PgSTAC).",
        ),
    ] = None
    items_limit: Annotated[
        Optional[int],
        Query(
            description="Return as soon as we have N items per geometry (defaults to 100 in PgSTAC).",
        ),
    ] = None
    time_limit: Annotated[
        Optional[int],
        Query(
            description="Return after N seconds to avoid long requests (defaults to 5 in PgSTAC).",
        ),
    ] = None
    exitwhenfull: Annotated[
        Optional[bool],
        Query(
            description="Return as soon as the geometry is fully covered (defaults to True in PgSTAC).",
        ),
    ] = None
    skipcovered: Annotated[
        Optional[bool],
        Query(
            description="Skip any items that would show up completely under the previous items (defaults to True in PgSTAC).",
        ),
    ] = None


@cached(  # type: ignore
    TTLCache(maxsize=cache_config.maxsize, ttl=cache_config.ttl),
    key=lambda pool, collection, item: hashkey(collection, item),
)
@retry(
    tries=retry_config.retry,
    delay=retry_config.delay,
    exceptions=(
        pgErrors.OperationalError,
        pgErrors.InterfaceError,
    ),
)
def get_stac_item(pool: ConnectionPool, collection: str, item: str) -> pystac.Item:
    """Get STAC Item from PGStac."""
    search = model.PgSTACSearch(ids=[item], collections=[collection])
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                ("SELECT * FROM pgstac.search(%s) LIMIT 1;"),
                (search.model_dump_json(by_alias=True, exclude_none=True),),
            )

            resp = cursor.fetchone()["search"]
            if not resp or "features" not in resp or len(resp["features"]) != 1:
                raise HTTPException(
                    status_code=404,
                    detail=f"No item '{item}' found in '{collection}' collection",
                )

            return pystac.Item.from_dict(resp["features"][0])


def ItemIdParams(
    request: Request,
    collection_id: Annotated[
        str,
        Path(description="STAC Collection Identifier"),
    ],
    item_id: Annotated[str, Path(description="STAC Item Identifier")],
) -> pystac.Item:
    """STAC Item dependency."""
    return get_stac_item(request.app.state.dbpool, collection_id, item_id)


def AssetIdParams(
    request: Request,
    collection_id: Annotated[
        str,
        Path(description="STAC Collection Identifier"),
    ],
    item_id: Annotated[str, Path(description="STAC Item Identifier")],
    asset_id: Annotated[str, Path(description="STAC Asset Identifier")],
) -> str:
    """STAC Asset dependency."""
    item = get_stac_item(request.app.state.dbpool, collection_id, item_id)
    asset_info = item.assets[asset_id]
    return asset_info.get_absolute_href() or asset_info.href


def TmsTileParams(
    z: Annotated[
        int,
        Path(
            description="Identifier (Z) selecting one of the scales defined in the TileMatrixSet and representing the scaleDenominator the tile.",
        ),
    ],
    x: Annotated[
        int,
        Path(
            description="Column (X) index of the tile on the selected TileMatrix. It cannot exceed the MatrixHeight-1 for the selected TileMatrix.",
        ),
    ],
    y: Annotated[
        int,
        Path(
            description="Row (Y) index of the tile on the selected TileMatrix. It cannot exceed the MatrixWidth-1 for the selected TileMatrix.",
        ),
    ],
) -> morecantile.Tile:
    """TileMatrixSet Tile parameters."""
    return morecantile.Tile(x, y, z)
