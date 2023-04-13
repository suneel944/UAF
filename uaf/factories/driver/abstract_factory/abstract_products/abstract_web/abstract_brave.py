from abc import ABC, abstractmethod
from typing import Any, Optional

from selenium.webdriver.chrome.options import Options as ChromeOptions


class AbstractBrave(ABC):
    """Distinct brave web base interface"""

    @abstractmethod
    def get_web_driver(self, *, options: Optional[ChromeOptions] = None):
        """Abstract skeleton method for fetching brave driver

        Args:
            caps (Optional[dict[str, Any]], optional): browser capabilities. Defaults to None.
        """
