"""``pytest`` configuration."""

import os
from typing import Any, Dict

import psycopg
import pytest
import pytest_pgsql
import rasterio
from pypgstac.db import PgstacDB
from pypgstac.load import Loader
from pypgstac.migrate import Migrate
from rasterio.io import MemoryFile

from starlette.testclient import TestClient

DATA_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
collection = os.path.join(DATA_DIR, "noaa-emergency-response.json")
items = os.path.join(DATA_DIR, "noaa-eri-nashville2020.json")

test_db = pytest_pgsql.TransactedPostgreSQLTestDB.create_fixture(
    "test_db", scope="session", use_restore_state=False
)


def parse_img(content: bytes) -> Dict[Any, Any]:
    """Read tile image and return metadata."""
    with MemoryFile(content) as mem:
        with mem.open() as dst:
            return dst.profile


def mock_rasterio_open(asset):
    """Mock rasterio Open."""
    assert asset.startswith(
        "https://noaa-eri-pds.s3.us-east-1.amazonaws.com/2020_Nashville_Tornado/20200307a_RGB/"
    )
    asset = asset.replace(
        "https://noaa-eri-pds.s3.us-east-1.amazonaws.com/2020_Nashville_Tornado/20200307a_RGB",
        DATA_DIR,
    )
    return rasterio.open(asset)


@pytest.fixture(scope="session")
def database_url(test_db):
    """
    Session scoped fixture to launch a postgresql database in a separate process.  We use psycopg2 to ingest test data
    because pytest-asyncio event loop is a function scoped fixture and cannot be called within the current scope.  Yields
    a database url which we pass to our application through a monkeypatched environment variable.
    """
    with PgstacDB(dsn=str(test_db.connection.engine.url)) as db:
        print("Running to PgSTAC migration...")
        migrator = Migrate(db)
        version = migrator.run_migration()
        assert version
        assert test_db.has_schema("pgstac")
        print(f"PgSTAC version: {version}")

        print("Load items and collection into PgSTAC")
        loader = Loader(db=db)
        loader.load_collections(collection)
        loader.load_items(items)

    # Make sure we have 1 collection and 163 items in pgstac
    with psycopg.connect(str(test_db.connection.engine.url)) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM pgstac.collections")
            val = cur.fetchone()[0]
            assert val == 1

            cur.execute("SELECT COUNT(*) FROM pgstac.items")
            val = cur.fetchone()[0]
            assert val == 163

    return test_db.connection.engine.url


@pytest.fixture(autouse=True)
def app(database_url, monkeypatch):
    """Create app with connection to the pytest database."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-west-2")
    monkeypatch.setenv("AWS_REGION", "us-west-2")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("TITILER_PGSTAC_CACHE_DISABLE", "TRUE")
    monkeypatch.setenv("TITILER_PGSTAC_API_DEBUG", "TRUE")

    monkeypatch.setenv("DATABASE_URL", str(database_url))

    from titiler.pgstac.main import app

    # Remove middlewares https://github.com/encode/starlette/issues/472
    app.user_middleware = []
    app.middleware_stack = app.build_middleware_stack()

    with TestClient(app) as app:
        yield app
