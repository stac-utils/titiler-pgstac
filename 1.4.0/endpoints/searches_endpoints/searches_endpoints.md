### STAC Searches endpoints

| Method | URL                                                                              | Output                                  | Description
| ------ | ---------------------------------------------------------------------------------|-----------------------------------------|--------------
| `GET`  | `/searches/{search_id}/{lon},{lat}/assets`                                          | JSON                                    | Return a list of assets which overlap a given point
| `GET`  | `/searches/{search_id}/tiles[/{TileMatrixSetId}]/{z}/{x}/{Y}/assets`                | JSON                                    | Return a list of assets which overlap a given tile
| `GET`  | `/searches/{search_id}/tiles[/{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]` | image/bin                               | Create a web map tile image for a search query and a tile index
| `GET`  | `/searches/{search_id}[/{TileMatrixSetId}]/tilejson.json`                           | JSON ([TileJSON][tilejson_model])       | Return a Mapbox TileJSON document
| `GET`  | `/searches/{search_id}[/{TileMatrixSetId}]/WMTSCapabilities.xml`                    | XML                                     | return OGC WMTS Get Capabilities
| `GET`  | `/searches/{search_id}[/{TileMatrixSetId}]/map`                                     | HTML                                    | simple map viewer
| `POST` | `/searches/{search_id}/statistics`                                                  | GeoJSON ([Statistics][statitics_model]) | Return statistics for geojson features
| `GET`  | `/searches/{search_id}/bbox/{minx},{miny},{maxx},{maxy}[/{width}x{height}].{format}`| image/bin                               | Create an image from part of a dataset
| `POST` | `/searches/{search_id}/feature[/{width}x{height}][.{format}]`                       | image/bin                               | Create an image from a GeoJSON feature
| `GET`  | `/searches/{search_id}/point/{lon},{lat}`                                           | JSON ([Point][point_model])             | Return pixel values from assets intersecting with a given point
| `GET`  | `/searches/{search_id}/info`                                                        | JSON ([Info][info_model])               | Return **Search** query infos
| `POST` | `/searches/register`                                                                | JSON ([Register][register_model])       | Register **Search** query
| `GET`  | `/searches/list`                                                                    | JSON ([Infos][infos_model])             | Return list of **Search** entries with `Mosaic` type

### Tiles

`:endpoint:/searches/{search_id}/tiles[/{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]`

