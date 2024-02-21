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

## Classes

### MosaicTilerFactory

```python3
class MosaicTilerFactory(
    reader: Type[cogeo_mosaic.backends.base.BaseBackend] = <class 'titiler.pgstac.mosaic.PGSTACBackend'>,
    router: fastapi.routing.APIRouter = <factory>,
    path_dependency: Callable[..., str] = <function PathParams at 0x7faf0f024ca0>,
    layer_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.AssetsBidxExprParams'>,
    dataset_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DatasetParams'>,
    process_dependency: Callable[..., Union[titiler.core.algorithm.base.BaseAlgorithm, NoneType]] = <function Algorithms.dependency.<locals>.post_process at 0x7faf0fe7bdc0>,
    rescale_dependency: Callable[..., Union[List[Tuple[float, ...]], NoneType]] = <function RescalingParams at 0x7faf08bbc430>,
    color_formula_dependency: Callable[..., Union[str, NoneType]] = <function ColorFormulaParams at 0x7faf03cf81f0>,
    colormap_dependency: Callable[..., Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]], NoneType]] = <function create_colormap_dependency.<locals>.deps at 0x7faf0cc73550>,
    render_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.ImageRenderingParams'>,
    reader_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DefaultDependency'>,
    environment_dependency: Callable[..., Dict] = <function BaseTilerFactory.<lambda> at 0x7faf0fe7bd30>,
    supported_tms: morecantile.defaults.TileMatrixSets = TileMatrixSets(tms={'CDB1GlobalGrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/CDB1GlobalGrid.json'), 'CanadianNAD83_LCC': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/CanadianNAD83_LCC.json'), 'EuropeanETRS89_LAEAQuad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/EuropeanETRS89_LAEAQuad.json'), 'GNOSISGlobalGrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/GNOSISGlobalGrid.json'), 'LINZAntarticaMapTilegrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/LINZAntarticaMapTilegrid.json'), 'NZTM2000Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/NZTM2000Quad.json'), 'UPSAntarcticWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UPSAntarcticWGS84Quad.json'), 'UPSArcticWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UPSArcticWGS84Quad.json'), 'UTM31WGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UTM31WGS84Quad.json'), 'WGS1984Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WGS1984Quad.json'), 'WebMercatorQuad': <TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>, 'WorldCRS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WorldCRS84Quad.json'), 'WorldMercatorWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WorldMercatorWGS84Quad.json')}),
    default_tms: str = 'WebMercatorQuad',
    router_prefix: str = '',
    optional_headers: List[titiler.core.resources.enums.OptionalHeader] = <factory>,
    route_dependencies: List[Tuple[List[titiler.core.routing.EndpointScope], List[fastapi.params.Depends]]] = <factory>,
    extensions: List[titiler.core.factory.FactoryExtension] = <factory>,
    templates: starlette.templating.Jinja2Templates = <starlette.templating.Jinja2Templates object at 0x7faf037c7b50>,
    stats_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.StatisticsParams'>,
    histogram_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.HistogramParams'>,
    img_part_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.PartFeatureParams'>,
    search_dependency: Callable[..., Tuple[titiler.pgstac.model.PgSTACSearch, titiler.pgstac.model.Metadata]] = <function SearchParams at 0x7faf03862b80>,
    pixel_selection_dependency: Callable[..., rio_tiler.mosaic.methods.base.MosaicMethodBase] = <function PixelSelectionParams at 0x7faf0363d550>,
    backend_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.pgstac.dependencies.BackendParams'>,
    add_statistics: bool = False,
    add_viewer: bool = False,
    add_mosaic_list: bool = False,
    add_part: bool = False
)
```

Custom MosaicTiler for PgSTAC Mosaic Backend.

#### Ancestors (in MRO)

* titiler.core.factory.BaseTilerFactory

#### Class variables

```python3
add_mosaic_list
```

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

    
#### check_query_params

