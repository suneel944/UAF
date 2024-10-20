from . import Enum, unique


@unique
class ExecutionMode(Enum):
    """Test execution modes as constant

    Args:
        Enum (ExecutionMode): enum
    """

    LOCAL = "local"
    REMOTE = "REMOTE"
