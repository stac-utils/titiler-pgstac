# Module titiler.pgstac.dependencies

titiler-pgstac dependencies.

## Variables

```python3
cache_config
```

```python3
retry_config
```

## Functions

    
### CollectionIdParams

```python3
def CollectionIdParams(
    request: starlette.requests.Request,
    collection_id: typing_extensions.Annotated[str, Path(PydanticUndefined)]
) -> str
```

collection_id Path Parameter

    
### ItemIdParams

```python3
def ItemIdParams(
    request: starlette.requests.Request,
    collection_id: typing_extensions.Annotated[str, Path(PydanticUndefined)],
    item_id: typing_extensions.Annotated[str, Path(PydanticUndefined)]
) -> pystac.item.Item
```

STAC Item dependency.

    
### SearchIdParams

```python3
def SearchIdParams(
    search_id: typing_extensions.Annotated[str, Path(PydanticUndefined)]
) -> str
```

search_id

    
### SearchParams

```python3
def SearchParams(
    body: titiler.pgstac.model.RegisterMosaic
) -> Tuple[titiler.pgstac.model.PgSTACSearch, titiler.pgstac.model.Metadata]
```

Search parameters.

    
### TmsTileParams

```python3
def TmsTileParams(
    z: typing_extensions.Annotated[int, Path(PydanticUndefined)],
    x: typing_extensions.Annotated[int, Path(PydanticUndefined)],
    y: typing_extensions.Annotated[int, Path(PydanticUndefined)]
) -> morecantile.commons.Tile
```

TileMatrixSet Tile parameters.

## Classes

### BackendParams

```python3
class BackendParams(
    request: starlette.requests.Request
)
```

backend parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### PgSTACParams

```python3
class PgSTACParams(
    scan_limit: typing_extensions.Annotated[Union[int, NoneType], Query(PydanticUndefined)] = None,
    items_limit: typing_extensions.Annotated[Union[int, NoneType], Query(PydanticUndefined)] = None,
    time_limit: typing_extensions.Annotated[Union[int, NoneType], Query(PydanticUndefined)] = None,
    exitwhenfull: typing_extensions.Annotated[Union[bool, NoneType], Query(PydanticUndefined)] = None,
    skipcovered: typing_extensions.Annotated[Union[bool, NoneType], Query(PydanticUndefined)] = None
)
```

PgSTAC parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
exitwhenfull
```

```python3
items_limit
```

```python3
scan_limit
```

```python3
skipcovered
```

```python3
time_limit
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.