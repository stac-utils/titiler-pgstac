"""Database connection handling."""

from psycopg_pool import ConnectionPool

from titiler.pgstac.settings import PostgresSettings

from fastapi import FastAPI

settings = PostgresSettings()


async def connect_to_db(app: FastAPI) -> None:
    """Connect to Database."""
    app.state.dbpool = ConnectionPool(
        conninfo=settings.connection_string,
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
