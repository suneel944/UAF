from abc import ABC, abstractmethod
from typing import Any


class AbstractAndroid(ABC):
    """Abstract base class for Android driver interface.

    This class provides the skeleton for creating Android driver instances.
    Any concrete class inheriting from this must implement the `get_driver` method.
    """

    @abstractmethod
    def get_driver(self, *, capabilities: dict[str, Any]):
        """Fetch or create an Android driver instance.

        Args:
            capabilities (dict[str, Any]): A dictionary of capabilities used to configure the Android driver.
        """
        pass
