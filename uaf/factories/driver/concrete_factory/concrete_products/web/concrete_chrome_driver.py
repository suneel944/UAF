from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_chrome import (
    AbstractChrome,
)

from . import webdriver


class ConcreteChromeDriver(AbstractChrome):
    """Concrete implementation class of chrome web driver"""

    def get_web_driver(self, *, options: ChromeOptions | None = None):
        """Concrete implementation method of fetching chrome web driver

        Args:
            capabilities (dict[str, Any]): chrome browser capabilities

        Returns:
            WebDriver: chrome webdriver instance
        """
        if options is None:
            options = ChromeOptions()
            options.add_argument("start-maximized")
        return webdriver.Chrome(
            options=options,
            service=Service(executable_path=ChromeDriverManager().install()),
        )
