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

```python3
jinja2_env
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
    search_dependency: Callable[..., Tuple[titiler.pgstac.model.PgSTACSearch, titiler.pgstac.model.Metadata]] = <function SearchParams at 0x7f0dd93eb670>,
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
    path_dependency: Callable[..., str] = <function DatasetPathParams at 0x7f0dde2b3040>,
    layer_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.AssetsBidxExprParams'>,
    dataset_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DatasetParams'>,
    process_dependency: Callable[..., Union[titiler.core.algorithm.base.BaseAlgorithm, NoneType]] = <function Algorithms.dependency.<locals>.post_process at 0x7f0dd8fa1670>,
    rescale_dependency: Callable[..., Union[List[Tuple[float, ...]], NoneType]] = <function RescalingParams at 0x7f0dde2b3a60>,
    color_formula_dependency: Callable[..., Union[str, NoneType]] = <function ColorFormulaParams at 0x7f0dd93db940>,
    colormap_dependency: Callable[..., Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]], NoneType]] = <function create_colormap_dependency.<locals>.deps at 0x7f0de211bb80>,
    render_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.ImageRenderingParams'>,
    reader_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DefaultDependency'>,
    environment_dependency: Callable[..., Dict] = <function BaseTilerFactory.<lambda> at 0x7f0de54338b0>,
    supported_tms: morecantile.defaults.TileMatrixSets = TileMatrixSets(tms={'CDB1GlobalGrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/CDB1GlobalGrid.json'), 'CanadianNAD83_LCC': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/CanadianNAD83_LCC.json'), 'EuropeanETRS89_LAEAQuad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/EuropeanETRS89_LAEAQuad.json'), 'GNOSISGlobalGrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/GNOSISGlobalGrid.json'), 'LINZAntarticaMapTilegrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/LINZAntarticaMapTilegrid.json'), 'NZTM2000Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/NZTM2000Quad.json'), 'UPSAntarcticWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UPSAntarcticWGS84Quad.json'), 'UPSArcticWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UPSArcticWGS84Quad.json'), 'UTM31WGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UTM31WGS84Quad.json'), 'WGS1984Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WGS1984Quad.json'), 'WebMercatorQuad': <TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>, 'WorldCRS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WorldCRS84Quad.json'), 'WorldMercatorWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WorldMercatorWGS84Quad.json')}),
    default_tms: str = 'WebMercatorQuad',
    router_prefix: str = '',
    optional_headers: List[titiler.core.resources.enums.OptionalHeader] = <factory>,
    route_dependencies: List[Tuple[List[titiler.core.routing.EndpointScope], List[fastapi.params.Depends]]] = <factory>,
    extensions: List[titiler.core.factory.FactoryExtension] = <factory>,
    templates: starlette.templating.Jinja2Templates = <starlette.templating.Jinja2Templates object at 0x7f0de542ff40>,
    stats_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.StatisticsParams'>,
    histogram_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.HistogramParams'>,
    tile_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.TileParams'>,
    img_part_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.PartFeatureParams'>,
    pixel_selection_dependency: Callable[..., rio_tiler.mosaic.methods.base.MosaicMethodBase] = <function PixelSelectionParams at 0x7f0dd8c850d0>,
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
    colormap_name: typing_extensions.Annotated[Literal['summer', 'gist_ncar_r', 'jet_r', 'brg_r', 'ocean_r', 'rdylbu_r', 'curl_r', 'twilight_r', 'flag_r', 'rdylbu', 'twilight_shifted', 'turbid_r', 'gist_stern_r', 'set1', 'brbg', 'ylorbr_r', 'viridis_r', 'tab20_r', 'tarn_r', 'viridis', 'amp_r', 'pubugn', 'bupu', 'jet', 'prism', 'ylgnbu', 'topo_r', 'ice', 'pubugn_r', 'hot_r', 'greys', 'gist_rainbow_r', 'reds_r', 'greens', 'autumn_r', 'nipy_spectral', 'cmrmap', 'accent_r', 'ylorrd', 'greys_r', 'terrain', 'rainbow', 'oxy_r', 'autumn', 'deep_r', 'twilight', 'pastel1', 'ocean', 'matter', 'phase', 'set3', 'pink_r', 'oranges_r', 'tab10', 'tab20c_r', 'balance_r', 'seismic', 'set2', 'dark2', 'afmhot', 'purd_r', 'puor', 'gnuplot_r', 'paired', 'turbo', 'tab10_r', 'coolwarm', 'gnbu', 'set1_r', 'diff', 'blues', 'gist_earth_r', 'solar_r', 'tarn', 'balance', 'tempo_r', 'ylorrd_r', 'paired_r', 'gist_heat_r', 'plasma', 'solar', 'cubehelix', 'gist_gray', 'brbg_r', 'magma_r', 'deep', 'binary', 'purd', 'magma', 'diff_r', 'cfastie', 'wistia_r', 'bupu_r', 'twilight_shifted_r', 'oranges', 'gist_yarg', 'prgn', 'gist_ncar', 'binary_r', 'wistia', 'ylgn_r', 'greens_r', 'blues_r', 'gray', 'turbid', 'rplumbo', 'dark2_r', 'topo', 'bwr', 'delta', 'speed_r', 'speed', 'gist_stern', 'inferno_r', 'puor_r', 'pubu', 'afmhot_r', 'gnbu_r', 'purples', 'ice_r', 'bugn_r', 'orrd_r', 'reds', 'pastel2_r', 'matter_r', 'inferno', 'gist_gray_r', 'rdbu', 'spectral_r', 'seismic_r', 'pink', 'summer_r', 'phase_r', 'piyg', 'copper_r', 'spring_r', 'algae_r', 'rdylgn', 'bugn', 'gist_heat', 'cubehelix_r', 'cmrmap_r', 'tab20', 'rain', 'rdylgn_r', 'amp', 'thermal', 'ylorbr', 'haline_r', 'bone_r', 'curl', 'ylgn', 'brg', 'ylgnbu_r', 'set2_r', 'dense', 'rdgy_r', 'tab20b_r', 'tab20c', 'prism_r', 'spring', 'gnuplot', 'pubu_r', 'purples_r', 'nipy_spectral_r', 'copper', 'prgn_r', 'bone', 'tab20b', 'rdpu', 'schwarzwald', 'oxy', 'terrain_r', 'coolwarm_r', 'cividis_r', 'gist_yarg_r', 'flag', 'rdbu_r', 'gist_rainbow', 'rain_r', 'cool_r', 'spectral', 'hsv', 'cool', 'thermal_r', 'dense_r', 'winter_r', 'set3_r', 'orrd', 'plasma_r', 'piyg_r', 'gist_earth', 'hot', 'gnuplot2', 'hsv_r', 'algae', 'pastel2', 'rainbow_r', 'gray_r', 'tempo', 'bwr_r', 'rdpu_r', 'pastel1_r', 'winter', 'accent', 'gnuplot2_r', 'turbo_r', 'haline', 'rdgy', 'delta_r', 'cividis'], Query(PydanticUndefined)] = None,
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