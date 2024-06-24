from abc import ABC, abstractmethod
from selenium.webdriver.chrome.options import Options as ChromeOptions


class AbstractChromium(ABC):
    """
    Abstract base class for defining a distinct Chromium-based web driver interface.

    This class provides a template for creating Chromium-based web driver instances.
    Subclasses should implement the method to fetch the Chromium-based web driver with the given capabilities.

    Methods:
        get_web_driver(options: ChromeOptions | None): Fetches a Chromium-based web driver instance.
    """

    @abstractmethod
    def get_web_driver(self, *, options: ChromeOptions | None = None):
        """
        Abstract method for fetching a Chromium-based web driver instance.

        This method should be implemented by subclasses to return a specific Chromium-based web driver
        instance configured with the provided capabilities.

        Args:
            options (ChromeOptions | None): Options object for Chromium-based browser capabilities, defaults to None.

        Returns:
            WebDriver: An instance of the Chromium-based web driver configured with the specified options.
        """
        pass
