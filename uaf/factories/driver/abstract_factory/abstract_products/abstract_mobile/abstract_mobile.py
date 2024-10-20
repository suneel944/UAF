from abc import ABC, abstractmethod
from typing import Any

from uaf.enums.mobile_os import MobileOs
from uaf.enums.environments import Environments
from uaf.enums.execution_mode import ExecutionMode
from uaf.enums.mobile_app_type import MobileAppType


class AbstractMobile(ABC):
    """Abstract base class for mobile interface.

    This class defines the skeleton for creating mobile instances and retrieving mobile drivers.
    All derived classes must implement the methods for initializing and retrieving mobile drivers.
    """

    @abstractmethod
    def __init__(
        self,
        *,
        os: MobileOs,
        app_type: MobileAppType,
        execution_mode: ExecutionMode,
        environment: Environments,
    ) -> None:
        """Initialize the mobile interface.

        This method serves as the constructor for any subclass implementing the mobile interface.

        Args:
            os (MobileOs): The operating system for the mobile device (e.g., Android, iOS).
            app_type (MobileAppType): The type of mobile application (e.g., native, web, hybrid).
            execution_mode (ExecutionMode): The mode of test execution (e.g., local, remote).
            environment (Environments): The environment where the mobile application will run (e.g., staging, production).
        """
        pass

    @abstractmethod
    def get_mobile_driver(self, *, capabilities: dict[str, Any]):
        """Retrieve or create a new mobile driver instance based on the provided capabilities.

        Args:
            capabilities (dict[str, Any]): A dictionary of desired capabilities for configuring the mobile driver.
        """
        pass
