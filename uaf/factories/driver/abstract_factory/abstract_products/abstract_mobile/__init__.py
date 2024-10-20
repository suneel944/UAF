"""
AbstractMobile Module

This module contains the abstract base classes used for creating mobile drivers within the factory design pattern. 
These classes provide a blueprint for different mobile platform drivers (e.g., Android, iOS), ensuring that any 
concrete implementations will adhere to a consistent interface for creating mobile drivers.

This module is part of the `factories.driver.abstract_factory.abstract_products.abstract_mobile` hierarchy and is 
responsible for defining platform-agnostic methods for creating mobile drivers. Each abstract class in this module 
corresponds to a specific mobile driver type (e.g., Android or iOS).

## Structure

The `abstract_mobile` module defines abstract classes for different mobile platforms:

- `abstract_android.py`: Abstract class for the Android mobile driver.
- `abstract_ios.py`: Abstract class for the iOS mobile driver.
- `abstract_mobile.py`: Common base class that both Android and iOS mobile drivers extend, defining shared behavior 
  and interfaces.

## Purpose

Each abstract class defines the blueprint for creating specific mobile drivers, which concrete classes will implement. 
This provides flexibility and a consistent interface for creating mobile drivers in the factory design pattern, ensuring 
easy extension and maintenance of different mobile platforms.

## Usage

Concrete mobile driver factories (e.g., `ConcreteAndroidDriver`, `ConcreteIOSDriver`) inherit from these abstract 
classes and implement the methods for creating the actual mobile drivers. The factories ensure that the instantiation 
logic is hidden from the client code, providing a clean interface for mobile driver creation.

Example of how the abstract mobile classes are extended:

```python
class ConcreteAndroidDriver(AbstractAndroid):
    def get_mobile_driver(self, capabilities: dict[str, Any]):
        # Implementation for creating Android mobile driver instance
        pass

class ConcreteIOSDriver(AbstractIOS):
    def get_mobile_driver(self, capabilities: dict[str, Any]):
        # Implementation for creating iOS mobile driver instance
        pass
"""
