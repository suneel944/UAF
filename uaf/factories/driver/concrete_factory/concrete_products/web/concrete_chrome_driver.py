from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_chrome import (
    AbstractChrome,
)

from . import webdriver


class ConcreteChromeDriver(AbstractChrome):
    """Concrete implementation class for creating a Chrome web driver."""

    def get_web_driver(self, *, options: ChromeOptions | None = None):
        """Fetches and returns a Chrome browser web driver instance.

        Args:
            options (ChromeOptions | None, optional): The Chrome options to configure the web driver. Defaults to None.
                                                      If not provided, default options (maximized window) will be applied.

        Returns:
            WebDriver: A Chrome WebDriver instance configured with the provided or default options.
        """
        if options is None:
            options = ChromeOptions()
            options.add_argument("start-maximized")

        return webdriver.Chrome(
            options=options,
            service=Service(executable_path=ChromeDriverManager().install()),
        )
