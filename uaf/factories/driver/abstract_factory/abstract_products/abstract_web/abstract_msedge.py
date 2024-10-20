from abc import ABC, abstractmethod

from selenium.webdriver.edge.options import Options as MsEdgeOptions


class AbstractMsedge(ABC):
    """Abstract base class for Microsoft Edge (MsEdge) web driver interface.

    This class provides a blueprint for creating Microsoft Edge browser driver instances.
    Any class inheriting from `AbstractMsedge` must implement the `get_web_driver` method,
    which handles the instantiation of the Microsoft Edge web driver with the appropriate options.

    ## Methods

    - `get_web_driver`: Abstract method that subclasses must implement to create and return
      a Microsoft Edge web driver instance.
    """

    @abstractmethod
    def get_web_driver(self, *, options: MsEdgeOptions | None = None):
        """Fetch or create a Microsoft Edge (MsEdge) web driver instance.

        Args:
            options (MsEdgeOptions | None, optional): A dictionary of options or capabilities for configuring
                                                      the Microsoft Edge web driver. Defaults to None.
        """
        pass
