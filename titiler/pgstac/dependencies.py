"""titiler-pgstac dependencies."""

from dataclasses import dataclass, field
from typing import Optional, Tuple

import morecantile
import pystac
from cachetools import TTLCache, cached
from cachetools.keys import hashkey
from cogeo_mosaic.errors import MosaicNotFoundError
from fastapi import HTTPException, Path, Query
from psycopg import errors as pgErrors
from psycopg.rows import class_row, dict_row
from psycopg_pool import ConnectionPool
from starlette.requests import Request
from typing_extensions import Annotated

from titiler.core.dependencies import DefaultDependency
from titiler.pgstac import model
from titiler.pgstac.settings import CacheSettings, RetrySettings
from titiler.pgstac.utils import retry

cache_config = CacheSettings()
retry_config = RetrySettings()


def SearchIdParams(
    search_id: Annotated[
        str,
        Path(description="PgSTAC Search Identifier (Hash)"),
    ]
) -> str:
    """search_id"""
    return search_id


@cached(  # type: ignore
    TTLCache(maxsize=cache_config.maxsize, ttl=cache_config.ttl),
    key=lambda pool, collection_id: hashkey(collection_id),
)
@retry(
    tries=retry_config.retry,
    delay=retry_config.delay,
    exceptions=(
        pgErrors.OperationalError,
        pgErrors.InterfaceError,
    ),
)
def get_collection_id(pool: ConnectionPool, collection_id: str) -> str:
    """Get Search Id for a Collection."""
    search = model.PgSTACSearch(collections=[collection_id])

    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                "SELECT * FROM pgstac.get_collection(%s);",
                (collection_id,),
            )
            collection = cursor.fetchone()["get_collection"]
            if not collection:
                raise MosaicNotFoundError(f"CollectionId `{collection_id}` not found")

            bbox = collection["extent"]["spatial"].get("bbox", [[-180, -90, 180, 90]])
            metadata = model.Metadata(
                name=f"Mosaic for '{collection_id}' Collection",
                bounds=bbox[0],
                # TODO: use asset extension to populate the `assets` attribute
            )

            cursor.row_factory = class_row(model.Search)
            cursor.execute(
                "SELECT * FROM search_query(%s, _metadata => %s);",
                (
                    search.model_dump_json(by_alias=True, exclude_none=True),
                    metadata.model_dump_json(exclude_none=True),
                ),
            )
            search_info = cursor.fetchone()

    return search_info.id


def CollectionIdParams(
    request: Request,
    collection_id: Annotated[
        str,
        Path(description="STAC Collection Identifier"),
    ],
) -> str:
    """collection_id Path Parameter"""
    return get_collection_id(request.app.state.dbpool, collection_id=collection_id)


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
