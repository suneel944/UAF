from . import Enum


class TestEnvironments(Enum):
    """Test environments as constant

    Args:
        Enum (TestEnvironments): enum
    """

    DEVELOPMENT = "dev"
    STAGE = "stage"
    QA = "qa"
    PRODUCTION = "prod"
