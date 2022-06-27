The `titiler.pgstac` package comes with a full FastAPI application with Mosaic and single STAC item support.

The `Item` endpoints are created using TiTiler's [MultiBaseTilerFactory](https://developmentseed.org/titiler/advanced/tiler_factories/#titilercorefactorymultibasetilerfactory)

| Method | URL                                                                  | Output                                           | Description
| ------ | -------------------------------------------------------------------- |------------------------------------------------- |--------------
| `GET`  | `/stac/bounds`                                                       | JSON ([Bounds][bounds_model])                    | return dataset's bounds
| `GET`  | `/stac/assets`                                                       | JSON                                             | return the list of available assets
| `GET`  | `/stac/info`                                                         | JSON ([Info][multiinfo_model])                   | return assets basic info
| `GET`  | `/stac/info.geojson`                                                 | GeoJSON ([InfoGeoJSON][multiinfo_geojson_model]) | return assets basic info as a GeoJSON feature
| `GET`  | `/stac/asset_statistics`                                             | JSON ([Statistics][multistats_model])            | return per asset statistics
| `GET`  | `/stac/statistics`                                                   | JSON ([Statistics][stats_model])                 | return assets statistics (merged)
| `POST` | `/stac/statistics`                                                   | GeoJSON ([Statistics][multistats_geojson_model]) | return assets statistics for a GeoJSON (merged)
| `GET`  | `/stac/tiles/[{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]`  | image/bin                                        | create a web map tile image from assets
| `GET`  | `/stac/[{TileMatrixSetId}]/tilejson.json`                            | JSON ([TileJSON][tilejson_model])                | return a Mapbox TileJSON document
| `GET`  | `/stac/{TileMatrixSetId}/WMTSCapabilities.xml`                       | XML                                              | return OGC WMTS Get Capabilities
| `GET`  | `/stac/point/{lon},{lat}`                                            | JSON ([Point][multipoint_model])                 | return pixel values from assets
| `GET`  | `/stac/preview[.{format}]`                                           | image/bin                                        | create a preview image from assets
| `GET`  | `/stac/crop/{minx},{miny},{maxx},{maxy}[/{width}x{height}].{format}` | image/bin                                        | create an image from part of assets
| `POST` | `/stac/crop[/{width}x{height}][.{format}]`                           | image/bin                                        | create an image from a geojson feature intersecting assets

### Tiles

`:endpoint:/stac/tiles/[{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]`

- PathParams:
    - **TileMatrixSetId** (str): TileMatrixSet name, default is `WebMercatorQuad`. **Optional**
    - **z** (int): TMS tile's zoom level.
    - **x** (int): TMS tile's column.
    - **y** (int): TMS tile's row.
    - **scale** (int): Tile size scale, default is set to 1 (256x256). **Optional**
    - **format** (str): Output image format, default is set to None and will be either JPEG or PNG depending on masked value. **Optional**

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1/Asset2`).
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.
    - **buffer** (float): Add buffer on each side of the tile (e.g 0.5 = 257x257, 1.0 = 258x258).

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/stac/tiles/1/2/3?collection=mycollection&item=oneitem&assets=B01&assets=B00`
- `https://myendpoint/stac/tiles/1/2/3.jpg?collection=mycollection&item=oneitem&assets=B01`
- `https://myendpoint/stac/tiles/WorldCRS84Quad/1/2/3@2x.png?collection=mycollection&item=oneitem&assets=B01`
- `https://myendpoint/stac/tiles/WorldCRS84Quad/1/2/3?collection=mycollection&item=oneitem&expression=B01/B02&rescale=0,1000&colormap_name=cfastie`

### Preview

`:endpoint:/stac/preview[.{format}]`

- PathParams:
    - **format**: Output image format, default is set to None and will be either JPEG or PNG depending on masked value. **Optional**

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1/Asset2`).
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **max_size** (int): Max image size, default is 1024.
    - **height** (int): Force output image height.
    - **width** (int): Force output image width.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.

!!! important
    - **assets** OR **expression** is required

    - if **height** and **width** are provided **max_size** will be ignored.

Example:

- `https://myendpoint/stac/preview?url=https://somewhere.com/item.json&assets=B01`
- `https://myendpoint/stac/preview.jpg?url=https://somewhere.com/item.json&assets=B01`
- `https://myendpoint/stac/preview?url=https://somewhere.com/item.json&assets=B01&rescale=0,1000&colormap_name=cfastie`

