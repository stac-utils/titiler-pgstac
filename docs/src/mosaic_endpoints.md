The `titiler.pgstac` package comes with a full FastAPI application with Mosaic and single STAC item support.

| Method | URL                                                                       | Output                            | Description
| ------ | --------------------------------------------------------------------------|-----------------------------------|--------------
| `POST` | `/mosaic/register`                                                               | JSON ([Register][register_model]) | Register **Search** query
| `GET`  | `/mosaic/{searchid}/info`                                                        | JSON ([Info][info_model])         | Return **Search** query infos
| `GET`  | `/mosaic/list`                                                                   | JSON ([Infos][infos_model])       | Return list of **Search** entries with `Mosaic` type
| `GET`  | `/mosaic/{searchid}/{lon},{lat}/assets`                                          | JSON                              | Return a list of assets which overlap a given point
| `GET`  | `/mosaic/{searchid}[/{TileMatrixSetId}]/{z}/{x}/{Y}/assets` **DEPRECATED**       | JSON                              | Return a list of assets which overlap a given tile
| `GET`  | `/mosaic/{searchid}/tiles[/{TileMatrixSetId}]/{z}/{x}/{Y}/assets`                | JSON                              | Return a list of assets which overlap a given tile
| `GET`  | `/mosaic/{searchid}/tiles[/{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]` | image/bin                         | Create a web map tile image for a search query and a tile index
| `GET`  | `/mosaic/{searchid}[/{TileMatrixSetId}]/tilejson.json`                           | JSON ([TileJSON][tilejson_model]) | Return a Mapbox TileJSON document
| `GET`  | `/mosaic/{searchid}[/{TileMatrixSetId}]/WMTSCapabilities.xml`                    | XML                               | return OGC WMTS Get Capabilities
| `GET`  | `/mosaic/{searchid}[/{TileMatrixSetId}]/map`                                     | HTML                              | simple map viewer

### Register a Search Request

`:endpoint:/mosaic/register - [POST]`

