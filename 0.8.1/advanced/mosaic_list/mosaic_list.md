

Starting with `titiler-pgstac>=0.2.0`, we've added a `/mosaic/list` endpoint to be able to list all registered mosaics. When we add a mosaic via `/mosaic/register` we add a specific `metadata.type: "mosaic"` to the pgstac `search` entry, which is then used by the `/mosaic/list` endpoint to filter the pgstac `searches`.

In order to make the mosaic list performant, users might want to alter their PgSTAC database to add an **index**

```sql
$ psql
postgis=# SET schema 'pgstac';
>> SET

postgis=# CREATE INDEX IF NOT EXISTS searches_mosaic ON searches ((true)) WHERE metadata->>'type'='mosaic';
>> NOTICE:  relation "searches_mosaic" already exists, skipping
>> CREATE INDEX

postgis=# SELECT
    indexname,
    indexdef
FROM
    pg_indexes
WHERE
    tablename = 'searches';

>>     indexname    |                                                         indexdef
>> -----------------+---------------------------------------------------------------------------------------------------------------------------
>>  searches_pkey   | CREATE UNIQUE INDEX searches_pkey ON pgstac.searches USING btree (hash)
>>  searches_mosaic | CREATE INDEX searches_mosaic ON pgstac.searches USING btree ((true)) WHERE ((metadata ->> 'type'::text) = 'mosaic'::text)
```

ref: https://github.com/developmentseed/eoAPI/blob/master/stack/handlers/db_handler.py#L204-L213