### Crop / Part

`:endpoint:/stac/crop/{minx},{miny},{maxx},{maxy}.{format}`
`:endpoint:/stac/crop/{minx},{miny},{maxx},{maxy}/{width}x{height}.{format}`

- PathParams:
    - **minx,miny,maxx,maxy** (str): Comma (',') delimited bounding box in WGS84.
    - **height** (int): Force output image height. **Optional**
    - **width** (int): Force output image width. **Optional**
    - **format** (str): Output image format, default is set to None and will be either JPEG or PNG depending on masked value. **Optional**

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1/Asset2`).
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **max_size** (int): Max image size, default is 1024.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.

!!! important
    - **assets** OR **expression** is required

    - if **height** and **width** are provided **max_size** will be ignored.

Example:

- `https://myendpoint/stac/crop/0,0,10,10.png?url=https://somewhere.com/item.json&assets=B01`
- `https://myendpoint/stac/crop/0,0,10,10.png?url=https://somewhere.com/item.json&assets=B01&rescale=0,1000&colormap_name=cfastie`

`:endpoint:/stac/crop[/{width}x{height}][].{format}] - [POST]`

- Body:
    - **feature** (JSON): A valid GeoJSON feature (Polygon or MultiPolygon)

- PathParams:
    - **height** (int): Force output image height. **Optional**
    - **width** (int): Force output image width. **Optional**
    - **format** (str): Output image format, default is set to None and will be either JPEG or PNG depending on masked value. **Optional**

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1/Asset2`).
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **max_size** (int): Max image size, default is 1024.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.

!!! important
    - **assets** OR **expression** is required

    - if **height** and **width** are provided **max_size** will be ignored.

Example:

- `https://myendpoint/stac/crop?url=https://somewhere.com/item.json&assets=B01`
- `https://myendpoint/stac/crop.png?url=https://somewhere.com/item.json&assets=B01`
- `https://myendpoint/stac/crop/100x100.png?url=https://somewhere.com/item.json&assets=B01&rescale=0,1000&colormap_name=cfastie`

### Point

`:endpoint:/cog/point/{lon},{lat}`

- PathParams:
    - **lon,lat,** (str): Comma (',') delimited point Longitude and Latitude WGS84.

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1/Asset2`).
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/stac/point/0,0?url=https://somewhere.com/item.json&assets=B01`

### TilesJSON

`:endpoint:/stac/[{TileMatrixSetId}]/tilejson.json` tileJSON document

- PathParams:
    - **TileMatrixSetId**: TileMatrixSet name, default is `WebMercatorQuad`.

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1/Asset2`).
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **tile_format** (str): Output image format, default is set to None and will be either JPEG or PNG depending on masked value.
    - **tile_scale** (int): Tile size scale, default is set to 1 (256x256).
    - **minzoom** (int): Overwrite default minzoom.
    - **maxzoom** (int): Overwrite default maxzoom.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **rescale** (array[str]): Comma (',') delimited Min,Max range (e.g `rescale=0,1000`, `rescale=0,1000&rescale=0,3000&rescale=0,2000`).
    - **color_formula** (str): rio-color formula.
    - **colormap** (str): JSON encoded custom Colormap.
    - **colormap_name** (str): rio-tiler color map name.
    - **return_mask** (bool): Add mask to the output data. Default is True.
    - **buffer** (float): Add buffer on each side of the tile (e.g 0.5 = 257x257, 1.0 = 258x258).

!!! important
    **assets** OR **expression** is required

Example:

- `https://myendpoint/stac/tilejson.json?url=https://somewhere.com/item.json&assets=B01`
- `https://myendpoint/stac/tilejson.json?url=https://somewhere.com/item.json&assets=B01&tile_format=png`
- `https://myendpoint/stac/WorldCRS84Quad/tilejson.json?url=https://somewhere.com/item.json&tile_scale=2&expression=B01/B02`

### Bounds

`:endpoint:/stac/bounds` - Return the bounds of the STAC item.

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**

Example:

- `https://myendpoint/stac/bounds?url=https://somewhere.com/item.json`


### Info

