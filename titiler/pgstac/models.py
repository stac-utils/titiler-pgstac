"""
Titiler.pgstac models.

Note: This is mostly a copy of https://github.com/stac-utils/stac-fastapi/blob/master/stac_fastapi/pgstac/stac_fastapi/pgstac/types/search.py
"""

import operator
from enum import Enum, auto
from types import DynamicClassAttribute
from typing import Any, Callable, Dict, List, Optional, Union

from geojson_pydantic.geometries import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from pydantic import BaseModel, Field, root_validator, validator
from stac_pydantic.shared import BBox
from stac_pydantic.utils import AutoValueEnum


class FilterLang(str, Enum):
    """filter language.

    ref: https://github.com/radiantearth/stac-api-spec/tree/master/fragments/filter#get-query-parameters-and-post-json-fields
    """

    cql_json = "cql-json"
    cql_text = "cql-text"
    cql2_json = "cql2-json"


class Operator(str, AutoValueEnum):
    """Defines the set of operators supported by the API."""

    eq = auto()
    ne = auto()
    lt = auto()
    lte = auto()
    gt = auto()
    gte = auto()
    # TODO: These are defined in the spec but aren't currently implemented by the api
    # startsWith = auto()
    # endsWith = auto()
    # contains = auto()
    # in = auto()

    @DynamicClassAttribute
    def operator(self) -> Callable[[Any, Any], bool]:
        """Return python operator."""
        return getattr(operator, self._value_)


class SearchQuery(BaseModel):
    """Search model.

    Notes/Diff with standard model:
        - 'fields' is not in the Model because it's defined at the tiler level
        - we don't set limit
    """

    collections: Optional[List[str]] = None
    ids: Optional[List[str]] = None
    bbox: Optional[BBox]
    intersects: Optional[
        Union[Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon]
    ]
    query: Optional[Dict[str, Dict[Operator, Any]]]
    filter: Optional[Dict]
    datetime: Optional[str] = None
    sortby: Any
    filter_lang: Optional[FilterLang] = Field(None, alias="filter-lang")

    # Metadata associated with the search
    metadata: Optional[Dict[str, Any]]

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
