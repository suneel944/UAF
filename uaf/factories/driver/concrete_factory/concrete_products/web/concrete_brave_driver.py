from typing import Optional

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_brave import AbstractBrave

from . import webdriver


class ConcreteBraveDriver(AbstractBrave):
    """Concrete implementation class of brave web driver"""

    def get_web_driver(self, *, options: Optional[ChromeOptions] = None):
        """Concrete implementation method of fetching brave web driver

        Args:
            capabilities (dict[str, Any]): brave browser capabilities

        Returns:
            WebDriver: brave webdriver instance
        """
        if options is None:
            import os

            env_data_fetch_response = os.getenv("BRAVE_EXECUTABLE", default=None)
            if isinstance(env_data_fetch_response, type(None)):
                raise RuntimeError("Environment variable 'BRAVE_EXECUTABLE' is not set!!")
            options = ChromeOptions()
            options.add_argument("start-maximized")
            options.binary_location = env_data_fetch_response
        return webdriver.Chrome(
            options=options,
            service=Service(executable_path=ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),
        )
