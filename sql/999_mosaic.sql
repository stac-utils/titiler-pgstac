SET SEARCH_PATH TO pgstac, public;

-- Create table to store the search id
DROP TABLE IF EXISTS mosaics;
CREATE TABLE mosaics (
    id VARCHAR GENERATED ALWAYS AS (md5(content::text)) STORED PRIMARY KEY,
    content JSONB NOT NULL,
    datetime timestamptz DEFAULT now() NOT NULL
);

-- Create Mosaic
CREATE OR REPLACE FUNCTION create_mosaic(body jsonb) RETURNS text AS $$
DECLARE
_id text;
BEGIN
    WITH _mosaic AS (
        INSERT INTO mosaics (content)
        VALUES (body)
        ON CONFLICT (id) DO NOTHING
        RETURNING id INTO _id
    ) SELECT COALESCE (
        -- when `id` already exists, SQL won't return anything
        (SELECT id FROM _mosaic),
        (SELECT id FROM mosaics WHERE content = body)
    ) AS _id;
    RETURN _id;
END;
$$ LANGUAGE PLPGSQL SET SEARCH_PATH TO pgstac,public;


-- Get Mosaic items for a bbox
CREATE OR REPLACE FUNCTION items_for_geom(
    mosaic_id text,
    geom jsonb
) RETURNS SETOF jsonb AS $$
DECLARE
_search jsonb;
BEGIN
    SELECT content INTO _search FROM mosaics WHERE id=mosaic_id;
    RETURN QUERY
    SELECT * from search(
        jsonb_set(_search, '{intersects}', geom)
    );
END;
$$ LANGUAGE PLPGSQL SET SEARCH_PATH TO pgstac,public;

