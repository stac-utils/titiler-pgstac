
Goal: enable support of Zarr/NetCDF assets.

By default titiler-pgstac (which is using rio-tiler's STACReader to access dataset) will only support 2D dataset (https://github.com/cogeotiff/rio-tiler/blob/83e8fc4ed765445d1aa0267cc3bccee15664b9b3/rio_tiler/io/stac.py#L42-L53). In this example we will create customized Readers enabling Zarr/NetCDF assets to use in the endpoint factories.

### 1. Custom STAC Readers

We need a Custom STACReader which can handle a new `md://{assetName}?variable={variableName}`. Note: here are the other query-parameters options https://github.com/developmentseed/titiler/blob/a1955706f02671cefac7e2806e43bab46f2a04dd/src/titiler/xarray/titiler/xarray/io.py#L252-L262

```python

import warnings
from typing import Optional, Set, Type, Tuple, Dict
from urllib.parse import urlparse, parse_qsl

import attr
from rio_tiler.types import AssetInfo
from rio_tiler.io import BaseReader, Reader
from rio_tiler.io.stac import DEFAULT_VALID_TYPE, STAC_ALTERNATE_KEY
from rio_tiler.errors import InvalidAssetName

from titiler.pgstac import reader
from titiler.xarray.io import Reader as XarrayReader


# Items Reader
# Used for `/collections/{collection_id}/items/{item_id}` endpoints
@attr.s
class PgSTACReader(reader.PgSTACReader):
    """

    Example:

        import httpx
        import pystac

        item = pystac.Item.from_dict(httpx.get("https://raw.githubusercontent.com/cogeotiff/rio-tiler/refs/heads/main/tests/fixtures/stac_netcdf.json").json())

        with PgSTACReader(item) as src:
            print(src)
            print(src._get_asset_info("netcdf"))
            print(src._get_reader(src._get_asset_info("netcdf")))
            print(src._get_reader(src._get_asset_info("md://netcdf?variable=data")))
            print(src._get_reader(src._get_asset_info("vrt://netcdf?sd_name=data")))

        >> PgSTACReader(bounds=(-170.085, 79.91999999999659, 169.91499999997504, -80.08), crs=CRS.from_epsg(4326), transform=[0.16999999999998752, 0, -170.085, 0, 0.1599999999999966, -80.08, 0, 0, 1], height=1000, width=2000, input=<Item id=my_stac>, tms=<TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>, minzoom=0, maxzoom=3, include_assets=None, exclude_assets=None, exclude_asset_types=None, assets=['geotiff', 'netcdf'], default_assets=None, reader=<class 'rio_tiler.io.rasterio.Reader'>, reader_options={}, ctx=<class 'rasterio.env.Env'>, item=<Item id=my_stac>, fetch_options=NOTHING, include_asset_types=['image/tiff; application=geotiff', 'image/tiff; profile=cloud-optimized; application=geotiff', 'application/x-hdf', 'image/jp2', 'application/x-hdf5', 'image/tiff', 'image/tiff; application=geotiff; profile=cloud-optimized', 'image/x.geotiff', 'image/vnd.stac.geotiff; cloud-optimized=true', 'application/x-netcdf', 'application/x-zarr', 'application/vnd+zarr'])
        >> {'url': 'dataset_2d.nc', 'metadata': {}, 'media_type': 'application/x-netcdf'}
        >> (<class 'titiler.xarray.io.Reader'>, {})
        >> (<class 'titiler.xarray.io.Reader'>, {'variable': 'data'})
        >> (<class 'rio_tiler.io.rasterio.Reader'>, {})

    """

    include_asset_types: Set[str] = attr.ib(
        default=[
            *DEFAULT_VALID_TYPE,
            "application/x-netcdf",
            "application/x-zarr",
            "application/vnd+zarr",
        ]
    )

    def _get_reader(self, asset_info: AssetInfo) -> Tuple[Type[BaseReader], Dict]:
        """Get Asset Reader."""
        asset_type = asset_info.get("media_type", None)
        if (
            asset_type and
            asset_type in [
                "application/x-netcdf",
                "application/x-zarr",
                "application/vnd+zarr"
            ] and
            not asset_info["url"].startswith("vrt://")
        ):
            return XarrayReader, asset_info.get("reader_options", {})

        return Reader, asset_info.get("reader_options", {})

    def _parse_md_asset(self, asset: str) -> Tuple[str, Optional[str]]:
        """Parse md:// prefixed asset."""
        if asset.startswith("md://") and asset not in self.assets:
            parsed = urlparse(asset)
            if not parsed.netloc:
                raise InvalidAssetName(
                    f"'{asset}' is not valid, couldn't find valid asset"
                )

            if parsed.netloc not in self.assets:
                raise InvalidAssetName(
                    f"'{parsed.netloc}' is not valid, should be one of {self.assets}"
                )


            return parsed.netloc, dict(parse_qsl(parsed.query))

        return asset, None


    # We need a Custom _get_asset_info method to handle
    # `md://{asset}:{variable}` form
    def _get_asset_info(self, asset: str) -> AssetInfo:
        # Catch vrt://{assetName}?{vrtOptions}
        asset, vrt_options = self._parse_vrt_asset(asset)

        # Catch md://{assetName}?{readerOptions}
        asset, reader_options = self._parse_md_asset(asset)

        if asset not in self.assets:
            raise InvalidAssetName(
                f"'{asset}' is not valid, should be one of {self.assets}"
            )

        asset_info = self.item.assets[asset]
        extras = asset_info.extra_fields

        info = AssetInfo(
            url=asset_info.get_absolute_href() or asset_info.href,
            metadata=extras if not vrt_options else None,
        )

        if STAC_ALTERNATE_KEY and extras.get("alternate"):
            if alternate := extras["alternate"].get(STAC_ALTERNATE_KEY):
                info["url"] = alternate["href"]

        if asset_info.media_type:
            info["media_type"] = asset_info.media_type

        # https://github.com/stac-extensions/file
        if head := extras.get("file:header_size"):
            info["env"] = {"GDAL_INGESTED_BYTES_AT_OPEN": head}

        # https://github.com/stac-extensions/raster
        if extras.get("raster:bands") and not vrt_options:
            bands = extras.get("raster:bands")
            stats = [
                (b["statistics"]["minimum"], b["statistics"]["maximum"])
                for b in bands
                if {"minimum", "maximum"}.issubset(b.get("statistics", {}))
            ]
            # check that stats data are all double and make warning if not
            if (
                stats
                and all(isinstance(v, (int, float)) for stat in stats for v in stat)
                and len(stats) == len(bands)
            ):
                info["dataset_statistics"] = stats
            else:
                warnings.warn(
                    "Some statistics data in STAC are invalid, they will be ignored."
                )

        if vrt_options:
            # Construct VRT url
            info["url"] = f"vrt://{info['url']}?{vrt_options}"

        if reader_options is not None:
            # NOTE: add `reader_options`,
            # not defined in AssetInfo structure
            info["reader_options"] = reader_options

        return info


# PgSTAC Backend Simple Reader
# Used for `/collections/{collection_id}` and `/searches/{search_id}` endpoints
# PgSTAC will return Items in form of Simple Dictionary
@attr.s
class SimpleSTACReader(reader.SimpleSTACReader):

    """
    Example:

        item =     {
            "id": "IAMASTACITEM",
            "collection": "mycollection",
            "bbox": (0, 0, 10, 10),
            "assets": {
                "COG": {
                    "href": "https://somewhereovertherainbow.io/cog.tif"
                },
                "NETCDF": {
                    "href": "https://somewhereovertherainbow.io/cog.nc",
                    "type": "application/x-netcdf"
                }
            }
        }

        with SimpleSTACReader(item) as src:
            print(src)
            print(src._get_asset_info("NETCDF"))
            print(src._get_reader(src._get_asset_info("NETCDF")))
            print(src._get_reader(src._get_asset_info("md://NETCDF?variable=data")))
            print(src._get_reader(src._get_asset_info("vrt://NETCDF?sd_name=data")))

        >> SimpleSTACReader(bounds=(0, 0, 10, 10), crs=CRS.from_epsg(4326), transform=None, height=None, width=None, input={'id': 'IAMASTACITEM', 'collection': 'mycollection', 'bbox': (0, 0, 10, 10), 'assets': {'COG': {'href': 'https://somewhereovertherainbow.io/cog.tif'}, 'NETCDF': {'href': 'https://somewhereovertherainbow.io/cog.nc', 'media_type': 'application/x-netcdf'}}}, tms=<TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>, minzoom=0, maxzoom=24, assets=['COG', 'NETCDF'], default_assets=None, reader=<class 'rio_tiler.io.rasterio.Reader'>, reader_options={}, ctx=<class 'rasterio.env.Env'>)
        >> {'url': 'https://somewhereovertherainbow.io/cog.nc', 'env': {}, 'media_type': 'application/x-netcdf'}
        >> (<class 'titiler.xarray.io.Reader'>, {})
        >> (<class 'titiler.xarray.io.Reader'>, {'variable': 'data'})
        >> (<class 'rio_tiler.io.rasterio.Reader'>, {})

    """

    def _get_reader(self, asset_info: AssetInfo) -> Tuple[Type[BaseReader], Dict]:
        """Get Asset Reader."""
        asset_type = asset_info.get("media_type", None)
        if (
            asset_type and
            asset_type in [
                "application/x-netcdf",
                "application/x-zarr",
                "application/vnd+zarr"
            ] and
            not asset_info["url"].startswith("vrt://")
        ):
            return XarrayReader, asset_info.get("reader_options", {})

        return Reader, asset_info.get("reader_options", {})

    def _parse_vrt_asset(self, asset: str) -> Tuple[str, Optional[str]]:
        if asset.startswith("vrt://") and asset not in self.assets:
            parsed = urlparse(asset)
            if not parsed.netloc:
                raise InvalidAssetName(
                    f"'{asset}' is not valid, couldn't find valid asset"
                )

            if parsed.netloc not in self.assets:
                raise InvalidAssetName(
                    f"'{parsed.netloc}' is not valid, should be one of {self.assets}"
                )

            return parsed.netloc, parsed.query

        return asset, None

    def _parse_md_asset(self, asset: str) -> Tuple[str, Optional[str]]:
        """Parse md:// prefixed asset."""
        if asset.startswith("md://") and asset not in self.assets:
            parsed = urlparse(asset)
            if not parsed.netloc:
                raise InvalidAssetName(
                    f"'{asset}' is not valid, couldn't find valid asset"
                )

            if parsed.netloc not in self.assets:
                raise InvalidAssetName(
                    f"'{parsed.netloc}' is not valid, should be one of {self.assets}"
                )


            return parsed.netloc, dict(parse_qsl(parsed.query))

        return asset, None

    # We need a Custom _get_asset_info method to handle
    # `md://{asset}:{variable}` form
    def _get_asset_info(self, asset: str) -> AssetInfo:
        # Catch vrt://{assetName}?{vrtOptions}
        asset, vrt_options = self._parse_vrt_asset(asset)

        # Catch md://{assetName}?{readerOptions}
        asset, reader_options = self._parse_md_asset(asset)

        if asset not in self.assets:
            raise InvalidAssetName(
                f"'{asset}' is not valid, should be one of {self.assets}"
            )

        asset_info = self.input["assets"][asset]
        info = AssetInfo(
            url=asset_info["href"],
            env={},
        )

        if media_type := asset_info.get("type"):
            info["media_type"] = media_type

        if header_size := asset_info.get("file:header_size"):
            info["env"]["GDAL_INGESTED_BYTES_AT_OPEN"] = header_size

        if bands := asset_info.get("raster:bands"):
            stats = [
                (b["statistics"]["minimum"], b["statistics"]["maximum"])
                for b in bands
                if {"minimum", "maximum"}.issubset(b.get("statistics", {}))
            ]
            if len(stats) == len(bands):
                info["dataset_statistics"] = stats

        if vrt_options:
            # Construct VRT url
            info["url"] = f"vrt://{info['url']}?{vrt_options}"

        if reader_options is not None:
            # NOTE: add `reader_options`,
            # not defined in AssetInfo structure
            info["reader_options"] = reader_options

        return info
```

### 2. Create Application

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from titiler.pgstac.dependencies import (
    CollectionIdParams,
    ItemIdParams,
    SearchIdParams,
)
from titiler.pgstac.db import close_db_connection, connect_to_db
from titiler.pgstac.factory import MosaicTilerFactory
from titiler.core.factory import MultiBaseTilerFactory

from .custom import SimpleSTACReader, PgSTACReader

postgres_settings = PostgresSettings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI Lifespan."""
    # Create Connection Pool
    await connect_to_db(app, settings=postgres_settings)
    yield
    # Close the Connection Pool
    await close_db_connection(app)


app = FastAPI(
    title=settings.name,
    openapi_url="/api",
    docs_url="/api.html",
    lifespan=lifespan,
)



###############################################################################
# STAC Search Endpoints
searches = MosaicTilerFactory(
    path_dependency=SearchIdParams,
    # Use our Custom Reader
    dataset_reader=SimpleSTACReader,
    router_prefix="/searches/{search_id}",
    add_viewer=True,
)
app.include_router(
    searches.router, tags=["STAC Search"], prefix="/searches/{search_id}"
)

###############################################################################
# STAC COLLECTION Endpoints
collection = MosaicTilerFactory(
    path_dependency=CollectionIdParams,
    # Use our Custom Reader
    dataset_reader=SimpleSTACReader,
    router_prefix="/collections/{collection_id}",
    add_viewer=True,
)
app.include_router(
    collection.router, tags=["STAC Collection"], prefix="/collections/{collection_id}"
)

###############################################################################
# STAC Item Endpoints
stac = MultiBaseTilerFactory(
    # Use our Custom Reader
    reader=PgSTACReader,
    path_dependency=ItemIdParams,
    router_prefix="/collections/{collection_id}/items/{item_id}",
    add_viewer=True,
)
app.include_router(
    stac.router,
    tags=["STAC Item"],
    prefix="/collections/{collection_id}/items/{item_id}",
)
```
