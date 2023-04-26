"""Database connection handling."""

import time
from contextlib import contextmanager
from typing import Any, Generator, List, Optional, Type, Union

import psycopg
from fastapi import FastAPI
from psycopg_pool import ConnectionPool

from titiler.pgstac.logger import logger
from titiler.pgstac.settings import PostgresSettings


async def connect_to_db(
    app: FastAPI, settings: Optional[PostgresSettings] = None
) -> None:
    """Connect to Database."""
    if not settings:
        settings = PostgresSettings()

    app.state.dbpool = ConnectionPool(
        conninfo=settings.database_url,
        min_size=settings.db_min_conn_size,
        max_size=settings.db_max_conn_size,
        max_waiting=settings.db_max_queries,
        max_idle=settings.db_max_idle,
        num_workers=settings.db_num_workers,
        kwargs={"options": "-c search_path=pgstac,public -c application_name=pgstac"},
    )


async def close_db_connection(app: FastAPI) -> None:
    """Close Pool."""
    app.state.dbpool.close()


def retry(
    tries: int,
    exceptions: Union[Type[Exception], List[Type[Exception]]] = Exception,
    delay: int = 0,
):
    """Retry Decorator"""

    def _decorator(func: Any):
        def _newfn(*args: Any, **kwargs: Any):

            attempt = 0
            while attempt < tries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:  # type: ignore
                    logger.debug(repr(e))
                    logger.warning(f"Retrying `{func}` | Attempt {attempt}")

                    attempt += 1
                    time.sleep(delay)

            return func(*args, **kwargs)

        return _newfn

    return _decorator


@retry(tries=3, exceptions=psycopg.OperationalError)
@contextmanager
def execute_query(
    pool: ConnectionPool,
    *,
    query: psycopg.abc.Query,
    params: Optional[psycopg.abc.Params] = None,
    row_factory: Optional[psycopg.rows.RowFactory[psycopg.rows.Row]] = None,
) -> Generator[psycopg.Cursor, None, None]:
    """Get Connection and Execute Query."""
    with pool.connection() as conn:
        with conn.cursor(row_factory=row_factory) as cursor:
            cursor.execute(query, params=params)
            yield cursor
