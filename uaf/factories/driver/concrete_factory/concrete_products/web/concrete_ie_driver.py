from typing import Optional

from selenium.webdriver.ie.options import Options as IeOptions
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import IEDriverManager

from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_ie import AbstractIE

from . import webdriver


class ConcreteIEDriver(AbstractIE):
    """Concrete implementation class of chromium web driver"""

    def get_web_driver(self, *, options: Optional[IeOptions] = None):
        """Concrete implementation method of fetching ie web driver

        Args:
            capabilities (dict[str, Any]): _description_

        Returns:
            WebDriver: ie webdriver instance
        """
        if options is None:
            options = IeOptions()

        return webdriver.Ie(
            options=options,
            service=Service(executable_path=IEDriverManager().install()),
        )
