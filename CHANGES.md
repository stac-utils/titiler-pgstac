# Release Notes

## 1.2.2 (2024-02-21)

* enable passing `ConnectionPool` *kwargs* option in `titiler.pgstac.db.connect_to_db` function (author @smohiudd, https://github.com/stac-utils/titiler-pgstac/pull/155)

## 1.2.1 (2024-01-19)

* fix invalid url parsing in HTML responses

## 1.2.0 (2024-01-17)

* update titiler requirement to `>=0.17.0,<0.18`
* use new `align_bounds_with_dataset=True` rio-tiler option in GeoJSON statistics methods for more precise calculation

## 1.1.0 (2024-01-10)

* update titiler requirement to `>=0.16.0,<0.17`
* use morecantile `TileMatrixSet.cellSize` property instead of deprecated/private `TileMatrixSet._resolution` method (author @hrodmn, https://github.com/stac-utils/titiler-pgstac/pull/148)
* add `/point/{lon},{lat}` endpoint in `MosaicTilerFactory` (co-author @hrodmn, https://github.com/stac-utils/titiler-pgstac/pull/150)

## 1.0.0 (2023-12-12)

* no change since `1.0.0a4`

## 1.0.0a4 (2023-11-10)

* add `algorithm` options for `/statistics [POST]` endpoints (back-ported from 0.8.1)

## 1.0.0a3 (2023-11-03)

* remove `reverse` option in `PGSTACBackend` mosaic backend. Reverse item order should be achieved with STAC search sortby.

## 1.0.0a2 (2023-11-02)

* update titiler's dependency to `>=0.15.2,<0.16`
* rename `dependencies.TileParams` to `dependencies.TmsTileParams`

## 1.0.0a1 (2023-10-20)

* rename `dependencies.ItemPathParams` to `ItemIdParams` **breaking change**

## 1.0.0a0 (2023-10-20)

* add `pgstac_dependency` attribute in `MosaicTilerFactory` (defaults to `dependencies.PgSTACParams`)

* add database's `pool` check in startup event

* add *metadata layers* links in mosaic's `/info` response for TileJSON, map and wmts endpoint links

* add `CollectionIdParams` dependency to retrieve a SearchId for a CollectionId

* add `/collections/{collection_id}` virtual mosaic endpoints

* update endpoints Tags (`STAC Search`, `STAC Collection`, `STAC Item`)

### Endpoint breaking changes

* move PgSTAC Search Virtual Mosaic's endpoints from `/mosaic` to `/searches`

* in `model.RegisterResponse` (model used in `/register` endpoint) rename `searchid` by `id`

    ```python
    # before
    resp = httpx.post("/mosaic/register", body={"collections": ["my-collection"], "filter-lang": "cql-json"})
    assert resp.json()["searchid"]

    # now
    resp = httpx.post("/searches/register", body={"collections": ["my-collection"], "filter-lang": "cql-json"})
    assert resp.json()["id"]
    ```

### API breaking changes

* rename `dependencies.PathParams` to `dependencies.SearchIdParams`

* rename `searchid` path parameter to `search_id` in `SearchIdParams`

* move `check_query_params` methods outside `MosaicTilerFactory` class

* make `path_dependency` a required input to `MosaicTilerFactory` class

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


* remove `/{search_id}` prefix in `MosaicTilerFactory` routes. Now use parameter injection from global prefix

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

* move `/info` endpoint outside the `MosaicTilerFactory` to its own *extension* (`titiler.pgstac.extension.searchInfoExtension`)

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

* move `/register` and `/list` endpoint creation outside the `MosaicTilerFactory` class

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

## 0.8.2 (2024-01-23)

* update rio-tiler version to `>6.3.0` (defined in `titiler>=0.17`)
* use new `align_bounds_with_dataset=True` rio-tiler option in GeoJSON statistics methods for more precise calculation [backported from 1.2.0]
* use morecantile `TileMatrixSet.cellSize` property instead of deprecated/private TileMatrixSet._resolution method [backported from 1.1.0]

## 0.8.1 (2023-11-10)

* add `algorithm` options for `/statistics [POST]` endpoints

## 0.8.0 (2023-10-06)

* update titiler requirement to `>=0.15.0,<0.16`
* remove `max_size` default for mosaic's `/statistics [POST]` endpoint  **breaking change**
* add `/bbox` and `/feature [POST]` optional endpoints
* add `img_part_dependency` attribute in `MosaicTilerFactory` (defaults to `titiler.code.dependencies.PartFeatureParams`)

## 0.7.0 (2023-09-28)

* update requirements to switch to pydantic~=2.0
  - pydantic>=2.4,<3.0
  - pydantic-settings~=2.0
  - geojson-pydantic~=1.0
  - cogeo-mosaic>=7.0,<8.0

* update titiler requirement to `>=0.14.0,<0.15`

    - replace `-` by `_` in query parameters

        * coord-crs -> coord_crs
        * dst-crs -> dst_crs

## 0.6.0 (2023-09-18)

* add `tilejson` URL links for `layers` defined in mosaic's metadata in `/mosaic/register` and `/mosaic/{mosaic_id}/info` response
* support multiple `layers` in `/mosaic/{mosaic_id}/WMTSCapabilities.xml` endpoint created from mosaic's metadata

**breaking change**

* In `/mosaic/WMTSCapabilities.xml` we removed the query-parameters related to the `tile` endpoint (which are forwarded) so `?assets=` is no more required.
The endpoint will still raise an error if there are no `layers` in the mosaic metadata and no required tile's parameters are passed.

    ```python
    # before
    response = httpx.get("/mosaic/{mosaic_id}/WMTSCapabilities.xml")
    assert response.status_code == 400

    response = httpx.get("/mosaic/{mosaic_id}/WMTSCapabilities.xml?assets=cog")
    assert response.status_code == 200

    # now
    # If the mosaic has `defaults` layers set in the metadata
    # we will construct a WMTS document with multiple layers, so no need for the user to pass any `assets=`
    response = httpx.get("/mosaic/{mosaic_id}/WMTSCapabilities.xml")
    assert response.status_code == 200
    with rasterio.open(io.BytesIO(response.content)) as src:
        assert src.profile["driver"] == "WMTS"
        assert len(src.subdatasets) == 2

    # If the user pass any valid `tile` parameters, an additional layer will be added to the one from the metadata
    response = httpx.get("/mosaic/{mosaic_id}/WMTSCapabilities.xml?assets=cog")
    assert response.status_code == 200
    with rasterio.open(io.BytesIO(response.content)) as src:
        assert src.profile["driver"] == "WMTS"
        assert len(src.subdatasets) == 3
    ```

## 0.5.1 (2023-08-03)

* add `python-dotenv` requirement

## 0.5.0 (2023-07-20)

* update `titiler` requirement to `>=0.12.0,<0.13`
* use `Annotated` Type for Query/Path parameters
* re-order endpoints in `MosaicTilerFactory` to avoid conflicts between `tiles` and `assets` endpoints
* remove `stac-pydantic` dependency
* add optional `root_path` setting to specify a url path prefix to use when running the app behind a reverse proxy
* add landing page `/`
* use `lifespan` option instead of deprecated `@app.on_event` method to initiate/close DB connection

**breaking changes**

* remove deprecated `/{searchid}/{z}/{x}/{y}/assets` endpoints
* use /api and /api.html for documentation (instead of /openapi.json and /docs)
* replace Enum's with `Literal` types
* replace variable `TileMatrixSetId` by `tileMatrixSetId`
* add `pixel_selection_dependency` attribute to the `MosaicTilerFactory`

## 0.4.1 (2023-06-21)

* update `titiler` requirement to `>=0.11.7`
* fix `/map` endpoint template name
* rename `add_map_viewer` to `add_viewer` option in `MosaicTilerFactory` for consistency with `titiler's` options

## 0.4.0 (2023-05-22)

* remove deprecated `/tiles/{searchid}/...` endpoints (replaced with `/{searchid}/tiles/...`)
* depreciate `/{searchid}/{z}/{x}/{y}/assets` endpoints and add `/{searchid}/tiles/{z}/{x}/{y}/assets`
* update minimum titiler requirement to `>=0.11.6`
* remove timing headers
* add `strict_zoom` option (controled with `MOSAIC_STRICT_ZOOM` environment variable) to raise (or not) error when fetching tile outside mosaic min/max zoom range

## 0.3.3 (2023-04-27)

* update python packaging/build system to `pdm-pep517`
* use `Ruff` for lint
* add retry mechanism on Database connection issues for `PGSTACBackend.get_assets()` and `get_stac_item` methods (back ported from 0.2.4)

## 0.3.2 (2023-03-14)

* update titiler requirement to `0.10.2`
* fix maximum version of FastAPI to 0.92 (to avoid breaking change of starlette >0.25)

## 0.3.1 (2022-12-16)

* update Type information for `dependencies.get_stac_item` (back ported from 0.2.2)

## 0.3.0 (2022-12-16)

**breaking changes**

* Use `/collections/{collection_id}/items/{item_id}` prefix for **Item** endpoint.
    ```
    # Before
    {endpoint}/stac/info?collection=collection1&item=item1

    # Now
    {endpoint}/collections/collection1/items/item1/info
    ```

* Change tile url path parameter order from `/tiles/{searchid}/{TileMatrixSetId}/{z}/{x}/{y}` to `/{searchid}/tiles/{TileMatrixSetId}/{z}/{x}/{y}`
    ```
    # Before
    {endpoint}/mosaic/tiles/20200307aC0853900w361030/0/0/0

    # Now
    {endpoint}/mosaic/20200307aC0853900w361030/tiles/0/0/0
    ```
## 0.2.4 (2023-04-27)

* add retry mechanism on Database connection issues for `PGSTACBackend.get_assets()` and `get_stac_item` methods

## 0.2.3 (2023-03-14)

* fix maximum version of FastAPI to 0.92 (to avoid breaking change of starlette >0.25)

## 0.2.2 (2022-12-16)

* update Type information for `dependencies.get_stac_item`

## 0.2.1 (2022-12-15)

* update titiler requirement to `>=0.10.1,<0.11` and fix `/map` endpoint (to accept multiple TMS)

## 0.2.0 (2022-12-13)

* add python 3.10 and 3.11 support
* update to rio-tiler 4.1
* add `/{searchid}/map` endpoint to the `MosaicTilerFactory` (added when `add_map_viewer` is set to `True`)
* add `/{searchid}/WMTSCapabilities.xml` OGC WMTS endpoint to the `MosaicTilerFactory`
* add `/list` to the `MosaicTilerFactory` to list available mosaics (added when `add_mosaic_list` is set to `True`)

**breaking changes**

* remove python 3.7 support
* update titiler requirement to `>=0.10.0`
* replace `connection_string` by `database_url` in `settings.PostgresSettings`. We can now directly set `DATABASE_URL` environment variable.

#### Frontend changes

- remove `asset_expression` (Mosaic and Item)
- histogram band names are prefixed with `b` (e.g `b1`) (Mosaic and Item) (ref: https://github.com/cogeotiff/rio-tiler/blob/main/docs/src/v4_migration.md#band-names)
- expression for STAC have to be in form of `{asset}_b{band_name}` (e.g `red_b1/green_b1`) (Mosaic and Item) (ref: https://github.com/cogeotiff/rio-tiler/blob/main/docs/src/v4_migration.md#multibasereader-expressions)
- added `asset_as_band` option to force expression to be in form of `{asset}` (e.g `red/green`) (Mosaic and Item)
- expression's band should now be delimited with `;` (previously `,` was accepted) (Mosaic and Item)
- point output model to include band_names (Item)
- added `algorithm` options

## 0.1.0 (2022-06-27)

* update `titiler.core` and `titiler.mosaic` requirement to `0.7`
* add `MosaicTilerFactory._tilejson_routes` method to register `TileJSON` routes
* raise `cogeo_mosaic.errors.MosaicNotFoundError` when SearchId is not found in *pgstac.searches* table

**breaking changes**

* move version definition in `titiler.pgstac.__version__`
* remove unused `fetch_options` in `titiler.pgstac.reader.PgSTACReader`

## 0.1.0a10 (2022-05-16) Pre-Release

* update `titiler` version and add `reader_dependency` and `backend_dependency` in endpoint factory.

## 0.1.0.a9 (2022-05-05) Pre-Release

* remove LRU cache on all settings classes to enable support for manually providing settings via keyword arguments and to minimize lines of code (author @alukach, https://github.com/stac-utils/titiler-pgstac/pull/54)

## 0.1.0.a8 (2022-05-02) Pre-Release

* Insert mosaic metadata `min/max zoom` and `bounds` in tilejson (https://github.com/stac-utils/titiler-pgstac/pull/51)
* allow users the ability to optionally provide `PostgresSettings` to `connect_to_db()` function in the event that they want to customize how their DB credentials are populated (author @alukach, https://github.com/stac-utils/titiler-pgstac/pull/53)

## 0.1.0.a7 (2022-04-05) Pre-Release

* add `feature()` method to `PGSTACBackend` mosaic backend
* add `/statistics` endpoint to return statistics given a GeoJSON feature or featureCollection
* add `collection` in allowed returned fields
* switch to `pgstac.search` to get the STAC Item in `titiler.pgstac.dependencies.get_stac_item` (https://github.com/stac-utils/titiler-pgstac/pull/50)

## 0.1.0.a6 (2022-03-14) Pre-Release

* move dependencies to `titiler.pgstac.dependencies`
* add `/stac` endpoints to work with PgSTAC items

**breaking changes**

* add `/mosaic` prefix to the PgSTAC mosaic endpoints

## 0.1.0.a5 (2022-03-03) Pre-Release

* Add `search_dependency` to allow customization of the PgSTAC Search query (Author @drnextgis, https://github.com/stac-utils/titiler-pgstac/pull/41)
* Add PgSTAC Search entries model (https://github.com/stac-utils/titiler-pgstac/pull/43)
* Add `Metadata` specification (https://github.com/stac-utils/titiler-pgstac/pull/38)

**breaking changes**

* update `titiler.core` and `titiler.mosaic` requirement to `>=0.5`
* When registering a `search` to PgSTAC with the `/register` endpoint, a default metadata `{"type": "mosaic"}` will be set.
* Renamed `titiler.pgstac.models` to `titiler.pgstac.model`
* Renamed `titiler.pgstac.models.SearchQuery` to `titiler.pgstac.model.PgSTACSearch` (and removed `metadata`)
* output response for `/register` endpoint:
```js
// before
{
    "searchid": "...",
    "metadata": "http://endpoint/.../info",
    "tiles": "http://endpoint/.../tilejson.json",
}

// now
{
    "searchid": "...",
    "links": [
        {
            "rel": "info",
            "href": "http://endpoint/.../info",
            "type": "application/json",
        },
        {
            "rel": "tilejson",
            "href": "http://endpoint/.../tilejson.json",
            "type": "application/json",
        }
    ]
}
```

* output response for `/info` endpoint:
```js
// before
{
    "hash": "...",
    "search": {},
    "_where": "...",
    ...
}

// now
{
    "search": {
        "hash": "...",
        "search": {},
        "_where": "...",
        ...
    },
    "links": [
        {
            "rel": "self",
            "href": "http://endpoint/.../info",
            "type": "application/json",
        },
        {
            "rel": "tilejson",
            "href": "http://endpoint/.../tilejson.json",
            "type": "application/json",
        }
    ]
}
```

## 0.1.0.a4 (2022-02-07) Pre-Release

* add tile `buffer` option to match rio-tiler tile options (https://github.com/stac-utils/titiler-pgstac/pull/31)

## 0.1.0.a3 (2021-12-15) Pre-Release

* Forward TMS to the STAC Reader (allow multiple TMS) (https://github.com/stac-utils/titiler-pgstac/pull/28)

## 0.1.0.a2 (2021-12-13) Pre-Release

* Switch to **psycopg3**
* add `filter-lang` in Search model to support newer PgSTAC (with CQL-2)
* add `metadata` in Search model to allow forwarding metadata to the search query entry in PgSTAC

**breaking changes**

* Unify *reader/writer* db pools to `request.app.state.dbpool`
* rename `PostgresSettings.db_max_inactive_conn_lifetime` to `PostgresSettings.max_idle`
* remove `PostgresSettings().reader_connection_string` and `PostgresSettings().writer_connection_string`. Replaced with `PostgresSettings().connection_string`
* update titiler requirement (>= 0.4)

## 0.1.0.a1 (2021-09-15) Pre-Release

* Surface PgSTAC options (`scan_limit`, `items_limit`, `time_limit`, `exitwhenfull` and `skipcovered`) in Tile endpoints

**breaking changes**

* remove `psycopg2` requirements to avoid conflict with `psycopg2-binary` (https://github.com/stac-utils/titiler-pgstac/pull/15)

## 0.1.0.a0 (2021-09-06) Pre-Release

Initial release
