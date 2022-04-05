"""titiler-pgstac dependencies."""

from dataclasses import dataclass
from typing import Dict, Optional, Tuple

import pystac
from cachetools import TTLCache, cached
from cachetools.keys import hashkey
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool

from titiler.core.dependencies import DefaultDependency
from titiler.pgstac import model
from titiler.pgstac.settings import CacheSettings

from fastapi import HTTPException, Path, Query

from starlette.requests import Request

cache_config = CacheSettings()


def PathParams(searchid: str = Path(..., description="Search Id")) -> str:
    """SearcId"""
    return searchid


def SearchParams(
    body: model.RegisterMosaic,
) -> Tuple[model.PgSTACSearch, model.Metadata]:
    """Search parameters."""
    search = body.dict(
        exclude_none=True,
        exclude={"metadata"},
        by_alias=True,
    )
    return model.PgSTACSearch(**search), body.metadata


@dataclass
class PgSTACParams(DefaultDependency):
    """PgSTAC parameters."""

    scan_limit: Optional[int] = Query(
        None,
        description="Return as soon as we scan N items (defaults to 10000 in PgSTAC).",
    )
    items_limit: Optional[int] = Query(
        None,
        description="Return as soon as we have N items per geometry (defaults to 100 in PgSTAC).",
    )
    time_limit: Optional[int] = Query(
        None,
        description="Return after N seconds to avoid long requests (defaults to 5 in PgSTAC).",
    )
    exitwhenfull: Optional[bool] = Query(
        None,
        description="Return as soon as the geometry is fully covered (defaults to True in PgSTAC).",
    )
    skipcovered: Optional[bool] = Query(
        None,
        description="Skip any items that would show up completely under the previous items (defaults to True in PgSTAC).",
    )


@cached(
    TTLCache(maxsize=cache_config.maxsize, ttl=cache_config.ttl),
    key=lambda pool, collection, item: hashkey(collection, item),
)
def get_stac_item(pool: ConnectionPool, collection: str, item: str) -> Dict:
    """Get STAC Item from PGStac."""
    search = model.PgSTACSearch(ids=[item], collections=[collection])
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                ("SELECT * FROM pgstac.search(%s) LIMIT 1;"),
                (search.json(by_alias=True, exclude_none=True),),
            )

            resp = cursor.fetchone()["search"]
            if not resp or "features" not in resp or len(resp["features"]) != 1:
                raise HTTPException(
                    status_code=404,
                    detail=f"No item '{item}' found in '{collection}' collection",
                )

            return pystac.Item.from_dict(resp["features"][0])


def ItemPathParams(
    request: Request,
    collection: str = Query(..., description="STAC Collection ID"),
    item: str = Query(..., description="STAC Item ID"),
) -> Dict:
    """STAC Item dependency."""
    return get_stac_item(request.app.state.dbpool, collection, item)
