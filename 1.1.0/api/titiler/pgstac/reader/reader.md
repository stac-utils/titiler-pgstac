# Module titiler.pgstac.reader

Custom STAC reader.

## Variables

```python3
DEFAULT_VALID_TYPE
```

```python3
WGS84_CRS
```

## Classes

### PgSTACReader

```python3
class PgSTACReader(
    input: pystac.item.Item,
    tms: morecantile.models.TileMatrixSet = <TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>,
    minzoom: int = NOTHING,
    maxzoom: int = NOTHING,
    geographic_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    include_assets: Union[Set[str], NoneType] = None,
    exclude_assets: Union[Set[str], NoneType] = None,
    include_asset_types: Set[str] = {'image/jp2', 'application/x-hdf5', 'image/tiff; application=geotiff; profile=cloud-optimized', 'image/tiff; application=geotiff', 'image/x.geotiff', 'application/x-hdf', 'image/vnd.stac.geotiff; cloud-optimized=true', 'image/tiff', 'image/tiff; profile=cloud-optimized; application=geotiff'},
    exclude_asset_types: Union[Set[str], NoneType] = None,
    reader: Type[rio_tiler.io.base.BaseReader] = <class 'rio_tiler.io.rasterio.Reader'>,
    reader_options: Dict = NOTHING,
    ctx: Any = <class 'rasterio.env.Env'>
)
```

Custom STAC Reader.

Only accept `pystac.Item` as input (while rio_tiler.io.STACReader accepts url or pystac.Item)

#### Ancestors (in MRO)

* rio_tiler.io.base.MultiBaseReader
* rio_tiler.io.base.SpatialMixin

#### Methods

    
#### feature

```python3
def feature(
    self,
    shape: Dict,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_as_band: bool = False,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

Read and merge parts defined by geojson feature from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| shape | dict | Valid GeoJSON feature. | None |
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| kwargs | optional | Options to forward to the `self.reader.feature` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### geographic_bounds

```python3
def geographic_bounds(
    ...
)
```

Return dataset bounds in geographic_crs.

    
#### info

```python3
def info(
    self,
    assets: Union[Sequence[str], str] = None,
    **kwargs: Any
) -> Dict[str, rio_tiler.models.Info]
```

Return metadata from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| assets | sequence of str or str | assets to fetch info from. Required keyword argument. | None |

**Returns:**

| Type | Description |
|---|---|
| dict | Multiple assets info in form of {"asset1": rio_tile.models.Info}. |

    
#### merged_statistics

```python3
def merged_statistics(
    self,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    categorical: bool = False,
    categories: Union[List[float], NoneType] = None,
    percentiles: Union[List[int], NoneType] = None,
    hist_options: Union[Dict, NoneType] = None,
    max_size: int = 1024,
    **kwargs: Any
) -> Dict[str, rio_tiler.models.BandStatistics]
```

Return array statistics for multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| categorical | bool | treat input data as categorical data. Defaults to False. | False |
| categories | list of numbers | list of categories to return value for. | None |
| percentiles | list of numbers | list of percentile values to calculate. Defaults to `[2, 98]`. | `[2, 98]` |
| hist_options | dict | Options to forward to numpy.histogram function. | None |
| max_size | int | Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024. | 1024 |
| kwargs | optional | Options to forward to the `self.preview` method. | None |

**Returns:**

| Type | Description |
|---|---|
| Dict[str, rio_tiler.models.BandStatistics] | bands statistics. |

    
#### parse_expression

```python3
def parse_expression(
    self,
    expression: str,
    asset_as_band: bool = False
) -> Tuple
```

Parse rio-tiler band math expression.

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_as_band: bool = False,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

Read and merge parts from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bbox | tuple | Output bounds (left, bottom, right, top) in target crs. | None |
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| kwargs | optional | Options to forward to the `self.reader.part` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### point

```python3
def point(
    self,
    lon: float,
    lat: float,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_as_band: bool = False,
    **kwargs: Any
) -> rio_tiler.models.PointData
```

Read pixel value from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| lon | float | Longitude. | None |
| lat | float | Latitude. | None |
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| kwargs | optional | Options to forward to the `self.reader.point` method. | None |

**Returns:**

| Type | Description |
|---|---|
| None | PointData |

    
#### preview

```python3
def preview(
    self,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_as_band: bool = False,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

Read and merge previews from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| kwargs | optional | Options to forward to the `self.reader.preview` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### statistics

```python3
def statistics(
    self,
    assets: Union[Sequence[str], str] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_expression: Union[Dict[str, str], NoneType] = None,
    **kwargs: Any
) -> Dict[str, Dict[str, rio_tiler.models.BandStatistics]]
```

Return array statistics for multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| assets | sequence of str or str | assets to fetch info from. | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| asset_expression | dict | rio-tiler expression for each asset (e.g. {"asset1": "b1/b2+b3", "asset2": ...}). | None |
| kwargs | optional | Options to forward to the `self.reader.statistics` method. | None |

**Returns:**

| Type | Description |
|---|---|
| dict | Multiple assets statistics in form of {"asset1": {"1": rio_tiler.models.BandStatistics, ...}}. |

    
#### tile

```python3
def tile(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_as_band: bool = False,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

Read and merge Wep Map tiles from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| kwargs | optional | Options to forward to the `self.reader.tile` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### tile_exists

```python3
def tile_exists(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int
) -> bool
```

Check if a tile intersects the dataset bounds.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |

**Returns:**

| Type | Description |
|---|---|
| bool | True if the tile intersects the dataset bounds. |