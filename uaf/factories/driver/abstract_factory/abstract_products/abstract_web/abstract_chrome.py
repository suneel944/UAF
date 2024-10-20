from abc import ABC, abstractmethod

from selenium.webdriver.chrome.options import Options as ChromeOptions


class AbstractChrome(ABC):
    """Abstract base class for Chrome web driver interface.

    This class provides the blueprint for creating Chrome browser driver instances.
    Any class inheriting from `AbstractChrome` must implement the `get_web_driver` method,
    which will handle the instantiation of the Chrome web driver with the appropriate options.

    ## Methods

    - `get_web_driver`: Abstract method that subclasses must implement to create and return
      a Chrome web driver instance.

    """

    @abstractmethod
    def get_web_driver(self, *, options: ChromeOptions | None = None):
        """Fetch or create a Chrome web driver instance.

        Args:
            options (ChromeOptions | None, optional): A dictionary of options or capabilities for configuring
                                                      the Chrome web driver. Defaults to None.
        """
        pass
