from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_chromium import (
    AbstractChromium,
)

from . import webdriver


class ConcreteChromiumDriver(AbstractChromium):
    """Concrete implementation class of chromium web driver"""

    def get_web_driver(self, *, options: ChromeOptions | None = None):
        """Concrete implementation method of fetching chromium web driver

        Args:
            capabilities (dict[str, Any]): chromium browser capabilities

        Returns:
            WebDriver: chromium webdriver instance
        """
        if options is None:
            options = ChromeOptions()
            options.add_argument("start-maximized")
        return webdriver.Chrome(
            options=options,
            service=Service(
                executable_path=ChromeDriverManager(
                    chrome_type=ChromeType.CHROMIUM
                ).install()
            ),
        )
