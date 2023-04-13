from abc import ABC, abstractmethod
from typing import Optional

from selenium.webdriver.ie.options import Options as IeOptions


class AbstractIE(ABC):
    """Distinct IE web base interface"""

    @abstractmethod
    def get_web_driver(self, *, options: Optional[IeOptions] = None):
        """Abstract skeleton method for fetching IE driver

        Args:
            caps (Optional[dict[str, Any]], optional): browser capabilities. Defaults to None.
        """
