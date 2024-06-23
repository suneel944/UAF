from abc import ABCMeta, abstractmethod
from typing import Any, Optional

from uaf.enums.browser_make import WebBrowserMake
from uaf.enums.mobile_os import MobileOs
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
        test_execution_mode: TestExecutionMode,
        test_environment: TestEnvironments,
        capabilities: dict[str, Any],
    ):
        """Abstract method skeleton for fetching mobile driver

        Args:
            os (MobileOs): _description_
            test_execution_mode (TestExecutionMode): _description_
            test_environment (TestEnvironments): _description_
            capabilities (dict[str, Any]): _description_
        """
        pass
