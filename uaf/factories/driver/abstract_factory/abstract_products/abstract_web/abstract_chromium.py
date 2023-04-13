from abc import ABC, abstractmethod
from typing import Optional

from selenium.webdriver.chrome.options import Options as ChromeOptions


class AbstractChromium(ABC):
    """Distinct chromium web base interface"""

    @abstractmethod
    def get_web_driver(self, *, options: Optional[ChromeOptions] = None):
        """Abstract skeleton method for fetching chromium driver

        Args:
            caps (Optional[dict[str, Any]], optional): browser capabilities. Defaults to None.
        """
