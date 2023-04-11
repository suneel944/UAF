from abc import ABC, abstractmethod
from typing import Optional
from selenium.webdriver.edge.options import Options as MsEdgeOptions


class AbstractMsedge(ABC):
    """Distinct msedge web base interface"""

    @abstractmethod
    def get_web_driver(self, *, options: Optional[MsEdgeOptions] = None):
        """Abstract skeleton method for fetching msedge driver

        Args:
            caps (Optional[dict[str, Any]], optional): _description_. Defaults to None.
        """
