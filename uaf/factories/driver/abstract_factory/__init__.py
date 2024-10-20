"""
AbstractFactory Module

This module contains the abstract base classes that define the blueprint for creating web and mobile drivers using the Factory Design Pattern. 
The abstract factory classes in this module provide the framework for platform-agnostic driver creation, allowing concrete implementations 
to define the specifics for each platform or browser type.

This module is part of the `factories.driver.abstract_factory` hierarchy and contains the essential base classes for creating both mobile 
and web drivers in a flexible and extendable manner.

## Structure

The `abstract_factory` module defines several abstract factories for creating drivers:

- `abstract_factory.py`: The central file that contains high-level factory base classes.
- `abstract_products/`: A subdirectory that contains abstract products, which are specific for both web and mobile drivers. These define 
  platform or browser-specific base classes for concrete implementations.
    - `abstract_mobile/`: Contains abstract base classes for mobile platforms such as Android and iOS.
    - `abstract_web/`: Contains abstract base classes for web browsers such as Chrome, Firefox, Edge, and others.

## Purpose

The purpose of this module is to define common interfaces for creating drivers in a structured and extendable way. These abstract factories 
ensure that all concrete driver factories follow a consistent pattern for creating web or mobile drivers.

By using these abstract base classes, the system can easily expand to support new platforms or browsers without modifying the core driver 
logic.

## Usage

Concrete factories (e.g., `ConcreteMobileDriverFactory`, `ConcreteWebDriverFactory`) inherit from the abstract factories defined in this 
module and implement platform-specific driver creation logic. This design pattern ensures that driver creation is encapsulated, 
and the client code only interacts with a simplified interface for driver retrieval.

Example of extending an abstract factory for mobile drivers:

```python
class ConcreteMobileDriverFactory(AbstractMobileDriverFactory):
    def get_mobile_driver(self, os: MobileOs, app_type: MobileAppType, execution_mode: ExecutionMode, environment: Environments, capabilities: dict[str, Any]):
        # Implementation for creating mobile driver instance (Android or iOS)
        pass

class ConcreteWebDriverFactory(AbstractWebDriverFactory):
    def get_web_driver(self, browser_make: WebBrowserMake, options: dict[str, Any] | None = None):
        # Implementation for creating web driver instance (Chrome, Firefox, etc.)
        pass
"""
