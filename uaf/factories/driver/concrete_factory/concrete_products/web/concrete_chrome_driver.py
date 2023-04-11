from typing import Optional
from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_chrome import (
    AbstractChrome,
)
from selenium.webdriver.chrome.options import Options as ChromeOptions
from . import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ConcreteChromeDriver(AbstractChrome):
    """Concrete implementation class of chrome web driver"""

    def get_web_driver(self, *, options: Optional[ChromeOptions] = None):
        """Concrete implementation method of fetching chrome web driver

        Args:
            capabilities (dict[str, Any]): _description_

        Returns:
            WebDriver: chrome webdriver instance
        """
        if options is None:
            options = ChromeOptions()
        return webdriver.Chrome(
            options=options,
            service=Service(executable_path=ChromeDriverManager().install()),
        )
