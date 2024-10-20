from abc import ABC, abstractmethod

from selenium.webdriver.chrome.options import Options as ChromeOptions


class AbstractBrave(ABC):
    """Abstract base class for Brave web driver interface.

    This class provides a blueprint for creating Brave browser driver instances.
    Any class that inherits from `AbstractBrave` must implement the `get_web_driver` method,
    which will handle the instantiation of the Brave web driver with the appropriate options.

    The Brave browser shares much of its functionality with Chrome, so `ChromeOptions` is used for
    configuring the driver options.

    ## Methods

    - `get_web_driver`: Abstract method that subclasses must implement to create and return a Brave
      web driver instance.

    """

    @abstractmethod
    def get_web_driver(self, *, options: ChromeOptions | None = None):
        """Fetch or create a Brave browser driver instance.

        Args:
            options (ChromeOptions | None, optional): A dictionary of options or capabilities for configuring
                                                      the Brave web driver. Defaults to None.
        """
        pass
