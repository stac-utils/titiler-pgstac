"""Compatibility layer.

Create an AsyncBaseReader from a BaseReader subclass.

"""

import asyncio
from inspect import isclass
from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)

import attr
import morecantile
from rasterio.crs import CRS
from rio_tiler import constants
from rio_tiler.constants import MAX_THREADS, BBox
from rio_tiler.errors import EmptyMosaicError, InvalidMosaicMethod, TileOutsideBounds
from rio_tiler.io import AsyncBaseReader, BaseReader, COGReader
from rio_tiler.models import ImageData, ImageStatistics, Info, Metadata
from rio_tiler.mosaic.methods.base import MosaicMethodBase
from rio_tiler.mosaic.methods.defaults import FirstMethod
from rio_tiler.utils import _chunks

from starlette.concurrency import run_in_threadpool


@attr.s
class AsyncReader(AsyncBaseReader):
    """Async Reader class."""

    src_path: str = attr.ib()
    tms: morecantile.TileMatrixSet = attr.ib(default=constants.WEB_MERCATOR_TMS)

    reader: Type[BaseReader] = COGReader

    def __attrs_post_init__(self):
        """PostInit."""
        self.dataset = self.reader(self.src_path)
        self.bounds = self.dataset.bounds
        self.minzoom = self.dataset.minzoom
        self.maxzoom = self.dataset.maxzoom

        self.assets = getattr(self.dataset, "assets", None)
        self.bands = getattr(self.dataset, "bands", None)
        self.colormap = getattr(self.dataset, "colormap", None)

        return self

    def close(self):
        """Close rasterio dataset."""
        if getattr(self.dataset, "close", None):
            self.dataset.close()

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        self.close()

    async def info(self, **kwargs: Any) -> Coroutine[Any, Any, Info]:
        """Return Dataset's info."""
        return await run_in_threadpool(self.dataset.info, **kwargs)  # type: ignore

    async def stats(
        self, pmin: float = 2.0, pmax: float = 98.0, **kwargs: Any
    ) -> Coroutine[Any, Any, Dict[str, ImageStatistics]]:
        """Return Dataset's statistics."""
        return await run_in_threadpool(self.dataset.stats, pmin, pmax, **kwargs)  # type: ignore

    async def metadata(
        self, pmin: float = 2.0, pmax: float = 98.0, **kwargs: Any
    ) -> Coroutine[Any, Any, Metadata]:
        """Return Dataset's statistics."""
        return await run_in_threadpool(self.dataset.metadata, pmin, pmax, **kwargs)  # type: ignore

    async def tile(
        self, tile_x: int, tile_y: int, tile_z: int, **kwargs: Any
    ) -> Coroutine[Any, Any, ImageData]:
        """Read a Map tile from the Dataset."""
        return await run_in_threadpool(
            self.dataset.tile, tile_x, tile_y, tile_z, **kwargs  # type: ignore
        )

    async def point(
        self, lon: float, lat: float, **kwargs: Any
    ) -> Coroutine[Any, Any, List]:
        """Read a value from a Dataset."""
        return await run_in_threadpool(self.dataset.point, lon, lat, **kwargs)  # type: ignore

    async def part(
        self, bbox: Tuple[float, float, float, float], **kwargs: Any
    ) -> Coroutine[Any, Any, ImageData]:
        """Read a Part of a Dataset."""
        return await run_in_threadpool(self.dataset.part, bbox, **kwargs)  # type: ignore

    async def preview(self, **kwargs: Any) -> Coroutine[Any, Any, ImageData]:
        """Return a preview of a Dataset."""
        return await run_in_threadpool(self.dataset.preview, **kwargs)  # type: ignore

    async def feature(
        self, shape: Dict, **kwargs: Any
    ) -> Coroutine[Any, Any, ImageData]:
        """Return a preview of a Dataset."""
        return await run_in_threadpool(self.dataset.feature, shape, **kwargs)  # type: ignore


async def async_mosaic_reader(
    mosaic_assets: Sequence[str],
    reader: Callable[..., Coroutine[Any, Any, ImageData]],
    *args: Any,
    pixel_selection: Union[Type[MosaicMethodBase], MosaicMethodBase] = FirstMethod,
    chunk_size: Optional[int] = None,
    threads: int = MAX_THREADS,
    allowed_exceptions: Tuple = (TileOutsideBounds,),
    **kwargs,
) -> Tuple[ImageData, List[str]]:
    """Async Version for rio_tiler.mosaic.reader.mosaic_reader.

    Args:

        mosaic_assets (sequence): List of assets.
        reader (callable): Reader function. The function MUST take `(asset, *args, **kwargs)` as arguments, and MUST return an ImageData.
        args (Any): Argument to forward to the reader function.
        pixel_selection (MosaicMethod, optional): Instance of MosaicMethodBase class. Defaults to `rio_tiler.mosaic.methods.defaults.FirstMethod`.
        chunk_size (int, optional): Control the number of asset to process per loop.
        threads (int, optional): Number of threads to use. If <= 1, runs single threaded without an event loop. By default reads from the MAX_THREADS environment variable, and if not found defaults to multiprocessing.cpu_count() * 5.
        allowed_exceptions (tuple, optional): List of exceptions which will be ignored. Note: `TileOutsideBounds` is likely to be raised and should be included in the allowed_exceptions. Defaults to `(TileOutsideBounds, )`.
        kwargs (optional): Reader callable's keywords options.

    Returns:
        tuple: ImageData and assets (list).

    Examples:
        >>> def reader(asset: str, *args, **kwargs) -> ImageData:
                with COGReader(asset) as cog:
                    return cog.tile(*args, **kwargs)

            x, y, z = 10, 10, 4
            img = mosaic_reader(["cog.tif", "cog2.tif"], reader, x, y, z)

        >>> def reader(asset: str, *args, **kwargs) -> ImageData:
                with COGReader(asset) as cog:
                    return cog.preview(*args, **kwargs)

            img = mosaic_reader(["cog.tif", "cog2.tif"], reader)


    """
    if isclass(pixel_selection):
        pixel_selection = cast(Type[MosaicMethodBase], pixel_selection)

        if issubclass(pixel_selection, MosaicMethodBase):
            pixel_selection = pixel_selection()

    if not isinstance(pixel_selection, MosaicMethodBase):
        raise InvalidMosaicMethod(
            "Mosaic filling algorithm should be an instance of "
            "'rio_tiler.mosaic.methods.base.MosaicMethodBase'"
        )

    if not chunk_size:
        chunk_size = threads if threads > 1 else len(mosaic_assets)

    assets_used: List[str] = []
    crs: Optional[CRS] = None
    bounds: Optional[BBox] = None

    for chunks in _chunks(mosaic_assets, chunk_size):
        for img in await asyncio.gather(
            *[reader(asset, *args, **kwargs) for asset in chunks],
            return_exceptions=True,
        ):
            if isinstance(img, allowed_exceptions):
                continue

            crs = img.crs
            bounds = img.bounds

            assets_used.append(img.assets)
            pixel_selection.feed(img.as_masked())

            if pixel_selection.is_done:
                data, mask = pixel_selection.data
                return (
                    ImageData(data, mask, assets=assets_used, crs=crs, bounds=bounds),
                    assets_used,
                )

    data, mask = pixel_selection.data
    if data is None:
        raise EmptyMosaicError("Method returned an empty array")

    return (
        ImageData(data, mask, assets=assets_used, crs=crs, bounds=bounds),
        assets_used,
    )
