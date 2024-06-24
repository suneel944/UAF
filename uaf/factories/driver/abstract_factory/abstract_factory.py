from abc import ABCMeta, abstractmethod
from typing import Any
from uaf.enums.browser_make import WebBrowserMake
from uaf.enums.mobile_os import MobileOs
from uaf.enums.test_environments import TestEnvironments
from uaf.enums.test_execution_mode import TestExecutionMode


class AbstractWebDriverFactory(metaclass=ABCMeta):
    """
    Abstract base class for defining a web browser factory interface.

    This class provides a template for creating web browser driver factories.
    Subclasses should implement methods for initializing and fetching web driver instances
    based on the browser type and capabilities.

    Methods:
        __init__(): Initializes a web browser factory instance.
        get_web_driver(browser_make: WebBrowserMake, options: dict[str, Any] | None): Fetches a web driver instance.
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Initializes a web browser factory instance.

        This method should be implemented by subclasses to handle the creation
        of a specific web driver factory instance.
        """
        pass

    @abstractmethod
    def get_web_driver(
        self,
        *,
        browser_make: WebBrowserMake,
        options: dict[str, Any] | None = None,
    ):
        """
        Abstract method for fetching a web browser driver instance.

        This method should be implemented by subclasses to return a specific web driver
        instance configured with the provided browser type and capabilities.

        Args:
            browser_make (WebBrowserMake): Enum representing the web browser type.
            options (dict[str, Any] | None): Dictionary of browser capabilities, defaults to None.

        Returns:
            WebDriver: An instance of the web driver configured with the specified options.
        """
        pass


class AbstractMobileDriverFactory(metaclass=ABCMeta):
    """
    Abstract base class for defining a mobile browser factory interface.

    This class provides a template for creating mobile browser driver factories.
    Subclasses should implement methods for fetching mobile driver instances
    based on the OS, execution mode, environment, and capabilities.

    Methods:
        get_mobile_driver(os: MobileOs, test_execution_mode: TestExecutionMode, test_environment: TestEnvironments, capabilities: dict[str, Any]): Fetches a mobile driver instance.
    """

    @abstractmethod
    def get_mobile_driver(
        self,
        *,
        os: MobileOs,
        test_execution_mode: TestExecutionMode,
        test_environment: TestEnvironments,
        capabilities: dict[str, Any],
    ):
        """
        Abstract method for fetching a mobile browser driver instance.

        This method should be implemented by subclasses to return a specific mobile driver
        instance configured with the provided OS, execution mode, environment, and capabilities.

        Args:
            os (MobileOs): Enum representing the mobile operating system.
            test_execution_mode (TestExecutionMode): Enum representing the test execution mode.
            test_environment (TestEnvironments): Enum representing the test environment.
            capabilities (dict[str, Any]): Dictionary of mobile driver capabilities.

        Returns:
            WebDriver: An instance of the mobile driver configured with the specified options.
        """
        pass
