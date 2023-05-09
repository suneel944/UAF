from typing import Optional

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_firefox import AbstractFirefox

from . import webdriver


class ConcreteFirefoxDriver(AbstractFirefox):
    """Concrete implementation class of firefox web driver"""

    def get_web_driver(self, *, options: Optional[FirefoxOptions] = None):
        """Concrete implementation method of fetching firefox web driver

        Args:
            capabilities (dict[str, Any]): firefox browser capabilities

        Returns:
            WebDriver: firefox webdriver instance
        """
        if options is None:
            options = FirefoxOptions()
            options.add_argument("--start-maximized")
        return webdriver.Firefox(
            options=options,
            service=Service(executable_path=GeckoDriverManager().install()),
        )
