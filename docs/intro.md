

**TiTiler.PgSTAC** is an extension of TiTiler, which connect PgSTAC database to a dynamic tiler, in order to create mosaics from STAC search queries.

## Userflow

### 1. Register a `Search` request

The first step of the mosaic create is to register a `Search` query within the PgSTAC database. `TiTiler.PgSTAC` has a `/register (POST)` endpoint which will return a `searchid` (== mosaicid).

![](https://user-images.githubusercontent.com/10407788/132193537-0560016f-09bc-4a25-8a2a-eac9b50bc28a.png)

#### Example

```
curl -X 'POST' 'http://127.0.0.1:8000/register' -H 'accept: application/json' -H 'Content-Type: application/json'
-d '{"collections":["landsat-c2l2-sr"], "bbox":[-123.75,34.30714385628804,-118.125,38.82259097617712]}' | jq
{
  "searchid": "f1ed59f0a6ad91ed80ae79b7b52bc707",
  "metadata": "http://127.0.0.1:8000/f1ed59f0a6ad91ed80ae79b7b52bc707/info",
  "tiles": "http://127.0.0.1:8000/f1ed59f0a6ad91ed80ae79b7b52bc707/tilejson.json"
}
```

Learn more about the **Search request** format: https://github.com/radiantearth/stac-api-spec/tree/master/item-search


### 2. Fech `tiles`

When we have a `searchid` we can now call the dynamic tiler and ask for tiles.


![](https://user-images.githubusercontent.com/10407788/132197899-e79b3118-313b-45e7-a431-5d3034984459.png)

Note: Because tiles will be create from STAC items we need to pass an `assets={stac asset}` to the tiler.

#### Example

```
curl 'http://127.0.0.1:8000/tiles/f1ed59f0a6ad91ed80ae79b7b52bc707/8/40/102.png?assets=B01&rescale=0,16000 > 8-40-102.png
```

#### tilejson

You can also use the `tilejson` endpoint to construct the `tiles` url.

```
curl http://127.0.0.1:8000/f1ed59f0a6ad91ed80ae79b7b52bc707/tilejson.json\?assets\=B01&tile_format=png | jq
{
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
