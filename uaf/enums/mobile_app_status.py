from . import Enum, unique


@unique
class MobileAppStatus(Enum):
    """Mobile application status to indicate whether the app is installed or requires installation.

    Args:
        Enum (MobileAppStatus): enum
    """

    EXISTING = "existing"
    REQUIRES_INSTALLATION = "requires_installation"