```python3
def check_query_params(
    self,
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
    colormap_name: typing_extensions.Annotated[Literal['brg', 'ice_r', 'plasma', 'greys', 'ocean', 'reds', 'topo_r', 'ylgn', 'haline_r', 'thermal_r', 'haline', 'topo', 'magma', 'cfastie', 'set2', 'puor', 'twilight_shifted', 'jet_r', 'purples', 'twilight_r', 'bupu_r', 'cmrmap_r', 'tarn_r', 'puor_r', 'gist_rainbow_r', 'reds_r', 'ylorbr_r', 'gist_gray', 'pubugn', 'coolwarm_r', 'flag_r', 'bugn', 'twilight', 'gist_ncar', 'orrd_r', 'gnuplot2', 'dense', 'ice', 'hsv_r', 'prism', 'speed_r', 'wistia', 'greens', 'afmhot', 'summer', 'pink', 'set3', 'bone_r', 'set1', 'tab20c', 'inferno', 'oranges_r', 'spring', 'pastel2_r', 'pastel2', 'delta_r', 'gnbu', 'piyg_r', 'ocean_r', 'purd_r', 'jet', 'brg_r', 'inferno_r', 'turbo_r', 'cmrmap', 'pastel1', 'dark2', 'gist_ncar_r', 'oranges', 'gist_stern', 'tab10_r', 'gist_gray_r', 'tab20b_r', 'cividis_r', 'autumn', 'tab20c_r', 'oxy_r', 'rplumbo', 'brbg_r', 'bwr', 'tempo', 'rdylgn_r', 'seismic_r', 'tab10', 'set2_r', 'cividis', 'pink_r', 'gist_heat', 'delta', 'phase_r', 'winter', 'gnuplot_r', 'ylgnbu', 'spring_r', 'gist_earth_r', 'rdylbu', 'tab20_r', 'coolwarm', 'accent', 'bugn_r', 'viridis_r', 'deep', 'ylgn_r', 'matter', 'binary_r', 'gist_yarg', 'rdpu', 'terrain_r', 'hot', 'ylgnbu_r', 'amp', 'autumn_r', 'flag', 'hsv', 'thermal', 'accent_r', 'ylorrd', 'gist_rainbow', 'winter_r', 'piyg', 'nipy_spectral', 'tempo_r', 'rdgy_r', 'tab20b', 'pastel1_r', 'rdpu_r', 'rdylbu_r', 'rainbow', 'nipy_spectral_r', 'gray', 'purples_r', 'prism_r', 'spectral', 'oxy', 'greys_r', 'terrain', 'paired_r', 'diff', 'rdylgn', 'amp_r', 'wistia_r', 'diff_r', 'ylorbr', 'plasma_r', 'afmhot_r', 'dense_r', 'turbo', 'matter_r', 'copper', 'solar_r', 'algae_r', 'dark2_r', 'gist_earth', 'rdgy', 'ylorrd_r', 'cool_r', 'solar', 'brbg', 'set1_r', 'rain', 'cool', 'bone', 'blues', 'prgn_r', 'turbid_r', 'gist_yarg_r', 'prgn', 'copper_r', 'cubehelix_r', 'viridis', 'cubehelix', 'tarn', 'curl_r', 'binary', 'curl', 'blues_r', 'rain_r', 'turbid', 'spectral_r', 'summer_r', 'pubugn_r', 'set3_r', 'twilight_shifted_r', 'phase', 'pubu', 'gnuplot2_r', 'pubu_r', 'hot_r', 'magma_r', 'rainbow_r', 'speed', 'deep_r', 'tab20', 'gnbu_r', 'orrd', 'bupu', 'gray_r', 'purd', 'balance_r', 'bwr_r', 'greens_r', 'algae', 'rdbu_r', 'gnuplot', 'gist_heat_r', 'rdbu', 'gist_stern_r', 'schwarzwald', 'paired', 'seismic', 'balance'], Query(PydanticUndefined)] = None,
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
    searchid: typing_extensions.Annotated[str, Path(PydanticUndefined)]
) -> str
```

SearchId

    
#### pixel_selection_dependency

```python3
def pixel_selection_dependency(
    pixel_selection: typing_extensions.Annotated[Literal['first', 'highest', 'lowest', 'mean', 'median', 'stdev', 'lastbandlow', 'lastbandhight', 'count'], Query(PydanticUndefined)] = 'first'
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

    
#### search_dependency

```python3
def search_dependency(
    body: titiler.pgstac.model.RegisterMosaic
) -> Tuple[titiler.pgstac.model.PgSTACSearch, titiler.pgstac.model.Metadata]
```

Search parameters.

    
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