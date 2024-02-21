# Module titiler.pgstac.mosaic

TiTiler.PgSTAC custom Mosaic Backend and Custom STACReader.

None

## Variables

```python3
WGS84_CRS
```

```python3
cache_config
```

```python3
retry_config
```

## Classes

### CustomSTACReader

```python3
class CustomSTACReader(
    input: Dict[str, Any],
    tms: morecantile.models.TileMatrixSet = <TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>,
    minzoom: int = NOTHING,
    maxzoom: int = NOTHING,
    reader: Type[rio_tiler.io.base.BaseReader] = <class 'rio_tiler.io.rasterio.Reader'>,
    reader_options: Dict = NOTHING,
    ctx: Any = <class 'rasterio.env.Env'>
)
```

#### Ancestors (in MRO)

* rio_tiler.io.base.MultiBaseReader
* rio_tiler.io.base.SpatialMixin

#### Instance variables

```python3
geographic_bounds
```

Return dataset bounds in geographic_crs.

#### Methods

    
#### feature

```python3
def feature(
    self,
    shape: Dict,
    assets: Union[Sequence[str], str] = None,
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
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
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
    categorical: bool = False,
    categories: Optional[List[float]] = None,
    percentiles: Optional[List[int]] = None,
    hist_options: Optional[Dict] = None,
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
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
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
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
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
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
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
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
    asset_expression: Optional[Dict[str, str]] = None,
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
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
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

### PGSTACBackend

```python3
class PGSTACBackend(
    input: str,
    pool: psycopg_pool.pool.ConnectionPool,
    tms: morecantile.models.TileMatrixSet = <TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>,
    minzoom: int = NOTHING,
    maxzoom: int = NOTHING,
    reader_options: Dict = NOTHING,
    bounds: Tuple[float, float, float, float] = (-180, -90, 180, 90),
    crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    geographic_crs: rasterio.crs.CRS = CRS.from_epsg(4326)
)
```

#### Ancestors (in MRO)

* cogeo_mosaic.backends.base.BaseBackend
* rio_tiler.io.base.BaseReader
* rio_tiler.io.base.SpatialMixin

#### Instance variables

```python3
center
```

Return center from the mosaic definition.

```python3
geographic_bounds
```

Return dataset bounds in geographic_crs.

```python3
mosaicid
```

Return sha224 id of the mosaicjson document.

```python3
quadkey_zoom
```

Return Quadkey zoom property.

#### Methods

    
#### assets_for_bbox

```python3
def assets_for_bbox(
    self,
    xmin: float,
    ymin: float,
    xmax: float,
    ymax: float,
    coord_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    **kwargs: Any
) -> List[Dict]
```

    
Retrieve assets for bbox.

    
#### assets_for_point

```python3
def assets_for_point(
    self,
    lng: float,
    lat: float,
    coord_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    **kwargs: Any
) -> List[Dict]
```

    
Retrieve assets for point.

    
#### assets_for_tile

```python3
def assets_for_tile(
    self,
    x: int,
    y: int,
    z: int,
    **kwargs: Any
) -> List[Dict]
```

    
Retrieve assets for tile.

    
#### feature

```python3
def feature(
    self,
    shape: Dict,
    dst_crs: Optional[rasterio.crs.CRS] = None,
    shape_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    max_size: int = 1024,
    reverse: bool = False,
    scan_limit: Optional[int] = None,
    items_limit: Optional[int] = None,
    time_limit: Optional[int] = None,
    exitwhenfull: Optional[bool] = None,
    skipcovered: Optional[bool] = None,
    **kwargs: Any
) -> Tuple[rio_tiler.models.ImageData, List[str]]
```

    
Create an Image from multiple items for a GeoJSON feature.

    
#### find_quadkeys

```python3
def find_quadkeys(
    self,
    tile: morecantile.commons.Tile,
    quadkey_zoom: int
) -> List[str]
```

    
Find quadkeys at desired zoom for tile

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile | morecantile.Tile | Input tile to use when searching for quadkeys | None |
| quadkey_zoom | int | Zoom level | None |

**Returns:**

| Type | Description |
|---|---|
| list | List[str] of quadkeys |

    
#### get_assets

```python3
def get_assets(
    *args: Any,
    **kwargs: Any
)
```

    

    
#### info

```python3
def info(
    self,
    quadkeys: bool = False
) -> cogeo_mosaic.models.Info
```

    
Mosaic info.

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    dst_crs: Optional[rasterio.crs.CRS] = None,
    bounds_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    reverse: bool = False,
    scan_limit: Optional[int] = None,
    items_limit: Optional[int] = None,
    time_limit: Optional[int] = None,
    exitwhenfull: Optional[bool] = None,
    skipcovered: Optional[bool] = None,
    **kwargs: Any
) -> Tuple[rio_tiler.models.ImageData, List[str]]
```

    
Create an Image from multiple items for a bbox.

    
#### point

```python3
def point(
    self,
    lon: float,
    lat: float,
    coord_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    reverse: bool = False,
    scan_limit: Optional[int] = None,
    items_limit: Optional[int] = None,
    time_limit: Optional[int] = None,
    exitwhenfull: Optional[bool] = None,
    skipcovered: Optional[bool] = None,
    **kwargs: Any
) -> List
```

    
Get Point value from multiple observation.

    
#### preview

```python3
def preview(
    self
)
```

    
PlaceHolder for BaseReader.preview.

    
#### statistics

```python3
def statistics(
    self
)
```

    
PlaceHolder for BaseReader.statistics.

    
#### tile

```python3
def tile(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    reverse: bool = False,
    scan_limit: Optional[int] = None,
    items_limit: Optional[int] = None,
    time_limit: Optional[int] = None,
    exitwhenfull: Optional[bool] = None,
    skipcovered: Optional[bool] = None,
    **kwargs: Any
) -> Tuple[rio_tiler.models.ImageData, List[str]]
```

    
Get Tile from multiple observation.

    
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

    
#### update

```python3
def update(
    self
) -> None
```

    
We overwrite the default method.

    
#### write

```python3
def write(
    self,
    overwrite: bool = True
) -> None
```

    
This method is not used but is required by the abstract class.