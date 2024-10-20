from typing import Any

from uaf.factories.driver.abstract_factory.abstract_products.abstract_mobile.abstract_android import (
    AbstractAndroid,
)


class ConcreteAndroidDriver(AbstractAndroid):
    """Concrete implementation class for creating an Android mobile driver."""

    def __init__(self, remote_url: str):
        """Initializes the ConcreteAndroidDriver with the provided remote URL for remote execution.

        Args:
            remote_url (str): The remote URL for executing the Android driver.
        """
        self.remote_url = remote_url

    def get_driver(self, *, capabilities: dict[str, Any]):
        """Fetches and returns the Android mobile driver instance.

        Args:
            capabilities (dict[str, Any]): The capabilities required to configure the Android driver.

        Returns:
            WebDriver: The Android driver instance configured with the provided capabilities.
        """
        from appium.options.android import UiAutomator2Options
        from appium.webdriver import Remote

        return Remote(
            self.remote_url,
            options=UiAutomator2Options().load_capabilities(capabilities),
            direct_connection=True,
        )
