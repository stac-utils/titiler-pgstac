from unittest.mock import patch

import pytest
from psycopg import OperationalError
from psycopg_pool import PoolTimeout


@pytest.mark.asyncio
async def test_database_online(app):
    response = await app.get("/healthz")
    assert response.status_code == 200
    resp = response.json()
    assert resp["database_online"]


@pytest.mark.asyncio
async def test_database_offline(app):
    with patch("psycopg.Connection.execute") as mock_execute:
        mock_execute.side_effect = OperationalError
        response = await app.get("/healthz")
        assert response.status_code == 200
        resp = response.json()
        assert not resp["database_online"]

    with patch("psycopg_pool.ConnectionPool.connection") as mock_conn:
        mock_conn.side_effect = PoolTimeout
        response = await app.get("/healthz")
        assert response.status_code == 200
        resp = response.json()
        assert not resp["database_online"]
