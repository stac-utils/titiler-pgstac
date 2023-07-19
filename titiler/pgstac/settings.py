"""API settings."""

from functools import lru_cache
from typing import Any, Dict, Optional

from pydantic import (
    BaseSettings,
    PostgresDsn,
    confloat,
    conint,
    root_validator,
    validator,
)


class ApiSettings(BaseSettings):
    """API settings"""

    name: str = "titiler-pgstac"
    cors_origins: str = "*"
    cachecontrol: str = "public, max-age=3600"
    root_path: str = ""
    debug: bool = False

    @validator("cors_origins")
    def parse_cors_origin(cls, v):
        """Parse CORS origins."""
        return [origin.strip() for origin in v.split(",")]

    class Config:
        """model config"""

        env_prefix = "TITILER_PGSTAC_API_"
        env_file = ".env"


class PostgresSettings(BaseSettings):
    """Postgres-specific API settings.

    Attributes:
        postgres_user: postgres username.
        postgres_pass: postgres password.
        postgres_host: database hostname.
        postgres_port: database port.
        postgres_dbname: database name.
    """

    postgres_user: Optional[str]
    postgres_pass: Optional[str]
    postgres_host: Optional[str]
    postgres_port: Optional[str]
    postgres_dbname: Optional[str]

    database_url: Optional[PostgresDsn] = None

    # see https://www.psycopg.org/psycopg3/docs/api/pool.html#the-connectionpool-class for options
    db_min_conn_size: int = 1  # The minimum number of connection the pool will hold
    db_max_conn_size: int = 10  # The maximum number of connections the pool will hold
    db_max_queries: int = (
        50000  # Maximum number of requests that can be queued to the pool
    )
    db_max_idle: float = 300  # Maximum time, in seconds, that a connection can stay unused in the pool before being closed, and the pool shrunk.
    db_num_workers: int = (
        3  # Number of background worker threads used to maintain the pool state
    )

    class Config:
        """model config"""

        env_file = ".env"

    @validator("database_url", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        """Validate database config."""
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("postgres_user"),
            password=values.get("postgres_pass"),
            host=values.get("postgres_host", ""),
            port=values.get("postgres_port", 5432),
            path=f"/{values.get('postgres_dbname') or ''}",
        )


class CacheSettings(BaseSettings):
    """Cache settings"""

    # TTL of the cache in seconds
    ttl: int = 300

    # Maximum size of the LRU cache in MB
    maxsize: int = 512

    # Whether or not caching is enabled
    disable: bool = False

    class Config:
        """model config"""

        env_prefix = "TITILER_PGSTAC_CACHE_"
        env_file = ".env"

    @root_validator
    def check_enable(cls, values):
        """Check if cache is desabled."""
        if values.get("disable"):
            values["ttl"] = 0
            values["maxsize"] = 0
        return values


class _RetrySettings(BaseSettings):
    """Retry settings"""

    retry: conint(ge=0) = 3  # type: ignore[valid-type]
    delay: confloat(ge=0) = 0.0  # type: ignore[valid-type]

    class Config:
        """model config"""

        env_prefix = "TITILER_PGSTAC_API_"
        env_file = ".env"


@lru_cache()
def RetrySettings() -> _RetrySettings:
    """This function returns a cached instance of the RetrySettings object."""
    return _RetrySettings()
