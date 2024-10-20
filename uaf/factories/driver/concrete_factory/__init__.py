"""
ConcreteFactory Module

This module contains the concrete implementations of the Factory Design Pattern for creating web and mobile drivers. 
The concrete factories in this module provide platform-specific logic to instantiate drivers for various environments 
and platforms (e.g., Android, iOS, Chrome, Firefox). These concrete classes inherit from the abstract factory base classes 
and define the actual creation logic for each driver type.

This module is part of the `factories.driver.concrete_factory` hierarchy and complements the abstract factory module 
by providing real-world driver instantiation implementations.

## Structure

The `concrete_factory` module is organized as follows:

- `concrete_mobile_driver_factory.py`: Contains the logic for creating mobile drivers, supporting Android and iOS platforms.
- `concrete_web_driver_factory.py`: Contains the logic for creating web drivers, supporting various browsers like Chrome, Firefox, and Edge.
- `concrete_products/`: A subdirectory that contains the concrete driver implementations for each platform.
    - `mobile/`: Contains concrete classes for mobile drivers.
        - `concrete_android_driver.py`: Defines the Android mobile driver instantiation logic.
        - `concrete_ios_driver.py`: Defines the iOS mobile driver instantiation logic.
    - `web/`: Contains concrete classes for web drivers.
        - `concrete_chrome_driver.py`: Defines the Chrome browser driver instantiation logic.
        - `concrete_firefox_driver.py`: Defines the Firefox browser driver instantiation logic.
        - `concrete_msedge_driver.py`: Defines the Microsoft Edge browser driver instantiation logic.
        - `concrete_ie_driver.py`: Defines the Internet Explorer browser driver instantiation logic.
        - `concrete_brave_driver.py`: Defines the Brave browser driver instantiation logic.
        - `concrete_web_driver.py`: Common concrete implementation for general web drivers.

## Purpose

The purpose of the `concrete_factory` module is to provide platform-specific implementations for the abstract factories defined in the 
`abstract_factory` module. These concrete classes are responsible for creating mobile and web drivers with platform-specific options 
and capabilities. This module makes it possible to easily extend support for new platforms or browsers without modifying the core logic.

## Usage

The `concrete_factory` module is used to instantiate drivers based on the provided platform or browser type. 
The concrete factories hide the complexity of driver creation from the client, ensuring that all drivers 
are created according to platform-specific requirements.

Example for creating a mobile driver:

```python
from factories.driver.concrete_factory.concrete_mobile_driver_factory import ConcreteMobileDriverFactory

mobile_driver_factory = ConcreteMobileDriverFactory()
driver = mobile_driver_factory.get_mobile_driver(
    os=MobileOs.ANDROID,
    app_type=MobileAppType.NATIVE,
    execution_mode=ExecutionMode.LOCAL,
    environment=Environments.STAGING,
    capabilities={"platformName": "Android", "deviceName": "Pixel_4"}
)

from factories.driver.concrete_factory.concrete_web_driver_factory import ConcreteWebDriverFactory

web_driver_factory = ConcreteWebDriverFactory()
driver = web_driver_factory.get_web_driver(
    browser_make=WebBrowserMake.CHROME,
    options={"headless": True}
)
"""

from typing import Any, Optional

from appium.webdriver.webdriver import WebDriver
from uaf.enums.browser_make import WebBrowserMake
from uaf.enums.mobile_os import MobileOs
from uaf.enums.environments import Environments
from uaf.enums.execution_mode import ExecutionMode
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
    "ExecutionMode",
    "MobileAppType",
    "Environments",
    "ConcreteMobileDriver",
    "ConcreteWebDriver",
]
