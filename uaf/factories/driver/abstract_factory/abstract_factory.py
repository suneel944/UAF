from abc import ABCMeta, abstractmethod
from typing import Any

from uaf.enums.browser_make import WebBrowserMake
from uaf.enums.mobile_os import MobileOs
from uaf.enums.mobile_app_type import MobileAppType
from uaf.enums.environments import Environments
from uaf.enums.execution_mode import ExecutionMode


class AbstractWebDriverFactory(metaclass=ABCMeta):
    """Abstract base class for web driver factories.

    This class defines the skeleton for creating web driver factory instances.
    All derived classes must implement the methods for creating and retrieving web drivers.
    """

    @abstractmethod
    def __init__(self) -> None:
        """Initialize the abstract web driver factory.

        This method serves as the constructor for any subclass implementing the web driver factory.
        """
        pass

    @abstractmethod
    def get_web_driver(
        self,
        *,
        browser_make: WebBrowserMake,
        options: dict[str, Any] | None = None,
    ):
        """Retrieve the web driver for a specified browser.

        Args:
            browser_make (WebBrowserMake): The web browser make enum specifying which browser to use.
            options (dict[str, Any], optional): A dictionary of browser options or capabilities. Defaults to None.
        """
        pass


class AbstractMobileDriverFactory(metaclass=ABCMeta):
    """Abstract base class for mobile driver factories.

    This class defines the skeleton for creating mobile driver factory instances.
    All derived classes must implement the methods for creating and retrieving mobile drivers.
    """

    @abstractmethod
    def get_mobile_driver(
        self,
        *,
        os: MobileOs,
        app_type: MobileAppType,
        execution_mode: ExecutionMode,
        environment: Environments,
        capabilities: dict[str, Any],
    ):
        """Retrieve the mobile driver based on specified parameters.

        Args:
            os (MobileOs): The operating system for the mobile device (e.g., Android, iOS).
            app_type (MobileAppType): The type of mobile application (e.g., native, web, hybrid).
            execution_mode (ExecutionMode): The mode in which the tests will be executed (e.g., local, remote).
            environment (Environments): The environment where the application will run (e.g., staging, production).
            capabilities (dict[str, Any]): A dictionary of desired capabilities for configuring the mobile driver.
        """
        pass
