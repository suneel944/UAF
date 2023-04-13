from abc import ABC, abstractmethod
from typing import Any


class AbstractAndroid(ABC):
    """Distinct Android base interface"""

    @abstractmethod
    def get_driver(self, *, capabilities: dict[str, Any]):
        """Abstract method skeleton for fetching android driver instance

        Args:
            capabilities (dict[str, Any]): android mobile driver capabilities
        """
        pass
