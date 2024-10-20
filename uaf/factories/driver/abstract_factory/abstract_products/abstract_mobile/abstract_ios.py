from abc import ABC, abstractmethod
from typing import Any


class AbstractIOS(ABC):
    """Abstract base class for iOS driver interface.

    This class provides the skeleton for creating iOS driver instances.
    Any concrete class inheriting from this must implement the `get_driver` method.
    """

    @abstractmethod
    def get_driver(self, *, capabilities: dict[str, Any]):
        """Fetch or create an iOS driver instance.

        Args:
            capabilities (dict[str, Any]): A dictionary of capabilities used to configure the iOS driver.
        """
        pass
