

## Mosaics: `titiler.pgstac.factory.MosaicTilerFactory`

`TiTiler.PgSTAC` provides a `MosaicTilerFactory` factory which is an helper functions to create FastAPI router (`fastapi.APIRouter`) with a minimal set of endpoints.

```python
# Minimal PgSTAC Mosaic Application
from contextlib import asynccontextmanager

from fastapi import FastAPI
from titiler.pgstac.db import close_db_connection, connect_to_db
from titiler.pgstac.factory import MosaicTilerFactory

@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI Lifespan."""
    # Create Connection Pool
    await connect_to_db(app)
    yield
    # Close the Connection Pool
    await close_db_connection(app)


app = FastAPI(lifespan=lifespan)

mosaic = MosaicTilerFactory(
    path_dependency=lambda: "aaaaaaaaaaaaaaaaaaaaa",
)
app.include_router(mosaic.router)
```

!!! Important

    The `MosaicTilerFactory` requires a `path_dependency`, which should be a `Callable` that return a *search_id* (PgSTAC Search Hash).

    For the `/searches/{search_id}` endpoints the `path_dependency` is set to `titiler.pgstac.dependencies.SearchIdParams` and to `titiler.pgstac.dependencies.CollectionIdParams` for the `/collections/{collection_id}` endpoints.
`


| Method | URL                                                                        | Output                                  | Description
| ------ | ---------------------------------------------------------------------------|---------------------------------------- |--------------
| `GET`  | `/{lon},{lat}/assets`                                          | JSON                                    | Return a list of assets which overlap a given point
| `GET`  | `/tiles[/{TileMatrixSetId}]/{z}/{x}/{Y}/assets`                | JSON                                    | Return a list of assets which overlap a given tile
| `GET`  | `/tiles[/{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]` | image/bin                               | Create a web map tile image for a search query and a tile index
| `GET`  | `[/{TileMatrixSetId}]/tilejson.json`                           | JSON ([TileJSON][tilejson_model])       | Return a Mapbox TileJSON document
| `GET`  | `[/{TileMatrixSetId}]/WMTSCapabilities.xml`                    | XML                                     | Return OGC WMTS Get Capabilities
| `GET`  | `[/{TileMatrixSetId}]/map`                                     | HTML                                    | Simple map viewer **OPTIONAL**
| `POST` | `/statistics`                                                  | GeoJSON ([Statistics][statitics_model]) | Return statistics for geojson features **OPTIONAL**
| `GET`  | `/bbox/{minx},{miny},{maxx},{maxy}[/{width}x{height}].{format}`| image/bin                               | Create an image from part of a dataset **OPTIONAL**
| `POST` | `/feature[/{width}x{height}][.{format}]`                       | image/bin                               | Create an image from a GeoJSON feature **OPTIONAL**

### Extensions

#### `searchInfoExtension`

| Method | URL                                                                        | Output                                  | Description
| ------ | ---------------------------------------------------------------------------|---------------------------------------- |--------------
| `GET`  | `/info`                                                        | JSON ([Infos][infos_model])             | Return list of **Search** entries with `Mosaic` type  **OPTIONAL**

```python
app = FastAPI()
mosaic = MosaicTilerFactory(
    path_dependency=lambda: "aaaaaaaaaaaaaaaaaaaaa",
    extensions=[
        searchInfoExtension(),
    ],
)
app.include_router(mosaic.router)
```

#### `register and list`

| Method | URL                                                                        | Output                                  | Description
| ------ | ---------------------------------------------------------------------------|---------------------------------------- |--------------
| `POST` | `/register`                                                                | JSON ([Register][register_model])       | Register **Search** query  **OPTIONAL**
| `GET`  | `/list`                                                                    | JSON ([Info][info_model])               | Return **Search** query infos  **OPTIONAL**

```python
app = FastAPI()
mosaic = MosaicTilerFactory(
    path_dependency=lambda: "aaaaaaaaaaaaaaaaaaaaa",
)
app.include_router(mosaic.router)

add_search_register_route(app)
add_search_list_route(app)
```

## Items: `titiler.core.factory.MultiBaseTilerFactory`

For the `single STAC item` endpoints we use TiTiler's [MultiBaseTilerFactory](https://developmentseed.org/titiler/advanced/tiler_factories/#titilercorefactorymultibasetilerfactory) with a custom [`path_dependency`]() to use `item_id` and `collection_id` path parameter (instead of the default `url` query param).

This custom `path_dependency` will connect to PgSTAC directly to fetch the STAC Item and pass it to a custom [Reader](https://github.com/stac-utils/titiler-pgstac/blob/d777eca04770622982121daa2df42d429e8c244d/titiler/pgstac/reader.py#L17-L25).

```python
# Minimal PgSTAC Item Application
from contextlib import asynccontextmanager

from fastapi import FastAPI

from titiler.core.factory import MultiBaseTilerFactory

from titiler.pgstac.db import close_db_connection, connect_to_db
from titiler.pgstac.dependencies import ItemPathParams
from titiler.pgstac.reader import PgSTACReader


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI Lifespan."""
    # Create Connection Pool
    await connect_to_db(app)
    yield
    # Close the Connection Pool
    await close_db_connection(app)


app = FastAPI(lifespan=lifespan)

item = MultiBaseTilerFactory(
    reader=PgSTACReader,
    path_dependency=ItemPathParams,
    router_prefix="/collections/{collection_id}/items/{item_id}",
)
app.include_router(item.router, prefix="/collections/{collection_id}/items/{item_id}")
```

[tilejson_model]: https://github.com/developmentseed/titiler/blob/2335048a407f17127099cbbc6c14e1328852d619/src/titiler/core/titiler/core/models/mapbox.py#L16-L38
[info_model]: https://github.com/stac-utils/titiler-pgstac/blob/047315da8851a974660032ca45f219db2c3a8d54/titiler/pgstac/model.py#L236-L240
[infos_model]: https://github.com/stac-utils/titiler-pgstac/blob/4f569fee1946f853be9b9149cb4dd2fd5c62b110/titiler/pgstac/model.py#L260-L265
[register_model]: https://github.com/stac-utils/titiler-pgstac/blob/047315da8851a974660032ca45f219db2c3a8d54/titiler/pgstac/model.py#L229-L233
[statitics_model]: https://github.com/developmentseed/titiler/blob/17cdff2f0ddf08dbd9a47c2140b13c4bbcc30b6d/src/titiler/core/titiler/core/models/responses.py#L49-L52
