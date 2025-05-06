"""titiler.pgstac errors."""

from starlette import status

from titiler.core.errors import TilerError


class ReadOnlyPgSTACError(TilerError):
    """Cannot Write to PgSTAC Database."""


class NoLayerFound(TilerError):
    """Cannot find any valid Layer."""


PGSTAC_STATUS_CODES = {
    ReadOnlyPgSTACError: status.HTTP_500_INTERNAL_SERVER_ERROR,
    NoLayerFound: status.HTTP_400_BAD_REQUEST,
}
