# Module titiler.pgstac.factory

Custom MosaicTiler Factory for PgSTAC Mosaic Backend.

None

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
    search_dependency: Callable[..., Tuple[titiler.pgstac.model.PgSTACSearch, titiler.pgstac.model.Metadata]] = <function SearchParams at 0x16b4203a0>,
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
    path_dependency: Callable[..., str] = <function DatasetPathParams at 0x1652775e0>,
    layer_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.AssetsBidxExprParams'>,
    dataset_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DatasetParams'>,
    process_dependency: Callable[..., Optional[titiler.core.algorithm.base.BaseAlgorithm]] = <function Algorithms.dependency.<locals>.post_process at 0x16b254700>,
    rescale_dependency: Callable[..., Optional[List[Tuple[float, ...]]]] = <function RescalingParams at 0x16af3cf70>,
    color_formula_dependency: Callable[..., Optional[str]] = <function ColorFormulaParams at 0x16af62160>,
    colormap_dependency: Callable[..., Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]], NoneType]] = <function create_colormap_dependency.<locals>.deps at 0x13d5c6670>,
    render_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.ImageRenderingParams'>,
    reader_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DefaultDependency'>,
    environment_dependency: Callable[..., Dict] = <function BaseTilerFactory.<lambda> at 0x16b235820>,
    supported_tms: morecantile.defaults.TileMatrixSets = TileMatrixSets(tms={'CDB1GlobalGrid': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/CDB1GlobalGrid.json'), 'CanadianNAD83_LCC': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/CanadianNAD83_LCC.json'), 'EuropeanETRS89_LAEAQuad': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/EuropeanETRS89_LAEAQuad.json'), 'GNOSISGlobalGrid': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/GNOSISGlobalGrid.json'), 'LINZAntarticaMapTilegrid': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/LINZAntarticaMapTilegrid.json'), 'NZTM2000Quad': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/NZTM2000Quad.json'), 'UPSAntarcticWGS84Quad': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/UPSAntarcticWGS84Quad.json'), 'UPSArcticWGS84Quad': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/UPSArcticWGS84Quad.json'), 'UTM31WGS84Quad': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/UTM31WGS84Quad.json'), 'WGS1984Quad': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/WGS1984Quad.json'), 'WebMercatorQuad': <TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>, 'WorldCRS84Quad': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/WorldCRS84Quad.json'), 'WorldMercatorWGS84Quad': PosixPath('/Users/vincentsarago/Dev/DevSeed/morecantile/morecantile/data/WorldMercatorWGS84Quad.json')}),
    default_tms: str = 'WebMercatorQuad',
    router_prefix: str = '',
    optional_headers: List[titiler.core.resources.enums.OptionalHeader] = <factory>,
    route_dependencies: List[Tuple[List[titiler.core.routing.EndpointScope], List[fastapi.params.Depends]]] = <factory>,
    extensions: List[titiler.core.factory.FactoryExtension] = <factory>,
    templates: starlette.templating.Jinja2Templates = <starlette.templating.Jinja2Templates object at 0x16b462580>,
    stats_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.StatisticsParams'>,
    histogram_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.HistogramParams'>,
    tile_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.TileParams'>,
    img_part_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.PartFeatureParams'>,
    pixel_selection_dependency: Callable[..., rio_tiler.mosaic.methods.base.MosaicMethodBase] = <function PixelSelectionParams at 0x16aea53a0>,
    pgstac_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.pgstac.dependencies.PgSTACParams'>,
    backend_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.pgstac.dependencies.BackendParams'>,
    add_statistics: bool = False,
    add_viewer: bool = False,
    add_part: bool = False
)
```

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
    colormap_name: Annotated[Literal['dense_r', 'delta', 'algae_r', 'ylorbr', 'oxy', 'copper', 'tab20c_r', 'cividis_r', 'solar', 'gnuplot', 'dark2_r', 'gist_yarg_r', 'balance_r', 'gist_earth', 'balance', 'jet', 'gist_heat', 'rdylgn', 'rainbow_r', 'turbid_r', 'magma_r', 'gist_stern_r', 'plasma', 'gnuplot2_r', 'rdylgn_r', 'matter', 'puor_r', 'cool', 'gist_gray_r', 'spectral', 'turbo_r', 'amp', 'gist_heat_r', 'accent', 'ice', 'brg', 'hsv_r', 'tab10', 'brg_r', 'ylgnbu', 'accent_r', 'coolwarm', 'winter_r', 'binary', 'bwr_r', 'wistia', 'bone', 'paired', 'rdylbu', 'inferno', 'summer_r', 'hot', 'gist_ncar', 'ylorbr_r', 'amp_r', 'tarn_r', 'orrd', 'bupu', 'dense', 'greens_r', 'hot_r', 'phase', 'ocean', 'plasma_r', 'afmhot_r', 'autumn', 'gist_stern', 'diff_r', 'prgn', 'tab20b_r', 'solar_r', 'cubehelix', 'prism', 'gnuplot_r', 'inferno_r', 'twilight_r', 'jet_r', 'brbg', 'autumn_r', 'afmhot', 'rain', 'purd_r', 'wistia_r', 'tab10_r', 'coolwarm_r', 'bugn_r', 'viridis', 'ylgn_r', 'gist_rainbow', 'rainbow', 'spring_r', 'puor', 'greys', 'pubu', 'dark2', 'bugn', 'phase_r', 'thermal_r', 'set2', 'flag_r', 'ylorrd_r', 'copper_r', 'spectral_r', 'prism_r', 'set3', 'ylgnbu_r', 'rain_r', 'brbg_r', 'terrain_r', 'pastel1_r', 'rdbu', 'bwr', 'set1', 'tab20b', 'blues_r', 'purples', 'terrain', 'gist_rainbow_r', 'haline', 'summer', 'tab20c', 'turbid', 'flag', 'twilight_shifted', 'gray_r', 'delta_r', 'nipy_spectral', 'topo_r', 'oranges_r', 'prgn_r', 'diff', 'set3_r', 'deep', 'ylorrd', 'cfastie', 'rplumbo', 'gray', 'deep_r', 'gist_yarg', 'twilight', 'rdbu_r', 'pink_r', 'reds', 'algae', 'speed_r', 'twilight_shifted_r', 'bone_r', 'cividis', 'set1_r', 'purples_r', 'rdgy_r', 'matter_r', 'gist_gray', 'cool_r', 'ice_r', 'speed', 'gist_ncar_r', 'rdgy', 'ylgn', 'oxy_r', 'pastel2_r', 'pastel2', 'nipy_spectral_r', 'tempo_r', 'haline_r', 'viridis_r', 'gnuplot2', 'pubu_r', 'bupu_r', 'pastel1', 'binary_r', 'greys_r', 'paired_r', 'orrd_r', 'gnbu', 'topo', 'pubugn', 'tempo', 'tab20_r', 'pink', 'gnbu_r', 'tab20', 'blues', 'rdpu_r', 'turbo', 'rdylbu_r', 'hsv', 'winter', 'magma', 'seismic', 'piyg', 'cmrmap_r', 'schwarzwald', 'gist_earth_r', 'cubehelix_r', 'piyg_r', 'seismic_r', 'thermal', 'cmrmap', 'purd', 'rdpu', 'oranges', 'set2_r', 'greens', 'ocean_r', 'spring', 'curl', 'tarn', 'curl_r', 'reds_r', 'pubugn_r'], Query(PydanticUndefined)] = None,
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
    pixel_selection: Annotated[Literal['first', 'highest', 'lowest', 'mean', 'median', 'stdev', 'lastbandlow', 'lastbandhight'], Query(PydanticUndefined)] = 'first'
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