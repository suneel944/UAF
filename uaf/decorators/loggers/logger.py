import time
from typing import Any, TypeVar, cast
from collections.abc import Callable
from functools import wraps
from collections.abc import Callable
import psutil
from . import _logger as logger


F = TypeVar("F", bound=Callable[..., Any])


def stringify_argument(arg: Any) -> str:
    """
    Converts a function argument into a string for logging. If the argument is an object,
    it converts the object's dictionary (__dict__) into a string. Otherwise, it uses the
    repr() function to get a string representation of the argument.

    Args:
        arg (Any): The argument to convert to a string.

    Returns:
        str: The string representation of the argument.
    """
    if hasattr(arg, "__dict__"):
        return str(arg.__dict__)
    else:
        return repr(arg)


def log(func: F) -> F:
    """
    Decorator that logs the parameters passed to the decorated function. Each parameter
    is converted to a string using stringify_argument and logged before the function
    execution.

    Args:
        func (Callable): The function to decorate.

    Returns:
        Callable: The decorated function with parameter logging.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args_str = ", ".join(map(stringify_argument, args))
        kwargs_str = ", ".join(
            [f"{key}={stringify_argument(value)}" for key, value in kwargs.items()]
        )
        all_args_str = ", ".join(filter(None, [args_str, kwargs_str]))
        logger.info(f"Arguments provided for function {func.__name__}: {all_args_str}")
        return func(*args, **kwargs)

    return cast(F, wrapper)


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
                    logger.info(
                        f"Function {func.__name__} took {execution_time:.2f} seconds to execute"
                    )
                    logger.info(f"CPU usage: {cpu_percent:.2f}%")
                    logger.info(f"Memory usage: {mem_usage:.2f} MB")
                else:
                    logger.info(
                        f"Function {func.__name__} took {execution_time:.2f} seconds to execute"
                    )
                return result

        return wrapper

    return _decorated
