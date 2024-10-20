from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_firefox import (
    AbstractFirefox,
)

from . import webdriver


class ConcreteFirefoxDriver(AbstractFirefox):
    """Concrete implementation class for creating a Firefox web driver."""

    def get_web_driver(self, *, options: FirefoxOptions | None = None):
        """Fetches and returns a Firefox browser web driver instance.

        Args:
            options (FirefoxOptions | None, optional): The Firefox options to configure the web driver.
                                                       Defaults to None. If not provided, default options
                                                       (maximized window) will be applied.

        Returns:
            WebDriver: A Firefox WebDriver instance configured with the provided or default options.
        """
        if options is None:
            options = FirefoxOptions()
            options.add_argument("--start-maximized")

        return webdriver.Firefox(
            options=options,
            service=Service(executable_path=GeckoDriverManager().install()),
        )