`:endpoint:/stac/info` - Return basic info on STAC item's COG.

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**
    - **assets** (array[str]): asset names. Default to all available assets.

Example:

- `https://myendpoint/stac/info?url=https://somewhere.com/item.json&assets=B01`

`:endpoint:/stac/info.geojson` - Return basic info on STAC item's COG as a GeoJSON feature

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**
    - **assets** (array[str]): asset names. Default to all available assets.

Example:

- `https://myendpoint/stac/info.geojson?url=https://somewhere.com/item.json&assets=B01`


`:endpoint:/stac/assets` - Return the list of available assets

Example:

- `https://myendpoint/stac/assets?url=https://somewhere.com/item.json`

### Statistics

`:endpoint:/stac/asset_statistics - [GET]`

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**
    - **assets** (array[str]): asset names. Default to all available assets.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **max_size** (int): Max image size from which to calculate statistics, default is 1024.
    - **height** (int): Force image height from which to calculate statistics.
    - **width** (int): Force image width from which to calculate statistics.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **categorical** (bool): Return statistics for categorical dataset, default is false.
    - **c** (array[float]): Pixels values for categories.
    - **p** (array[int]): Percentile values.
    - **histogram_bins** (str): Histogram bins.
    - **histogram_range** (str): Comma (',') delimited Min,Max histogram bounds

Example:

- `https://myendpoint/stac/statistics?url=https://somewhere.com/item.json&assets=B01&categorical=true&c=1&c=2&c=3&p=2&p98`


`:endpoint:/stac/statistics - [GET]`

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**
    - **assets** (array[str]): asset names. Default to all available assets.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1/Asset2`).
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **max_size** (int): Max image size from which to calculate statistics, default is 1024.
    - **height** (int): Force image height from which to calculate statistics.
    - **width** (int): Force image width from which to calculate statistics.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **categorical** (bool): Return statistics for categorical dataset, default is false.
    - **c** (array[float]): Pixels values for categories.
    - **p** (array[int]): Percentile values.
    - **histogram_bins** (str): Histogram bins.
    - **histogram_range** (str): Comma (',') delimited Min,Max histogram bounds

Example:

- `https://myendpoint/stac/statistics?url=https://somewhere.com/item.json&assets=B01&categorical=true&c=1&c=2&c=3&p=2&p98`


`:endpoint:/stac/statistics - [POST]`

- Body:
    - **feature** (JSON): A valid GeoJSON feature or FeatureCollection

- QueryParams:
    - **collection** (str): STAC Collection ID. **Required**
    - **item** (str): STAC Item ID. **Required**
    - **assets** (array[str]): asset names. Default to all available assets.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **asset_expression** (array[str]): Per asset band math expression (e.g `Asset1|b1\*b2`).
    - **max_size** (int): Max image size from which to calculate statistics, default is 1024.
    - **height** (int): Force image height from which to calculate statistics.
    - **width** (int): Force image width from which to calculate statistics.
    - **nodata** (str, int, float): Overwrite internal Nodata value.
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): rasterio resampling method. Default is `nearest`.
    - **categorical** (bool): Return statistics for categorical dataset, default is false.
    - **c** (array[float]): Pixels values for categories.
    - **p** (array[int]): Percentile values.
    - **histogram_bins** (str): Histogram bins.
    - **histogram_range** (str): Comma (',') delimited Min,Max histogram bounds

Example:

- `https://myendpoint/stac/statistics?url=https://somewhere.com/item.json&assets=B01&categorical=true&c=1&c=2&c=3&p=2&p98`


[bounds_model]: https://github.com/cogeotiff/rio-tiler/blob/9aaa88000399ee8d36e71d176f67b6ea3ec53f2d/rio_tiler/models.py#L43-L46
[tilejson_model]: https://github.com/developmentseed/titiler/blob/2335048a407f17127099cbbc6c14e1328852d619/src/titiler/core/titiler/core/models/mapbox.py#L16-L38
[stats_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L32
[multiinfo_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L52
[multiinfo_geojson_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L53
[multipoint_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L23-L27
[multistats_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L55
[multistats_geojson_model]: https://github.com/developmentseed/titiler/blob/c97e251c46b51703d41b1c9e66bc584649aa231c/src/titiler/core/titiler/core/models/responses.py#L56-L59
