from . import Enum, unique


@unique
class WebBrowserMake(Enum):
    """Web browser names as constants"""

    CHROME = "chrome"
    FIREFOX = "firefox"
    BRAVE = "brave"
    MSEDGE = "msedge"
    IE = "ie"
    CHROMIUM = "chromium"
    SAFARI = "safari"


@unique
class MobileWebBrowserMake(Enum):
    """Mobile web browser name as constants"""

    CHROME = "Chrome"
    SAFARI = "Safari"
    CHROMIUM = "Chromium"
    BROWSER = "Browser"
