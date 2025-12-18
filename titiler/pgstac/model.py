"""
Titiler.pgstac models.

Note: This is mostly a copy of https://github.com/stac-utils/stac-fastapi/blob/master/stac_fastapi/pgstac/stac_fastapi/pgstac/types/search.py
"""

import json
import warnings
from copy import deepcopy
from datetime import datetime
from typing import Any, Literal

from geojson_pydantic.geometries import Geometry
from geojson_pydantic.types import BBox
from pydantic import BaseModel, Field, ValidationInfo, field_validator, model_validator
from typing_extensions import Annotated

from titiler.core.resources.enums import MediaType

# ref: https://github.com/stac-api-extensions/query
# TODO: add "startsWith", "endsWith", "contains", "in"
Operator = Literal["eq", "neq", "lt", "lte", "gt", "gte"]


class Metadata(BaseModel):
    """Metadata Model."""

    type: Literal["mosaic", "search"] = "mosaic"

    # WGS84 bounds
    bounds: BBox | None = None

    # Min/Max zoom for WebMercatorQuad TMS
    minzoom: int | None = None
    maxzoom: int | None = None
    # Name
    name: str | None = None

    # List of available assets
    assets: list[str] | None = None

    # Set of default configuration
    # e.g
    # {
    #     "true_color": {
    #         "assets": ["B4", "B3", "B2"],
    #         "color_formula": "Gamma RGB 3.5 Saturation 1.7 Sigmoidal RGB 15 0.35",
    #     },
    #     "ndvi": {
    #         "expression": "(B4-B3)/(B4+B3)",
    #         "rescale": [[-1, 1]],
    #         "colormap_name": "viridis"
    #     }
    # }
    defaults: dict[str, Any] | None = None

    model_config = {"extra": "allow"}

    @property
    def defaults_params(self) -> dict[str, Any]:  # noqa: C901
        """Return defaults in a form compatible with TiTiler dependencies."""
        params: dict[str, Any] = {}
        if self.defaults is not None:
            renders = deepcopy(self.defaults)
            for name, values in renders.items():
                # special encoding for Rescale
                # Per Specification, the rescale entry is a 2d array in form of `[[min, max], [min,max]]`
                # We need to convert this to `['{min},{max}', '{min},{max}']` for titiler dependency
                if rescale := values.pop("rescale", None):
                    rescales = []
                    for r in rescale:
                        if not isinstance(r, str):
                            rescales.append(",".join(map(str, r)))
                        else:
                            rescales.append(r)

                    values["rescale"] = rescales

                # special encoding for ColorMaps
                # Per Specification, the colormap is a JSON object. TiTiler dependency expects a string encoded dict
                if colormap := values.pop("colormap", None):
                    if not isinstance(colormap, str):
                        colormap = json.dumps(colormap)

                    values["colormap"] = colormap

                # Previously we were allowing {assets: "b"} instead of {assets: ["b"]}
                if assets := values.pop("assets", None):
                    if isinstance(assets, str):
                        warnings.warn(
                            f"Invalid assets form: `{assets}`, will be replaced with `[{assets}]`",
                            UserWarning,
                            stacklevel=2,
                        )
                        assets = [assets]
                    values["assets"] = assets

                if asset_bidx := values.pop("asset_bidx", None):
                    if isinstance(asset_bidx, str):
                        warnings.warn(
                            f"Invalid assets form: `{asset_bidx}`, will be replaced with `[{asset_bidx}]`",
                            UserWarning,
                            stacklevel=2,
                        )
                        asset_bidx = [asset_bidx]
                    values["asset_bidx"] = asset_bidx

                params[name] = values

        return params


class SortExtension(BaseModel):
    """
    https://github.com/radiantearth/stac-api-spec/tree/master/extensions/sort#sort-api-extension
    """

    field: str = Field(..., alias="field", min_length=1)
    direction: Literal["asc", "desc"]


