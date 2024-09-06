

**TiTiler.PgSTAC** is a TiTiler extension, which create dynamic tiler connected to PgSTAC databases.

By default the main application (`titiler.pgstac.main.app`) provides three sets of endpoints:

- `/searches/{search_id}`: Dynamic **mosaic** tiler based on PgSTAC Search Query

- `/collections/{collection_id}`: Dynamic **mosaic** tiler based on STAC Collection

- `/collections/{collection_id}/items/{item_id}`: Dynamic tiler for single STAC item (stored in PgSTAC)

Two other sets of endpoints can be enabled using environment variable:

- `/collections/{collection_id}/items/{item_id}/assets/{asset_id}`: Dynamic tiler of single STAC Asset (stored in PgSTAC), enabled setting `TITILER_PGSTAC_API_ENABLE_ASSETS_ENDPOINTS=TRUE`

- `/external`: Dynamic tiler of single Cloud Optimized dataset, enabled setting `TITILER_PGSTAC_API_ENABLE_EXTERNAL_DATASET_ENDPOINTS=TRUE`

## STAC Searches - `/searches/{search_id}`

#### Register a PgSTAC `Search` request

![](https://user-images.githubusercontent.com/10407788/132193537-0560016f-09bc-4a25-8a2a-eac9b50bc28a.png)

!!! Important
    In `TiTiler.PgSTAC` a STAC [`Search Query`](https://github.com/radiantearth/stac-api-spec/tree/master/item-search) is equivalent to a *Virtual Mosaic* and a
    PgSTAC [`Search Hash`](https://github.com/stac-utils/pgstac/blob/main/src/pgstac/sql/004_search.sql#L411-L427) is equivalent to a *Mosaic Identifier*.


Before being able to create Map Tiles, the user needs to register a `Search Query` within the PgSTAC database (in the `searches` table). By default, `TiTiler.PgSTAC` has a `/searches/register (POST)` endpoint which will:

  - validate the search query (based on the STAC API specification [`item-search`]((https://github.com/radiantearth/stac-api-spec/tree/master/item-search)))

  - send the search query to the postgres database using the [`search_query`](https://github.com/stac-utils/pgstac/blob/76512ab50e1373e3f77c65843cf328cbe6dd0dec/sql/004_search.sql#L1000) PgSTAC function

  - return a PgSTAC Search hash

**Example**

```bash
curl -X 'POST' 'http://127.0.0.1:8081/searches/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"collections":["landsat-c2l2-sr"], "bbox":[-123.75,34.30714385628804,-118.125,38.82259097617712], "filter-lang": "cql-json"}' | jq

>> {
  "id": "5a1b82d38d53a5d200273cbada886bd7",
  "links": [
    {
      "rel": "metadata",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/searches/5a1b82d38d53a5d200273cbada886bd7/info"
    },
    {
      "rel": "tilejson",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/searches/5a1b82d38d53a5d200273cbada886bd7/tilejson.json"
    }
  ]
}

# Or using CQL-2
curl -X 'POST' 'http://127.0.0.1:8081/searches/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"filter": {"op": "and", "args": [{"op": "=", "args": [{"property": "collection"}, "landsat-c2l2-sr"]}, {"op": "s_intersects", "args": [{"property": "geometry"}, {"coordinates": [[[-123.75, 34.30714385628804], [-123.75, 38.82259097617712], [-118.125, 38.82259097617712], [-118.125, 34.30714385628804], [-123.75, 34.30714385628804]]], "type": "Polygon"}]}]}}' | jq

>> {
  "id": "5063721f06957d6b2320326d82e90d1e",
  "links": [
    {
      "rel": "metadata",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/searches/5063721f06957d6b2320326d82e90d1e/info"
    },
    {
      "rel": "tilejson",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/searches/5063721f06957d6b2320326d82e90d1e/tilejson.json"
    }
  ]
}
```


```bash
curl http://127.0.0.1:8081/searches/5063721f06957d6b2320326d82e90d1e/info | jq

>> {
  "search": {
    "hash": "5063721f06957d6b2320326d82e90d1e",  # <-- this is the PgSTAC Hash = search/mosaic identifier
    "search": {  # <-- Summary of the search request
      "filter": {  # <-- this is CQL2 filter associated with the search
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
    "_where": "(  ( (collection_id = 'landsat-c2l2-sr') and st_intersects(geometry, '0103000020E610000001000000050000000000000000F05EC055F6687D502741400000000000F05EC02D553EA94A6943400000000000885DC02D553EA94A6943400000000000885DC055F6687D502741400000000000F05EC055F6687D50274140'::geometry) )  )  ",  # <-- internal pgstac WHERE expression
    "orderby": "datetime DESC, id DESC",
    "lastused": "2022-03-03T11:44:55.878504+00:00",  # <-- internal pgstac variable
    "usecount": 2,  # <-- internal pgstac variable
    "metadata": {  # <-- titiler-pgstac Mosaic Metadata
      "type": "mosaic"  # <-- when we use the `/searches/register` endpoint, titiler-pgstac will add `type=mosaic` to the metadata
    }
  },
  "links": [
    {
      "rel": "self",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/searches/5063721f06957d6b2320326d82e90d1e/info"
    },
    {
      "rel": "tilejson",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/searches/5063721f06957d6b2320326d82e90d1e/tilejson.json"
    }
  ]
}
```

#### Mosaic Metadata

In addition to the `search query`, a user can pass `metadata`, which will be saved in the postgres table.

```bash
curl -X 'POST' 'http://127.0.0.1:8081/searches/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"collections":["landsat-c2l2-sr"], "bbox":[-123.75,34.30714385628804,-118.125,38.82259097617712], "filter-lang": "cql-json", "metadata": {"minzoom": 8, "maxzoom": 13, "assets": ["B04", "B03", "B02"], "defaults": {"true_color": {"assets": ["B04", "B03", "B02"], "color_formula": "Gamma RGB 3.5 Saturation 1.7 Sigmoidal RGB 15 0.35"}}}}' | jq

>> {
  "id": "f31d7de8a5ddfa3a80b9a9dd06378db1",
  "links": [
    {
      "rel": "metadata",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/searches/f31d7de8a5ddfa3a80b9a9dd06378db1/info"
    },
    {
      "rel": "tilejson",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/searches/f31d7de8a5ddfa3a80b9a9dd06378db1/tilejson.json"
    }
  ]
}

curl http://127.0.0.1:8081/searches/f31d7de8a5ddfa3a80b9a9dd06378db1/info | jq '.search.metadata'
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

#### Fetch mosaic `Tiles`

When we have an **id** we can call the dynamic tiler and ask for Map Tiles.

![](https://user-images.githubusercontent.com/10407788/132197899-e79b3118-313b-45e7-a431-5d3034984459.png)

**How it works**

On each `Tile` request, the tiler api is going to call the PgSTAC [`geometrysearch`](https://github.com/stac-utils/pgstac/blob/76512ab50e1373e3f77c65843cf328cbe6dd0dec/sql/006_tilesearch.sql#L4) function with the `id` and the `Tile geometry` to get the list of **STAC Items** ([code](https://github.com/stac-utils/titiler-pgstac/blob/0f2b5b4ba50bb3458237ab21cf9a154d7b811851/titiler/pgstac/mosaic.py#L238-L247)). Then based on the `assets` parameter, the tiler will construct the tile image ([code](https://github.com/stac-utils/titiler-pgstac/blob/0f2b5b4ba50bb3458237ab21cf9a154d7b811851/titiler/pgstac/mosaic.py#L257-L263)).

!!! important
    Because `Tiles` will be created from **STAC Items** we HAVE TO pass **`assets={stac asset}`** option to the tile endpoint to tell the tiler which **STAC assets** has to be used.

    See full list of [options](../mosaic_endpoints/#tiles)

**Example**

```bash
curl 'http://127.0.0.1:8081/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/8/40/102.png?assets=B01&rescale=0,16000 > 8-40-102.png
```

## STAC Collection - `/collections/{collection_id}`

No need for the user to `register` search queries for those endpoints. The tiler will automatically `register` a search query (`collection={collection_id}`).

**example**

```bash
curl http://127.0.0.1:8081/collections/my-collection/tilejson.json?assets=data
{
  "tilejson": "2.2.0",
  "name": "Mosaic for 'my-collection' Collection",
  "version": "1.0.0",
  "scheme": "xyz",
  "tiles": [
    "http://127.0.0.1:8081/collections/my-collection/tiles/WebMercatorQuad/{z}/{x}/{y}?assets=data"
  ],
  "minzoom": 0,
  "maxzoom": 24,
  "bounds": [
    -180,
    -90,
    180,
    90
  ],
  "center": [
    0,
    0,
    0
  ]
}
```

## STAC Item - `/collections/{collection_id}/items/{item_id}`

`titiler-pgstac` can also be used to access individual item stored in the PgSTAC database. By default the `titiler-pgstac` application will have a set of `/collections/{collection_id}/items/{item_id}/...` endpoints. The endpoints are created using [titiler.core.factory.MultiBaseTilerFactory](https://developmentseed.org/titiler/advanced/tiler_factories/#titilercorefactorymultibasetilerfactory) but using a custom `path_dependency` with `collection_id` and `item_id` path parameters instead of the STAC url as query parameter.

**example**

```bash
curl http://127.0.0.1:8081/collections/world/items/world_20000_5000/info | jq
{
  "asset": {
    "bounds": [
      153.5000000000667,
      -76.83333333336668,
      179.8333333334053,
      6.4999999999833165
    ],
    "minzoom": 3,
    "maxzoom": 6,
    "band_metadata": [
      [
        "b1",
        {}
      ],
      [
        "b2",
        {}
      ],
      [
        "b3",
        {}
      ]
    ],
    "band_descriptions": [
      [
        "b1",
        ""
      ],
      [
        "b2",
        ""
      ],
      [
        "b3",
        ""
      ]
    ],
    "dtype": "uint8",
    "nodata_type": "None",
    "colorinterp": [
      "red",
      "green",
      "blue"
    ],
    "driver": "GTiff",
    "count": 3,
    "width": 1580,
    "height": 5000,
    "overviews": [
      2,
      4,
      8,
      16
    ]
  }
}

```

See full list of [endpoints](../endpoints/items_endpoints/)
