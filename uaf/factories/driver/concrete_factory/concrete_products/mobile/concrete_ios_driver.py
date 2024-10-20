from typing import Any

from uaf.factories.driver.abstract_factory.abstract_products.abstract_mobile.abstract_ios import (
    AbstractIOS,
)


class ConcreteIOSDriver(AbstractIOS):
    """Concrete implementation class for creating an iOS mobile driver."""

    def __init__(self, remote_url: str):
        """Initializes the ConcreteIOSDriver with the provided remote URL for remote execution.

        Args:
            remote_url (str): The remote URL for executing the iOS driver.
        """
        self.remote_url = remote_url

    def get_driver(self, *, capabilities: dict[str, Any]):
        """Fetches and returns the iOS mobile driver instance.

        Args:
            capabilities (dict[str, Any]): The capabilities required to configure the iOS driver.

        Returns:
            WebDriver: The iOS driver instance configured with the provided capabilities.
        """
        from appium.options.ios import XCUITestOptions
        from appium.webdriver import Remote

        options = XCUITestOptions().load_capabilities(capabilities)
        return Remote(
            self.remote_url,
            options=options,
            direct_connection=True,
        )
