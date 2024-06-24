from abc import ABC, abstractmethod
from typing import Any
from uaf.enums.browser_make import WebBrowserMake


class AbstractWebDriver(ABC):
    """
    Abstract base class for defining a distinct web driver interface.

    This class serves as a template for creating specific web driver instances
    based on the browser type. Subclasses must implement the methods to initialize
    and fetch the web driver with the given browser capabilities.

    Attributes:
        browser_make (WebBrowserMake): Enum representing the type of web browser.
    """

    @abstractmethod
    def __init__(self, *, browser_make: WebBrowserMake) -> None:
        """
        Initializes a web driver instance.

        This method must be implemented by subclasses to handle the creation
        of a specific web driver instance for the given browser type.

        Args:
            browser_make (WebBrowserMake): Enum representing the web browser type.
        """
        pass

    @abstractmethod
    def get_web_driver(self, *, options: dict[str, Any] | None = None):
        """
        Fetches a web driver instance.

        This method must be implemented by subclasses to return a specific
        web driver instance configured with the provided browser capabilities.

        Args:
            options (Optional[dict[str, Any]]): Dictionary of browser capabilities, defaults to None.

        Returns:
            WebDriver: An instance of the web driver configured with the specified options.
        """
        pass
