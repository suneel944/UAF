from abc import ABC, abstractmethod
from typing import Any


class AbstractAndroid(ABC):
    """
    Abstract base class for defining a distinct Android mobile driver interface.

    This class provides a template for creating Android mobile driver instances.
    Subclasses should implement the method to fetch the Android mobile driver with the given capabilities.

    Methods:
        get_driver(capabilities: dict[str, Any]): Fetches an Android mobile driver instance.
    """

    @abstractmethod
    def get_driver(self, *, capabilities: dict[str, Any]):
        """
        Abstract method for fetching an Android mobile driver instance.

        This method should be implemented by subclasses to return a specific Android mobile driver
        instance configured with the provided capabilities.

        Args:
            capabilities (dict[str, Any]): Dictionary of Android mobile driver capabilities.

        Returns:
            WebDriver: An instance of the Android mobile driver configured with the specified capabilities.
        """
        pass
