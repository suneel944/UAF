from abc import ABC, abstractmethod

from selenium.webdriver.firefox.options import Options as FirefoxOptions


class AbstractFirefox(ABC):
    """Abstract base class for Firefox web driver interface.

    This class provides a blueprint for creating Firefox browser driver instances.
    Any class inheriting from `AbstractFirefox` must implement the `get_web_driver` method,
    which handles the instantiation of the Firefox web driver with the appropriate options.

    ## Methods

    - `get_web_driver`: Abstract method that subclasses must implement to create and return
      a Firefox web driver instance.
    """

    @abstractmethod
    def get_web_driver(self, *, options: FirefoxOptions | None = None):
        """Fetch or create a Firefox web driver instance.

        Args:
            options (FirefoxOptions | None, optional): A dictionary of options or capabilities for configuring
                                                      the Firefox web driver. Defaults to None.
        """
        pass
