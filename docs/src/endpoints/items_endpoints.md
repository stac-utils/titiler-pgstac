### STAC Items endpoints

The `Item` endpoints are created using TiTiler's [MultiBaseTilerFactory](https://developmentseed.org/titiler/advanced/tiler_factories/#titilercorefactorymultibasetilerfactory)

| Method | URL                                                                  | Output                                           | Description
| ------ | -------------------------------------------------------------------- |------------------------------------------------- |--------------
| `GET`  | `/collections/{collection_id}/items/{item_id}/bounds`                                                       | JSON ([Bounds][bounds_model])                    | return dataset's bounds
| `GET`  | `/collections/{collection_id}/items/{item_id}/assets`                                                       | JSON                                             | return the list of available assets
| `GET`  | `/collections/{collection_id}/items/{item_id}/info`                                                         | JSON ([Info][multiinfo_model])                   | return assets basic info
| `GET`  | `/collections/{collection_id}/items/{item_id}/info.geojson`                                                 | GeoJSON ([InfoGeoJSON][multiinfo_geojson_model]) | return assets basic info as a GeoJSON feature
| `GET`  | `/collections/{collection_id}/items/{item_id}/asset_statistics`                                             | JSON ([Statistics][multistats_model])            | return per asset statistics
| `GET`  | `/collections/{collection_id}/items/{item_id}/statistics`                                                   | JSON ([Statistics][stats_model])                 | return assets statistics (merged)
| `POST` | `/collections/{collection_id}/items/{item_id}/statistics`                                                   | GeoJSON ([Statistics][multistats_geojson_model]) | return assets statistics for a GeoJSON (merged)
| `GET`  | `/collections/{collection_id}/items/{item_id}/tiles[/{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]`  | image/bin                                        | create a web map tile image from assets
| `GET`  | `/collections/{collection_id}/items/{item_id}[/{TileMatrixSetId}]/tilejson.json`                            | JSON ([TileJSON][tilejson_model])                | return a Mapbox TileJSON document
| `GET`  | `/collections/{collection_id}/items/{item_id}[/{TileMatrixSetId}]/WMTSCapabilities.xml`                     | XML                                              | return OGC WMTS Get Capabilities
| `GET`  | `/collections/{collection_id}/items/{item_id}[/{TileMatrixSetId}]/map`                                      | HTML                                             | simple map viewer
| `GET`  | `/collections/{collection_id}/items/{item_id}/point/{lon},{lat}`                                            | JSON ([Point][multipoint_model])                 | return pixel values from assets
| `GET`  | `/collections/{collection_id}/items/{item_id}/preview[.{format}]`                                           | image/bin                                        | create a preview image from assets
| `GET`  | `/collections/{collection_id}/items/{item_id}/bbox/{minx},{miny},{maxx},{maxy}[/{width}x{height}].{format}` | image/bin                                        | create an image from part of assets
| `POST` | `/collections/{collection_id}/items/{item_id}/feature[/{width}x{height}][.{format}]`                        | image/bin                                        | create an image from a geojson feature intersecting assets

### Tiles

`:endpoint:/collections/{collection_id}/items/{item_id}/tiles[/{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]`

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.
    - **TileMatrixSetId** (str): TileMatrixSet name, default is `WebMercatorQuad`. **Optional**
    - **z** (int): TMS tile's zoom level.
    - **x** (int): TMS tile's column.
    - **y** (int): TMS tile's row.
    - **scale** (int): Tile size scale, default is set to 1 (256x256). **Optional**
    - **format** (str): Output image format, default is set to None and will be either JPEG or PNG depending on masked value. **Optional**

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
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
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/tiles/1/2/3?assets=B01&assets=B00`
- `https://myendpoint/collections/mycollection/items/oneitem/tiles/1/2/3.jpg?assets=B01`
- `https://myendpoint/collections/mycollection/items/oneitem/tiles/WorldCRS84Quad/1/2/3@2x.png?assets=B01`
- `https://myendpoint/collections/mycollection/items/oneitem/tiles/WorldCRS84Quad/1/2/3?expression=B01/B02&rescale=0,1000&colormap_name=cfastie&asset_as_band=True`

### Preview

`:endpoint:/collections/{collection_id}/items/{item_id}/preview[.{format}]`

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.
    - **format**: Output image format, default is set to None and will be either JPEG or PNG depending on masked value. **Optional**

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **max_size** (int): Max image size, default is 1024.
    - **height** (int): Force output image height.
    - **width** (int): Force output image width.
    - **dst_crs** (str): Output Coordinate Reference System. Default to dataset's CRS.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **reproject** (str): WarpKernel resampling algorithm (only used when doing re-projection). Defaults to `nearest`.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.

