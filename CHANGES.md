# Release Notes

## 0.1.0.a2 (TDB) Pre-Release

* Switch to **psycopg3**

**breaking changes**

* Unify *reader/writer* db pools to `request.app.state.dbpool`
* rename `PostgresSettings.db_max_inactive_conn_lifetime` to `PostgresSettings.max_idle`
* remove `PostgresSettings().reader_connection_string` and `PostgresSettings().writer_connection_string`. Replaced with `PostgresSettings().connection_string`
* update titiler requirement (>= 0.4)
* add `filter-lang` in Search model to support newer PgSTAC (with CQL-2)

## 0.1.0.a1 (2021-09-15) Pre-Release

* Surface PgSTAC options (`scan_limit`, `items_limit`, `time_limit`, `exitwhenfull` and `skipcovered`) in Tile endpoints

**breaking changes**

* remove `psycopg2` requirements to avoid conflict with `psycopg2-binary` (https://github.com/stac-utils/titiler-pgstac/pull/15)

## 0.1.0.a0 (2021-09-06) Pre-Release

Initial release
