from abc import ABC, abstractmethod
from selenium.webdriver.ie.options import Options as IeOptions


class AbstractIE(ABC):
    """
    Abstract base class for defining a distinct Internet Explorer (IE) web driver interface.

    This class provides a template for creating Internet Explorer web driver instances.
    Subclasses should implement the method to fetch the IE web driver with the given capabilities.

    Methods:
        get_web_driver(options: IeOptions | None): Fetches an IE web driver instance.
    """

    @abstractmethod
    def get_web_driver(self, *, options: IeOptions | None = None):
        """
        Abstract method for fetching an Internet Explorer (IE) web driver instance.

        This method should be implemented by subclasses to return a specific IE web driver
        instance configured with the provided capabilities.

        Args:
            options (IeOptions | None): Options object for IE capabilities, defaults to None.

        Returns:
            WebDriver: An instance of the IE web driver configured with the specified options.
        """
        pass
