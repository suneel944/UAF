from abc import ABC, abstractmethod
from typing import Any

from uaf.enums.browser_make import WebBrowserMake


class AbstractWebDriver(ABC):
    """Abstract base class for web driver interface.

    This class provides a blueprint for creating browser-specific web driver instances.
    Any class inheriting from `AbstractWebDriver` must implement the `__init__` method
    to initialize the browser type and the `get_web_driver` method to fetch the configured web driver.

    ## Methods

    - `__init__`: Abstract method for initializing the web driver with the specific browser make (e.g., Chrome, Firefox).
    - `get_web_driver`: Abstract method to create and return a web driver instance based on the provided options.

    """

    @abstractmethod
    def __init__(self, *, browser_make: WebBrowserMake) -> None:
        """Initialize the web driver with the specified browser make.

        Args:
            browser_make (WebBrowserMake): The browser make enum (e.g., Chrome, Firefox, Edge).
        """
        pass

    @abstractmethod
    def get_web_driver(self, *, options: dict[str, Any] | None = None):
        """Fetch or create a web driver instance based on the specified browser make.

        Args:
            options (dict[str, Any] | None, optional): A dictionary of browser capabilities and options. Defaults to None.
        """
        pass
