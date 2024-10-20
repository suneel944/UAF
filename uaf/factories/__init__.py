"""
Factories Package

This package implements the Factory Design Pattern for creating web and mobile drivers. It provides 
a modular and extensible structure for instantiating drivers based on various platforms (e.g., Android, iOS, 
Chrome, Firefox). The goal of the `factories` package is to encapsulate the instantiation logic for different 
platforms and browsers, making the system flexible and scalable.

## Structure

The `factories` package is organized into the following submodules:

1. **driver/**:
   - This submodule contains the core logic for creating both mobile and web drivers using the Factory Design Pattern. 
   - Divided into `abstract_factory/` (for abstract base classes) and `concrete_factory/` (for concrete implementations), 
     the `driver` module handles the logic for driver creation across platforms and browsers.

2. **abstract_factory/driver/**:
   - Contains abstract base classes that define the blueprints for creating mobile and web drivers.
   - **Abstract Mobile Factory**:
     - `abstract_mobile_driver_factory.py`: Defines the structure for creating mobile drivers.
     - `abstract_products/abstract_mobile/`: Contains abstract classes for platform-specific mobile drivers like Android and iOS.
   - **Abstract Web Factory**:
     - `abstract_web_driver_factory.py`: Defines the structure for creating web drivers.
     - `abstract_products/abstract_web/`: Contains abstract classes for platform-specific web drivers like Chrome, Firefox, Edge, etc.

3. **concrete_factory/driver/**:
   - Contains concrete implementations of the abstract factories, providing platform-specific logic to create drivers.
   - **Concrete Mobile Factory**:
     - `concrete_mobile_driver_factory.py`: Implements the mobile driver creation logic for platforms like Android and iOS.
     - `concrete_products/mobile/`: Contains concrete classes for Android and iOS driver implementations.
   - **Concrete Web Factory**:
     - `concrete_web_driver_factory.py`: Implements the web driver creation logic for browsers like Chrome, Firefox, and Edge.
     - `concrete_products/web/`: Contains concrete classes for browser-specific implementations such as Chrome, Firefox, and Edge.

## Purpose

The purpose of the `factories` package is to provide an extensible and modular system for driver creation using 
the Factory Design Pattern. This pattern allows the system to grow by adding support for new platforms, browsers, 
or environments without modifying the core logic.

The package is designed to abstract the complexity of driver creation from the client code, 
ensuring that all drivers are created consistently and conform to predefined interfaces.

## Usage

The `factories` package is designed to be used by clients who need to create mobile or web drivers 
without worrying about the underlying details of instantiation. The factories take platform-specific 
or browser-specific parameters and return a configured driver instance.

Example for mobile driver creation:

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
