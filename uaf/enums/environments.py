from . import Enum, unique


@unique
class Environments(Enum):
    """Test environments as constant

    Args:
        Enum (Environments): enum
    """

    DEVELOPMENT = "dev"
    STAGE = "stage"
    QA = "qa"
    PRODUCTION = "prod"
