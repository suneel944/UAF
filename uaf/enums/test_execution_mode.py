from . import Enum, unique


@unique
class TestExecutionMode(Enum):
    """Test execution modes as constant

    Args:
        Enum (TestExecutionMode): enum
    """

    LOCAL = "local"
    REMOTE = "REMOTE"
