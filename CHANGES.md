# Release Notes

## 0.1.0.a1 (2021-09-15) Pre-Release

- Surface PgSTAC options (`scan_limit`, `items_limit`, `time_limit`, `exitwhenfull` and `skipcovered`) in Tile endpoints

**breaking changes**

- remove `psycopg2` requirements to avoid conflict with `psycopg2-binary` (https://github.com/stac-utils/titiler-pgstac/pull/15)

## 0.1.0.a0 (2021-09-06) Pre-Release

Initial release