!!! important
    - **assets** OR **expression** is required

    - if **height** and **width** are provided **max_size** will be ignored.

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/preview?assets=B01`
- `https://myendpoint/collections/mycollection/items/oneitem/preview.jpg?assets=B01`
- `https://myendpoint/collections/mycollection/items/oneitem/preview?assets=B01&rescale=0,1000&colormap_name=cfastie`

### BBOX/Feature

`:endpoint:/collections/{collection_id}/items/{item_id}/bbox/{minx},{miny},{maxx},{maxy}.{format}`
`:endpoint:/collections/{collection_id}/items/{item_id}/bbox/{minx},{miny},{maxx},{maxy}/{width}x{height}.{format}`

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.
    - **minx,miny,maxx,maxy** (str): Comma (',') delimited bounding box in WGS84.
    - **height** (int): Force output image height. **Optional**
    - **width** (int): Force output image width. **Optional**
    - **format** (str): Output image format, default is set to None and will be either JPEG or PNG depending on masked value. **Optional**

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **max_size** (int): Max image size.
    - **coord_crs** (str): Coordinate Reference System of the input coordinates. Default to `epsg:4326`.
    - **dst_crs** (str): Output Coordinate Reference System. Default to `coord_crs`.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **reproject** (str): WarpKernel resampling algorithm (only used when doing re-projection). Defaults to `nearest`.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.

!!! important
    - **assets** OR **expression** is required

    - if **height** and **width** are provided **max_size** will be ignored.

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/bbox/0,0,10,10.png?assets=B01`
- `https://myendpoint/collections/mycollection/items/oneitem/bbox/0,0,10,10.png?assets=B01&rescale=0,1000&colormap_name=cfastie`

`:endpoint:/collections/{collection_id}/items/{item_id}/feature[/{width}x{height}][].{format}] - [POST]`

- Body:
    - **feature** (JSON): A valid GeoJSON feature (Polygon or MultiPolygon)

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.
    - **height** (int): Force output image height. **Optional**
    - **width** (int): Force output image width. **Optional**
    - **format** (str): Output image format, default is set to None and will be either JPEG or PNG depending on masked value. **Optional**

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **max_size** (int): Max image size.
    - **coord_crs** (str): Coordinate Reference System of the input coordinates. Default to `epsg:4326`.
    - **dst_crs** (str): Output Coordinate Reference System. Default to `coord_crs`.
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
    - **algorithm** (str): Custom algorithm name (e.g `hillshade`).
    - **algorithm_params** (str): JSON encoded algorithm parameters.

!!! important
    - **assets** OR **expression** is required

    - if **height** and **width** are provided **max_size** will be ignored.

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/crop?assets=B01`
- `https://myendpoint/collections/mycollection/items/oneitem/crop.png?assets=B01`
- `https://myendpoint/collections/mycollection/items/oneitem/100x100.png?assets=B01&rescale=0,1000&colormap_name=cfastie`

### Point

`:endpoint:/collections/{collection_id}/items/{item_id}/point/{lon},{lat}`

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.
    - **lon,lat,** (str): Comma (',') delimited point Longitude and Latitude WGS84.

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **reproject** (str): WarpKernel resampling algorithm (only used when doing re-projection). Defaults to `nearest`.

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/point/0,0?assets=B01`

### TilesJSON

`:endpoint:/collections/{collection_id}/items/{item_id}[/{TileMatrixSetId}]/tilejson.json` tileJSON document

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.
    - **TileMatrixSetId**: TileMatrixSet name, default is `WebMercatorQuad`.

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **tile_format** (str): Output image format, default is set to None and will be either JPEG or PNG depending on masked value.
    - **tile_scale** (int): Tile size scale, default is set to 1 (256x256).
    - **minzoom** (int): Overwrite default minzoom.
    - **maxzoom** (int): Overwrite default maxzoom.
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

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/tilejson.json?assets=B01`
- `https://myendpoint/collections/mycollection/items/oneitem/tilejson.json?assets=B01&tile_format=png`
- `https://myendpoint/collections/mycollection/items/oneitem/WorldCRS84Quad/tilejson.json?tile_scale=2&expression=B01/B02&asset_as_band=True`

### Bounds

