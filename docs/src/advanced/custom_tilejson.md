
Goal: enable users to select a predefined configuration stored in the mosaic Metadata.


```python
import sys
from typing import Optional
from dataclasses import dataclass

from morecantile import TileMatrixSet
from titiler.core.resources.enums import ImageType
from titiler.core.models.mapbox import TileJSON
from titiler.pgstac import factory as TitilerPgSTACFactory
from titiler.pgstac.dependencies import PgSTACParams
from typing_extensions import Annotated

from fastapi import Depends, Query

from starlette.requests import Request


@dataclass
class MosaicTilerFactory(TitilerPgSTACFactory.MosaicTilerFactory):
    """Custom factory."""

    def tilejson(self) -> None:
        """Custom TileJSON endpoint."""

        @self.router.get(
            "/{tileMatrixSetId}/tilejson.json",
            response_model=TileJSON,
            responses={200: {"description": "Return a tilejson"}},
            response_model_exclude_none=True,
        )
        def tilejson(
            request: Request,
            tileMatrixSetId: Annotated[
                Literal[tuple(self.supported_tms.list())],
                Path(
                    description="Identifier selecting one of the TileMatrixSetId supported."
                ),
            ],
            ########################################################
            # CUSTOM: add `layer=` query-parameter
            layer: Annotated[
                str,
                Query(description="Name of default configuration"),
            ] = None,
            ########################################################
            tile_format: Annotated[
                Optional[ImageType],
                Query(
                    description="Default will be automatically defined if the output image needs a mask (png) or not (jpeg).",
                ),
            ] = None,
            tile_scale: Annotated[
                Optional[int],
                Query(
                    gt=0, lt=4, description="Tile size scale. 1=256x256, 2=512x512..."
                ),
            ] = None,
            minzoom: Annotated[
                Optional[int],
                Query(description="Overwrite default minzoom."),
            ] = None,
            maxzoom: Annotated[
                Optional[int],
                Query(description="Overwrite default maxzoom."),
            ] = None,
            search_id=Depends(self.path_dependency),
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
        ):
            """Return TileJSON document for a SearchId."""
            with request.app.state.dbpool.connection() as conn:
                with conn.cursor(row_factory=class_row(model.Search)) as cursor:
                    cursor.execute(
                        "SELECT * FROM searches WHERE hash=%s;",
                        (search_id,),
                    )
                    search_info = cursor.fetchone()
                    if not search_info:
                        raise KeyError(f"search {search_id} not found")

            route_params = {
                "search_id": search_info.id,
                "z": "{z}",
                "x": "{x}",
                "y": "{y}",
                "tileMatrixSetId": tileMatrixSetId,
            }
            if tile_scale:
                route_params["scale"] = tile_scale
            if tile_format:
                route_params["format"] = tile_format.value

            tiles_url = self.url_for(request, "tile", **route_params)

            qs_key_to_remove = [
                "tilematrixsetid",
                "tile_format",
                "tile_scale",
                "minzoom",
                "maxzoom",
                "layer",
            ]
            qs = [
                (key, value)
                for (key, value) in request.query_params._list
                if key.lower() not in qs_key_to_remove
            ]

            if layer:
                config = search_info.metadata.defaults_params.get(layer)
                if not config:
                    raise HTTPException(status_code=404, detail=f"Invalid {layer} configuration.")

                # This assume the default configuration follows the endpoint expected format
                # as `"true_color": {"assets": ["B4", "B3", "B2"]}`
                qs = QueryParams(config)

            if qs:
                tiles_url += f"?{urlencode(qs, doseq=True)}"

            minzoom = _first_value([minzoom, search_info.metadata.minzoom], tms.minzoom)
            maxzoom = _first_value([maxzoom, search_info.metadata.maxzoom], tms.maxzoom)
            bounds = _first_value(
                [search_info.input_search.get("bbox"), search_info.metadata.bounds],
                tms.bbox,
            )
            return {
                "bounds": bounds,
                "minzoom": minzoom,
                "maxzoom": maxzoom,
                "name": search_info.metadata.name or search_info.id,
                "tiles": [tiles_url],
            }
```
