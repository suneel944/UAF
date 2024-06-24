from abc import ABC, abstractmethod
from typing import Any
from uaf.enums.mobile_os import MobileOs
from uaf.enums.test_environments import TestEnvironments
from uaf.enums.test_execution_mode import TestExecutionMode


class AbstractMobile(ABC):
    """
    Abstract base class for defining a mobile driver interface.

    This class provides a template for creating mobile driver instances.
    Subclasses should implement methods for initializing and fetching mobile driver instances
    based on the OS, execution mode, environment, and capabilities.

    Attributes:
        os (MobileOs): Enum representing the mobile operating system.
        test_execution_mode (TestExecutionMode): Enum representing the test execution mode.
        test_environment (TestEnvironments): Enum representing the test environment.
    """

    @abstractmethod
    def __init__(
        self,
        *,
        os: MobileOs,
        test_execution_mode: TestExecutionMode,
        test_environment: TestEnvironments,
    ) -> None:
        """
        Initializes a mobile driver instance.

        This method should be implemented by subclasses to handle the creation
        of a specific mobile driver instance for the given OS, execution mode, and environment.

        Args:
            os (MobileOs): Enum representing the mobile operating system.
            test_execution_mode (TestExecutionMode): Enum representing the test execution mode.
            test_environment (TestEnvironments): Enum representing the test environment.
        """
        pass

    @abstractmethod
    def get_mobile_driver(self, *, capabilities: dict[str, Any]):
        """
        Fetches a mobile driver instance if present or creates and returns a new instance.

        This method should be implemented by subclasses to return a specific mobile driver
        instance configured with the provided capabilities.

        Args:
            capabilities (dict[str, Any]): Dictionary of mobile driver capabilities.

        Returns:
            WebDriver: An instance of the mobile driver configured with the specified capabilities.
        """
        pass
