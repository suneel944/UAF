from abc import ABC, abstractmethod
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class AbstractFirefox(ABC):
    """
    Abstract base class for defining a distinct Firefox web driver interface.

    This class provides a template for creating Firefox web driver instances.
    Subclasses should implement the method to fetch the Firefox web driver with the given capabilities.

    Methods:
        get_web_driver(options: FirefoxOptions | None): Fetches a Firefox web driver instance.
    """

    @abstractmethod
    def get_web_driver(self, *, options: FirefoxOptions | None = None):
        """
        Abstract method for fetching a Firefox web driver instance.

        This method should be implemented by subclasses to return a specific Firefox web driver
        instance configured with the provided capabilities.

        Args:
            options (FirefoxOptions | None): Options object for Firefox capabilities, defaults to None.

        Returns:
            WebDriver: An instance of the Firefox web driver configured with the specified options.
        """
        pass
