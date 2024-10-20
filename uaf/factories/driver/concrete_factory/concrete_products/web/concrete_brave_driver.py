from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_brave import (
    AbstractBrave,
)

from . import webdriver


class ConcreteBraveDriver(AbstractBrave):
    """Concrete implementation class for creating a Brave browser web driver."""

    def get_web_driver(self, *, options: ChromeOptions | None = None):
        """Fetches and returns a Brave browser web driver instance.

        Args:
            options (ChromeOptions | None, optional): The Chrome options to configure the Brave web driver. If not provided,
                                                      it will attempt to load from the environment variable `BRAVE_EXECUTABLE`.

        Raises:
            RuntimeError: If the environment variable 'BRAVE_EXECUTABLE' is not set when options are None.

        Returns:
            WebDriver: An instance of the Brave web driver configured with the provided or default options.
        """
        if options is None:
            import os

            env_data_fetch_response = os.getenv("BRAVE_EXECUTABLE", default=None)
            if env_data_fetch_response is None:
                raise RuntimeError(
                    "Environment variable 'BRAVE_EXECUTABLE' is not set!!"
                )
            options = ChromeOptions()
            options.add_argument("start-maximized")
            options.binary_location = env_data_fetch_response

        return webdriver.Chrome(
            options=options,
            service=Service(
                executable_path=ChromeDriverManager(
                    chrome_type=ChromeType.BRAVE
                ).install()
            ),
        )
