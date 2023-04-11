from typing import Optional, Any
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
from uaf.factories.driver.concrete_factory.concrete_products.web.concrete_firefox_driver import (
    ConcreteFirefoxDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.web.concrete_ie_driver import (
    ConcreteIEDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.web.concrete_msedge_driver import (
    ConcreteMsedgeDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.web.concrete_chromium_driver import (
    ConcreteChromiumDriver,
)


class ConcreteWebDriver(AbstractWebDriver):
    """
    Concrete web browser factory produce a family of web browsers that belong to
    web variant. The factory gurantees that resulting web browsers are compaitible.
    Note that signature of the concrete web browser factory's methods return an abstract
    web browser, while inside the method a concrete product is instantiated.
    """

    def __init__(self, *, browser_make: WebBrowserMake):
        """Concrete implementation of web driver instance creation"""
        self.browser_make = browser_make

    def get_web_driver(self, *, options: Optional[dict[str, Any]] = None):
        """Concrete method implementation of fetching user specific web browser

        Args:
            browser_make (WebBrowserMake): _description_
            caps (_type_, optional): _description_. Defaults to Optional[dict[str, Any]]=Nones.

        Raises:
            ValueError: if invalid browser type is specified

        Returns:
            WebDriver: web browser instance of user choice
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
                raise ValueError("invalid browser type specified")
