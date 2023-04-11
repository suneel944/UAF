from . import Enum


class WebBrowserMake(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"
    BRAVE = "brave"
    MSEDGE = "msedge"
    IE = "ie"
    CHROMIUM = "chromium"
    SAFARI = "safari"


class MobileWebBrowserMake(Enum):
    CHROME = "Chrome"
    SAFARI = "Safari"
    CHROMIUM = "Chromium"
    BROWSER = "Browser"
