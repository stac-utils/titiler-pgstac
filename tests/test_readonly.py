"""test read-only pgstac instance."""

import os
from contextlib import asynccontextmanager
from urllib.parse import quote_plus as quote

import psycopg
import pytest
from fastapi import FastAPI
from psycopg.rows import class_row, dict_row
from pypgstac.db import PgstacDB
from pypgstac.load import Loader
from pypgstac.migrate import Migrate
from starlette.requests import Request
from starlette.testclient import TestClient

from titiler.pgstac.errors import ReadOnlyPgSTACError
from titiler.pgstac.model import Metadata, PgSTACSearch, Search

DATA_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
collection = os.path.join(DATA_DIR, "noaa-emergency-response.json")
items = os.path.join(DATA_DIR, "noaa-eri-nashville2020.json")


@pytest.fixture(
    params=[
        True,
        False,
    ],
    scope="session",
)
def pgstac_ro(request, database):
    """Create PgSTAC fixture."""
    read_only = request.param

    connection = f"postgresql://{database.user}:{quote(database.password)}@{database.host}:{database.port}/{database.dbname}"
    with psycopg.connect(connection) as conn:
        with conn.cursor() as cur:
            cur.execute("DROP SCHEMA IF EXISTS pgstac CASCADE;")

    with PgstacDB(dsn=connection) as db:
        migrator = Migrate(db)
        version = migrator.run_migration()
        assert version

        loader = Loader(db=db)
        loader.load_collections(collection)
        loader.load_items(items)

    # register one search
    with psycopg.connect(
        connection,
        options="-c search_path=pgstac,public -c application_name=pgstac",
    ) as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            search = PgSTACSearch(collections=["noaa-emergency-response"])
            metadata = Metadata(name="noaa-emergency-response")
            cursor.row_factory = class_row(Search)
            cursor.execute(
                "SELECT * FROM search_query(%s, _metadata => %s);",
                (
                    search.model_dump_json(by_alias=True, exclude_none=True),
                    metadata.model_dump_json(exclude_none=True),
                ),
            )
            cursor.fetchone()

    if read_only:
        with psycopg.connect(connection) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE pgstac.pgstac_settings SET value = true WHERE name = 'readonly';"
                )

    yield connection, read_only


@pytest.fixture(autouse=True)
def app_ro(pgstac_ro, monkeypatch):
    """create app fixture."""
    monkeypatch.setenv("TITILER_PGSTAC_CACHE_DISABLE", "TRUE")

    dsn, ro = pgstac_ro

    from titiler.pgstac.db import close_db_connection, connect_to_db
    from titiler.pgstac.dependencies import CollectionIdParams, SearchIdParams
    from titiler.pgstac.extensions import searchInfoExtension
    from titiler.pgstac.factory import (
        MosaicTilerFactory,
        add_search_list_route,
        add_search_register_route,
    )
    from titiler.pgstac.settings import PostgresSettings

    postgres_settings = PostgresSettings(database_url=dsn)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        """FastAPI Lifespan."""
        # Create Connection Pool
        await connect_to_db(app, settings=postgres_settings)
        yield
        # Close the Connection Pool
        await close_db_connection(app)

    app = FastAPI(lifespan=lifespan)
    app.state.readonly = ro

    @app.get("/pgstac")
    def pgstac_info(request: Request):
        """Retrieve PgSTAC Info."""
        with request.app.state.dbpool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cursor:
                cursor.execute("SELECT pgstac.readonly()")
                pgstac_readonly = cursor.fetchone()["readonly"]

        return {
            "pgstac_readonly": pgstac_readonly,
        }

    searches = MosaicTilerFactory(
        path_dependency=SearchIdParams,
        router_prefix="/searches/{search_id}",
        extensions=[
            searchInfoExtension(),
        ],
    )
    app.include_router(searches.router, prefix="/searches/{search_id}")
    add_search_register_route(
        app,
        prefix="/searches",
        tile_dependencies=[
            searches.layer_dependency,
            searches.dataset_dependency,
            searches.pixel_selection_dependency,
            searches.process_dependency,
            searches.render_dependency,
            searches.pgstac_dependency,
            searches.reader_dependency,
            searches.backend_dependency,
        ],
    )
    add_search_list_route(app, prefix="/searches", tags=["STAC Search"])

    collection = MosaicTilerFactory(
        path_dependency=CollectionIdParams,
        router_prefix="/collections/{collection_id}",
        extensions=[
            searchInfoExtension(),
        ],
    )
    app.include_router(collection.router, prefix="/collections/{collection_id}")

    with TestClient(app) as app:
        yield app, ro


def test_pgstac_config(app_ro):
    """should return pgstac read-only info."""
    client, ro = app_ro

    response = client.get("/pgstac")
    assert response.status_code == 200
    assert response.json()["pgstac_readonly"] == ro


def test_searches_ro(app_ro):
    """Register Search should only work for non-read-only pgstac."""
    client, ro = app_ro

    response = client.get("/searches/list", params={"limit": 1})
    assert response.status_code == 200
    resp = response.json()
    assert resp["context"]["matched"] == 1
    search_id = resp["searches"][0]["search"]["hash"]

    response = client.get(f"/searches/{search_id}/info")
    assert response.status_code == 200

    if ro:
        with pytest.raises(ReadOnlyPgSTACError):
            client.post("/searches/register", json={"collections": ["collection"]})
    else:
        response = client.post(
            "/searches/register", json={"collections": ["collection"]}
        )
        assert response.status_code == 200


def test_collections_ro(app_ro):
    """collections should only work for non-read-only pgstac."""
    client, ro = app_ro

    if ro:
        with pytest.raises(ReadOnlyPgSTACError):
            client.get("/collections/noaa-emergency-response/info")
    else:
        response = client.get("/collections/noaa-emergency-response/info")
        assert response.status_code == 200
