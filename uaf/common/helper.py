from typing import Any, Dict
from uaf import version as uaf_version


def library_version() -> str:
    """Return a version of this python library

    Returns:
        str: library version
    """
    return uaf_version.version
