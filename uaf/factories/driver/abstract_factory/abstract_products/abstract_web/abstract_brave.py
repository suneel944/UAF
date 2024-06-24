from abc import ABC, abstractmethod
from selenium.webdriver.chrome.options import Options as ChromeOptions


class AbstractBrave(ABC):
    """
    Abstract base class for defining a distinct Brave web driver interface.

    This class provides a template for creating Brave web driver instances.
    Subclasses should implement the method to fetch the Brave web driver with the given capabilities.

    Methods:
        get_web_driver(options: ChromeOptions | None): Fetches a Brave web driver instance.
    """

    @abstractmethod
    def get_web_driver(self, *, options: ChromeOptions | None = None):
        """
        Abstract method for fetching a Brave web driver instance.

        This method should be implemented by subclasses to return a specific Brave web driver
        instance configured with the provided capabilities.

        Args:
            options (ChromeOptions | None): Options object for Brave browser capabilities, defaults to None.

        Returns:
            WebDriver: An instance of the Brave web driver configured with the specified options.
        """
        pass
