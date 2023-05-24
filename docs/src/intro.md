

**TiTiler.PgSTAC** is a TiTiler extension, which create dynamic tiler connected to PgSTAC databases.

By default the main application (`titiler.pgstac.main.app`) provides two sets of endpoints:

- `/mosaic`: Dynamic mosaic tiler based on STAC Queries

- `/stac`: Dynamic tiler for single STAC item (stored in PgSTAC)

## Mosaic

#### 1. Register a `Search` request (Mosaic)

![](https://user-images.githubusercontent.com/10407788/132193537-0560016f-09bc-4a25-8a2a-eac9b50bc28a.png)

!!! Important
    In `TiTiler.PgSTAC` a STAC [`Search Query`](https://github.com/radiantearth/stac-api-spec/tree/master/item-search) is equivalent to a Mosaic.

Before being able to create Map Tiles, the user needs to register a `Search Query` within the PgSTAC database (in the `searches` table). By default, `TiTiler.PgSTAC` has a `/mosaic/register (POST)` endpoint which will:

  - validate the search query (based on the STAC API specification [`item-search`]((https://github.com/radiantearth/stac-api-spec/tree/master/item-search)))
  - send the search query to the postgres database using the [`search_query`](https://github.com/stac-utils/pgstac/blob/76512ab50e1373e3f77c65843cf328cbe6dd0dec/sql/004_search.sql#L1000) PgSTAC function
  - return a `searchid` (might be also called `mosaicid`).

**Example**

```bash
curl -X 'POST' 'http://127.0.0.1:8081/mosaic/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"collections":["landsat-c2l2-sr"], "bbox":[-123.75,34.30714385628804,-118.125,38.82259097617712], "filter-lang": "cql-json"}' | jq

>> {
  "searchid": "5a1b82d38d53a5d200273cbada886bd7",
  "links": [
    {
      "rel": "metadata",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/5a1b82d38d53a5d200273cbada886bd7/info"
    },
    {
      "rel": "tilejson",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/5a1b82d38d53a5d200273cbada886bd7/tilejson.json"
    }
  ]
}

# Or using CQL-2
curl -X 'POST' 'http://127.0.0.1:8081/mosaic/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"filter": {"op": "and", "args": [{"op": "=", "args": [{"property": "collection"}, "landsat-c2l2-sr"]}, {"op": "s_intersects", "args": [{"property": "geometry"}, {"coordinates": [[[-123.75, 34.30714385628804], [-123.75, 38.82259097617712], [-118.125, 38.82259097617712], [-118.125, 34.30714385628804], [-123.75, 34.30714385628804]]], "type": "Polygon"}]}]}}' | jq

>> {
  "searchid": "5063721f06957d6b2320326d82e90d1e",
  "links": [
    {
      "rel": "metadata",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/5063721f06957d6b2320326d82e90d1e/info"
    },
    {
      "rel": "tilejson",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/5063721f06957d6b2320326d82e90d1e/tilejson.json"
    }
  ]
}
```

##### 1.1 Get Mosaic metadata

```bash
curl http://127.0.0.1:8081/mosaic/5063721f06957d6b2320326d82e90d1e/info | jq

>> {
  "search": {
    "hash": "5063721f06957d6b2320326d82e90d1e",
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
    "_where": "(  ( (collection_id = 'landsat-c2l2-sr') and st_intersects(geometry, '0103000020E610000001000000050000000000000000F05EC055F6687D502741400000000000F05EC02D553EA94A6943400000000000885DC02D553EA94A6943400000000000885DC055F6687D502741400000000000F05EC055F6687D50274140'::geometry) )  )  ",
    "orderby": "datetime DESC, id DESC",
    "lastused": "2022-03-03T11:44:55.878504+00:00",
    "usecount": 2,
    "metadata": {
      "type": "mosaic"
    }
  },
  "links": [
    {
      "rel": "self",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/5063721f06957d6b2320326d82e90d1e/info"
    },
    {
      "rel": "tilejson",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/5063721f06957d6b2320326d82e90d1e/tilejson.json"
    }
  ]
}
```

Note: In addition to the `search query`, a user can pass `metadata`, which will be saved in the postgres table.

```bash
curl -X 'POST' 'http://127.0.0.1:8081/mosaic/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"collections":["landsat-c2l2-sr"], "bbox":[-123.75,34.30714385628804,-118.125,38.82259097617712], "filter-lang": "cql-json", "metadata": {"minzoom": 8, "maxzoom": 13, "assets": ["B04", "B03", "B02"], "defaults": {"true_color": {"assets": ["B04", "B03", "B02"], "color_formula": "Gamma RGB 3.5 Saturation 1.7 Sigmoidal RGB 15 0.35"}}}}' | jq

>> {
  "searchid": "f31d7de8a5ddfa3a80b9a9dd06378db1",
  "links": [
    {
      "rel": "metadata",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/f31d7de8a5ddfa3a80b9a9dd06378db1/info"
    },
    {
      "rel": "tilejson",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/f31d7de8a5ddfa3a80b9a9dd06378db1/tilejson.json"
    }
  ]
}

curl http://127.0.0.1:8081/mosaic/f31d7de8a5ddfa3a80b9a9dd06378db1/info | jq '.search.metadata'
>> {
  "type": "mosaic",
  "minzoom": 8,
  "maxzoom": 13,
  "assets": [
    "B04",
    "B03",
    "B02"
  ],
  "defaults": {
    "true_color": {
      "assets": [
        "B04",
        "B03",
        "B02"
      ],
      "color_formula": "Gamma RGB 3.5 Saturation 1.7 Sigmoidal RGB 15 0.35"
    }
  }
}
```

#### 2. Fetch mosaic `Tiles`

When we have a `searchid` we can now call the dynamic tiler and ask for Map Tiles.

![](https://user-images.githubusercontent.com/10407788/132197899-e79b3118-313b-45e7-a431-5d3034984459.png)

**How it works**

On each `Tile` request, the tiler api is going to call the PgSTAC [`geometrysearch`](https://github.com/stac-utils/pgstac/blob/76512ab50e1373e3f77c65843cf328cbe6dd0dec/sql/006_tilesearch.sql#L4) function with the `searchid` and the Tile geometry to get the list of STAC items ([code](https://github.com/stac-utils/titiler-pgstac/blob/0f2b5b4ba50bb3458237ab21cf9a154d7b811851/titiler/pgstac/mosaic.py#L238-L247)). Then based on the `assets` parameter, the tiler will construct the tile image ([code](https://github.com/stac-utils/titiler-pgstac/blob/0f2b5b4ba50bb3458237ab21cf9a154d7b811851/titiler/pgstac/mosaic.py#L257-L263)).

!!! important
  Because `Tiles` will be created from STAC items we HAVE TO pass **`assets={stac asset}`** option to the tile endpoint.

  See full list of [options](../mosaic_endpoints/#tiles)

**Example**

```bash
curl 'http://127.0.0.1:8081/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/8/40/102.png?assets=B01&rescale=0,16000 > 8-40-102.png
```

## Items

Set of endpoints created using TiTiler's [`MultiBaseTilerFactory`]() but with `item` and `collection` query parameter (instead of the default `url`).

**example**

```bash
curl http://127.0.0.1:8081/stac/info?collection=landsat-c2l2-sr&item=LC08_L1TP_028004_20171002_20171018_01_A1
```

See full list of [endpoints](../item_endpoints)
