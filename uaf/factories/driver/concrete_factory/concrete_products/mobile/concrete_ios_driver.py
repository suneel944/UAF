from typing import Any

from uaf.factories.driver.abstract_factory.abstract_products.abstract_mobie.abstract_ios import (
    AbstractIOS,
)


class ConcreteIOSDriver(AbstractIOS):
    """
    Concrete implementation class for iOS driver.

    This class provides the specific implementation for initializing and fetching
    an iOS mobile driver instance using the given capabilities and remote URL.

    Attributes:
        remote_url (str): The remote URL for remote execution.

    Methods:
        __init__(remote_url: str): Initializes the ConcreteIOSDriver with the given remote URL.
        get_driver(capabilities: dict[str, Any]): Fetches an iOS mobile driver instance configured with the specified capabilities.
    """

    def __init__(self, remote_url: str):
        """
        Initializes a ConcreteIOSDriver instance.

        Args:
            remote_url (str): The remote URL for remote execution.
        """
        self.remote_url = remote_url

    def get_driver(self, *, capabilities: dict[str, Any]):
        """
        Fetches an iOS mobile driver instance.

        This method creates and returns a WebDriver instance for iOS devices
        configured with the provided capabilities.

        Args:
            capabilities (dict[str, Any]): Dictionary of iOS driver capabilities.

        Returns:
            WebDriver: An instance of the iOS mobile driver configured with the specified capabilities.

        Example:
            capabilities = {
                "platformName": "iOS",
                "platformVersion": "14.0",
                "deviceName": "iPhone Simulator",
                "app": "/path/to/your/app.app"
            }

            driver = ConcreteIOSDriver(remote_url="http://127.0.0.1:4723/wd/hub").get_driver(capabilities=capabilities)
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
