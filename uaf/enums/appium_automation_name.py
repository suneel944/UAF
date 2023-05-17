from . import Enum, unique


@unique
class AppiumAutomationName(Enum):
    """Appium automation name constants"""

    UIAUTOMATOR2 = "UiAutomator2"
    ESPRESSO = "Espresso"
    UiAutomator1 = "UiAutomator1"
    XCUITEST = "XCUITest"
    INSTRUMENTS = "Instruments"
    YOU_I_ENGINE = "YouiEngine"
