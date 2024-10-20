"""
Driver Module

This module provides the core structure for managing driver creation through the Factory Design Pattern. 
It encapsulates the logic for creating both mobile and web drivers, supporting various platforms (e.g., Android, iOS) 
and browsers (e.g., Chrome, Firefox, Edge, etc.). The `driver` module serves as a central location for defining 
the abstract and concrete factories required for driver instantiation.

This module is part of the `factories.driver` hierarchy, which is divided into abstract factories, concrete 
factories, and platform-specific product definitions.

## Structure

The `driver` module is organized as follows:

- `abstract_factory/`: Contains abstract base classes for creating web and mobile drivers.
    - `abstract_factory.py`: Core abstract factory definitions for web and mobile drivers.
    - `abstract_products/`: Contains product-specific abstract base classes.
        - `abstract_mobile/`: Contains abstract classes for mobile driver platforms.
            - `abstract_android.py`: Defines the abstract Android driver class.
            - `abstract_ios.py`: Defines the abstract iOS driver class.
            - `abstract_mobile.py`: Common base class for mobile drivers.
        - `abstract_web/`: Contains abstract classes for web driver platforms.
            - `abstract_chrome.py`: Defines the abstract Chrome web driver class.
            - `abstract_firefox.py`: Defines the abstract Firefox web driver class.
            - `abstract_msedge.py`: Defines the abstract Microsoft Edge web driver class.
            - `abstract_ie.py`: Defines the abstract Internet Explorer driver class.
            - `abstract_chromium.py`: Defines the abstract Chromium driver class.
            - `abstract_brave.py`: Defines the abstract Brave browser driver class.
            - `abstract_web_driver.py`: Common base class for web drivers, defining shared behavior.

- `concrete_factory/`: Contains concrete implementations of the abstract factories.
    - `concrete_mobile_driver_factory.py`: Concrete factory for creating mobile drivers (e.g., Android, iOS).
    - `concrete_web_driver_factory.py`: Concrete factory for creating web drivers (e.g., Chrome, Firefox, etc.).
    - `concrete_products/`: Contains platform-specific concrete driver classes.
        - `mobile/`: Concrete implementations for mobile drivers.
            - `concrete_android_driver.py`: Concrete implementation for the Android mobile driver.
            - `concrete_ios_driver.py`: Concrete implementation for the iOS mobile driver.
        - `web/`: Concrete implementations for web drivers.
            - `concrete_chrome_driver.py`: Concrete implementation for the Chrome web driver.
            - `concrete_firefox_driver.py`: Concrete implementation for the Firefox web driver.
            - `concrete_msedge_driver.py`: Concrete implementation for the Microsoft Edge web driver.
            - `concrete_ie_driver.py`: Concrete implementation for the Internet Explorer web driver.
            - `concrete_brave_driver.py`: Concrete implementation for the Brave browser driver.
            - `concrete_web_driver.py`: Common concrete implementation for general web drivers.

## Purpose

The `driver` module is responsible for managing driver creation using the Factory Design Pattern. By separating 
abstract and concrete implementations, this module allows for flexibility in driver creation while supporting 
multiple platforms and browsers. The factories enable consistent and scalable driver instantiation for both 
mobile and web applications.

This module makes it easy to extend support for new platforms or browsers without modifying existing code, 
ensuring the system remains maintainable and scalable.

## Usage

The `driver` module follows the Factory Design Pattern, where concrete factories extend abstract factory base classes 
and provide specific logic for driver creation. Client code interacts with these factories to create mobile or 
web drivers based on the required platform or browser.

Example of creating a mobile driver:

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
