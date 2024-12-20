"""titiler.pgstac utilities."""

import time
from typing import Any, Sequence, Type, Union

from titiler.pgstac.logger import logger


def retry(
    tries: int,
    exceptions: Union[Type[Exception], Sequence[Type[Exception]]] = Exception,
    delay: float = 0.0,
):
    """Retry Decorator"""

    def _decorator(func: Any):
        def _newfn(*args: Any, **kwargs: Any):
            attempt = 0
            while attempt < tries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:  # type: ignore
                    logger.debug(repr(e))
                    logger.warning(f"Retrying `{func}` | Attempt {attempt}")

                    attempt += 1
                    time.sleep(delay)

            return func(*args, **kwargs)

        return _newfn

    return _decorator
