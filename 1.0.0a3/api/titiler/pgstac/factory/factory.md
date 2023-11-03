# Module titiler.pgstac.factory

Custom MosaicTiler Factory for PgSTAC Mosaic Backend.

## Variables

```python3
DEFAULT_TEMPLATES
```

```python3
MAX_THREADS
```

```python3
MOSAIC_STRICT_ZOOM
```

```python3
MOSAIC_THREADS
```

```python3
WGS84_CRS
```

```python3
img_endpoint_params
```

## Functions

    
### add_search_list_route

```python3
def add_search_list_route(
    app: fastapi.applications.FastAPI,
    *,
    prefix: str = '',
    tags: Union[List[str], NoneType] = None
)
```

Add PgSTAC Search (of type mosaic) listing route.

    
### add_search_register_route

```python3
def add_search_register_route(
    app: fastapi.applications.FastAPI,
    *,
    prefix: str = '',
    search_dependency: Callable[..., Tuple[titiler.pgstac.model.PgSTACSearch, titiler.pgstac.model.Metadata]] = <function SearchParams at 0x7feb581690d0>,
    tile_dependencies: Union[List[Callable], NoneType] = None,
    tags: Union[List[str], NoneType] = None
)
```

add `/register` route

    
### check_query_params

```python3
def check_query_params(
    *,
    dependencies: List[Callable],
    query_params: starlette.datastructures.QueryParams
) -> None
```

Check QueryParams for Query dependency.

1. `get_dependant` is used to get the query-parameters required by the `callable`
2. we use `request_params_to_args` to construct arguments needed to call the `callable`
3. we call the `callable` and catch any errors

Important: We assume the `callable` in not a co-routine

## Classes

### MosaicTilerFactory

```python3
class MosaicTilerFactory(
    reader: Type[cogeo_mosaic.backends.base.BaseBackend] = <class 'titiler.pgstac.mosaic.PGSTACBackend'>,
    router: fastapi.routing.APIRouter = <factory>,
    path_dependency: Callable[..., str] = <function DatasetPathParams at 0x7feb5af49820>,
    layer_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.AssetsBidxExprParams'>,
    dataset_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DatasetParams'>,
    process_dependency: Callable[..., Union[titiler.core.algorithm.base.BaseAlgorithm, NoneType]] = <function Algorithms.dependency.<locals>.post_process at 0x7feb5837cd30>,
    rescale_dependency: Callable[..., Union[List[Tuple[float, ...]], NoneType]] = <function RescalingParams at 0x7feb5af62280>,
    color_formula_dependency: Callable[..., Union[str, NoneType]] = <function ColorFormulaParams at 0x7feb58488ee0>,
    colormap_dependency: Callable[..., Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]], NoneType]] = <function create_colormap_dependency.<locals>.deps at 0x7feb5f1d83a0>,
    render_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.ImageRenderingParams'>,
    reader_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DefaultDependency'>,
    environment_dependency: Callable[..., Dict] = <function BaseTilerFactory.<lambda> at 0x7feb5837c700>,
    supported_tms: morecantile.defaults.TileMatrixSets = TileMatrixSets(tms={'CDB1GlobalGrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/CDB1GlobalGrid.json'), 'CanadianNAD83_LCC': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/CanadianNAD83_LCC.json'), 'EuropeanETRS89_LAEAQuad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/EuropeanETRS89_LAEAQuad.json'), 'GNOSISGlobalGrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/GNOSISGlobalGrid.json'), 'LINZAntarticaMapTilegrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/LINZAntarticaMapTilegrid.json'), 'NZTM2000Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/NZTM2000Quad.json'), 'UPSAntarcticWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UPSAntarcticWGS84Quad.json'), 'UPSArcticWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UPSArcticWGS84Quad.json'), 'UTM31WGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UTM31WGS84Quad.json'), 'WGS1984Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WGS1984Quad.json'), 'WebMercatorQuad': <TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>, 'WorldCRS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WorldCRS84Quad.json'), 'WorldMercatorWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WorldMercatorWGS84Quad.json')}),
    default_tms: str = 'WebMercatorQuad',
    router_prefix: str = '',
    optional_headers: List[titiler.core.resources.enums.OptionalHeader] = <factory>,
    route_dependencies: List[Tuple[List[titiler.core.routing.EndpointScope], List[fastapi.params.Depends]]] = <factory>,
    extensions: List[titiler.core.factory.FactoryExtension] = <factory>,
    templates: starlette.templating.Jinja2Templates = <starlette.templating.Jinja2Templates object at 0x7feb5812fca0>,
    stats_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.StatisticsParams'>,
    histogram_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.HistogramParams'>,
    tile_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.TileParams'>,
    img_part_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.PartFeatureParams'>,
    pixel_selection_dependency: Callable[..., rio_tiler.mosaic.methods.base.MosaicMethodBase] = <function PixelSelectionParams at 0x7feb57dd5160>,
    pgstac_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.pgstac.dependencies.PgSTACParams'>,
    backend_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.pgstac.dependencies.BackendParams'>,
    add_statistics: bool = False,
    add_viewer: bool = False,
    add_part: bool = False
)
```

