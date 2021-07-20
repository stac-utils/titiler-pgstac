"""Ingest sample data during docker-compose"""

import json

import requests


def ingest_joplin_data():
    """ingest data."""

    with open("collection.json") as f:
        collection = json.load(f)

    r = requests.post("http://0.0.0.0:8000/collections", json=collection)
    if r.status_code not in (200, 409):
        r.raise_for_status()

    with open("index.geojson") as f:
        index = json.load(f)

    for feat in index["features"]:
        feat.pop("stac_extensions", None)
        r = requests.post("http://0.0.0.0:8000/collections/joplin/items", json=feat)
        if r.status_code == 409:
            continue
        r.raise_for_status()


if __name__ == "__main__":
    ingest_joplin_data()
