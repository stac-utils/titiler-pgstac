Starting with version `0.1.0a7` we've added a `feature()` method to the Mosaic backend which enable reading geojson defined shape for a mosaic (used for the `/statistics` endpoint).

Here is how you can customize `MosaicTilerFactory` to add a *proper* feature endpoint which return an image to the `MosaicTilerFactory`.

!!! Important
    The `feature` method could need to open a lot of items/assets to construct the image, which can impact the performance.

```python
import os
import sys
from typing import Optional
from dataclasses import dataclass

from geojson_pydantic import Feature
from rio_tiler.constants import MAX_THREADS

from titiler.core.factory import img_endpoint_params
from titiler.core.resources.enums import ImageType, OptionalHeader
from titiler.pgstac import factory as TitilerPgSTACFactory
from titiler.pgstac.dependencies import PgSTACParams

from fastapi import Body, Depends, Query

from starlette.requests import Request
from starlette.responses import Response

if sys.version_info >= (3, 9):
    from typing import Annotated  # pylint: disable=no-name-in-module
else:
    from typing_extensions import Annotated


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
            geojson: Annotated[
                Feature,
                Body(description="GeoJSON Feature."),
            ],
            searchid=Depends(self.path_dependency),
            format: Annotated[
                ImageType,
                "Default will be automatically defined if the output image needs a mask (png) or not (jpeg).",
            ] = None,
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            pixel_selection=Depends(self.pixel_selection_dependency),
            buffer: Annotated[
                Optional[float],
                Query(
                    gt=0,
                    title="Tile buffer.",
                    description="Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).",
                ),
            ] = None,
            post_process=Depends(self.process_dependency),
            rescale=Depends(self.rescale_dependency),
            color_formula: Annotated[
                Optional[str],
                Query(
                    title="Color Formula",
                    description="rio-color formula (info: https://github.com/mapbox/rio-color)",
                ),
            ] = None,
            colormap=Depends(self.colormap_dependency),
            render_params=Depends(self.render_dependency),
            pgstac_params: PgSTACParams = Depends(),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Create image from a geojson feature."""
            threads = int(os.getenv("MOSAIC_CONCURRENCY", MAX_THREADS))

            with rasterio.Env(**self.gdal_config):
                with self.reader(
                    searchid,
                    reader_options={**reader_params},
                    **backend_params,
                ) as src_dst:
                    image, assets = src_dst.feature(
                        geojson.dict(exclude_none=True),
                        pixel_selection=pixel_selection.method(),
                        threads=threads,
                        max_size=max_size,
                        **layer_params,
                        **dataset_params,
                        **pgstac_params,
                    )

            if post_process:
                image = post_process(image)

            if rescale:
                image.rescale(rescale)

            if color_formula:
                image.apply_color_formula(color_formula)

            if colormap:
                image = image.apply_colormap(colormap)

            if not format:
                format = ImageType.jpeg if image.mask.all() else ImageType.png

            content = image.render(
                img_format=format.driver,
                **format.profile,
                **render_params,
            )

            headers: Dict[str, str] = {}
            if OptionalHeader.x_assets in self.optional_headers:
                ids = [x["id"] for x in assets]
                headers["X-Assets"] = ",".join(ids)

            return Response(content, media_type=format.mediatype, headers=headers)
```
