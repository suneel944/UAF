from abc import ABC, abstractmethod
from typing import Any
from uaf.enums.mobile_os import MobileOs
from uaf.enums.test_execution_mode import TestExecutionMode
from uaf.enums.test_environments import TestEnvironments


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
            os (MobileOs): _description_
            test_execution_mode (TestExecutionMode): _description_
            test_environment (TestEnvironments): _description_
        """
        pass

    @abstractmethod
    def get_mobile_driver(self, *, capabilities: dict[str, Any]):
        """Retrives mobile driver if present or creates and returns a new instance

        Args:
            capabilities (dict[str, Any]): _description_
        """
        pass
