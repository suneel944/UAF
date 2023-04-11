from abc import ABC, abstractmethod
from typing import Any


class AbstractIOS(ABC):
    """Distinct IOS base interface"""

    @abstractmethod
    def get_driver(self, *, capabilities: dict[str, Any]):
        """Abstract method skeleton for fetching ios mobile driver instance

        Args:
            capabilities (dict[str, Any]): _description_
        """
        pass
