from selenium.webdriver.ie.options import Options as IeOptions
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import IEDriverManager

from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_ie import (
    AbstractIE,
)

from . import webdriver


class ConcreteIEDriver(AbstractIE):
    """Concrete implementation class for creating an Internet Explorer (IE) web driver."""

    def get_web_driver(self, *, options: IeOptions | None = None):
        """Fetches and returns an Internet Explorer (IE) web driver instance.

        Args:
            options (IeOptions | None, optional): The Internet Explorer options to configure the web driver.
                                                  Defaults to None. If not provided, default options
                                                  (maximized window) will be applied.

        Returns:
            WebDriver: An IE WebDriver instance configured with the provided or default options.
        """
        if options is None:
            options = IeOptions()
            options.add_argument("start-maximized")

        return webdriver.Ie(
            options=options,
            service=Service(executable_path=IEDriverManager().install()),
        )
