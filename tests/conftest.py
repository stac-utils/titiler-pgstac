"""``pytest`` configuration."""

import asyncio
import os
from typing import Any, Dict

import asyncpg
import pytest
import rasterio
from pypgstac import pypgstac
from rasterio.io import MemoryFile

from starlette.testclient import TestClient

DATA_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
collection = os.path.join(DATA_DIR, "noaa-emergency-response.json")
items = os.path.join(DATA_DIR, "noaa-eri-nashville2020.json")


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
def event_loop():
    """event loop for fixtures."""
    return asyncio.get_event_loop()


@pytest.fixture(scope="session")
async def app():
    """Setup DB."""
    print("Setting up test db")

    with pytest.MonkeyPatch.context() as mp:
        mp.setenv("AWS_ACCESS_KEY_ID", "jqt")
        mp.setenv("AWS_SECRET_ACCESS_KEY", "rde")
        mp.setenv("AWS_DEFAULT_REGION", "us-west-2")
        mp.setenv("AWS_REGION", "us-west-2")
        mp.delenv("AWS_PROFILE", raising=False)
        mp.setenv("POSTGRES_DBNAME", "pgstactestdb")
        mp.setenv("TITILER_PGSTAC_CACHE_DISABLE", "TRUE")
        mp.setenv("TITILER_PGSTAC_API_DEBUG", "TRUE")

        from titiler.pgstac.db import close_db_connection, connect_to_db
        from titiler.pgstac.main import app
        from titiler.pgstac.settings import PostgresSettings

        settings = PostgresSettings()
        assert settings.postgres_dbname == "pgstactestdb"

        defaut_dsn = settings.connection_string.replace("/pgstactestdb", "/postgres")
        print(f"Connecting to database {defaut_dsn}")
        conn = await asyncpg.connect(dsn=defaut_dsn)

        print("creating tmp database...")
        try:
            await conn.execute("CREATE DATABASE pgstactestdb;")
            await conn.execute(
                "ALTER DATABASE pgstactestdb SET search_path to pgstac, public;"
            )
        except asyncpg.exceptions.DuplicateDatabaseError:
            print("pgstactestdb already exists, cleaning it...")
            await conn.execute("DROP DATABASE pgstactestdb;")
            await conn.execute("CREATE DATABASE pgstactestdb;")
            await conn.execute(
                "ALTER DATABASE pgstactestdb SET search_path to pgstac, public;"
            )
        finally:
            await conn.close()

        try:
            print("migrating...")
            os.environ["postgres_dbname"] = "pgstactestdb"
            conn = await asyncpg.connect(dsn=settings.connection_string)
            val = await conn.fetchval("SELECT true")
            assert val
            await conn.close()

            version = await pypgstac.run_migration(dsn=settings.connection_string)
            print(f"PGStac Migrated to {version}")

            print("Registering collection and items")
            conn = await asyncpg.connect(dsn=settings.connection_string)
            await conn.copy_to_table(
                "collections",
                source=collection,
                columns=["content"],
                format="csv",
                quote=chr(27),
                delimiter=chr(31),
            )
            # Make sure we have our collection
            val = await conn.fetchval("SELECT COUNT(*) FROM collections")
            print(f"registered {val} collection")
            assert val == 1

            await conn.copy_to_table(
                "items_staging",
                source=items,
                columns=["content"],
                format="csv",
                quote=chr(27),
                delimiter=chr(31),
            )
            # Make sure we have all our items
            val = await conn.fetchval("SELECT COUNT(*) FROM items")
            print(f"registered {val} items")
            assert val == 163

            await conn.close()

            await connect_to_db(app)
            yield TestClient(app)
            await close_db_connection(app)

        finally:
            print()
            print("Getting rid of test database")
            conn = await asyncpg.connect(dsn=defaut_dsn)
            await conn.execute("DROP DATABASE pgstactestdb;")
            await conn.close()
