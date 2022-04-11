# Release Notes

## Unreleased

* Insert mosaic metadata `min/max zoom` and `bounds` in tilejson

## 0.1.0.a7 (2022-04-05) Pre-Release

* add `feature()` method to `PGSTACBackend` mosaic backend
* add `/statistics` endpoint to return statistics given a GeoJSON feature or featureCollection
* add `collection` in allowed returned fields
* switch to `pgstac.search` to get the STAC Item in `titiler.pgstac.dependencies.get_stac_item` (https://github.com/stac-utils/titiler-pgstac/pull/50)

## 0.1.0.a6 (2022-03-14) Pre-Release

* move dependencies to `titiler.pgstac.dependencies`
* add `/stac` endpoints to work with PgSTAC items

**breaking changes**

* add `/mosaic` prefix to the PgSTAC mosaic endpoints

## 0.1.0.a5 (2022-03-03) Pre-Release

* Add `search_dependency` to allow customization of the PgSTAC Search query (Author @drnextgis, https://github.com/stac-utils/titiler-pgstac/pull/41)
* Add PgSTAC Search entries model (https://github.com/stac-utils/titiler-pgstac/pull/43)
* Add `Metadata` specification (https://github.com/stac-utils/titiler-pgstac/pull/38)

**breaking changes**

* update `titiler.core` and `titiler.mosaic` requirement to `>=0.5`
* When registering a `search` to PgSTAC with the `/register` endpoint, a default metadata `{"type": "mosaic"}` will be set.
* Renamed `titiler.pgstac.models` to `titiler.pgstac.model`
* Renamed `titiler.pgstac.models.SearchQuery` to `titiler.pgstac.model.PgSTACSearch` (and removed `metadata`)
* output response for `/register` endpoint:
```js
// before
{
    "searchid": "...",
    "metadata": "http://endpoint/.../info",
    "tiles": "http://endpoint/.../tilejson.json",
}

// now
{
    "searchid": "...",
    "links": [
        {
            "rel": "info",
            "href": "http://endpoint/.../info",
            "type": "application/json",
        },
        {
            "rel": "tilejson",
            "href": "http://endpoint/.../tilejson.json",
            "type": "application/json",
        }
    ]
}
```

* output response for `/info` endpoint:
```js
// before
{
    "hash": "...",
    "search": {},
    "_where": "...",
    ...
}

// now
{
    "search": {
        "hash": "...",
        "search": {},
        "_where": "...",
        ...
    },
    "links": [
        {
            "rel": "self",
            "href": "http://endpoint/.../info",
            "type": "application/json",
        },
        {
            "rel": "tilejson",
            "href": "http://endpoint/.../tilejson.json",
            "type": "application/json",
        }
    ]
}
```

## 0.1.0.a4 (2022-02-07) Pre-Release

* add tile `buffer` option to match rio-tiler tile options (https://github.com/stac-utils/titiler-pgstac/pull/31)

## 0.1.0.a3 (2021-12-15) Pre-Release

* Forward TMS to the STAC Reader (allow multiple TMS) (https://github.com/stac-utils/titiler-pgstac/pull/28)

## 0.1.0.a2 (2021-12-13) Pre-Release

* Switch to **psycopg3**
* add `filter-lang` in Search model to support newer PgSTAC (with CQL-2)
* add `metadata` in Search model to allow forwarding metadata to the search query entry in PgSTAC

**breaking changes**

* Unify *reader/writer* db pools to `request.app.state.dbpool`
* rename `PostgresSettings.db_max_inactive_conn_lifetime` to `PostgresSettings.max_idle`
* remove `PostgresSettings().reader_connection_string` and `PostgresSettings().writer_connection_string`. Replaced with `PostgresSettings().connection_string`
* update titiler requirement (>= 0.4)

## 0.1.0.a1 (2021-09-15) Pre-Release

* Surface PgSTAC options (`scan_limit`, `items_limit`, `time_limit`, `exitwhenfull` and `skipcovered`) in Tile endpoints

**breaking changes**

* remove `psycopg2` requirements to avoid conflict with `psycopg2-binary` (https://github.com/stac-utils/titiler-pgstac/pull/15)

## 0.1.0.a0 (2021-09-06) Pre-Release

Initial release
