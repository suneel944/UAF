import os
import sys

from loguru import logger as _logger

__all__ = ["_logger"]

# Remove the default logger
_logger.remove(0)

# Define the different logging levels and their corresponding colors
logging_levels = {
    "TRACE": "<fg #808080>",
    "DEBUG": "<fg #008080>",
    "INFO": "<fg #0000FF>",
    "SUCCESS": "<fg #00FF00>",
    "WARNING": "<fg #FFA500>",
    "ERROR": "<fg #FF0000>",
    "CRITICAL": "<fg #8B0000>",
}

# Configure console logger for INFO and higher level logs
_logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSSSSS}</green> | {level} | {message}",
)

# Configure file logger for ERROR and higher level logs
_logger.add(
    os.path.join("logs", "error.log"),
    rotation="1 day",
    retention="7 days",
    level="ERROR",
    encoding="utf-8",
    enqueue=True,
    format="{time:YYYY-MM-DD HH:mm:ss.SSSSSS} | {level} | {message}",
)

# Configure file logger for all level logs
_logger.add(
    os.path.join("logs", "all.log"),
    rotation="1 day",
    retention="7 days",
    encoding="utf-8",
    enqueue=True,
    format="{time:YYYY-MM-DD HH:mm:ss.SSSSSS} | {level} | {message}",
)

# Add custom logging levels
for level, color in logging_levels.items():
    _logger.level(level, color=color)


def exception_hook(exception_type, value, traceback):
    _logger.opt(depth=1).critical("Unhandled exception occurred", exception=(exception_type, value, traceback))


# Add the custom exception hook
sys.excepthook = exception_hook
