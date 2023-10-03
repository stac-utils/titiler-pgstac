`TiTiler.PgSTAC` provides a `MosaicTilerFactory` factory which is an helper functions to create FastAPI router (`fastapi.APIRouter`) with a minimal set of endpoints.

## `titiler.pgstac.factory.MosaicTilerFactory`

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

mosaic = MosaicTilerFactory()
app.include_router(mosaic.router)
```

| Method | URL                                                                       | Output                                  | Description
| ------ | --------------------------------------------------------------------------|---------------------------------------- |--------------
| `POST` | `/register`                                                               | JSON ([Register][register_model])       | Register **Search** query  **OPTIONAL**
| `GET`  | `/list`                                                                   | JSON ([Info][info_model])               | Return **Search** query infos  **OPTIONAL**
| `GET`  | `/{searchid}/info`                                                        | JSON ([Infos][infos_model])             | Return list of **Search** entries with `Mosaic` type  **OPTIONAL**
| `GET`  | `/{searchid}/{lon},{lat}/assets`                                          | JSON                                    | Return a list of assets which overlap a given point
| `GET`  | `/{searchid}/tiles[/{TileMatrixSetId}]/{z}/{x}/{Y}/assets`                | JSON                                    | Return a list of assets which overlap a given tile
| `GET`  | `/{searchid}/tiles[/{TileMatrixSetId}]/{z}/{x}/{y}[@{scale}x][.{format}]` | image/bin                               | Create a web map tile image for a search query and a tile index
| `GET`  | `/{searchid}[/{TileMatrixSetId}]/tilejson.json`                           | JSON ([TileJSON][tilejson_model])       | Return a Mapbox TileJSON document
| `GET`  | `/{searchid}[/{TileMatrixSetId}]/WMTSCapabilities.xml`                    | XML                                     | Return OGC WMTS Get Capabilities
| `GET`  | `/{searchid}[/{TileMatrixSetId}]/map`                                     | HTML                                    | Simple map viewer **OPTIONAL**
| `POST` | `/{searchid}/statistics`                                                  | GeoJSON ([Statistics][statitics_model]) | Return statistics for geojson features **OPTIONAL**
| `GET`  | `/{searchid}/bbox/{minx},{miny},{maxx},{maxy}[/{width}x{height}].{format}`| image/bin                               | Create an image from part of a dataset **OPTIONAL**
| `POST` | `/{searchid}/feature[/{width}x{height}][.{format}]`                       | image/bin                               | Create an image from a GeoJSON feature **OPTIONAL**


## Item

For the `single STAC item` endpoints we use TiTiler's [`MultiBaseTilerFactory`]() with a custom [`path_dependency`]() to use `item` and `collection` path parameter (instead of the default `url` query param).

This custom `path_dependency` will connect to PgSTAC directly to fetch the STAC Item and pass it to a custom [Reader]() based on [`rio_tiler.io.MultiBaseReader`]().

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
