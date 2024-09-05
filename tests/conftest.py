"""``pytest`` configuration."""

import os
import warnings
from typing import Any, Dict
from urllib.parse import quote_plus as quote

import psycopg
import pytest
import rasterio
from pypgstac.db import PgstacDB
from pypgstac.load import Loader
from pypgstac.migrate import Migrate
from pytest_postgresql.janitor import DatabaseJanitor
from rasterio.errors import NotGeoreferencedWarning
from rasterio.io import MemoryFile
from starlette.testclient import TestClient

DATA_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
collection = os.path.join(DATA_DIR, "noaa-emergency-response.json")
collection_maxar = os.path.join(DATA_DIR, "maxar_BayOfBengal.json")
items = os.path.join(DATA_DIR, "noaa-eri-nashville2020.json")


def parse_img(content: bytes) -> Dict[Any, Any]:
    """Read tile image and return metadata."""
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            category=NotGeoreferencedWarning,
            module="rasterio",
        )
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
def database(postgresql_proc):
    """Create Database fixture."""
    with DatabaseJanitor(
        user=postgresql_proc.user,
        host=postgresql_proc.host,
        port=postgresql_proc.port,
        dbname="pgstacrw",
        version=postgresql_proc.version,
        password="a2Vw:yk=)CdSis[fek]tW=/o",
    ) as jan:
        connection = f"postgresql://{jan.user}:{quote(jan.password)}@{jan.host}:{jan.port}/{jan.dbname}"
        # make sure the DB is set to use UTC
        with psycopg.connect(connection) as conn:
            with conn.cursor() as cur:
                cur.execute(f"ALTER DATABASE {jan.dbname} SET TIMEZONE='UTC';")

        yield jan


@pytest.fixture(scope="session")
def pgstac(database):
    """Create PgSTAC fixture."""
    connection = f"postgresql://{database.user}:{quote(database.password)}@{database.host}:{database.port}/{database.dbname}"

    # Clear PgSTAC
    with psycopg.connect(connection) as conn:
        with conn.cursor() as cur:
            cur.execute("DROP SCHEMA IF EXISTS pgstac CASCADE;")

    print("Running to PgSTAC migration...")
    with PgstacDB(dsn=connection) as db:
        migrator = Migrate(db)
        version = migrator.run_migration()
        assert version
        print(f"PgSTAC version: {version}")

        print("Load items and collection into PgSTAC")
        loader = Loader(db=db)
        loader.load_collections(collection)
        loader.load_collections(collection_maxar)
        loader.load_items(items)

    # Make sure we have 1 collection and 163 items in pgstac
    with psycopg.connect(connection) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM pgstac.collections")
            val = cur.fetchone()[0]
            assert val == 2

            cur.execute("SELECT COUNT(*) FROM pgstac.items")
            val = cur.fetchone()[0]
            assert val == 163

    yield connection


@pytest.fixture(autouse=True)
def app(pgstac, monkeypatch):
    """Create app with connection to the pytest database."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-west-2")
    monkeypatch.setenv("AWS_REGION", "us-west-2")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("TITILER_PGSTAC_CACHE_DISABLE", "TRUE")
    monkeypatch.setenv("TITILER_PGSTAC_API_DEBUG", "TRUE")
    monkeypatch.setenv("TITILER_PGSTAC_API_ENABLE_ASSETS_ENDPOINTS", "TRUE")
    monkeypatch.setenv("TITILER_PGSTAC_API_ENABLE_EXTERNAL_DATASET_ENDPOINTS", "TRUE")
    monkeypatch.setenv("DATABASE_URL", pgstac)

    from titiler.pgstac.main import app

    with TestClient(app) as app:
        yield app
