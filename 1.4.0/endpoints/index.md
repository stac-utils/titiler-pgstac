---

title: Endpoints

---

<p align="center">
  <img alt="titiler-pgstac OpenAPI documentation" src="https://github.com/user-attachments/assets/3f6b6b35-c54a-4932-98fc-6c2e11abd19a"/>
</p>

By default the main application (`titiler.pgstac.main.app`) provides three sets of endpoints of access raster dataset:

- [**Searches**](searches_endpoints.md): Dynamic **mosaic** tiler based on PgSTAC Search Query
- [**Collections**](collections_endpoints.md): Dynamic **mosaic** tiler based on STAC Collection
- [**Items**](items_endpoints.md): Dynamic tiler for single STAC item (stored in PgSTAC)

Some optional endpoints:

- [**Assets**](https://developmentseed.org/titiler/advanced/endpoints_factories/#endpoints) (external link): Dynamic tiler a single STAC Asset (stored in PgSTAC), enabled setting `TITILER_PGSTAC_API_ENABLE_ASSETS_ENDPOINTS=TRUE`
- [**External Dataset**](https://developmentseed.org/titiler/advanced/endpoints_factories/#endpoints) (external link): Dynamic tiler a single Cloud Optimized dataset, enabled setting `TITILER_PGSTAC_API_ENABLE_EXTERNAL_DATASET_ENDPOINTS=TRUE`

And some `metadata` endpoints:

- [**TileMatrixSets**](tms_endpoints.md): Available TileMatrixSets for the service
- [**Algorithms**](https://developmentseed.org/titiler/endpoints/algorithms/) (external link): Available Algorithms for the service
- [**Colormaps**](https://developmentseed.org/titiler/endpoints/colormaps/) (external link): Available Colormaps for the service
