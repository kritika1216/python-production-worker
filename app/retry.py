import asyncio
import functools
from collections.abc import Callable


def retry(max_attempts: int, delay: float) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return await func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts:
                        raise

                    await asyncio.sleep(delay)

        return wrapper

    return decorator
