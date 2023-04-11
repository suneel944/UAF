from abc import ABC, abstractmethod
from typing import Any, Optional

from uaf.enums.browser_make import WebBrowserMake


class AbstractWebDriver(ABC):
    """Distinct Web base interface"""

    @abstractmethod
    def __init__(self, *, browser_make: WebBrowserMake) -> None:
        """Abstract skeleton for user specific browser instance creation

        Args:
            browser_make (WebBrowserMake): _description_
        """
        pass

    @abstractmethod
    def get_web_driver(self, *, options: Optional[dict[str, Any]] = None):
        """Abstract skeleton method for fetching user specific web driver"""