- PathParams:
    - **search_id**: PgSTAC Search Identifier (Hash).
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
    - **asset_bidx** (array[str]): Per asset band index (e.g `Asset1|1;2;3`).
    - **nodata**: Overwrite internal Nodata value. OPTIONAL
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **reproject** (str): WarpKernel resampling algorithm (only used when doing re-projection). Defaults to `nearest`.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.
    - **buffer** (float): Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).
    - **padding** (int): Padding to apply to each tile edge. Helps reduce resampling artefacts along edges. Defaults to `0`
    - **pixel_selection** (str): Pixel selection method (https://cogeotiff.github.io/rio-tiler/mosaic/).
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/1/2/3?assets=B01`
- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/1/2/3.jpg?assets=B01`
- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/WorldCRS84Quad/1/2/3@2x.png?assets=B01&assets=B02&assets=B03`
- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/WorldCRS84Quad/1/2/3?assets=B01&rescale=0,1000&colormap_name=cfastie`

### TilesJSON

`:endpoint:/searches/{search_id}[/{TileMatrixSetId}]/tilejson.json`

- PathParams:
    - **search_id**: PgSTAC Search Identifier (Hash).
    - **TileMatrixSetId**: TileMatrixSet name, default is `WebMercatorQuad`. OPTIONAL

- QueryParams:
    - **tile_format**: Output image format, default is set to None and will be either JPEG or PNG depending on masked value.
    - **tile_scale**: Tile size scale, default is set to 1 (256x256). OPTIONAL
    - **minzoom**: Overwrite default minzoom. OPTIONAL
    - **maxzoom**: Overwrite default maxzoom. OPTIONAL
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band index (e.g `Asset1|1;2;3`).
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **reproject** (str): WarpKernel resampling algorithm (only used when doing re-projection). Defaults to `nearest`.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.
    - **buffer** (float): Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).
    - **padding** (int): Padding to apply to each tile edge. Helps reduce resampling artefacts along edges. Defaults to `0`
    - **pixel_selection** (str): Pixel selection method (https://cogeotiff.github.io/rio-tiler/mosaic/).
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/tilejson.json?assets=B01`
- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/tilejson.json?assets=B01&tile_format=png`
- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/WorldCRS84Quad/tilejson.json?assets=B01&tile_scale=2`


### WMTS

`:endpoint:/searches/{search_id}[/{TileMatrixSetId}]/WMTSCapabilities.xml`

- PathParams:
    - **search_id**: PgSTAC Search Identifier (Hash).
    - **TileMatrixSetId**: TileMatrixSet name, default is `WebMercatorQuad`. OPTIONAL

- QueryParams:
    - **tile_format**: Output image format, default is set to PNG.
    - **tile_scale**: Tile size scale, default is set to 1 (256x256). OPTIONAL
    - **minzoom**: Overwrite default minzoom. OPTIONAL
    - **maxzoom**: Overwrite default maxzoom. OPTIONAL


!!! important
    additional query-parameters will be forwarded to the `tile` URL. If no `defaults` mosaic metadata, **assets** OR **expression** will be required

Example:

- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/WMTSCapabilities.xml?assets=B01`
- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/WMTSCapabilities.xml?assets=B01&tile_format=png`
- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/WorldCRS84Quad/WMTSCapabilities.xml?assets=B01&tile_scale=2`


### Assets

`:endpoint:/searches/{search_id}/tiles/[{TileMatrixSetId}]/{z}/{x}/{y}/assets`

- PathParams:
    - **search_id**: PgSTAC Search Identifier (Hash).
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

- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/tiles/0/0/0/assets`

`:endpoint:/searches/{search_id}/{lon},{lat}/assets`

- PathParams:
    - **search_id**: PgSTAC Search Identifier (Hash).
    - **lon**: Longitude (in WGS84 CRS).
    - **lat**: Latitude (in WGS84 CRS).

- QueryParams:
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

Example:

- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/0.0,0.0/assets`

### Statistics

`:endpoint:/searches/{search_id}/statistics - [POST]`

- Body:
    - **feature** (JSON): A valid GeoJSON feature or FeatureCollection

- PathParams:
    - **search_id**: PgSTAC Search Identifier (Hash).

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band index (e.g `Asset1|1;2;3`).
    - **coord_crs** (str): Coordinate Reference System of the input geometry. Default to `epsg:4326`.
    - **dst_crs** (str): Output Coordinate Reference System. Default to `coord_crs`.
    - **max_size** (int): Max image size from which to calculate statistics.
    - **height** (int): Force image height from which to calculate statistics.
    - **width** (int): Force image width from which to calculate statistics.
    - **nodata**: Overwrite internal Nodata value. OPTIONAL
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **reproject** (str): WarpKernel resampling algorithm (only used when doing re-projection). Defaults to `nearest`.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.
    - **categorical** (bool): Return statistics for categorical dataset, default is false.
    - **c** (array[float]): Pixels values for categories.
    - **p** (array[int]): Percentile values.
    - **histogram_bins** (str): Histogram bins.
    - **histogram_range** (str): Comma (',') delimited Min,Max histogram bounds.
    - **pixel_selection** (str): Pixel selection method (https://cogeotiff.github.io/rio-tiler/mosaic/).
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

!!! important
    if **height** and **width** are provided **max_size** will be ignored.

Example:

- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/statistics?assets=B01`

### BBOX/Feature

`:endpoint:/searches/{search_id}/bbox/{minx},{miny},{maxx},{maxy}.{format}`

`:endpoint:/searches/{search_id}/bbox/{minx},{miny},{maxx},{maxy}/{width}x{height}.{format}`

- PathParams:
    - **search_id**: PgSTAC Search Identifier (Hash).
    - **minx,miny,maxx,maxy** (str): Comma (',') delimited bounding box in WGS84.
    - **format** (str): Output image format.
    - **height** (int): Force output image height.
    - **width** (int): Force output image width.

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band index (e.g `Asset1|1;2;3`).
    - **coord_crs** (str): Coordinate Reference System of the input coordinates. Default to `epsg:4326`.
    - **dst_crs** (str): Output Coordinate Reference System. Default to `coord_crs`.
    - **max_size** (int): Max image size.
    - **nodata**: Overwrite internal Nodata value. OPTIONAL
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **reproject** (str): WarpKernel resampling algorithm (only used when doing re-projection). Defaults to `nearest`.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.
    - **pixel_selection** (str): Pixel selection method (https://cogeotiff.github.io/rio-tiler/mosaic/).
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

!!! important
    if **height** and **width** are provided **max_size** will be ignored.

Example:

- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/bbox/0,0,10,10.png?assets=B01`
- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/bbox/0,0,10,10/400x300.png?assets=B01`


`:endpoint:/searches/{search_id}/feature[/{width}x{height}][].{format}] - [POST]`

- Body:
    - **feature** (JSON): A valid GeoJSON feature (Polygon or MultiPolygon)

- PathParams:
    - **search_id**: PgSTAC Search Identifier (Hash).
    - **height** (int): Force output image height. **Optional**
    - **width** (int): Force output image width. **Optional**
    - **format** (str): Output image format, default is set to None and will be either JPEG or PNG depending on masked value. **Optional**

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band index (e.g `Asset1|1;2;3`).
    - **coord_crs** (str): Coordinate Reference System of the input geometry. Default to `epsg:4326`.
    - **dst_crs** (str): Output Coordinate Reference System. Default to `coord_crs`.
    - **max_size** (int): Max image size.
    - **nodata**: Overwrite internal Nodata value. OPTIONAL
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **reproject** (str): WarpKernel resampling algorithm (only used when doing re-projection). Defaults to `nearest`.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.
    - **pixel_selection** (str): Pixel selection method (https://cogeotiff.github.io/rio-tiler/mosaic/).
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

!!! important
    if **height** and **width** are provided **max_size** will be ignored.

Example:

- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/feature?assets=B01`
- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/feature.png?assets=B01f`
- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/feature/100x100.png?assets=B01`

### Point

`:endpoint:/searches/{search_id}/point/{lon},{lat}`

- PathParams:
    - **search_id**: PgSTAC Search Identifier (Hash).
    - **lon**: Longitude (in `coord-crs`, defaults to `WGS84`).
    - **lat**: Latitude (in `coord-crs`, defaults to `WGS84`).

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band index (e.g `Asset1|1;2;3`).
    - **coord_crs** (str): Coordinate Reference System of the input geometry. Default to `epsg:4326`.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **reproject** (str): WarpKernel resampling algorithm (only used when doing re-projection). Defaults to `nearest`.
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/searches/f1ed59f0a6ad91ed80ae79b7b52bc707/point/0,0?assets=B01`

### Register a Search Request

`:endpoint:/searches/register - [POST]`

- **Body** (a combination of Search+Metadata): A JSON body composed of a valid **STAC Search** query (see: https://github.com/radiantearth/stac-api-spec/tree/master/item-search) and Mosaic's metadata.

```json
// titiler-pgstac search body example
{
  // STAC search query
  "collections": [
    "string"
  ],
  "ids": [
    "string"
  ],
  "bbox": [
    "number",
    "number",
    "number",
    "number"
  ],
  "intersects": {
    "type": "Point",
    "coordinates": [
      "number",
      "number"
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
  // titiler-pgstac mosaic metadata
  "metadata": {
    "type": "mosaic",
    "bounds": [
      "number",
      "number",
      "number",
      "number"
    ],
    "minzoom": "number",
    "maxzoom": "number",
    "name": "string",
    "assets": [
      "string",
      "string",
    ],
    "defaults": {}
  }
}
```

!!! important
    In `titiler-pgstac` we extended the regular `stac` search to add a metadata entry.
    Metadata defaults to `{"type": "mosaic"}`.

Example:

- `https://myendpoint/searches/register`

```bash
curl -X 'POST' 'http://127.0.0.1:8081/searches/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"collections":["landsat-c2l2-sr"], "bbox":[-123.75,34.30714385628804,-118.125,38.82259097617712], "filter-lang": "cql-json"}' | jq
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

# or using CQL2
curl -X 'POST' 'http://127.0.0.1:8081/searches/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"filter": {"op": "=", "args": [{"property": "collection"}, "landsat-c2l2-sr"]}}'

# or using CQL2 with metadata
curl -X 'POST' 'http://127.0.0.1:8081/searches/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"filter": {"op": "=", "args": [{"property": "collection"}, "landsat-c2l2-sr"]}, "metadata": {"name": "landsat mosaic"}}'
```

### Search infos

`:endpoint:/searches/{search_id}/info - [GET]`

- PathParams:
    - **search_id**: PgSTAC Search Identifier (Hash).

Example:

- `https://myendpoint/searches/5a1b82d38d53a5d200273cbada886bd7/info`

```bash
curl 'http://127.0.0.1:8081/searches/5a1b82d38d53a5d200273cbada886bd7/info' | jq
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
      "href": "http://127.0.0.1:8081/searches/5a1b82d38d53a5d200273cbada886bd7/info"
    },
    {
      "rel": "tilejson",
      "type": "application/json",
      "href": "http://127.0.0.1:8081/searches/5a1b82d38d53a5d200273cbada886bd7/tilejson.json"
    }
  ]
}
```

### List Searches

`:endpoint:/searches/list - [GET]`

- QueryParams:
    - **limit** (int): Page size limit, Default is `10`.
    - **offset** (int): Page offset.
    - **sortby** (str): Sort the searches by Metadata properties (ascending (default) or descending (`-`)).

!!! Important
    Additional query-parameters (form `PROP=VALUE`) will be considered as a **property filter**.

Example:

- `https://myendpoint/searches/list`
- `https://myendpoint/searches/list?limit=100`
- `https://myendpoint/searches/list?limit=10&offset=10` (page 2)
- `https://myendpoint/searches/list?data=noaa` (only show mosaics with `metadata.data == noaa`)
- `https://myendpoint/searches/list?sortby=lastused` (sort mosaic by `lastused` pgstac search property)
- `https://myendpoint/searches/list?sortby=-prop` (sort mosaic (descending) by `metadata.prop` values)



[tilejson_model]: https://github.com/developmentseed/titiler/blob/2335048a407f17127099cbbc6c14e1328852d619/src/titiler/core/titiler/core/models/mapbox.py#L16-L38
[info_model]: https://github.com/stac-utils/titiler-pgstac/blob/047315da8851a974660032ca45f219db2c3a8d54/titiler/pgstac/model.py#L236-L240
[infos_model]: https://github.com/stac-utils/titiler-pgstac/blob/4f569fee1946f853be9b9149cb4dd2fd5c62b110/titiler/pgstac/model.py#L260-L265
[register_model]: https://github.com/stac-utils/titiler-pgstac/blob/047315da8851a974660032ca45f219db2c3a8d54/titiler/pgstac/model.py#L229-L233
[statitics_model]: https://github.com/developmentseed/titiler/blob/17cdff2f0ddf08dbd9a47c2140b13c4bbcc30b6d/src/titiler/core/titiler/core/models/responses.py#L49-L52
[point_model]: https://github.com/developmentseed/titiler/blob/e396959e7f818909a5494301a809b5f795aa202e/src/titiler/mosaic/titiler/mosaic/models/responses.py#L8-L17
