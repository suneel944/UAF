from . import Enum


class MobileAppType(Enum):
    """Mobile app type as constant

    Args:
        Enum (MobileAppType): enum
    """

    HYBRID = "hybrid"
    NATIVE = "native"
    WEB = "web"
