`TiTiler-PgSTAC` uses PgSTAC [search](https://github.com/stac-utils/pgstac/blob/3499daa2bfa700ae7bb07503795c169bf2ebafc7/sql/004_search.sql#L907-L915) to host mosaic parameters for performance purposes. To help users we added the possibility to add `metadata` to search entries and in `TiTiler-PgSTAC` we introduced a `non-official` specification to help user storing meaningful informations.

### Specification

```js
{
    // OPTIONAL. Default: "mosaic" (No other value accepted for now). Describe the `type` of metadata.
    "type": "mosaic",

    // OPTIONAL. Default: null.
    // The maximum extent of available map tiles. The bounds are represented in WGS:84
    // latitude and longitude values, in the order left, bottom, right, top.
    // Values may be integers or floating point numbers.
    "bounds": [ -180, -85.05112877980659, 180, 85.0511287798066 ],

    // OPTIONAL. Default: null.
    // An integer specifying the minimum zoom level.
    "minzoom": 0,

    // OPTIONAL. Default: null.
    // An integer specifying the maximum zoom level. MUST be >= minzoom.
    "maxzoom": 11,

    // OPTIONAL. Default: null. The name can contain any legal character.
    "name": "compositing",

    // OPTIONAL. Default: null. An array of available assets.
    "assets": ["image", "cog"],

    // OPTIONAL. Default: null. A set of `defaults` configuration to be forwarded to the /tiles endpoints.
    "defaults": {
        "true_color": {
            "assets": ["B4", "B3", "B2"],
            "color_formula": "Gamma RGB 3.5 Saturation 1.7 Sigmoidal RGB 15 0.35",
        },
        "ndvi": {
            "expression": "(B4-B3)/(B4+B3)",
            "rescale": "-1,1",
            "colormap_name": "viridis"
        }
    }
}
```

!!! Important
    - When using the `/mosaic/register` endpoint, `{"type": "mosaic"}` will be set by default
    - All metadata fields are optional and custom fields are also allowed.


```
curl -X 'POST' 'http://127.0.0.1:8081/mosaic/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"filter": {"op": "=", "args": [{"property": "collection"}, "landsat-c2l2-sr"]}, "metadata": {"name": "landsat mosaic"}}'
>> {
  "searchid": "d7fcdefd0457c949ea7a6192bc2c7122",
  "links": [
    {
      "rel": "metadata",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/d7fcdefd0457c949ea7a6192bc2c7122/info"
    },
    {
      "rel": "tilejson",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/d7fcdefd0457c949ea7a6192bc2c7122/tilejson.json"
    }
  ]
}

curl http://127.0.0.1:8081/mosaic/d7fcdefd0457c949ea7a6192bc2c7122/info | jq '.search.metadata'
>> {
  "type": "mosaic",
  "name": "landsat mosaic"
}
```

```
curl -X 'POST' 'http://127.0.0.1:8081/mosaic/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"collections": ["noaa-emergency-response"], "bbox": [-87.0251, 36.0999, -85.4249, 36.2251], "filter-lang": "cql-json", "metadata": {"bounds": [-87.0251, 36.0999, -85.4249, 36.2251], "minzoom": 14, "maxzoom": 18, "assets": ["cog"], "defaults": {"true_color": {"bidx": [1, 2, 3]}}}}'
>> {
  "searchid":"4b0db3dbd1858d54a3a55f84de97d1ca",
  "links":[
    {
      "rel": "metadata",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/4b0db3dbd1858d54a3a55f84de97d1ca/info"
    },
    {
      "rel": "tilejson",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/mosaic/4b0db3dbd1858d54a3a55f84de97d1ca/tilejson.json"
    }
  ]
}

curl http://127.0.0.1:8081/mosaic/4b0db3dbd1858d54a3a55f84de97d1ca/info | jq '.search.metadata'
>> {
  "type": "mosaic",
  "bounds": [
    -87.0251,
    36.0999,
    -85.4249,
    36.2251
  ],
  "minzoom": 14,
  "maxzoom": 18,
  "assets": [
    "cog"
  ],
  "defaults": {
    "true_color": {
      "bidx": [
        1,
        2,
        3
      ]
    }
  }
}
```
