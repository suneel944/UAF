from abc import ABC, abstractmethod

from selenium.webdriver.chrome.options import Options as ChromeOptions


class AbstractChromium(ABC):
    """Abstract base class for Chromium web driver interface.

    This class provides a blueprint for creating Chromium-based browser driver instances.
    Any class inheriting from `AbstractChromium` must implement the `get_web_driver` method,
    which handles the instantiation of the Chromium web driver using the appropriate options.

    Chromium is the open-source foundation for browsers like Chrome, so `ChromeOptions` is used
    for configuring the driver options.

    ## Methods

    - `get_web_driver`: Abstract method that subclasses must implement to create and return
      a Chromium web driver instance.
    """

    @abstractmethod
    def get_web_driver(self, *, options: ChromeOptions | None = None):
        """Fetch or create a Chromium web driver instance.

        Args:
            options (ChromeOptions | None, optional): A dictionary of options or capabilities for configuring
                                                      the Chromium web driver. Defaults to None.
        """
        pass
