from typing import Any
from uaf.factories.driver.abstract_factory.abstract_products.abstract_mobie.abstract_android import (
    AbstractAndroid,
)


class ConcreteAndroidDriver(AbstractAndroid):
    """
    Concrete implementation class for Android driver.

    This class provides the specific implementation for initializing and fetching
    an Android mobile driver instance using the given capabilities and remote URL.

    Attributes:
        remote_url (str): The remote URL for remote execution.

    Methods:
        __init__(remote_url: str): Initializes the ConcreteAndroidDriver with the given remote URL.
        get_driver(capabilities: dict[str, Any]): Fetches an Android mobile driver instance configured with the specified capabilities.
    """

    def __init__(self, remote_url: str):
        """
        Initializes a ConcreteAndroidDriver instance.

        Args:
            remote_url (str): The remote URL for remote execution.
        """
        self.remote_url = remote_url

    def get_driver(self, *, capabilities: dict[str, Any]):
        """
        Fetches an Android mobile driver instance.

        This method creates and returns a WebDriver instance for Android devices
        configured with the provided capabilities.

        Args:
            capabilities (dict[str, Any]): Dictionary of Android driver capabilities.

        Returns:
            WebDriver: An instance of the Android mobile driver configured with the specified capabilities.

        Example:
            capabilities = {
                "platformName": "Android",
                "platformVersion": "11.0",
                "deviceName": "Android Emulator",
                "app": "/path/to/your/app.apk"
            }

            driver = ConcreteAndroidDriver(remote_url="http://127.0.0.1:4723/wd/hub").get_driver(capabilities=capabilities)
        """
        from appium.options.android import UiAutomator2Options
        from appium.webdriver import Remote

        # Create and return the Android driver instance
        return Remote(
            self.remote_url,
            options=UiAutomator2Options().load_capabilities(capabilities),
            direct_connection=True,
        )
