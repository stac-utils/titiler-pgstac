"""API settings."""

from functools import lru_cache

import pydantic


class _ApiSettings(pydantic.BaseSettings):
    """API settings"""

    name: str = "titiler-pgstac"
    cors_origins: str = "*"
    cachecontrol: str = "public, max-age=3600"
    debug: bool = False

    @pydantic.validator("cors_origins")
    def parse_cors_origin(cls, v):
        """Parse CORS origins."""
        return [origin.strip() for origin in v.split(",")]

    class Config:
        """model config"""

        env_prefix = "TITILER_PGSTAC_API_"
        env_file = ".env"


@lru_cache()
def ApiSettings() -> _ApiSettings:
    """
    This function returns a cached instance of the APISettings object.
    Caching is used to prevent re-reading the environment every time the API settings are used in an endpoint.
    If you want to change an environment variable and reset the cache (e.g., during testing), this can be done
    using the `lru_cache` instance method `ApiSettings.cache_clear()`.

    From https://github.com/dmontagu/fastapi-utils/blob/af95ff4a8195caaa9edaa3dbd5b6eeb09691d9c7/fastapi_utils/api_settings.py#L60-L69
    """
    return _ApiSettings()


class _PostgresSettings(pydantic.BaseSettings):
    """Postgres-specific API settings.

    Attributes:
        postgres_user: postgres username.
        postgres_pass: postgres password.
        postgres_host: database hostname.
        postgres_port: database port.
        postgres_dbname: database name.
    """

    postgres_user: str
    postgres_pass: str
    postgres_host: str
    postgres_port: str
    postgres_dbname: str

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

    @property
    def connection_string(self):
        """Create reader psql connection string."""
        return f"postgresql://{self.postgres_user}:{self.postgres_pass}@{self.postgres_host}:{self.postgres_port}/{self.postgres_dbname}"


@lru_cache()
def PostgresSettings() -> _PostgresSettings:
    """Postgres Settings."""
    return _PostgresSettings()


class _CacheSettings(pydantic.BaseSettings):
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

    @pydantic.root_validator
    def check_enable(cls, values):
        """Check if cache is desabled."""
        if values.get("disable"):
            values["ttl"] = 0
            values["maxsize"] = 0
        return values


@lru_cache()
def CacheSettings() -> _CacheSettings:
    """Cache settings."""
    return _CacheSettings()
