"""
AbstractWeb Module

This module contains the abstract base classes used for creating web drivers within the factory design pattern. 
These classes provide a blueprint for different web browser drivers (e.g., Chrome, Firefox, Edge), ensuring that 
any concrete implementations will adhere to a consistent interface for creating web drivers.

This module is part of the `factories.driver.abstract_factory.abstract_products.abstract_web` hierarchy and 
is responsible for defining platform-agnostic methods for creating web drivers. Each abstract class in this 
module corresponds to a specific browser or web driver type.

## Structure

The `abstract_web` module defines abstract classes for different web browsers:

- `abstract_chrome.py`: Abstract class for Chrome web driver.
- `abstract_firefox.py`: Abstract class for Firefox web driver.
- `abstract_msedge.py`: Abstract class for Microsoft Edge web driver.
- `abstract_chromium.py`: Abstract class for Chromium-based web drivers.
- `abstract_ie.py`: Abstract class for Internet Explorer web driver.
- `abstract_brave.py`: Abstract class for Brave browser driver.
- `abstract_web_driver.py`: Common base class that all other web drivers extend, defining shared behavior and interfaces.

## Purpose

Each abstract class defines the blueprint for creating specific web drivers, which concrete classes 
will implement. This provides flexibility and a consistent interface for creating web drivers 
in the factory design pattern, ensuring easy extension and maintenance of different browser drivers.

## Usage

Concrete web driver factories (e.g., `ConcreteChromeDriver`, `ConcreteFirefoxDriver`) inherit from these 
abstract classes and implement the methods for creating the actual browser drivers. The factories ensure 
that the instantiation logic is hidden from the client code, providing a clean interface for web driver 
creation.

Example of how the abstract web classes are extended:

```python
class ConcreteChromeDriver(AbstractChrome):
    def get_driver(self, capabilities: dict[str, Any]):
        # Implementation for creating Chrome web driver instance
        pass
"""
