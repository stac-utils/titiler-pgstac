"""
Titiler.pgstac models.

Note: This is mostly a copy of https://github.com/stac-utils/stac-fastapi/blob/master/stac_fastapi/pgstac/stac_fastapi/pgstac/types/search.py
"""

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional

from geojson_pydantic.geometries import Geometry
from geojson_pydantic.types import BBox
from pydantic import BaseModel, Field, root_validator, validator

from titiler.core.resources.enums import MediaType

# ref: https://github.com/stac-api-extensions/query
# TODO: add "startsWith", "endsWith", "contains", "in"
Operator = Literal["eq", "neq", "lt", "lte", "gt", "gte"]

# ref: https://github.com/radiantearth/stac-api-spec/tree/master/fragments/filter#get-query-parameters-and-post-json-fields
FilterLang = Literal["cql-json", "cql-text", "cql2-json"]

SearchType = Literal["mosaic", "search"]


class Metadata(BaseModel):
    """Metadata Model."""

    type: SearchType = "mosaic"

    # WGS84 bounds
    bounds: Optional[BBox]

    # Min/Max zoom for WebMercatorQuad TMS
    minzoom: Optional[int]
    maxzoom: Optional[int]

    # Name
    name: Optional[str]

    # List of available assets
    assets: Optional[List[str]]

    # Set of default configuration
    # e.g
    # {
    #     "true_color": {
    #         "assets": ["B4", "B3", "B2"],
    #         "color_formula": "Gamma RGB 3.5 Saturation 1.7 Sigmoidal RGB 15 0.35",
    #     },
    #     "ndvi": {
    #         "expression": "(B4-B3)/(B4+B3)",
    #         "rescale": "-1,1",
    #         "colormap_name": "viridis"
    #     }
    # }
    defaults: Optional[Dict[str, Any]]

    class Config:
        """Config for model."""

        extra = "allow"


class PgSTACSearch(BaseModel):
    """Search Query model.

    Notes/Diff with standard model:
        - 'fields' is not in the Model because it's defined at the tiler level
        - we don't set limit
    """

    collections: Optional[List[str]] = None
    ids: Optional[List[str]] = None
    bbox: Optional[BBox]
    intersects: Optional[Geometry]
    query: Optional[Dict[str, Dict[Operator, Any]]]
    filter: Optional[Dict]
    datetime: Optional[str] = None
    sortby: Any
    filter_lang: Optional[FilterLang] = Field(None, alias="filter-lang")

    class Config:
        """Config for model."""

        use_enum_values = True
        extra = "allow"

    @root_validator(pre=True)
    def validate_query_fields(cls, values: Dict) -> Dict:
        """Pgstac does not require the base validator for query fields."""
        return values

    @validator("datetime")
    def validate_datetime(cls, v):
        """Pgstac does not require the base validator for datetime."""
        return v

    @validator("intersects")
    def validate_spatial(cls, v, values):
        """Make sure bbox is not used with Intersects."""
        if v and values["bbox"]:
            raise ValueError("intersects and bbox parameters are mutually exclusive")
        return v

    @validator("bbox")
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

    metadata: Metadata = Field(default_factory=Metadata)


class Search(BaseModel):
    """PgSTAC Search entry.

    ref: https://github.com/stac-utils/pgstac/blob/3499daa2bfa700ae7bb07503795c169bf2ebafc7/sql/004_search.sql#L907-L915
    """

    id: str = Field(alias="hash")
    input_search: Dict[str, Any] = Field(alias="search")
    sql_where: str = Field(alias="_where")
    orderby: str
    lastused: datetime
    usecount: int
    metadata: Metadata

    @validator("metadata", pre=True)
    def validate_metadata(cls, v):
        """Set SearchType.search when not present in metadata."""
        if "type" not in v:
            v["type"] = "search"

        return v


class Link(BaseModel):
    """Link model.

    Ref: http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/schemas/link.yaml
    """

    rel: Optional[str]
    title: Optional[str]
    type: Optional[MediaType] = MediaType.json
    href: str
    hreflang: Optional[str]
    length: Optional[int]

    class Config:
        """Link model configuration."""

        use_enum_values = True


class RegisterResponse(BaseModel):
    """Response model for /register endpoint."""

    searchid: str
    links: Optional[List[Link]]


class Info(BaseModel):
    """Response model for /info endpoint."""

    search: Search
    links: Optional[List[Link]]


class Context(BaseModel):
    """Context Model."""

    returned: int
    limit: Optional[int]
    matched: Optional[int]

    @validator("limit")
    def validate_limit(cls, v, values):
        """validate limit."""
        if values["returned"] > v:
            raise ValueError(
                "Number of returned items must be less than or equal to the limit"
            )
        return v


class Infos(BaseModel):
    """Response model for /list endpoint."""

    searches: List[Info]
    links: Optional[List[Link]]
    context: Context
