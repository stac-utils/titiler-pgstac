

**TiTiler.PgSTAC** is an extension of TiTiler, which connect PgSTAC database to a dynamic tiler, in order to create mosaics from STAC search queries.

## Userflow

### 1. Register a `Search` request (Mosaic)

![](https://user-images.githubusercontent.com/10407788/132193537-0560016f-09bc-4a25-8a2a-eac9b50bc28a.png)

In `TiTiler.PgSTAC` a STAC [`Search Query`](https://github.com/radiantearth/stac-api-spec/tree/master/item-search) is equivalent to a Mosaic.

Before being able to create Map Tiles, the user needs to register a `Search Query` within the PgSTAC database (in the `searches` table). By default, `TiTiler.PgSTAC` has a `/register (POST)` endpoint which will:

  - validate the search query (based on the STAC API specification [`item-search`]((https://github.com/radiantearth/stac-api-spec/tree/master/item-search)))
  - send the search query to the postgres database using the [`search_query`](https://github.com/stac-utils/pgstac/blob/76512ab50e1373e3f77c65843cf328cbe6dd0dec/sql/004_search.sql#L1000) PgSTAC function
  - return a `searchid` (might be also called `mosaicid`).

#### Example

```bash
curl -X 'POST' 'http://127.0.0.1:8081/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"collections":["landsat-c2l2-sr"], "bbox":[-123.75,34.30714385628804,-118.125,38.82259097617712], "filter-lang": "cql-json"}' | jq

>> {
  "searchid": "5181a09f58f348db706aa761cd594ce7",
  "metadata": "http://127.0.0.1:8081/5181a09f58f348db706aa761cd594ce7/info",
  "tiles": "http://127.0.0.1:8081/5181a09f58f348db706aa761cd594ce7/tilejson.json"
}

# Or using CQL-2
curl -X 'POST' 'http://127.0.0.1:8081/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"filter": {"op": "and", "args": [{"op": "=", "args": [{"property": "collection"}, "landsat-c2l2-sr"]}, {"op": "s_intersects", "args": [{"property": "geometry"}, {"coordinates": [[[-123.75, 34.30714385628804], [-123.75, 38.82259097617712], [-118.125, 38.82259097617712], [-118.125, 34.30714385628804], [-123.75, 34.30714385628804]]], "type": "Polygon"}]}]}}' | jq

>> {
  "searchid": "3e3ab7cb3d1064728cc1a58bbf6b2b0f",
  "metadata": "http://127.0.0.1:8081/3e3ab7cb3d1064728cc1a58bbf6b2b0f/info",
  "tiles": "http://127.0.0.1:8081/3e3ab7cb3d1064728cc1a58bbf6b2b0f/tilejson.json"
}
```

#### 1.1 Get Mosaic metadata

```bash
curl http://127.0.0.1:8081/3e3ab7cb3d1064728cc1a58bbf6b2b0f/info | jq

>> {
  "hash": "3e3ab7cb3d1064728cc1a58bbf6b2b0f",
  "search": {
    "filter": {
      "op": "and",
      "args": [
        {
          "op": "=",
          "args": [
            {
              "property": "collection"
            },
            "landsat-c2l2-sr"
          ]
        },
        {
          "op": "s_intersects",
          "args": [
            {
              "property": "geometry"
            },
            {
              "type": "Polygon",
              "coordinates": [
                [
                  [
                    -123.75,
                    34.30714385628804
                  ],
                  [
                    -123.75,
                    38.82259097617712
                  ],
                  [
                    -118.125,
                    38.82259097617712
                  ],
                  [
                    -118.125,
                    34.30714385628804
                  ],
                  [
                    -123.75,
                    34.30714385628804
                  ]
                ]
              ]
            }
          ]
        }
      ]
    }
  },
  "_where": " ( (collection_id = 'landsat-c2l2-sr') and st_intersects(geometry, '0103000020E610000001000000050000000000000000F05EC055F6687D502741400000000000F05EC02D553EA94A6943400000000000885DC02D553EA94A6943400000000000885DC055F6687D502741400000000000F05EC055F6687D50274140'::geometry) ) ",
  "orderby": "datetime DESC, id DESC",
  "lastused": "2021-12-16T08:42:21.247913+00:00",
  "usecount": 2,
  "metadata": {}
}
```

Note: In addition to the `search query`, a user can pass `metadata`, which will be saved in the postgres table.

```bash
curl -X 'POST' 'http://127.0.0.1:8081/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"collections":["landsat-c2l2-sr"], "bbox":[-123.75,34.30714385628804,-118.125,38.82259097617712], "filter-lang": "cql-json", "metadata": {"minzoom": 8, "maxzoom": 13, "default-assets": ["B04", "B03", "B02"]}}' | jq

>> {
  "searchid": "5f6f9df1bdb034d3886eb5d04b23a99d",
  "metadata": "http://127.0.0.1:8081/5f6f9df1bdb034d3886eb5d04b23a99d/info",
  "tiles": "http://127.0.0.1:8081/5f6f9df1bdb034d3886eb5d04b23a99d/tilejson.json"
}

curl http://127.0.0.1:8081/5f6f9df1bdb034d3886eb5d04b23a99d/info | jq '.metadata'
>> {
  "maxzoom": 13,
  "minzoom": 8,
  "default-assets": [
    "B04",
    "B03",
    "B02"
  ]
}
```

### 2. Fecth mosaic `Tiles`

When we have a `searchid` we can now call the dynamic tiler and ask for Map Tiles.

![](https://user-images.githubusercontent.com/10407788/132197899-e79b3118-313b-45e7-a431-5d3034984459.png)

**How it works**

On each `Tile` request, the tiler api is going to call the PgSTAC [`geometrysearch`](https://github.com/stac-utils/pgstac/blob/76512ab50e1373e3f77c65843cf328cbe6dd0dec/sql/006_tilesearch.sql#L4) function with the `searchid` and the Tile geometry to get the list of STAC items ([code](https://github.com/stac-utils/titiler-pgstac/blob/0f2b5b4ba50bb3458237ab21cf9a154d7b811851/titiler/pgstac/mosaic.py#L238-L247)). Then based on the `assets` parameter, the tiler will construct the tile image ([code](https://github.com/stac-utils/titiler-pgstac/blob/0f2b5b4ba50bb3458237ab21cf9a154d7b811851/titiler/pgstac/mosaic.py#L257-L263)).

!!! important
  Because `Tiles` will be created from STAC items we HAVE TO pass **`assets={stac asset}`** option to the tile endpoint.

  See full list of [options](../endpoints/#tiles)

#### Example

```bash
curl 'http://127.0.0.1:8081/tiles/f1ed59f0a6ad91ed80ae79b7b52bc707/8/40/102.png?assets=B01&rescale=0,16000 > 8-40-102.png
```

#### tilejson

You can also use the `tilejson` endpoint to construct the `tiles` url.

```bash
curl http://127.0.0.1:8000/f1ed59f0a6ad91ed80ae79b7b52bc707/tilejson.json\?assets\=B01&tile_format=png | jq
>> {
  "tilejson": "2.2.0",
  "name": "f1ed59f0a6ad91ed80ae79b7b52bc707",
  "version": "1.0.0",
  "scheme": "xyz",
  "tiles": [
    "http://127.0.0.1:8000/tiles/f1ed59f0a6ad91ed80ae79b7b52bc707/WebMercatorQuad/{z}/{x}/{y}@1x.png?assets=B01"
  ],
  "minzoom": 0,
  "maxzoom": 24,
  "bounds": [
    -123.75,
    34.30714385628804,
    -118.125,
    38.82259097617712
  ],
  "center": [
    -120.9375,
    36.56486741623258,
    0
  ]
}
```
