"""Database connection handling."""

import functools
import os
from typing import Any, Dict, Optional, Union

import boto3
from fastapi import FastAPI
from psycopg_pool import ConnectionPool

from titiler.pgstac.settings import PostgresSettings


def get_rds_token(
    host: Union[str, None],
    port: Union[int, None],
    user: Union[str, None],
    region: Union[str, None],
) -> str:
    """Get RDS token for IAM auth"""
    print(
        f"Retrieving RDS IAM token with host: {host}, port: {port}, user: {user}, region: {region}"
    )
    rds_client = boto3.client("rds")
    token = rds_client.generate_db_auth_token(
        DBHostname=host,
        Port=port,
        DBUsername=user,
        Region=region or rds_client.meta.region_name,
    )
    return token


async def connect_to_db(
    app: FastAPI,
    settings: Optional[PostgresSettings] = None,
    pool_kwargs: Optional[Dict[str, Any]] = None,
) -> None:
    """Connect to Database."""
    if not settings:
        settings = PostgresSettings()

    pool_kwargs = (
        pool_kwargs
        if pool_kwargs is not None
        else {"options": "-c search_path=pgstac,public -c application_name=pgstac"}
    )

    if os.environ.get("IAM_AUTH_ENABLED") == "TRUE":
        pool_kwargs["password"] = functools.partial(
            get_rds_token,
            settings.postgres_host,
            settings.postgres_port,
            settings.postgres_user,
            settings.aws_region,
        )

    app.state.dbpool = ConnectionPool(
        conninfo=str(settings.database_url),
        min_size=settings.db_min_conn_size,
        max_size=settings.db_max_conn_size,
        max_waiting=settings.db_max_queries,
        max_idle=settings.db_max_idle,
        num_workers=settings.db_num_workers,
        kwargs=pool_kwargs,
        open=True,
    )

    # Make sure the pool is ready
    # ref: https://www.psycopg.org/psycopg3/docs/advanced/pool.html#pool-startup-check
    app.state.dbpool.wait()


async def close_db_connection(app: FastAPI) -> None:
    """Close Pool."""
    app.state.dbpool.close()
