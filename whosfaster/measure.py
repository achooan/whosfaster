import random
import time
from functools import wraps
from typing import Callable

from .config import _msg, c


def measure(func: Callable):
    """
    Measure the given functions
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time.perf_counter()
        result = func(*args, **kwargs)
        time_taken = time.perf_counter() - st
        print(_msg.format(random.choice(c), func, args, kwargs, time_taken))

        return result
    return wrapper


def async_measure(func):
    """
    Measure the given async functions
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        st = time.perf_counter()
        result = await func(*args, **kwargs)
        time_taken = time.perf_counter() - st
        print(_msg.format(random.choice(c), func, args, kwargs, time_taken))

        return result
    return wrapper
