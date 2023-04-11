from typing import Tuple
from webdriver_manager.core.manager import DriverManager
from . import Enum
from . import (
    ChromeDriverManager,
    GeckoDriverManager,
    IEDriverManager,
    EdgeChromiumDriverManager,
    OperaDriverManager,
)


class DriverExecutablePaths(Enum):
    CHROME: Tuple[str, str] = ("chromedriver", ChromeDriverManager())
    FIREFOX: Tuple[str, str] = ("geckodriver", GeckoDriverManager())
    IE: Tuple[str, str] = ("IEDriverServer", IEDriverManager())
    MSEDGE: Tuple[str, str] = ("msedgedriver", EdgeChromiumDriverManager())
    OPERA: Tuple[str, str] = ("operadriver", OperaDriverManager())

    # defined to resolve mypy error
    driver_manager: DriverManager

    def __new__(cls, value, driver_manager):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.driver_manager = driver_manager
        return obj

    def get_path(self):
        return self.driver_manager.install()

    @classmethod
    def get_driver_path(cls, driver: "DriverExecutablePaths"):
        for enum_val in cls:
            if enum_val == driver:
                return enum_val.get_path()
        raise ValueError(f"Unknown driver: {driver}")
