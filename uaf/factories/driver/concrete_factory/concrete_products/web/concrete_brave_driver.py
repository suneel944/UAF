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
            capabilities (dict[str, Any]): _description_

        Returns:
            WebDriver: brave webdriver instance
        """
        if options is None:
            options = ChromeOptions()
        return webdriver.Chrome(
            options=options,
            service=Service(executable_path=ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),
        )
