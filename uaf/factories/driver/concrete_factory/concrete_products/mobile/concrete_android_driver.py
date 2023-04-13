from typing import Any

from uaf.factories.driver.abstract_factory.abstract_products.abstract_mobie.abstract_android import AbstractAndroid


class ConcreteAndroidDriver(AbstractAndroid):
    """Concrete implementation class of android driver"""

    def __init__(self, remote_url: str):
        """constructor

        Args:
            remote_url (str): remote url for remote execution
        """
        self.remote_url = remote_url

    def get_driver(self, *, capabilities: dict[str, Any]):
        """Concrete implementation method of fetching android mobile driver

        Args:
            capabilities (dict[str, Any]): android capabilities

        Returns:
            WebDriver: Android driver instance
        """
        from appium.options.android import UiAutomator2Options
        from appium.webdriver import Remote

        # launch android driver
        return Remote(
            self.remote_url,
            options=UiAutomator2Options().load_capabilities(capabilities),
            direct_connection=True,
        )
