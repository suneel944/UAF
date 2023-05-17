from . import Enum, unique


@unique
class MobileOs(Enum):
    """Mobile Os variants as constant

    Args:
        Enum (MobileOs): enum
    """

    ANDROID = "android"
    IOS = "ios"
    FIREFOX_OS = "FirefoxOS"
