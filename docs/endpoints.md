The `titiler.pgstac` package comes with a full FastAPI application.

## API

| Method | URL                                                                       | Output    | Description
| ------ | --------------------------------------------------------------------------|---------- |--------------
| `POST` | `/register`                                                               | JSON      | Register Search query
| `GET`  | `/{searchid}/info`                                                        | JSON      | Return metadata info about a search query
| `GET`  | `/{searchid}/[{TileMatrixSetId}]/{z}/{x}/{Y}/assets`                      | JSON      | Return a list of assets which overlap a given tile
| `GET`  | `/{searchid}/{lon},{lat}/assets`                                          | JSON      | Return a list of assets which overlap a given point
| `GET`  | `/tiles/{searchid}/[{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]` | image/bin | Create a web map tile image for a search query and a tile index
| `GET`  | `/{searchid}/[{TileMatrixSetId}]/tilejson.json`                           | JSON      | Return a Mapbox TileJSON document
| `GET`  | `/tileMatrixSets`                   | JSON      | return the list of supported TileMatrixSet
| `GET`  | `/tileMatrixSets/{TileMatrixSetId}` | JSON      | return the TileMatrixSet JSON document

## Description

### Register a Search Request

`:endpoint:/register - [POST]`

- Body: A valid STAC Search query (see: https://github.com/radiantearth/stac-api-spec/tree/master/item-search)

Example:

- `https://myendpoint/register`

```bash
curl -X 'POST' 'http://127.0.0.1:8000/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"collections":["landsat-c2l2-sr"], "bbox":[-123.75,34.30714385628804,-118.125,38.82259097617712], "filter-lang": "cql-json"}' | jq
{
  "searchid": "5181a09f58f348db706aa761cd594ce7",
  "metadata": "http://127.0.0.1:8000/5181a09f58f348db706aa761cd594ce7/info",
  "tiles": "http://127.0.0.1:8000/5181a09f58f348db706aa761cd594ce7/tilejson.json"
}

# or using CQL2
curl -X 'POST' 'http://127.0.0.1:8081/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"filter": {"op": "=", "args": [{"property": "collection"}, "landsat-c2l2-sr"]}}'

# or using CQL2 with metadata
curl -X 'POST' 'http://127.0.0.1:8081/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"filter": {"op": "=", "args": [{"property": "collection"}, "landsat-c2l2-sr"]}, "metadata": {"name": "landsat mosaic"}}'
```

### Search metadata

`:endpoint:/{searchid}/info - [GET]`

- PathParams:
    - **searchid**: search query hashkey.

Example:

- `https://myendpoint/f1ed59f0a6ad91ed80ae79b7b52bc707/info`

```bash
curl 'http://127.0.0.1:8000/f1ed59f0a6ad91ed80ae79b7b52bc707/info' | jq
{
  "hash": "5181a09f58f348db706aa761cd594ce7",
  "search": {
    "bbox": [
      -123.75,
      34.30714385628804,
      -118.125,
      38.82259097617712
    ],
    "collections": [
      "landsat-c2l2-sr"
    ],
    "filter-lang": "cql-json"
  },
  "_where": "(((collection_id = ANY ( '{landsat-c2l2-sr}'::text[] )) AND st_intersects(geometry, '0103000020E610000001000000050000000000000000F05EC055F6687D502741400000000000F05EC02D553EA94A6943400000000000885DC02D553EA94A6943400000000000885DC055F6687D502741400000000000F05EC055F6687D50274140'::geometry)))",
  "orderby": "datetime DESC, id DESC",
  "lastused": "2021-12-13T16:43:55.959925+00:00",
  "usecount": 2,
  "metadata": {}
}
```

### Tiles

`:endpoint:/tiles/{searchid}/[{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]`

- PathParams:
    - **searchid**: search query hashkey.
    - **TileMatrixSetId**: TileMatrixSet name, default is `WebMercatorQuad`. OPTIONAL
    - **z**: Mercator tile's zoom level.
    - **x**: Mercator tile's column.
    - **y**: Mercator tile's row.
    - **scale**: Tile size scale, default is set to 1 (256x256). OPTIONAL
    - **format**: Output image format, default is set to None and will be either JPEG or PNG depending on masked value. OPTIONAL

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1/Asset2`).
    - **asset_bidx** (array[str]): Per asset band indexes (e.g `Asset1|1,2,3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **nodata**: Overwrite internal Nodata value. OPTIONAL
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/tiles/f1ed59f0a6ad91ed80ae79b7b52bc707/1/2/3?assets=B01`
- `https://myendpoint/tiles/f1ed59f0a6ad91ed80ae79b7b52bc707/1/2/3.jpg?assets=B01`
- `https://myendpoint/tiles/f1ed59f0a6ad91ed80ae79b7b52bc707/WorldCRS84Quad/1/2/3@2x.png?assets=B01&assets=B02&assets=B03`
- `https://myendpoint/tiles/f1ed59f0a6ad91ed80ae79b7b52bc707/WorldCRS84Quad/1/2/3?assets=B01&rescale=0,1000&colormap_name=cfastie`

### TilesJSON

`:endpoint:/{searchid}/[{TileMatrixSetId}]/tilejson.json` tileJSON document

- PathParams:
    - **searchid**: search query hashkey.
    - **TileMatrixSetId**: TileMatrixSet name, default is `WebMercatorQuad`. OPTIONAL

- QueryParams:
    - **tile_format**: Output image format, default is set to None and will be either JPEG or PNG depending on masked value.
    - **tile_scale**: Tile size scale, default is set to 1 (256x256). OPTIONAL
    - **minzoom**: Overwrite default minzoom. OPTIONAL
    - **maxzoom**: Overwrite default maxzoom. OPTIONAL
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1/Asset2`).
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1,2,3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/f1ed59f0a6ad91ed80ae79b7b52bc707/tilejson.json?assets=B01`
- `https://myendpoint/f1ed59f0a6ad91ed80ae79b7b52bc707/tilejson.json?assets=B01&tile_format=png`
- `https://myendpoint/f1ed59f0a6ad91ed80ae79b7b52bc707/WorldCRS84Quad/tilejson.json?assets=B01&tile_scale=2`

### List TMS

`:endpoint:/tileMatrixSets` - Get the list of supported TileMatrixSet

```bash
$ curl https://myendpoint/tileMatrixSets | jq

{
  "tileMatrixSets": [
    {
      "id": "LINZAntarticaMapTilegrid",
      "title": "LINZ Antarctic Map Tile Grid (Ross Sea Region)",
      "links": [
        {
          "href": "https://myendpoint/tileMatrixSets/LINZAntarticaMapTilegrid",
          "rel": "item",
          "type": "application/json"
        }
      ]
    },
    ...
  ]
}
```

### Get TMS info

`:endpoint:/tileMatrixSets/{TileMatrixSetId}` - Get the TileMatrixSet JSON document

- PathParams:
    - **TileMatrixSetId**: TileMatrixSet name

```bash
$ curl http://127.0.0.1:8000/tileMatrixSets/WebMercatorQuad | jq

{
  "type": "TileMatrixSetType",
  "title": "Google Maps Compatible for the World",
  "identifier": "WebMercatorQuad",
  "supportedCRS": "http://www.opengis.net/def/crs/EPSG/0/3857",
  "wellKnownScaleSet": "http://www.opengis.net/def/wkss/OGC/1.0/GoogleMapsCompatible",
  "boundingBox": {
    "type": "BoundingBoxType",
    "crs": "http://www.opengis.net/def/crs/EPSG/0/3857",
    "lowerCorner": [
      -20037508.3427892,
      -20037508.3427892
    ],
    "upperCorner": [
      20037508.3427892,
      20037508.3427892
    ]
  },
  "tileMatrix": [
    {
      "type": "TileMatrixType",
      "identifier": "0",
      "scaleDenominator": 559082264.028717,
      "topLeftCorner": [
        -20037508.3427892,
        20037508.3427892
      ],
      "tileWidth": 256,
      "tileHeight": 256,
      "matrixWidth": 1,
      "matrixHeight": 1
    },
    ...
```