- **Body**: A valid STAC Search query (see: https://github.com/radiantearth/stac-api-spec/tree/master/item-search)

```json
// titiler-pgstac search body example
{
  "collections": [
    "string"
  ],
  "ids": [
    "string"
  ],
  "bbox": [
    "string",
    "string",
    "string",
    "string"
  ],
  "intersects": {
    "type": "Point",
    "coordinates": [
      "string",
      "string"
    ]
  },
  "query": {
    "additionalProp1": {},
    "additionalProp2": {},
    "additionalProp3": {}
  },
  "filter": {},
  "datetime": "string",
  "sortby": "string",
  "filter-lang": "cql-json",
  "metadata": {
    "type": "mosaic",
    "bounds": [
      "string",
      "string",
      "string",
      "string"
    ],
    "minzoom": 0,
    "maxzoom": 0,
    "name": "string",
    "assets": [
      "string"
    ],
    "defaults": {}
  }
}
```

!!! important
    In `titiler-pgstac` we extended the regular `stac` search to add a metadata entry.
    Metadata defaults to `{"type": "mosaic"}`.

Example:

- `https://myendpoint/mosaic/register`

```bash
curl -X 'POST' 'http://127.0.0.1:8081/mosaic/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"collections":["landsat-c2l2-sr"], "bbox":[-123.75,34.30714385628804,-118.125,38.82259097617712], "filter-lang": "cql-json"}' | jq
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

# or using CQL2
curl -X 'POST' 'http://127.0.0.1:8081/mosaic/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"filter": {"op": "=", "args": [{"property": "collection"}, "landsat-c2l2-sr"]}}'

# or using CQL2 with metadata
curl -X 'POST' 'http://127.0.0.1:8081/mosaic/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"filter": {"op": "=", "args": [{"property": "collection"}, "landsat-c2l2-sr"]}, "metadata": {"name": "landsat mosaic"}}'
```

### Search infos

`:endpoint:/mosaic/{searchid}/info - [GET]`

- PathParams:
    - **searchid**: search query hashkey.

Example:

- `https://myendpoint/mosaic/5a1b82d38d53a5d200273cbada886bd7/info`

```bash
curl 'http://127.0.0.1:8081/mosaic/5a1b82d38d53a5d200273cbada886bd7/info' | jq
>> {
  "search": {
    "hash": "5a1b82d38d53a5d200273cbada886bd7",
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
    "_where": "(  TRUE  )  AND collection_id = ANY ('{landsat-c2l2-sr}')  AND geometry && '0103000020E610000001000000050000000000000000F05EC055F6687D502741400000000000F05EC02D553EA94A6943400000000000885DC02D553EA94A6943400000000000885DC055F6687D502741400000000000F05EC055F6687D50274140' ",
    "orderby": "datetime DESC, id DESC",
    "lastused": "2022-03-03T11:42:07.213313+00:00",
    "usecount": 2,
    "metadata": {
      "type": "mosaic"
    }
  },
  "links": [
    {
      "rel": "self",
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
```

### List Searches

`:endpoint:/mosaic/list - [GET]`

- QueryParams:
    - **limit** (int): Page size limit, Default is `10`.
    - **offset** (int): Page offset.
    - **sortby** (str): Sort the searches by Metadata properties (ascending (default) or descending (`-`)).

!!! Important
    Additional query-parameters (form `PROP=VALUE`) will be considered as a **property filter**.

Example:

- `https://myendpoint/mosaic/list`
- `https://myendpoint/mosaic/list?limit=100`
- `https://myendpoint/mosaic/list?limit=10&offset=10` (page 2)
- `https://myendpoint/mosaic/list?data=noaa` (only show mosaics with `metadata.data == noaa`)
- `https://myendpoint/mosaic/list?sortby=lastused` (sort mosaic by `lastused` pgstac search property)
- `https://myendpoint/mosaic/list?sortby=-prop` (sort mosaic (descending) by `metadata.prop` values)


### Tiles

`:endpoint:/mosaic/{searchid}/tiles[/{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]`

- PathParams:
    - **searchid**: search query hashkey.
    - **TileMatrixSetId**: TileMatrixSet name, default is `WebMercatorQuad`. OPTIONAL
    - **z**: Tile's zoom level.
    - **x**: Tile's column.
    - **y**: Tile's row.
    - **scale**: Tile size scale, default is set to 1 (256x256). OPTIONAL
    - **format**: Output image format, default is set to None and will be either JPEG or PNG depending on masked value. OPTIONAL

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **nodata**: Overwrite internal Nodata value. OPTIONAL
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.
    - **buffer** (float): Add buffer on each side of the tile (e.g 0.5 = 257x257, 1.0 = 258x258).
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/1/2/3?assets=B01`
- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/1/2/3.jpg?assets=B01`
- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/WorldCRS84Quad/1/2/3@2x.png?assets=B01&assets=B02&assets=B03`
- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/WorldCRS84Quad/1/2/3?assets=B01&rescale=0,1000&colormap_name=cfastie`

### TilesJSON

`:endpoint:/mosaic/{searchid}[/{TileMatrixSetId}]/tilejson.json`

- PathParams:
    - **searchid**: search query hashkey.
    - **TileMatrixSetId**: TileMatrixSet name, default is `WebMercatorQuad`. OPTIONAL

- QueryParams:
    - **tile_format**: Output image format, default is set to None and will be either JPEG or PNG depending on masked value.
    - **tile_scale**: Tile size scale, default is set to 1 (256x256). OPTIONAL
    - **minzoom**: Overwrite default minzoom. OPTIONAL
    - **maxzoom**: Overwrite default maxzoom. OPTIONAL
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.
    - **buffer** (float): Add buffer on each side of the tile (e.g 0.5 = 257x257, 1.0 = 258x258).
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/tilejson.json?assets=B01`
- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/tilejson.json?assets=B01&tile_format=png`
- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/WorldCRS84Quad/tilejson.json?assets=B01&tile_scale=2`


### WMTS

`:endpoint:/mosaic/{searchid}[/{TileMatrixSetId}]/WMTSCapabilities.xml`

- PathParams:
    - **searchid**: search query hashkey.
    - **TileMatrixSetId**: TileMatrixSet name, default is `WebMercatorQuad`. OPTIONAL

- QueryParams:
    - **tile_format**: Output image format, default is set to None and will be either JPEG or PNG depending on masked value.
    - **tile_scale**: Tile size scale, default is set to 1 (256x256). OPTIONAL
    - **minzoom**: Overwrite default minzoom. OPTIONAL
    - **maxzoom**: Overwrite default maxzoom. OPTIONAL
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.
    - **buffer** (float): Add buffer on each side of the tile (e.g 0.5 = 257x257, 1.0 = 258x258).
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/WMTSCapabilities.xml?assets=B01`
- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/WMTSCapabilities.xml?assets=B01&tile_format=png`
- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/WorldCRS84Quad/WMTSCapabilities.xml?assets=B01&tile_scale=2`


### Assets

`:endpoint:/mosaic/{searchid}/tiles/[{TileMatrixSetId}]/{z}/{x}/{y}/assets`

- PathParams:
    - **searchid**: search query hashkey.
    - **TileMatrixSetId**: TileMatrixSet name, default is `WebMercatorQuad`. OPTIONAL
    - **z**: Tile's zoom level.
    - **x**: Tile's column.
    - **y**: Tile's row.

- QueryParams:
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

Example:

- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/0/0/0/assets`

`:endpoint:/mosaic/{searchid}/{lon},{lat}/assets`

- PathParams:
    - **searchid**: search query hashkey.
    - **lon**: Longitude (in WGS84 CRS).
    - **lat**: Latitude (in WGS84 CRS).

- QueryParams:
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

Example:

- `https://myendpoint/mosaic/f1ed59f0a6ad91ed80ae79b7b52bc707/0.0,0.0/assets`

[tilejson_model]: https://github.com/developmentseed/titiler/blob/2335048a407f17127099cbbc6c14e1328852d619/src/titiler/core/titiler/core/models/mapbox.py#L16-L38
[info_model]: https://github.com/stac-utils/titiler-pgstac/blob/047315da8851a974660032ca45f219db2c3a8d54/titiler/pgstac/model.py#L236-L240
[infos_model]: https://github.com/stac-utils/titiler-pgstac/blob/4f569fee1946f853be9b9149cb4dd2fd5c62b110/titiler/pgstac/model.py#L260-L265
[register_model]: https://github.com/stac-utils/titiler-pgstac/blob/047315da8851a974660032ca45f219db2c3a8d54/titiler/pgstac/model.py#L229-L233