`:endpoint:/collections/{collection_id}/items/{item_id}/bounds` - Return the bounds of the STAC item.

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/bounds`


### Info

`:endpoint:/collections/{collection_id}/items/{item_id}/info` - Return basic info on STAC item's COG.

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.

- QueryParams:
    - **assets** (array[str]): asset names. Default to all available assets.

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/info?assets=B01`

`:endpoint:/collections/{collection_id}/items/{item_id}/info.geojson` - Return basic info on STAC item's COG as a GeoJSON feature

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.

- QueryParams:
    - **collection** (str): STAC Collection Identifier. **Required**
    - **item** (str): STAC Item Identifier. **Required**
    - **assets** (array[str]): asset names. Default to all available assets.

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/info.geojson?assets=B01`


`:endpoint:/collections/{collection_id}/items/{item_id}/assets` - Return the list of available assets


### Available Assets

`:endpoint:/collections/{collection_id}/items/{item_id}/assets` - Return a list of available assets

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/assets`

### Statistics

`:endpoint:/collections/{collection_id}/items/{item_id}/asset_statistics - [GET]`

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.

- QueryParams:
    - **collection** (str): STAC Collection Identifier. **Required**
    - **item** (str): STAC Item Identifier. **Required**
    - **assets** (array[str]): asset names. Default to all available assets.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **max_size** (int): Max image size from which to calculate statistics, default is 1024.
    - **height** (int): Force image height from which to calculate statistics.
    - **width** (int): Force image width from which to calculate statistics.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **categorical** (bool): Return statistics for categorical dataset, default is false.
    - **c** (array[float]): Pixels values for categories.
    - **p** (array[int]): Percentile values.
    - **histogram_bins** (str): Histogram bins.
    - **histogram_range** (str): Comma (',') delimited Min,Max histogram bounds

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/statistics?assets=B01&categorical=true&c=1&c=2&c=3&p=2&p98`


`:endpoint:/collections/{collection_id}/items/{item_id}/statistics - [GET]`

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.

- QueryParams:
    - **collection** (str): STAC Collection Identifier. **Required**
    - **item** (str): STAC Item Identifier. **Required**
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **max_size** (int): Max image size from which to calculate statistics, default is 1024.
    - **height** (int): Force image height from which to calculate statistics.
    - **width** (int): Force image width from which to calculate statistics.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **categorical** (bool): Return statistics for categorical dataset, default is false.
    - **c** (array[float]): Pixels values for categories.
    - **p** (array[int]): Percentile values.
    - **histogram_bins** (str): Histogram bins.
    - **histogram_range** (str): Comma (',') delimited Min,Max histogram bounds

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/statistics?assets=B01&categorical=true&c=1&c=2&c=3&p=2&p98`


`:endpoint:/collections/{collection_id}/items/{item_id}/statistics - [POST]`

- Body:
    - **feature** (JSON): A valid GeoJSON feature or FeatureCollection

- PathParams:
    - **collection_id** (str): STAC Collection Identifier.
    - **item_id** (str): STAC Item Identifier.

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **max_size** (int): Max image size from which to calculate statistics.
    - **height** (int): Force image height from which to calculate statistics.
    - **width** (int): Force image width from which to calculate statistics.
    - **coord_crs** (str): Coordinate Reference System of the input coordinates. Default to `epsg:4326`.
    - **dst_crs** (str): Output Coordinate Reference System. Default to `coord_crs`.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
    - **reproject** (str): WarpKernel resampling algorithm (only used when doing re-projection). Defaults to `nearest`.
    - **categorical** (bool): Return statistics for categorical dataset, default is false.
    - **c** (array[float]): Pixels values for categories.
    - **p** (array[int]): Percentile values.
    - **histogram_bins** (str): Histogram bins.
    - **histogram_range** (str): Comma (',') delimited Min,Max histogram bounds

Example:

- `https://myendpoint/collections/mycollection/items/oneitem/statistics?assets=B01&categorical=true&c=1&c=2&c=3&p=2&p98`


[bounds_model]: https://github.com/cogeotiff/rio-tiler/blob/9aaa88000399ee8d36e71d176f67b6ea3ec53f2d/rio_tiler/models.py#L43-L46
[tilejson_model]: https://github.com/developmentseed/titiler/blob/2335048a407f17127099cbbc6c14e1328852d619/src/titiler/core/titiler/core/models/mapbox.py#L16-L38
[stats_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L32
[multiinfo_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L52
[multiinfo_geojson_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L53
[multipoint_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L23-L27
[multistats_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L55
[multistats_geojson_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L56-L59
