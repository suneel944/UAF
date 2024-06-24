from selenium.webdriver.edge.options import Options as MsEdgeOptions
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_msedge import (
    AbstractMsedge,
)

from . import webdriver


class ConcreteMsedgeDriver(AbstractMsedge):
    """Concrete implementation class of msedge web driver"""

    def get_web_driver(self, *, options: MsEdgeOptions | None = None):
        """Concrete implementation method of fetching msedge web driver

        Args:
            capabilities (dict[str, Any]): msedge browser capabilities

        Returns:
            WebDriver: msedge webdriver instance
        """
        if options is None:
            options = MsEdgeOptions()
            options.add_argument("start-maximized")
        return webdriver.Edge(
            options=options,
            service=Service(executable_path=EdgeChromiumDriverManager().install()),
        )
