Starting with version `0.1.0a7` we've added a `feature()` method to the Mosaic backend which enable reading geojson defined shape for a mosaic (used for the `/statistics` endpoint).

Here is how you can customize `MosaicTilerFactory` to add a *proper* feature endpoint which return an image to the `MosaicTilerFactory`.

!!! Important
    The `feature` method could need to open a lot of items/assets to construct the image, which can impact the performance.

```python
import os
from dataclasses import dataclass

from geojson_pydantic import Feature, FeatureCollection
from rio_tiler.constants import MAX_THREADS

from titiler.core.factory import img_endpoint_params
from titiler.core.resources.enums import ImageType, OptionalHeader
from titiler.core.utils import Timer
from titiler.mosaic.resources.enums import PixelSelectionMethod
from titiler.pgstac import factory as TitilerPgSTACFactory
from titiler.pgstac.dependencies import PgSTACParams

from fastapi import Body, Depends, Path, Query

from starlette.requests import Request
from starlette.responses import Response


@dataclass
class MosaicTilerFactory(TitilerPgSTACFactory.MosaicTilerFactory):
    """Custom endpoints factory."""

    def register_routes(self) -> None:
        """This Method register routes to the router."""
        super().register_routes()

    # POST endpoints
    @self.router.post(
        "/{searchid}/feature", **img_endpoint_params,
    )
    @self.router.post(
        "/{searchid}/feature.{format}", **img_endpoint_params,
    )
    def geojson_crop(
        request: Request,
        searchid=Depends(self.path_dependency),
        geojson: Feature = Body(..., description="GeoJSON Feature."),
        format: ImageType = Query(
            None, description="Output image type. Default is auto."
        ),
        layer_params=Depends(self.layer_dependency),
        dataset_params=Depends(self.dataset_dependency),
        pixel_selection: PixelSelectionMethod = Query(
            PixelSelectionMethod.first, description="Pixel selection method."
        ),
        max_size: int = Query(1024, description="Maximum image size to read onto."),
        post_process=Depends(self.process_dependency),
        rescale: Optional[List[Tuple[float, ...]]] = Depends(RescalingParams),
        color_formula: Optional[str] = Query(
            None,
            title="Color Formula",
            description="rio-color formula (info: https://github.com/mapbox/rio-color)",
        ),
        colormap=Depends(self.colormap_dependency),
        render_params=Depends(self.render_dependency),
        pgstac_params: PgSTACParams = Depends(),
    ):
        """Create image from a geojson feature."""
        timings = []
        headers: Dict[str, str] = {}

        threads = int(os.getenv("MOSAIC_CONCURRENCY", MAX_THREADS))

        with Timer() as t:
            with rasterio.Env(**self.gdal_config):
                with self.reader(
                    searchid,
                    pool=request.app.state.dbpool,
                    **self.backend_options,
                ) as src_dst:
                    mosaic_read = t.from_start
                    timings.append(("mosaicread", round(mosaic_read * 1000, 2)))

                    image, _ = src_dst.feature(
                        geojson.dict(exclude_none=True),
                        pixel_selection=pixel_selection.method(),
                        threads=threads,
                        max_size=max_size,
                        **layer_params,
                        **dataset_params,
                        **pgstac_params,
                    )

        timings.append(("dataread", round(t.elapsed * 1000, 2)))

        with Timer() as t:
            if post_process:
                image = post_process(image)

            if rescale:
                image.rescale(rescale)

            if color_formula:
                image.apply_color_formula(color_formula)
        timings.append(("postprocess", round(t.elapsed * 1000, 2)))

        if not format:
            format = ImageType.jpeg if image.mask.all() else ImageType.png

        with Timer() as t:
            content = image.render(
                img_format=format.driver,
                colormap=colormap,
                **format.profile,
                **render_params,
            )
        timings.append(("format", round(t.elapsed * 1000, 2)))

        if OptionalHeader.server_timing in self.optional_headers:
            headers["Server-Timing"] = ", ".join(
                [f"{name};dur={time}" for (name, time) in timings]
            )

        if OptionalHeader.x_assets in self.optional_headers:
            ids = [x["id"] for x in data.assets]
            headers["X-Assets"] = ",".join(ids)

        return Response(content, media_type=format.mediatype, headers=headers)
```
