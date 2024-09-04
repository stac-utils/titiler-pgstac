"""titiler.pgstac errors."""

from starlette import status

from titiler.core.errors import TilerError


class ReadOnlyPgSTACError(TilerError):
    """Cannot Write to PgSTAC Database."""


PGSTAC_STATUS_CODES = {ReadOnlyPgSTACError: status.HTTP_500_INTERNAL_SERVER_ERROR}
