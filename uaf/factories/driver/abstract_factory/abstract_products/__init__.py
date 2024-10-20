"""
AbstractProducts Module

This module contains abstract base classes representing platform-specific products (web and mobile drivers). 
It serves as the core for defining platform-agnostic driver creation logic within the Factory Design Pattern. 
The classes in this module act as the blueprint for different browser drivers and mobile platform drivers, 
ensuring consistency across concrete implementations.

This module is part of the `factories.driver.abstract_factory.abstract_products` hierarchy, 
and it is further divided into submodules for mobile and web driver products.

## Structure

The `abstract_products` module is organized into the following submodules:

- `abstract_mobile/`: Contains abstract base classes for creating mobile drivers.
    - `abstract_android.py`: Abstract class for Android mobile drivers.
    - `abstract_ios.py`: Abstract class for iOS mobile drivers.
    - `abstract_mobile.py`: Common base class for mobile drivers (Android and iOS).
  
- `abstract_web/`: Contains abstract base classes for creating web drivers.
    - `abstract_chrome.py`: Abstract class for Chrome web drivers.
    - `abstract_firefox.py`: Abstract class for Firefox web drivers.
    - `abstract_msedge.py`: Abstract class for Microsoft Edge web drivers.
    - `abstract_chromium.py`: Abstract class for Chromium-based web drivers.
    - `abstract_ie.py`: Abstract class for Internet Explorer web drivers.
    - `abstract_brave.py`: Abstract class for Brave web drivers.
    - `abstract_web_driver.py`: Common base class for all web drivers, defining shared behaviors.

## Purpose

The purpose of this module is to provide a structure that ensures platform-specific (web and mobile) drivers follow a 
consistent creation pattern. Each abstract product represents a browser or mobile platform driver, and concrete classes 
implement these abstract products to provide platform-specific functionality.

These abstract classes allow the factories to define driver creation in a modular way, ensuring easy expansion to new 
platforms or browsers while adhering to the predefined structure.

## Usage

Concrete products (e.g., `ConcreteAndroidDriver`, `ConcreteChromeDriver`) inherit from the abstract products defined in this module 
and implement platform-specific logic for driver creation. By adhering to the abstract products, driver creation remains 
consistent and extensible across platforms.

Example of extending an abstract product for a mobile driver:

```python
class ConcreteAndroidDriver(AbstractAndroid):
    def get_driver(self, capabilities: dict[str, Any]):
        # Implementation for creating Android mobile driver
        pass

class ConcreteChromeDriver(AbstractChrome):
    def get_web_driver(self, options: dict[str, Any] | None = None):
        # Implementation for creating Chrome web driver
        pass
"""
