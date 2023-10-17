"""``pytest`` configuration."""

import os

import httpx
import pytest


@pytest.fixture(scope="session")
def search_id():
    """Mosaic ID fixture"""
    host = os.environ.get("HOST", "0.0.0.0")
    port = os.environ.get("PORT", "8081")

    query = {"collections": ["world"]}
    response = httpx.post(f"http://{host}:{port}/searches/register", json=query)
    assert response.status_code == 200

    resp = response.json()
    return resp["id"]
