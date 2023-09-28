"""API settings."""

from functools import lru_cache
from typing import Any, Optional

from pydantic import (
    Field,
    PostgresDsn,
    ValidationInfo,
    field_validator,
    model_validator,
)
from pydantic_settings import BaseSettings
from typing_extensions import Annotated


class ApiSettings(BaseSettings):
    """API settings"""

    name: str = "titiler-pgstac"
    cors_origins: str = "*"
    cachecontrol: str = "public, max-age=3600"
    root_path: str = ""
    debug: bool = False

    model_config = {
        "env_prefix": "TITILER_PGSTAC_API_",
        "env_file": ".env",
        "extra": "ignore",
    }

    @field_validator("cors_origins")
    def parse_cors_origin(cls, v):
        """Parse CORS origins."""
        return [origin.strip() for origin in v.split(",")]


class PostgresSettings(BaseSettings):
    """Postgres-specific API settings.

    Attributes:
        postgres_user: postgres username.
        postgres_pass: postgres password.
        postgres_host: database hostname.
        postgres_port: database port.
        postgres_dbname: database name.
    """

    postgres_user: Optional[str] = None
    postgres_pass: Optional[str] = None
    postgres_host: Optional[str] = None
    postgres_port: Optional[int] = None
    postgres_dbname: Optional[str] = None

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

    model_config = {"env_file": ".env", "extra": "ignore"}

    @field_validator("database_url", mode="before")
    def assemble_db_connection(cls, v: Optional[str], info: ValidationInfo) -> Any:
        """Validate database config."""
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql",
            username=info.data.get("postgres_user"),
            password=info.data.get("postgres_pass"),
            host=info.data.get("postgres_host", ""),
            port=info.data.get("postgres_port", 5432),
            path=info.data.get("postgres_dbname", ""),
        )


class CacheSettings(BaseSettings):
    """Cache settings"""

    # TTL of the cache in seconds
    ttl: int = 300

    # Maximum size of the LRU cache in MB
    maxsize: int = 512

    # Whether or not caching is enabled
    disable: bool = False

    model_config = {"env_prefix": "TITILER_PGSTAC_CACHE_", "env_file": ".env"}

    @model_validator(mode="after")
    def check_enable(self):
        """Check if cache is disabled."""
        if self.disable:
            self.ttl = 0
            self.maxsize = 0

        return self


class _RetrySettings(BaseSettings):
    """Retry settings"""

    retry: Annotated[int, Field(ge=0)] = 3
    delay: Annotated[float, Field(ge=0.0)] = 0.0

    model_config = {
        "env_prefix": "TITILER_PGSTAC_API_",
        "env_file": ".env",
        "extra": "ignore",
    }


@lru_cache()
def RetrySettings() -> _RetrySettings:
    """This function returns a cached instance of the RetrySettings object."""
    return _RetrySettings()