class PgSTACSearch(BaseModel, extra="allow"):
    """Search Query model.

    Notes/Diff with standard model:
        - 'fields' is not in the Model because it's defined at the tiler level
        - we don't set limit
    """

    collections: list[str] | None = None
    ids: list[str] | None = None
    bbox: BBox | None = None
    intersects: Geometry | None = None
    datetime: str | None = None
    # Extensions
    query: dict[str, dict[Operator, Any]] | None = None
    sortby: list[SortExtension] | None = Field(
        default=None,
        description="An array of property (field) names, and direction in form of '{'field': '<property_name>', 'direction':'<direction>'}'",  # noqa: E501
        json_schema_extra={
            "examples": [
                # user-provided
                None,
                # creation-time
                [
                    {
                        "field": "properties.created",
                        "direction": "asc",
                    }
                ],
            ],
        },
    )
    filter_expr: dict[str, Any] | None = Field(
        default=None,
        alias="filter",
        description="A CQL filter expression for filtering items.",
        json_schema_extra={
            "examples": [
                # user-provided
                None,
                # landsat8-item
                {
                    "op": "and",
                    "args": [
                        {
                            "op": "=",
                            "args": [
                                {"property": "id"},
                                "LC08_L1TP_060247_20180905_20180912_01_T1_L1TP",
                            ],
                        },
                        {
                            "op": "=",
                            "args": [{"property": "collection"}, "landsat8_l1tp"],
                        },
                    ],
                },
            ],
        },
    )
    filter_lang: Literal["cql2-json"] | None = Field(
        default="cql2-json",
        alias="filter-lang",
        description="The CQL filter encoding that the 'filter' value uses.",
    )

    @model_validator(mode="before")
    def validate_query_fields(cls, values: dict) -> dict:
        """Pgstac does not require the base validator for query fields."""
        return values

    @field_validator("datetime")
    def validate_datetime(cls, v):
        """Pgstac does not require the base validator for datetime."""
        return v

    @field_validator("intersects")
    def validate_spatial(cls, v: Geometry | None, info: ValidationInfo):
        """Make sure bbox is not used with Intersects."""
        if v and info.data["bbox"]:
            raise ValueError("intersects and bbox parameters are mutually exclusive")

        return v

    @field_validator("bbox")
    def validate_bbox(cls, v: BBox):
        """Validate BBOX."""
        if v:
            # Validate order
            if len(v) == 4:
                xmin, ymin, xmax, ymax = v
            else:
                xmin, ymin, min_elev, xmax, ymax, max_elev = v
                if max_elev < min_elev:
                    raise ValueError(
                        "Maximum elevation must greater than minimum elevation"
                    )

            if xmax < xmin:
                raise ValueError(
                    "Maximum longitude must be greater than minimum longitude"
                )

            if ymax < ymin:
                raise ValueError(
                    "Maximum longitude must be greater than minimum longitude"
                )

            # Validate against WGS84
            if xmin < -180 or ymin < -90 or xmax > 180 or ymax > 90:
                raise ValueError("Bounding box must be within (-180, -90, 180, 90)")

        return v


class RegisterMosaic(PgSTACSearch):
    """Model of /register endpoint input."""

    metadata: Annotated[Metadata, Field(default_factory=Metadata)]


class Search(BaseModel):
    """PgSTAC Search entry.

    ref: https://github.com/stac-utils/pgstac/blob/3499daa2bfa700ae7bb07503795c169bf2ebafc7/sql/004_search.sql#L907-L915
    """

    id: str = Field(alias="hash")
    input_search: dict[str, Any] = Field(alias="search")
    sql_where: str | None = Field(default=None, alias="_where")
    orderby: str | None = None
    lastused: datetime
    usecount: int
    metadata: Metadata

    @field_validator("metadata", mode="before")
    def validate_metadata(cls, v):
        """Set SearchType.search when not present in metadata."""
        if "type" not in v:
            v["type"] = "search"

        return v


class Link(BaseModel):
    """Link model.

    Ref: https://github.com/opengeospatial/ogcapi-tiles/blob/master/openapi/schemas/common-core/link.yaml

    Code generated using https://github.com/koxudaxi/datamodel-code-generator/
    """

    href: Annotated[
        str,
        Field(
            description="Supplies the URI to a remote resource (or resource fragment).",
            json_schema_extra={
                "example": "http://data.example.com/buildings/123",
            },
        ),
    ]
    rel: Annotated[
        str,
        Field(
            description="The type or semantics of the relation.",
            json_schema_extra={
                "example": "alternate",
            },
        ),
    ]
    type: Annotated[
        MediaType | None,
        Field(
            description="A hint indicating what the media type of the result of dereferencing the link should be.",
            json_schema_extra={
                "example": "application/geo+json",
            },
        ),
    ] = None
    templated: Annotated[
        bool | None,
        Field(description="This flag set to true if the link is a URL template."),
    ] = None
    varBase: Annotated[
        str | None,
        Field(
            description="A base path to retrieve semantic information about the variables used in URL template.",
            json_schema_extra={
                "example": "/ogcapi/vars/",
            },
        ),
    ] = None
    hreflang: Annotated[
        str | None,
        Field(
            description="A hint indicating what the language of the result of dereferencing the link should be.",
            json_schema_extra={
                "example": "en",
            },
        ),
    ] = None
    title: Annotated[
        str | None,
        Field(
            description="Used to label the destination of a link such that it can be used as a human-readable identifier.",
            json_schema_extra={
                "example": "Trierer Strasse 70, 53115 Bonn",
            },
        ),
    ] = None
    length: int | None = None

    model_config = {"use_enum_values": True}


class RegisterResponse(BaseModel):
    """Response model for /register endpoint."""

    id: str
    links: list[Link] | None = None


class Info(BaseModel):
    """Response model for /info endpoint."""

    search: Search
    links: list[Link] | None = None


class Context(BaseModel):
    """Context Model."""

    returned: int
    limit: int | None = None
    matched: int | None = None

    @field_validator("limit")
    def validate_limit(cls, v, info: ValidationInfo):
        """validate limit."""
        if info.data["returned"] > v:
            raise ValueError(
                "Number of returned items must be less than or equal to the limit"
            )

        return v


class Infos(BaseModel):
    """Response model for /list endpoint."""

    searches: list[Info]
    links: list[Link] | None = None
    context: Context
