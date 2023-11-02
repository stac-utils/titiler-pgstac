
### STAC Collections endpoints


| Method | URL                                                                              | Output                                  | Description
| ------ | ---------------------------------------------------------------------------------|-----------------------------------------|--------------
| `GET`  | `/collections/{collection_id}/{lon},{lat}/assets`                                          | JSON                                    | Return a list of assets which overlap a given point
| `GET`  | `/collections/{collection_id}/tiles[/{TileMatrixSetId}]/{z}/{x}/{Y}/assets`                | JSON                                    | Return a list of assets which overlap a given tile
| `GET`  | `/collections/{collection_id}/tiles[/{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]` | image/bin                               | Create a web map tile image for a collection and a tile index
| `GET`  | `/collections/{collection_id}[/{TileMatrixSetId}]/tilejson.json`                           | JSON ([TileJSON][tilejson_model])       | Return a Mapbox TileJSON document
| `GET`  | `/collections/{collection_id}[/{TileMatrixSetId}]/WMTSCapabilities.xml`                    | XML                                     | return OGC WMTS Get Capabilities
| `GET`  | `/collections/{collection_id}[/{TileMatrixSetId}]/map`                                     | HTML                                    | simple map viewer
| `POST` | `/collections/{collection_id}/statistics`                                                  | GeoJSON ([Statistics][statitics_model]) | Return statistics for geojson features
| `GET`  | `/collections/{collection_id}/bbox/{minx},{miny},{maxx},{maxy}[/{width}x{height}].{format}`| image/bin                               | Create an image from part of a dataset
| `POST` | `/collections/{collection_id}/feature[/{width}x{height}][.{format}]`                       | image/bin                               | Create an image from a GeoJSON feature

### Tiles

`:endpoint:/collections/{collection_id}/tiles[/{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]`

- PathParams:
    - **collection_id**: STAC Collection Identifier.
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
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
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

- `https://myendpoint/collections/my-collection/tiles/1/2/3?assets=B01`
- `https://myendpoint/collections/my-collection/tiles/1/2/3.jpg?assets=B01`
- `https://myendpoint/collections/my-collection/tiles/WorldCRS84Quad/1/2/3@2x.png?assets=B01&assets=B02&assets=B03`
- `https://myendpoint/collections/my-collection/tiles/WorldCRS84Quad/1/2/3?assets=B01&rescale=0,1000&colormap_name=cfastie`

### TilesJSON

`:endpoint:/collections/{collection_id}[/{TileMatrixSetId}]/tilejson.json`

- PathParams:
    - **collection_id**: STAC Collection Identifier.
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
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
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

- `https://myendpoint/collections/my-collection/tilejson.json?assets=B01`
- `https://myendpoint/collections/my-collection/tilejson.json?assets=B01&tile_format=png`
- `https://myendpoint/collections/my-collection/WorldCRS84Quad/tilejson.json?assets=B01&tile_scale=2`


### WMTS

`:endpoint:/collections/{collection_id}[/{TileMatrixSetId}]/WMTSCapabilities.xml`

- PathParams:
    - **collection_id**: STAC Collection Identifier.
    - **TileMatrixSetId**: TileMatrixSet name, default is `WebMercatorQuad`. OPTIONAL

- QueryParams:
    - **tile_format**: Output image format, default is set to PNG.
    - **tile_scale**: Tile size scale, default is set to 1 (256x256). OPTIONAL
    - **minzoom**: Overwrite default minzoom. OPTIONAL
    - **maxzoom**: Overwrite default maxzoom. OPTIONAL


!!! important
    additional query-parameters will be forwarded to the `tile` URL. If no `defaults` mosaic metadata, **assets** OR **expression** will be required

Example:

- `https://myendpoint/collections/my-collection/WMTSCapabilities.xml?assets=B01`
- `https://myendpoint/collections/my-collection/WMTSCapabilities.xml?assets=B01&tile_format=png`
- `https://myendpoint/collections/my-collection/WorldCRS84Quad/WMTSCapabilities.xml?assets=B01&tile_scale=2`


### Assets

`:endpoint:/collections/{collection_id}/tiles/[{TileMatrixSetId}]/{z}/{x}/{y}/assets`

- PathParams:
    - **collection_id**: STAC Collection Identifier.
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

- `https://myendpoint/collections/my-collection/tiles/0/0/0/assets`

`:endpoint:/collections/{collection_id}/{lon},{lat}/assets`

- PathParams:
    - **collection_id**: STAC Collection Identifier.
    - **lon**: Longitude (in WGS84 CRS).
    - **lat**: Latitude (in WGS84 CRS).

