from abc import ABC, abstractmethod
from typing import Optional

from selenium.webdriver.firefox.options import Options as FirefoxOptions


class AbstractFirefox(ABC):
    """Distinct firefox web base interface"""

    @abstractmethod
    def get_web_driver(self, *, options: Optional[FirefoxOptions] = None):
        """Abstract skeleton method for fetching firefox driver

        Args:
            caps (Optional[dict[str, Any]], optional): browser capabilities. Defaults to None.
        """
