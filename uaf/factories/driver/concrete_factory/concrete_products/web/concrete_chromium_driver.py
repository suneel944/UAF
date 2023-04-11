from typing import Optional
from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_chromium import (
    AbstractChromium,
)
from selenium.webdriver.chrome.options import Options as ChromeOptions
from . import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class ConcreteChromiumDriver(AbstractChromium):
    """Concrete implementation class of chromium web driver"""

    def get_web_driver(self, *, options: Optional[ChromeOptions] = None):
        """Concrete implementation method of fetching chromium web driver

        Args:
            capabilities (dict[str, Any]): _description_

        Returns:
            WebDriver: chromium webdriver instance
        """
        if options is None:
            options = ChromeOptions()
        return webdriver.Chrome(
            options=options,
            service=Service(
                executable_path=ChromeDriverManager(
                    chrome_type=ChromeType.CHROMIUM
                ).install()
            ),
        )
