from . import Enum, unique


@unique
class MobileAppType(Enum):
    """Mobile app type as constant

    Args:
        Enum (MobileAppType): enum
    """

    HYBRID = "hybrid"
    NATIVE = "native"
    WEB = "web"
