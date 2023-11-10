# Module titiler.pgstac.dependencies

titiler-pgstac dependencies.

None

## Variables

```python3
cache_config
```

```python3
retry_config
```

## Functions

    
### ItemPathParams

```python3
def ItemPathParams(
    request: starlette.requests.Request,
    collection_id: typing.Annotated[str, Path(PydanticUndefined)],
    item_id: typing.Annotated[str, Path(PydanticUndefined)]
) -> pystac.item.Item
```

    
STAC Item dependency.

    
### PathParams

```python3
def PathParams(
    searchid: typing.Annotated[str, Path(PydanticUndefined)]
) -> str
```

    
SearchId

    
### SearchParams

```python3
def SearchParams(
    body: titiler.pgstac.model.RegisterMosaic
) -> Tuple[titiler.pgstac.model.PgSTACSearch, titiler.pgstac.model.Metadata]
```

    
Search parameters.

    
### TileParams

```python3
def TileParams(
    z: typing.Annotated[int, Path(PydanticUndefined)],
    x: typing.Annotated[int, Path(PydanticUndefined)],
    y: typing.Annotated[int, Path(PydanticUndefined)]
) -> morecantile.commons.Tile
```

    
Tile parameters.

## Classes

### BackendParams

```python3
class BackendParams(
    request: starlette.requests.Request
)
```

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
    scan_limit: Annotated[Optional[int], Query(PydanticUndefined)] = None,
    items_limit: Annotated[Optional[int], Query(PydanticUndefined)] = None,
    time_limit: Annotated[Optional[int], Query(PydanticUndefined)] = None,
    exitwhenfull: Annotated[Optional[bool], Query(PydanticUndefined)] = None,
    skipcovered: Annotated[Optional[bool], Query(PydanticUndefined)] = None
)
```

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