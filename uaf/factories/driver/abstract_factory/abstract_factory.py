from abc import ABCMeta, abstractmethod
from typing import Any

from uaf.enums.browser_make import WebBrowserMake
from uaf.enums.mobile_os import MobileOs
from uaf.enums.mobile_app_type import MobileAppType
from uaf.enums.test_environments import TestEnvironments
from uaf.enums.test_execution_mode import TestExecutionMode


class AbstractWebDriverFactory(metaclass=ABCMeta):
    """Abstract web browser factory skeleton"""

    @abstractmethod
    def __init__(self) -> None:
        """Abstract skeleton for web browser factory instance creation"""
        pass

    @abstractmethod
    def get_web_driver(
        self,
        *,
        browser_make: WebBrowserMake,
        options: dict[str, Any] | None = None,
    ):
        """Abstract method skeleton for fetching web browser

        Args:
            browser_make (WebBrowserMake): web browser make enum
            options (str, optional): browser capabilities. Defaults to None.
        """
        pass


class AbstractMobileDriverFactory(metaclass=ABCMeta):
    """Abstract mobile browser factory skeleton"""

    @abstractmethod
    def get_mobile_driver(
        self,
        *,
        os: MobileOs,
        app_type: MobileAppType,
        test_execution_mode: TestExecutionMode,
        test_environment: TestEnvironments,
        capabilities: dict[str, Any],
    ):
        """Abstract method skeleton for fetching mobile driver

        Args:
            os (MobileOs): The operating system for the mobile device.
            app_type (MobileAppType): The type of mobile application (e.g., native, web).
            test_execution_mode (TestExecutionMode): The mode of test execution (e.g., parallel, sequential).
            test_environment (TestEnvironments): The environment in which the test will run (e.g., staging, production).
            capabilities (dict[str, Any]): A dictionary of desired capabilities for the mobile driver.
        """
        pass
