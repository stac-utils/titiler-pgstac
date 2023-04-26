"""Test healtz endpoint."""

from unittest.mock import patch

from psycopg import OperationalError
from psycopg_pool import PoolTimeout


def test_database_online(app):
    """check health endpoints."""
    response = app.get("/healthz")
    assert response.status_code == 200
    resp = response.json()
    assert resp["database_online"]


def test_database_offline(app):
    """check health endpoints."""
    with patch("psycopg.Connection.execute") as mock_execute:
        mock_execute.side_effect = OperationalError
        response = app.get("/healthz")
        assert response.status_code == 200
        resp = response.json()
        assert not resp["database_online"]

    with patch("psycopg_pool.ConnectionPool.connection") as mock_conn:
        mock_conn.side_effect = PoolTimeout
        response = app.get("/healthz")
        assert response.status_code == 200
        resp = response.json()
        assert not resp["database_online"]
