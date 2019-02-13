import random
import time
from typing import Callable, Tuple

from .config import c


def _get_perf(func: Callable, params: Tuple = None) -> float:
    """TODO: memory usage
    """
    st = time.perf_counter()
    if params:
        func(*params)
    else:
        func()

    return func, params, time.perf_counter() - st


def measure(*funcs: Tuple[Callable, Tuple]) -> None:
    """Measure the given functions

    Args:
        *funcs: a tuple of function object and parameters.
                If params are not required, only pass the function
                or omit the param tuple.
    """
    for func in funcs:
        func, params, time_taken = _get_perf(*func)

        print(f'{random.choice(c)} \U0001F3C1 '
              f'| func: {func.__name__}({hex(id(func))}) '
              f'| args: {str(params):10} '
              f'| {time_taken:>10.5f} second(s)')
