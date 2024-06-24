from abc import ABC, abstractmethod
from typing import Any


class AbstractIOS(ABC):
    """
    Abstract base class for defining a distinct iOS mobile driver interface.

    This class provides a template for creating iOS mobile driver instances.
    Subclasses should implement the method to fetch the iOS mobile driver with the given capabilities.

    Methods:
        get_driver(capabilities: dict[str, Any]): Fetches an iOS mobile driver instance.
    """

    @abstractmethod
    def get_driver(self, *, capabilities: dict[str, Any]):
        """
        Abstract method for fetching an iOS mobile driver instance.

        This method should be implemented by subclasses to return a specific iOS mobile driver
        instance configured with the provided capabilities.

        Args:
            capabilities (dict[str, Any]): Dictionary of iOS mobile driver capabilities.

        Returns:
            WebDriver: An instance of the iOS mobile driver configured with the specified capabilities.
        """
        pass
