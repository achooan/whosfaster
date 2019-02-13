import asyncio
import random
import time
from typing import Callable, Tuple

from .config import c


async def _get_perf(func: Callable, params: Tuple = None) -> float:
    """TODO: memory usage
    """
    st = time.perf_counter()
    if params:
        await func(*params)
    else:
        await func()

    return func, params, time.perf_counter() - st


async def _ameasure(*funcs: Tuple[Callable, Tuple]) -> None:
    """Measure the given async functions

    Args:
        *funcs: a tuple of async function object and parameters.
                If params are not required, only pass the function
                or omit the param tuple.
    """
    _tasks = []

    for func in funcs:
        _tasks.append(asyncio.create_task(_get_perf(*func)))

    for res in asyncio.as_completed(_tasks):
        func, params, time_taken = await res

        print(f'{random.choice(c)} \U0001F3C1 '
              f'| func: {func.__name__}({hex(id(func))}) '
              f'| args: {str(params):10} '
              f'| {time_taken:>10.5f} second(s)')


def ameasure(*funcs: Tuple[Callable, Tuple]) -> None:
    asyncio.run(_ameasure(*funcs))
