from typing import Any

from uaf.enums.browser_make import WebBrowserMake
from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_web_driver import (
    AbstractWebDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.web.concrete_brave_driver import (
    ConcreteBraveDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.web.concrete_chrome_driver import (
    ConcreteChromeDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.web.concrete_chromium_driver import (
    ConcreteChromiumDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.web.concrete_firefox_driver import (
    ConcreteFirefoxDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.web.concrete_ie_driver import (
    ConcreteIEDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.web.concrete_msedge_driver import (
    ConcreteMsedgeDriver,
)


class ConcreteWebDriver(AbstractWebDriver):
    """
    Concrete implementation class for creating web browser drivers.

    This factory class produces web drivers for various web browsers, ensuring that the correct driver is instantiated
    based on the specified browser type. It supports different browser variants (e.g., Chrome, Brave, Firefox, etc.)
    and guarantees that the resulting web driver is compatible with the user's requested browser.

    The `get_web_driver` method returns an abstract web browser interface, while internally, it instantiates a
    concrete product based on the user's choice.
    """

    def __init__(self, *, browser_make: WebBrowserMake):
        """Initializes the ConcreteWebDriver with the specified browser type.

        Args:
            browser_make (WebBrowserMake): Enum specifying the web browser type (e.g., Chrome, Firefox, Brave).
        """
        self.browser_make = browser_make

    def get_web_driver(self, *, options: dict[str, Any] | None = None):
        """Fetches and returns the web driver instance for the specified browser type.

        Args:
            options (dict[str, Any] | None, optional): Browser capabilities or options. Defaults to None.

        Raises:
            ValueError: If an invalid browser type is specified.

        Returns:
            WebDriver: A web driver instance for the specified browser.
        """
        match self.browser_make.value:
            case WebBrowserMake.BRAVE.value:
                return ConcreteBraveDriver().get_web_driver(options=options)
            case WebBrowserMake.CHROME.value:
                return ConcreteChromeDriver().get_web_driver(options=options)
            case WebBrowserMake.CHROMIUM.value:
                return ConcreteChromiumDriver().get_web_driver(options=options)
            case WebBrowserMake.IE.value:
                return ConcreteIEDriver().get_web_driver(options=options)
            case WebBrowserMake.MSEDGE.value:
                return ConcreteMsedgeDriver().get_web_driver(options=options)
            case WebBrowserMake.FIREFOX.value:
                return ConcreteFirefoxDriver().get_web_driver(options=options)
            case _:
                raise ValueError("Invalid browser type specified.")