Custom MosaicTiler for PgSTAC Mosaic Backend.

#### Ancestors (in MRO)

* titiler.core.factory.BaseTilerFactory

#### Class variables

```python3
add_part
```

```python3
add_statistics
```

```python3
add_viewer
```

```python3
backend_dependency
```

```python3
dataset_dependency
```

```python3
default_tms
```

```python3
histogram_dependency
```

```python3
img_part_dependency
```

```python3
layer_dependency
```

```python3
pgstac_dependency
```

```python3
reader
```

```python3
reader_dependency
```

```python3
render_dependency
```

```python3
router_prefix
```

```python3
stats_dependency
```

```python3
supported_tms
```

```python3
templates
```

```python3
tile_dependency
```

#### Methods

    
#### add_route_dependencies

```python3
def add_route_dependencies(
    self,
    *,
    scopes: List[titiler.core.routing.EndpointScope],
    dependencies=typing.List[fastapi.params.Depends]
)
```

Add dependencies to routes.

Allows a developer to add dependencies to a route after the route has been defined.

    
#### color_formula_dependency

```python3
def color_formula_dependency(
    color_formula: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
) -> Union[str, NoneType]
```

ColorFormula Parameter.

    
#### colormap_dependency

```python3
def colormap_dependency(
    colormap_name: typing_extensions.Annotated[Literal['oranges', 'gist_earth', 'gray', 'dense', 'purples', 'puor', 'gnuplot2_r', 'spectral', 'rain', 'cfastie', 'tab20_r', 'curl', 'solar_r', 'terrain', 'afmhot_r', 'cubehelix', 'jet_r', 'magma_r', 'gist_yarg', 'tab20', 'rdgy', 'afmhot', 'gist_earth_r', 'rdgy_r', 'viridis_r', 'reds_r', 'binary_r', 'flag', 'turbid', 'accent', 'thermal', 'pink', 'plasma', 'balance_r', 'cool', 'pubugn_r', 'set3', 'gnuplot', 'ocean', 'copper_r', 'bwr', 'matter_r', 'turbid_r', 'gnuplot_r', 'amp', 'orrd', 'tab20b_r', 'algae', 'rdylgn_r', 'gist_gray_r', 'prism_r', 'ocean_r', 'autumn_r', 'piyg', 'tarn', 'greys_r', 'set2_r', 'winter_r', 'brbg_r', 'gist_rainbow', 'pubu', 'ylgn_r', 'gist_heat_r', 'seismic', 'dark2', 'hot', 'rdylgn', 'oranges_r', 'puor_r', 'bwr_r', 'ylorrd_r', 'inferno', 'speed', 'set3_r', 'ylgnbu', 'balance', 'rdylbu', 'greens', 'ylgnbu_r', 'topo_r', 'wistia', 'prgn_r', 'bupu', 'jet', 'gist_gray', 'ylgn', 'tab10_r', 'seismic_r', 'twilight', 'tab20c_r', 'hsv_r', 'ylorbr_r', 'orrd_r', 'gist_heat', 'blues', 'gist_ncar', 'coolwarm_r', 'paired', 'wistia_r', 'purd_r', 'autumn', 'greys', 'diff', 'topo', 'tab20b', 'oxy_r', 'purples_r', 'diff_r', 'rdylbu_r', 'tempo', 'tab20c', 'gist_stern_r', 'prism', 'tarn_r', 'gnuplot2', 'set1_r', 'bugn_r', 'purd', 'cmrmap_r', 'cividis_r', 'spectral_r', 'dark2_r', 'pastel1_r', 'inferno_r', 'twilight_shifted_r', 'delta', 'pubu_r', 'terrain_r', 'ice', 'brbg', 'viridis', 'hot_r', 'rainbow_r', 'haline', 'rdpu', 'cool_r', 'magma', 'tab10', 'solar', 'twilight_shifted', 'gist_yarg_r', 'coolwarm', 'oxy', 'amp_r', 'tempo_r', 'flag_r', 'brg', 'rdpu_r', 'pubugn', 'bone_r', 'deep', 'winter', 'dense_r', 'gnbu', 'blues_r', 'summer_r', 'cubehelix_r', 'speed_r', 'cividis', 'hsv', 'gray_r', 'piyg_r', 'binary', 'plasma_r', 'gist_rainbow_r', 'pastel1', 'set1', 'nipy_spectral_r', 'gnbu_r', 'prgn', 'copper', 'rplumbo', 'thermal_r', 'pastel2', 'rdbu', 'spring_r', 'delta_r', 'set2', 'rainbow', 'bugn', 'greens_r', 'brg_r', 'reds', 'turbo', 'ylorrd', 'curl_r', 'gist_stern', 'schwarzwald', 'phase', 'rain_r', 'matter', 'deep_r', 'ice_r', 'paired_r', 'cmrmap', 'bupu_r', 'pastel2_r', 'spring', 'phase_r', 'algae_r', 'turbo_r', 'rdbu_r', 'nipy_spectral', 'bone', 'ylorbr', 'pink_r', 'gist_ncar_r', 'twilight_r', 'accent_r', 'summer', 'haline_r'], Query(PydanticUndefined)] = None,
    colormap: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

    
#### environment_dependency

```python3
def environment_dependency(
    
)
```

    
#### path_dependency

```python3
def path_dependency(
    url: typing_extensions.Annotated[str, Query(PydanticUndefined)]
) -> str
```

Create dataset path from args

    
#### pixel_selection_dependency

```python3
def pixel_selection_dependency(
    pixel_selection: typing_extensions.Annotated[Literal['first', 'highest', 'lowest', 'mean', 'median', 'stdev', 'lastbandlow', 'lastbandhight'], Query(PydanticUndefined)] = 'first'
) -> rio_tiler.mosaic.methods.base.MosaicMethodBase
```

Returns the mosaic method used to combine datasets together.

    
#### process_dependency

```python3
def process_dependency(
    algorithm: typing_extensions.Annotated[Literal['hillshade', 'contours', 'normalizedIndex', 'terrarium', 'terrainrgb'], Query(PydanticUndefined)] = None,
    algorithm_params: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
) -> Union[titiler.core.algorithm.base.BaseAlgorithm, NoneType]
```

Data Post-Processing options.

    
#### register_routes

```python3
def register_routes(
    self
) -> None
```

This Method register routes to the router.

    
#### rescale_dependency

```python3
def rescale_dependency(
    rescale: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None
) -> Union[List[Tuple[float, ...]], NoneType]
```

Min/Max data Rescaling

    
#### url_for

```python3
def url_for(
    self,
    request: starlette.requests.Request,
    name: str,
    **path_params: Any
) -> str
```

Return full url (with prefix) for a specific endpoint.