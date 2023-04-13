import time
from functools import wraps
from traceback import format_exc
from typing import Any, Callable, Optional, TypeVar

import psutil

from . import _logger as logger

T = TypeVar("T", bound=Callable[..., Any])


def log(func: Optional[T] = None, *, log_return_value: bool = True) -> Callable[[Any], Any]:
    """Logs info and errors for any decorated function

    Args:
        func (Optional[T], optional): decorating function. Defaults to None.
        log_return_value (bool, optional): condition to decide whether to print return value or not. Defaults to True.

    Returns:
        Callable[[Any], Any]: decorated func
    """

    def _decorated(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            arg_names = func.__code__.co_varnames[: func.__code__.co_argcount]
            arg_dict = dict(zip(arg_names, args))
            arg_dict.update(kwargs)
            logger.info(f"{func.__name__} called with arguments: {arg_dict}")
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.error(f"{func.__name__} raised an exception: {format_exc()}")
                raise e
            else:
                if log_return_value:
                    logger.info(f"{func.__name__} returned {result}")
                return result

        return wrapper

    if func is None:
        return _decorated
    else:
        # provision to run custom decorator
        return _decorated(func)


def log_performance(condition=None):
    """
    Logs performance metrics based on the requirement

    Ex: @log_performance(condition=lambda f, r: (time.time() - f.start_time) > 5)
        def my_slow_function(arg1, arg2):
            pass

        @log_performance()
        def my_slow_function2(arg1):
            pass
    """

    def _decorated(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            """
            process.memory_info().rss / 1024 / 1024 captures the current resident set size
            (RSS) of the Python process, which is the portion of the memory occupied by the process that
            is held in RAM (i.e., not swapped out to disk).

            The psutil library's memory_info method returns a named tuple containing several memory-related
            metrics for the process, including its RSS. The RSS is expressed in bytes, so dividing it by 1024
            twice converts it to megabytes, which is a more human-readable unit of measurement.
            """
            mem_before = psutil.Process().memory_info().rss / 1024 / 1024
            cpu_before = psutil.Process().cpu_percent()
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error in function {func.__name__}: {e}")
                raise e
            finally:
                end_time = time.time()
                execution_time = end_time - start_time
                mem_after = psutil.Process().memory_info().rss / 1024 / 1024
                cpu_after = psutil.Process().cpu_percent()
                if condition and condition(func, result):
                    cpu_percent = cpu_after - cpu_before
                    mem_usage = mem_after - mem_before
                    logger.info(f"Function {func.__name__} took {execution_time:.2f} seconds to execute")
                    logger.info(f"CPU usage: {cpu_percent:.2f}%")
                    logger.info(f"Memory usage: {mem_usage:.2f} MB")
                else:
                    logger.info(f"Function {func.__name__} took {execution_time:.2f} seconds to execute")
                return result

        return wrapper

    return _decorated
