"""
Mobile ConcreteProducts Module

This module provides the concrete implementations for mobile platform drivers, specifically targeting Android and iOS platforms. 
These concrete classes extend the abstract mobile driver products defined in the `abstract_mobile` module and implement the 
logic required to instantiate mobile drivers for these platforms.

This module is part of the `factories.driver.concrete_factory.concrete_products.mobile` hierarchy and works in conjunction 
with the concrete mobile factories to provide fully configured mobile drivers based on the provided capabilities and platform configurations.

## Structure

The `mobile` module contains the following concrete classes:

- `concrete_android_driver.py`: Implements the logic to create an Android mobile driver instance.
- `concrete_ios_driver.py`: Implements the logic to create an iOS mobile driver instance.
- `concrete_mobile_driver.py`: General implementation for mobile driver creation, combining the logic for Android and iOS platforms.

## Purpose

The purpose of this module is to provide platform-specific driver creation logic for Android and iOS devices. These classes handle the 
complexity of setting up mobile drivers and abstract the details from the client, ensuring that mobile drivers can be created 
consistently and easily across different environments.

This module is part of the broader Factory Design Pattern used in the project, where the concrete mobile driver factories utilize 
these platform-specific implementations to create the correct driver instance.

## Usage

This module is used by the `concrete_mobile_driver_factory.py` to instantiate mobile drivers for Android and iOS platforms. The 
concrete classes within the `mobile` module encapsulate the platform-specific logic required to create and configure these drivers.

Example for creating an Android mobile driver:

```python
from factories.driver.concrete_factory.concrete_products.mobile.concrete_android_driver import ConcreteAndroidDriver

android_driver = ConcreteAndroidDriver(remote_url="http://localhost:4723/wd/hub")
driver = android_driver.get_driver(capabilities={"platformName": "Android", "deviceName": "Pixel_4"})

from factories.driver.concrete_factory.concrete_products.mobile.concrete_ios_driver import ConcreteIOSDriver

ios_driver = ConcreteIOSDriver(remote_url="http://localhost:4723/wd/hub")
driver = ios_driver.get_driver(capabilities={"platformName": "iOS", "deviceName": "iPhone_12"})
"""