- QueryParams:
    - **scan_limit** (int): Return as soon as we scan N items, Default is 10,000 in PgSTAC.
    - **items_limit** (int): Return as soon as we have N items per geometry, Default is 100 in PgSTAC.
    - **time_limit** (int): Return after N seconds to avoid long requests, Default is 5sec in PgSTAC.
    - **exitwhenfull** (bool): Return as soon as the geometry is fully covered, Default is `True` in PgSTAC.
    - **skipcovered** (bool): Skip any items that would show up completely under the previous items, Default is `True` in PgSTAC.

Example:

- `https://myendpoint/collections/my-collection/0.0,0.0/assets`

### Statistics

`:endpoint:/collections/{collection_id}/statistics - [POST]`

- Body:
    - **feature** (JSON): A valid GeoJSON feature or FeatureCollection

- PathParams:
    - **collection_id**: STAC Collection Identifier.

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **coord_crs** (str): Coordinate Reference System of the input geometry. Default to `epsg:4326`.
    - **dst_crs** (str): Output Coordinate Reference System. Default to `coord_crs`.
    - **max_size** (int): Max image size from which to calculate statistics.
    - **height** (int): Force image height from which to calculate statistics.
    - **width** (int): Force image width from which to calculate statistics.
    - **nodata**: Overwrite internal Nodata value. OPTIONAL
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
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

- `https://myendpoint/collections/my-collection/statistics?assets=B01`

### BBOX/Feature

`:endpoint:/collections/{collection_id}/bbox/{minx},{miny},{maxx},{maxy}.{format}`

`:endpoint:/collections/{collection_id}/bbox/{minx},{miny},{maxx},{maxy}/{width}x{height}.{format}`

- PathParams:
    - **collection_id**: STAC Collection Identifier.
    - **minx,miny,maxx,maxy** (str): Comma (',') delimited bounding box in WGS84.
    - **format** (str): Output image format.
    - **height** (int): Force output image height.
    - **width** (int): Force output image width.

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **coord_crs** (str): Coordinate Reference System of the input coordinates. Default to `epsg:4326`.
    - **dst_crs** (str): Output Coordinate Reference System. Default to `coord_crs`.
    - **max_size** (int): Max image size.
    - **nodata**: Overwrite internal Nodata value. OPTIONAL
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
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

- `https://myendpoint/collections/my-collection/bbox/0,0,10,10.png?assets=B01`
- `https://myendpoint/collections/my-collection/bbox/0,0,10,10/400x300.png?assets=B01`


`:endpoint:/collections/{collection_id}/feature[/{width}x{height}][].{format}] - [POST]`

- Body:
    - **feature** (JSON): A valid GeoJSON feature (Polygon or MultiPolygon)

- PathParams:
    - **collection_id**: STAC Collection Identifier.
    - **height** (int): Force output image height. **Optional**
    - **width** (int): Force output image width. **Optional**
    - **format** (str): Output image format, default is set to None and will be either JPEG or PNG depending on masked value. **Optional**

- QueryParams:
    - **assets** (array[str]): asset names.
    - **expression** (str): rio-tiler's math expression with asset names (e.g `Asset1_b1/Asset2_b1`).
    - **asset_as_band** (bool): tell rio-tiler that each asset is a 1 band dataset, so expression `Asset1/Asset2` can be passed.
    - **asset_bidx** (array[str]): Per asset band math expression (e.g `Asset1|1;2;3`).
    - **coord_crs** (str): Coordinate Reference System of the input geometry. Default to `epsg:4326`.
    - **dst_crs** (str): Output Coordinate Reference System. Default to `coord_crs`.
    - **max_size** (int): Max image size.
    - **nodata**: Overwrite internal Nodata value. OPTIONAL
    - **unscale** (bool): Apply dataset internal Scale/Offset.
    - **resampling** (str): RasterIO resampling algorithm. Defaults to `nearest`.
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

- `https://myendpoint/collections/my-collection/feature?assets=B01`
- `https://myendpoint/collections/my-collection/feature.png?assets=B01f`
- `https://myendpoint/collections/my-collection/feature/100x100.png?assets=B01`


[tilejson_model]: https://github.com/developmentseed/titiler/blob/2335048a407f17127099cbbc6c14e1328852d619/src/titiler/core/titiler/core/models/mapbox.py#L16-L38
[statitics_model]: https://github.com/developmentseed/titiler/blob/17cdff2f0ddf08dbd9a47c2140b13c4bbcc30b6d/src/titiler/core/titiler/core/models/responses.py#L49-L52
