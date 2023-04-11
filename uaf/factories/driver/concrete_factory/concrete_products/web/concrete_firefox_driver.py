from typing import Optional
from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_firefox import (
    AbstractFirefox,
)
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from . import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class ConcreteFirefoxDriver(AbstractFirefox):
    """Concrete implementation class of firefox web driver"""

    def get_web_driver(self, *, options: Optional[FirefoxOptions] = None):
        """Concrete implementation method of fetching firefox web driver

        Args:
            capabilities (dict[str, Any]): _description_

        Returns:
            WebDriver: firefox webdriver instance
        """
        if options is None:
            options = FirefoxOptions()

        return webdriver.Firefox(
            options=options,
            service=Service(executable_path=GeckoDriverManager().install()),
        )
