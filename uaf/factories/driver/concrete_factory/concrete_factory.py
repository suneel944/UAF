from . import (
    Any,
    ConcreteMobileDriver,
    ConcreteWebDriver,
    MobileOs,
    Optional,
    WebDriver,
    Environments,
    ExecutionMode,
    MobileAppType,
    WebBrowserMake,
    abstract_factory,
)


class ConcreteMobileDriverFactory(abstract_factory.AbstractMobileDriverFactory):
    """Concrete implementation of a mobile driver factory.

    This class implements the method to fetch or create mobile driver instances based on
    the mobile OS, app type, execution mode, environment, and capabilities provided.
    """

    def get_mobile_driver(
        self,
        *,
        os: MobileOs,
        app_type: MobileAppType,
        execution_mode: ExecutionMode,
        environment: Environments,
        capabilities: dict[str, Any],
    ) -> tuple[WebDriver, int]:
        """Fetch or create a mobile driver instance.

        Args:
            os (MobileOs): The mobile operating system (e.g., Android, iOS).
            app_type (MobileAppType): The type of mobile application (e.g., native, web, hybrid).
            execution_mode (ExecutionMode): The test execution mode (e.g., local, remote).
            environment (Environments): The environment where the mobile application will run (e.g., staging, production).
            capabilities (dict[str, Any]): A dictionary of desired capabilities for configuring the mobile driver.

        Returns:
            tuple[WebDriver, int]: A tuple containing the mobile driver instance and a session identifier.
        """
        return ConcreteMobileDriver(
            os=os,
            app_type=app_type,
            execution_mode=execution_mode,
            environment=environment,
        ).get_mobile_driver(
            capabilities=capabilities
        )  # type: ignore[misc]


class ConcreteWebDriverFactory(abstract_factory.AbstractWebDriverFactory):
    """Concrete implementation of a web driver factory.

    This class implements the method to fetch or create web driver instances based on
    the browser make and provided options.
    """

    def __init__(self) -> None:
        """Initialize the web driver factory."""
        pass

    def get_web_driver(
        self,
        *,
        browser_make: WebBrowserMake,
        options: Optional[dict[str, Any]] = None,
    ) -> WebDriver:
        """Fetch or create a web driver instance.

        Args:
            browser_make (WebBrowserMake): The web browser make enum specifying which browser to use.
            options (Optional[dict[str, Any]], optional): A dictionary of browser options or capabilities. Defaults to None.

        Raises:
            ValueError: If an invalid browser type is specified.

        Returns:
            WebDriver: The browser driver instance based on the selected browser make.
        """
        try:
            WebBrowserMake(browser_make)
        except ValueError:
            raise ValueError(f"Invalid browser type specified: {browser_make}")
        return ConcreteWebDriver(browser_make=browser_make).get_web_driver(
            options=options
        )
