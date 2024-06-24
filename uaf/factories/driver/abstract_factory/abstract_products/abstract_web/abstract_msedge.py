from abc import ABC, abstractmethod
from selenium.webdriver.edge.options import Options as MsEdgeOptions


class AbstractMsedge(ABC):
    """
    Abstract base class for defining a distinct Microsoft Edge web driver interface.

    This class provides a template for creating Microsoft Edge web driver instances.
    Subclasses should implement the method to fetch the Edge web driver with the given capabilities.

    Methods:
        get_web_driver(options: MsEdgeOptions | None): Fetches an Edge web driver instance.
    """

    @abstractmethod
    def get_web_driver(self, *, options: MsEdgeOptions | None = None):
        """
        Abstract method for fetching a Microsoft Edge web driver instance.

        This method should be implemented by subclasses to return a specific Edge web driver
        instance configured with the provided capabilities.

        Args:
            options (MsEdgeOptions | None): Options object for Microsoft Edge capabilities, defaults to None.

        Returns:
            WebDriver: An instance of the Microsoft Edge web driver configured with the specified options.
        """
        pass
