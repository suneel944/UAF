from . import (
    Any,
    ConcreteMobileDriver,
    ConcreteWebDriver,
    MobileOs,
    Optional,
    TestEnvironments,
    TestExecutionMode,
    WebBrowserMake,
    abstract_factory,
)


class ConcreteMobileDriverFactory(abstract_factory.AbstractMobileDriverFactory):
    """Concrete implementation of mobile driver factory"""

    def get_mobile_driver(
        self,
        *,
        os: MobileOs,
        test_execution_mode: TestExecutionMode,
        test_environment: TestEnvironments,
        capabilities: dict[str, Any],
    ):
        """Concrete implementation of fetching mobile driver

        Args:
            os (MobileOs): _description_
            test_execution_mode (TestExecutionMode): _description_
            test_environment (TestEnvironments): _description_
            capabilities (dict[str, Any]): _description_
        """
        return ConcreteMobileDriver(
            os=os,
            test_execution_mode=test_execution_mode,
            test_environment=test_environment,
        ).get_mobile_driver(
            capabilities=capabilities
        )  # type: ignore[misc]


class ConcreteWebDriverFactory(abstract_factory.AbstractWebDriverFactory):
    """Concrete implementation of web driver factory"""

    def get_web_driver(
        self,
        *,
        browser_make: WebBrowserMake,
        options: Optional[dict[str, Any]] = None,
    ):
        """Concrete implementation of fetching web driver

        Args:
            browser_make (WebBrowserMake): _description_
            options (Optional[dict[str, Any]], optional): _description_. Defaults to None.

        Returns:
            WebDriver: browser driver instance based on user choice of browser make
        """
        return ConcreteWebDriver(browser_make=browser_make).get_web_driver(options=options)
