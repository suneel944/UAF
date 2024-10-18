from typing import Any, Optional

from appium.webdriver.webdriver import WebDriver
from uaf.enums.browser_make import WebBrowserMake
from uaf.enums.mobile_os import MobileOs
from uaf.enums.test_environments import TestEnvironments
from uaf.enums.test_execution_mode import TestExecutionMode
from uaf.enums.mobile_app_type import MobileAppType
from uaf.factories.driver.abstract_factory import abstract_factory
from uaf.factories.driver.concrete_factory.concrete_products.mobile.concrete_mobile_driver import (
    ConcreteMobileDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.web.concrete_web_driver import (
    ConcreteWebDriver,
)

__all__ = [
    "abstract_factory",
    "Optional",
    "Any",
    "WebDriver",
    "WebBrowserMake",
    "MobileOs",
    "TestExecutionMode",
    "MobileAppType",
    "TestEnvironments",
    "ConcreteMobileDriver",
    "ConcreteWebDriver",
]
