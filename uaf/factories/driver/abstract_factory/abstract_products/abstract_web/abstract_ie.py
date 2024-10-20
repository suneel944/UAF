from abc import ABC, abstractmethod

from selenium.webdriver.ie.options import Options as IeOptions


class AbstractIE(ABC):
    """Abstract base class for Internet Explorer (IE) web driver interface.

    This class provides a blueprint for creating Internet Explorer (IE) browser driver instances.
    Any class inheriting from `AbstractIE` must implement the `get_web_driver` method,
    which handles the instantiation of the IE web driver with the appropriate options.

    ## Methods

    - `get_web_driver`: Abstract method that subclasses must implement to create and return
      an IE web driver instance.
    """

    @abstractmethod
    def get_web_driver(self, *, options: IeOptions | None = None):
        """Fetch or create an Internet Explorer (IE) web driver instance.

        Args:
            options (IeOptions | None, optional): A dictionary of options or capabilities for configuring
                                                  the IE web driver. Defaults to None.
        """
        pass
