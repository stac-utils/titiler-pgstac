`titiler-pgstac` version 1.0 introduced [many breaking changes](../release-notes.md). This
document aims to help with migrating your code and client application to use `titiler-pgstac~=1.0`.

## Endpoints

### New `/collections/{collection_id}` endpoints

With this new set of endpoints, there is no more need to *register* a PgSTAC Search in advance. The tiler will do it dynamically at request time.

<details>

```python
# Simplified version of the CollectionIdParams
# https://github.com/stac-utils/titiler-pgstac/blob/7da390e42d3abaace5ca9a7172c799289e4cacf7/titiler/pgstac/dependencies.py#L37-L91
def CollectionIdParams(
    request: Request,
    collection_id: Annotated[
        str,
        Path(description="STAC Collection Identifier"),
    ],
) -> str:
    """collection_id Path Parameter"""
    search = model.PgSTACSearch(collections=[collection_id])

    with request.app.state.dbpool.connection() as conn:
        with conn.cursor(row_factory=class_row(model.Search)) as cursor:

            metadata = model.Metadata(
                name=f"Mosaic for '{collection_id}' Collection",
            )
            cursor.execute(
                "SELECT * FROM search_query(%s, _metadata => %s);",
                (
                    search.model_dump_json(by_alias=True, exclude_none=True),
                    metadata.model_dump_json(exclude_none=True),
                ),
            )
            search_info = cursor.fetchone()

    return search_info.id
```

</details>

### `/mosaic/{searchid}` -> `/searches/{search_id}`

We chose to rename the prefix of the PgSTAC Searches endpoints from `/mosaic` to `/searches` to match the collections and items endpoint prefixes.

Note: We also renamed `searchid` to `search_id` but this should be seamless for users.

```python

# before
resp = httpx.get("/mosaic/{{ searchid }}/info")

# now
resp = httpx.get("/searches/{{ search_id }}/info")
```

!!! important

    You can change the *prefix* for the `MosaicTilerFactory`'s endpoints and could
    easily revert this change in your own application.

    ```python
    from fastapi import FastAPI

    from titiler.pgstac.factory import (
        MosaicTilerFactory,
        add_search_list_route,
        add_search_register_route,
    )
    from titiler.pgstac.dependencies import SearchIdParams
    from titiler.pgstac.extensions import searchInfoExtension

    app = FastAPI()

    # STAC Search Endpoints
    searches = MosaicTilerFactory(
        path_dependency=SearchIdParams,
        router_prefix="/mosaic/{search_id}",
        add_statistics=True,
        add_viewer=True,
        add_part=True,
        extensions=[
            searchInfoExtension(),
        ],
    )
    app.include_router(
        searches.router, tags=["STAC Search"], prefix="/mosaic/{search_id}"
    )
    add_search_register_route(
        app,
        prefix="/mosaic",
        tile_dependencies=[
            searches.layer_dependency,
            searches.dataset_dependency,
            searches.pixel_selection_dependency,
            searches.process_dependency,
            searches.rescale_dependency,
            searches.colormap_dependency,
            searches.render_dependency,
            searches.pgstac_dependency,
            searches.reader_dependency,
            searches.backend_dependency,
        ],
        tags=["STAC Search"],
    )
    add_search_list_route(app, prefix="/mosaic", tags=["STAC Search"])
    ```

### `searchid` -> `id`

In `titiler.pgstac.model.RegisterResponse`, model used in `/register` endpoint, we renamed `searchid` by `id`.

```python
# before
resp = httpx.post("/mosaic/register", body={"collections": ["my-collection"], "filter-lang": "cql-json"})
assert resp.json()["searchid"]

# now
resp = httpx.post("/searches/register", body={"collections": ["my-collection"], "filter-lang": "cql-json"})
assert resp.json()["id"]
```

## API

### `PathParams / ItemPathParams` -> `SearchIdParams / ItemIdParams`

We renamed both `PathParams` and `ItemPathParams` classes to `SearchIdParams` and `ItemIdParams` to better match with the `CollectionIdParams` dependency.

### remove `/{search_id}` prefix in `MosaicTilerFactory`

In order to re-use the `MosaicTilerFactory` for *collections* we had to remove the `/{search_id}` prefix which was hardcoded in each endpoint routes. This is now added to the `router_prefix`.

```python
# Before
app = FastAPI()
mosaic = MosaicTilerFactory(
    ...,
    router_prefix="/mosaics"
)
app.include_router(mosaic.router, prefix="/mosaics")

# Now
app = FastAPI()
mosaic = MosaicTilerFactory(
    ...
    router_prefix="/mosaics/{search_id}"
)
app.include_router(mosaic.router, prefix="/mosaics/{search_id}")
```

### `path_dependency` required input for `MosaicTilerFactory` class

With the introduction of the *collections* endpoints, and because we removed the default `{search_id}` prefix, we cannot default to `SearchIdParams` for the `path_dependency` (the dependency which sends the PgSTAC search identifier to the Mosaic Reader) and thus is now a required attribute when initializing the endpoints.

```python
# before
app = FastAPI()
mosaic = MosaicTilerFactory(...)
app.include_router(mosaic.router)

# now
app = FastAPI()
mosaic = MosaicTilerFactory(
    ...,
    path_dependency=lambda: "aaaaaaaaaaaaaa"
)
app.include_router(mosaic.router)
```

### `searchInfoExtension`

We moved the `MosaicTilerFactory` *info* endpoint outside the class to its own extension.

```python
# Before
app = FastAPI()
mosaic = MosaicTilerFactory(...)
app.include_router(mosaic.router)

# Now
app = FastAPI()
mosaic = MosaicTilerFactory(
    ...
    extensions=[
        searchInfoExtension(),
    ]
)
app.include_router(mosaic.router)
```

### `Register` and `List` endpoints

we moved the `/register` and `/list` endpoints creation outside the `MosaicTilerFactory` class because they are not usable for the collection's endpoint and do not need the `/{search_id}` prefix.

```python
# before
from titiler.pgstac.factory import MosaicTilerFactory

mosaic = MosaicTilerFactory(
    ...,
    router_prefix="/{search_id}",
)
app.include_router(mosaic.router, prefix="/{search_id}")

# Now
from titiler.pgstac.factory import (
    MosaicTilerFactory,
    add_search_register_route,
    add_mosaic_register_route,
)

mosaic = MosaicTilerFactory(
    ...,
    router_prefix="/{search_id}",
)
app.include_router(mosaic.router, prefix="/{search_id}")

# add /register endpoint
add_search_register_route(
    app,
    # any dependency we want to validate
    # when creating the tilejson/map links
    tile_dependencies=[
        mosaic.layer_dependency,
        mosaic.dataset_dependency,
        mosaic.pixel_selection_dependency,
        mosaic.process_dependency,
        mosaic.rescale_dependency,
        mosaic.colormap_dependency,
        mosaic.render_dependency,
        mosaic.pgstac_dependency,
        mosaic.reader_dependency,
        mosaic.backend_dependency,
    ],
)
# add /list endpoint
add_search_list_route(app)
```
