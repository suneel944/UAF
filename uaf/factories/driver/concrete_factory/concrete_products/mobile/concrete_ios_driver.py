from typing import Any

from uaf.factories.driver.abstract_factory.abstract_products.abstract_mobie.abstract_ios import (
    AbstractIOS,
)


class ConcreteIOSDriver(AbstractIOS):
    """Concrete implementation class of ios driver"""

    def __init__(self, remote_url):
        """constructor

        Args:
            remote_url (str): remote url for remote execution
        """
        self.remote_url = remote_url

    def get_driver(self, *, capabilities: dict[str, Any]):
        """Concrete implementation method of fetching ios driver

        Args:
            capabilities (dict[str, Any]): ios capabilities

        Returns:
            WebDriver: ios driver instance
        """
        from appium.options.ios import XCUITestOptions
        from appium.webdriver import Remote

        # launch ios driver
        options = (XCUITestOptions()).load_capabilities(capabilities)
        return Remote(
            self.remote_url,
            options=options,
            direct_connection=True,
        )
