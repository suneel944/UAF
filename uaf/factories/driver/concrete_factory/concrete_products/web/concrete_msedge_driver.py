from selenium.webdriver.edge.options import Options as MsEdgeOptions
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from uaf.factories.driver.abstract_factory.abstract_products.abstract_web.abstract_msedge import (
    AbstractMsedge,
)

from . import webdriver


class ConcreteMsedgeDriver(AbstractMsedge):
    """Concrete implementation class for creating a Microsoft Edge (MsEdge) web driver."""

    def get_web_driver(self, *, options: MsEdgeOptions | None = None):
        """Fetches and returns a Microsoft Edge (MsEdge) web driver instance.

        Args:
            options (MsEdgeOptions | None, optional): The Microsoft Edge options to configure the web driver.
                                                      Defaults to None. If not provided, default options
                                                      (maximized window) will be applied.

        Returns:
            WebDriver: A Microsoft Edge WebDriver instance configured with the provided or default options.
        """
        if options is None:
            options = MsEdgeOptions()
            options.add_argument("start-maximized")

        return webdriver.Edge(
            options=options,
            service=Service(executable_path=EdgeChromiumDriverManager().install()),
        )
