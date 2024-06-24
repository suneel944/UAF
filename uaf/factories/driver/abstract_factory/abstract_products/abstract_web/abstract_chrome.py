from abc import ABC, abstractmethod
from selenium.webdriver.chrome.options import Options as ChromeOptions


class AbstractChrome(ABC):
    """
    Abstract base class for defining a distinct Chrome web driver interface.

    This class provides a template for creating Chrome web driver instances.
    Subclasses should implement the method to fetch the Chrome web driver with the given capabilities.

    Methods:
        get_web_driver(options: ChromeOptions | None): Fetches a Chrome web driver instance.
    """

    @abstractmethod
    def get_web_driver(self, *, options: ChromeOptions | None = None):
        """
        Abstract method for fetching a Chrome web driver instance.

        This method should be implemented by subclasses to return a specific Chrome web driver
        instance configured with the provided capabilities.

        Args:
            options (ChromeOptions | None): Options object for Chrome browser capabilities, defaults to None.

        Returns:
            WebDriver: An instance of the Chrome web driver configured with the specified options.
        """
        pass
