from abc import ABC, abstractmethod
from typing import Any

from uaf.enums.mobile_os import MobileOs
from uaf.enums.test_environments import TestEnvironments
from uaf.enums.test_execution_mode import TestExecutionMode


class AbstractMobile(ABC):
    """Mobile interface"""

    @abstractmethod
    def __init__(
        self,
        *,
        os: MobileOs,
        test_execution_mode: TestExecutionMode,
        test_environment: TestEnvironments,
    ) -> None:
        """Instance creation skeleton

        Args:
            os (MobileOs): enum
            test_execution_mode (TestExecutionMode): enum
            test_environment (TestEnvironments): enum
        """
        pass

    @abstractmethod
    def get_mobile_driver(self, *, capabilities: dict[str, Any]):
        """Retrives mobile driver if present or creates and returns a new instance

        Args:
            capabilities (dict[str, Any]): mobile driver capabilities
        """
        pass
