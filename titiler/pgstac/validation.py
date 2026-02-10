"""
Validation functions for caller-provided data.
"""

from typing import Literal, cast

from cql2 import Expr
from geojson_pydantic.types import BBox
from pydantic import ValidationError

from titiler.core.validation import validate_json


def validate_filter(
    filter_expr: str | None, filter_lang: Literal["cql2-text", "cql2-json"]
) -> None:
    """
    Verify that a filter string can be parsed, parsing is determined by the language used.
    :param filter_expr: Caller-provided filter value.
    :type filter_expr: str | None
    :param filter_lang: Caller-provided language value.
    :type filter_lang: str
    """
    if filter_expr is None:
        return
    if filter_lang == "cql2-json":
        try:
            validate_json(json_str=filter_expr)
        except ValueError as e:
            raise ValidationError(str(e), []) from e
    elif filter_lang == "cql2-text":
        try:
            Expr(filter_expr).validate()
        except Exception as e:
            raise ValidationError(str(e), []) from e


def validate_bbox(v: BBox | None):
    """Validate BBOX values."""
    if v:
        # Validate order
        if len(v) == 4:
            xmin, ymin, xmax, ymax = v
        elif len(v) == 6:
            xmin, ymin, min_elev, xmax, ymax, max_elev = v
            if max_elev < min_elev:
                raise ValueError(
                    "Maximum elevation must greater than minimum elevation"
                )
        else:
            raise ValueError("Bounding box must have 4 or 6 numbers")

        if xmax < xmin:
            raise ValueError("Maximum longitude must be greater than minimum longitude")

        if ymax < ymin:
            raise ValueError("Maximum longitude must be greater than minimum longitude")

        # Validate against WGS84
        if xmin < -180 or ymin < -90 or xmax > 180 or ymax > 90:
            raise ValueError("Bounding box must be within (-180, -90, 180, 90)")

    return v


def parse_and_validate_bbox(value: str | None):
    """Validate BBOX format and values."""
    if value is None:
        return None
    try:
        parsed_value = cast(BBox, [float(x) for x in value.split(",")])
    except ValueError as e:
        raise ValueError(
            "Bounding box must be a comma-separated list of numbers"
        ) from e

    validate_bbox(parsed_value)
    return value
