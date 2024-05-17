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
    tags: Optional[List[str]] = None
)
```

Add PgSTAC Search (of type mosaic) listing route.

    
### add_search_register_route

```python3
def add_search_register_route(
    app: fastapi.applications.FastAPI,
    *,
    prefix: str = '',
    search_dependency: Callable[..., Tuple[titiler.pgstac.model.PgSTACSearch, titiler.pgstac.model.Metadata]] = <function SearchParams at 0x7f56f67a4400>,
    tile_dependencies: Optional[List[Callable]] = None,
    tags: Optional[List[str]] = None
)
```

add `/register` route

    
### check_query_params

```python3
def check_query_params(
    *,
    dependencies: List[Callable],
    query_params: Union[starlette.datastructures.QueryParams, Dict]
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
    path_dependency: Callable[..., str] = <function DatasetPathParams at 0x7f56ff3c9e40>,
    layer_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.AssetsBidxExprParams'>,
    dataset_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DatasetParams'>,
    process_dependency: Callable[..., Optional[titiler.core.algorithm.base.BaseAlgorithm]] = <function Algorithms.dependency.<locals>.post_process at 0x7f56f66db560>,
    rescale_dependency: Callable[..., Optional[List[Tuple[float, ...]]]] = <function RescalingParams at 0x7f56f6aa71a0>,
    color_formula_dependency: Callable[..., Optional[str]] = <function ColorFormulaParams at 0x7f56f68d1da0>,
    colormap_dependency: Callable[..., Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]], NoneType]] = <function create_colormap_dependency.<locals>.deps at 0x7f56ff3c9da0>,
    render_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.ImageRenderingParams'>,
    reader_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DefaultDependency'>,
    environment_dependency: Callable[..., Dict] = <function BaseTilerFactory.<lambda> at 0x7f56f66db380>,
    supported_tms: morecantile.defaults.TileMatrixSets = TileMatrixSets(tms={'CDB1GlobalGrid': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/CDB1GlobalGrid.json'), 'CanadianNAD83_LCC': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/CanadianNAD83_LCC.json'), 'EuropeanETRS89_LAEAQuad': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/EuropeanETRS89_LAEAQuad.json'), 'GNOSISGlobalGrid': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/GNOSISGlobalGrid.json'), 'LINZAntarticaMapTilegrid': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/LINZAntarticaMapTilegrid.json'), 'NZTM2000Quad': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/NZTM2000Quad.json'), 'UPSAntarcticWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/UPSAntarcticWGS84Quad.json'), 'UPSArcticWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/UPSArcticWGS84Quad.json'), 'UTM31WGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/UTM31WGS84Quad.json'), 'WGS1984Quad': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/WGS1984Quad.json'), 'WebMercatorQuad': <TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>, 'WorldCRS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/WorldCRS84Quad.json'), 'WorldMercatorWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.11.9/x64/lib/python3.11/site-packages/morecantile/data/WorldMercatorWGS84Quad.json')}),
    default_tms: Optional[str] = None,
    router_prefix: str = '',
    optional_headers: List[titiler.core.resources.enums.OptionalHeader] = <factory>,
    route_dependencies: List[Tuple[List[titiler.core.routing.EndpointScope], List[fastapi.params.Depends]]] = <factory>,
    extensions: List[titiler.core.factory.FactoryExtension] = <factory>,
    templates: starlette.templating.Jinja2Templates = <starlette.templating.Jinja2Templates object at 0x7f56f6626dd0>,
    stats_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.StatisticsParams'>,
    histogram_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.HistogramParams'>,
    tile_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.TileParams'>,
    img_part_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.PartFeatureParams'>,
    pixel_selection_dependency: Callable[..., rio_tiler.mosaic.methods.base.MosaicMethodBase] = <function PixelSelectionParams at 0x7f56f60caca0>,
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
    color_formula: Annotated[Optional[str], Query(PydanticUndefined)] = None
) -> Optional[str]
```

ColorFormula Parameter.

    
#### colormap_dependency

```python3
def colormap_dependency(
    colormap_name: Annotated[Literal['plasma_r', 'pastel2', 'rdylbu_r', 'cividis', 'purples_r', 'twilight_shifted_r', 'brbg_r', 'gist_ncar_r', 'tarn', 'set1_r', 'rainbow_r', 'bupu_r', 'turbid', 'diff', 'turbid_r', 'ice_r', 'ocean', 'accent_r', 'hot', 'reds_r', 'rdylgn_r', 'gist_yarg', 'hsv', 'nipy_spectral_r', 'greens', 'inferno_r', 'ylgnbu', 'prism_r', 'winter', 'set2_r', 'gnuplot2', 'gnuplot2_r', 'set3', 'speed', 'seismic_r', 'cool', 'bwr', 'purples', 'topo_r', 'spring_r', 'blues', 'rdpu_r', 'terrain_r', 'pastel2_r', 'brg_r', 'rain_r', 'binary_r', 'gist_heat', 'tarn_r', 'amp_r', 'topo', 'prgn', 'phase_r', 'gist_ncar', 'blues_r', 'delta_r', 'tab20_r', 'delta', 'solar_r', 'summer_r', 'oranges', 'tempo', 'spectral_r', 'gist_earth', 'gnuplot', 'piyg', 'viridis', 'orrd', 'cubehelix_r', 'phase', 'magma_r', 'viridis_r', 'twilight_r', 'wistia', 'curl', 'cividis_r', 'tab20b', 'gist_rainbow', 'winter_r', 'pastel1_r', 'flag_r', 'ocean_r', 'bugn', 'rdgy', 'rain', 'algae_r', 'wistia_r', 'accent', 'tempo_r', 'afmhot', 'amp', 'rdbu_r', 'puor_r', 'ylorrd', 'pubu_r', 'brbg', 'pink_r', 'greys_r', 'pubugn_r', 'cmrmap', 'flag', 'turbo', 'oxy_r', 'ylorbr_r', 'matter_r', 'twilight', 'deep', 'purd', 'coolwarm', 'gist_rainbow_r', 'spring', 'autumn', 'spectral', 'hot_r', 'coolwarm_r', 'schwarzwald', 'tab10_r', 'speed_r', 'ylgn_r', 'gnuplot_r', 'gist_heat_r', 'rdylbu', 'orrd_r', 'piyg_r', 'balance', 'balance_r', 'pubu', 'pink', 'prgn_r', 'inferno', 'bupu', 'dark2_r', 'deep_r', 'matter', 'jet', 'tab20c_r', 'diff_r', 'nipy_spectral', 'gist_earth_r', 'gist_stern_r', 'haline', 'turbo_r', 'prism', 'purd_r', 'haline_r', 'rplumbo', 'gist_gray', 'greens_r', 'gray', 'algae', 'tab10', 'hsv_r', 'autumn_r', 'rdpu', 'thermal_r', 'oxy', 'cmrmap_r', 'cubehelix', 'ylgnbu_r', 'dense', 'bugn_r', 'gist_stern', 'tab20', 'ylorbr', 'summer', 'rdylgn', 'tab20b_r', 'jet_r', 'paired_r', 'dark2', 'binary', 'twilight_shifted', 'seismic', 'pubugn', 'ylgn', 'rdbu', 'bone', 'tab20c', 'dense_r', 'gnbu', 'set2', 'paired', 'gnbu_r', 'copper_r', 'gist_yarg_r', 'pastel1', 'bwr_r', 'greys', 'puor', 'oranges_r', 'cool_r', 'afmhot_r', 'rdgy_r', 'bone_r', 'thermal', 'ice', 'gray_r', 'copper', 'cfastie', 'curl_r', 'reds', 'brg', 'solar', 'ylorrd_r', 'magma', 'plasma', 'set3_r', 'rainbow', 'terrain', 'gist_gray_r', 'set1'], Query(PydanticUndefined)] = None,
    colormap: Annotated[Optional[str], Query(PydanticUndefined)] = None
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
    url: typing.Annotated[str, Query(PydanticUndefined)]
) -> str
```

Create dataset path from args

    
#### pixel_selection_dependency

```python3
def pixel_selection_dependency(
    pixel_selection: Annotated[Literal['first', 'highest', 'lowest', 'mean', 'median', 'stdev', 'lastbandlow', 'lastbandhight', 'count'], Query(PydanticUndefined)] = 'first'
) -> rio_tiler.mosaic.methods.base.MosaicMethodBase
```

Returns the mosaic method used to combine datasets together.

    
#### process_dependency

```python3
def process_dependency(
    algorithm: Annotated[Literal['hillshade', 'contours', 'normalizedIndex', 'terrarium', 'terrainrgb'], Query(PydanticUndefined)] = None,
    algorithm_params: Annotated[Optional[str], Query(PydanticUndefined)] = None
) -> Optional[titiler.core.algorithm.base.BaseAlgorithm]
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
    rescale: Annotated[Optional[List[str]], Query(PydanticUndefined)] = None
) -> Optional[List[Tuple[float, ...]]]
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