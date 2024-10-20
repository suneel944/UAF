"""
Web ConcreteProducts Module

This module contains the concrete implementations for web browser drivers within the Factory Design Pattern. 
It supports various web browsers such as Chrome, Firefox, Microsoft Edge, Internet Explorer, and Brave. 
Each concrete class in this module implements the logic for creating and configuring web drivers specific to the browser 
requested, based on the abstract classes defined in the `abstract_web` module.

This module is part of the `factories.driver.concrete_factory.concrete_products.web` hierarchy, 
and it works alongside the concrete web driver factories to instantiate fully configured web drivers.

## Structure

The `web` module contains the following concrete classes for web browsers:

- `concrete_chrome_driver.py`: Implements the logic to create a Chrome web driver instance.
- `concrete_firefox_driver.py`: Implements the logic to create a Firefox web driver instance.
- `concrete_msedge_driver.py`: Implements the logic to create a Microsoft Edge web driver instance.
- `concrete_ie_driver.py`: Implements the logic to create an Internet Explorer web driver instance.
- `concrete_brave_driver.py`: Implements the logic to create a Brave browser driver instance.
- `concrete_chromium_driver.py`: Implements the logic to create a Chromium-based web driver instance.
- `concrete_web_driver.py`: Provides a common implementation for browser-agnostic web driver creation.

## Purpose

The purpose of this module is to provide concrete, browser-specific implementations for web drivers, ensuring that 
each browser’s unique requirements and configurations are handled properly. These concrete classes extend the abstract 
web driver products, encapsulating the logic for creating and launching web drivers for Chrome, Firefox, Edge, and others.

This module works within the Factory Design Pattern, where concrete web driver factories use these classes to create 
browser driver instances based on the client's requirements.

## Usage

The `web` module is used by the `concrete_web_driver_factory.py` to instantiate drivers for specific web browsers. 
The concrete classes within this module handle browser-specific details and ensure that drivers are created with 
the correct options and configurations.

Example for creating a Chrome web driver:

```python
from factories.driver.concrete_factory.concrete_products.web.concrete_chrome_driver import ConcreteChromeDriver

chrome_driver = ConcreteChromeDriver(remote_url="http://localhost:4444/wd/hub")
driver = chrome_driver.get_driver(options={"headless": True})

from factories.driver.concrete_factory.concrete_products.web.concrete_firefox_driver import ConcreteFirefoxDriver

firefox_driver = ConcreteFirefoxDriver(remote_url="http://localhost:4444/wd/hub")
driver = firefox_driver.get_driver(options={"headless": True})
"""

from selenium import webdriver

__all__ = ["webdriver"]
