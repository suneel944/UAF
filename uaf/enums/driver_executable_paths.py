from typing import Tuple

from webdriver_manager.core.manager import DriverManager

from . import (
    ChromeDriverManager,
    EdgeChromiumDriverManager,
    Enum,
    GeckoDriverManager,
    IEDriverManager,
    OperaDriverManager,
    unique,
)


@unique
class DriverExecutablePaths(Enum):
    """Driver exectable paths as constants

    Args:
        Enum (DriverExecutablePaths): enum

    Raises:
        ValueError: if unknown driver is specified

    Returns:
        str: driver executable path
    """

    CHROME: Tuple[str, str] = ("chromedriver", ChromeDriverManager())
    FIREFOX: Tuple[str, str] = ("geckodriver", GeckoDriverManager())
    IE: Tuple[str, str] = ("IEDriverServer", IEDriverManager())
    MSEDGE: Tuple[str, str] = ("msedgedriver", EdgeChromiumDriverManager())
    OPERA: Tuple[str, str] = ("operadriver", OperaDriverManager())

    # defined to resolve mypy error
    driver_manager: DriverManager

    def __new__(cls, value, driver_manager):
        """Create custom instance of DriverExecutablePaths enum

        Args:
            value (str): value of the enum constant being created
            driver_manager (WebDriver): value of the enum constant being created

        Returns:
            DriverExecutablePaths: instance
        """
        obj = object.__new__(cls)
        obj._value_ = value
        obj.driver_manager = driver_manager
        return obj

    def __get_path(self):
        """Fetches path of the driver executable

        Returns:
            str: driver executable path
        """
        return self.driver_manager.install()

    @classmethod
    def get_driver_path(cls, driver: "DriverExecutablePaths"):
        """Fetches driver executable path

        Args:
            driver (DriverExecutablePaths): enum

        Raises:
            ValueError: if unknown driver is specified

        Returns:
            str: driver executable path
        """
        for enum_val in cls:
            if enum_val == driver:
                return enum_val.__get_path()
        raise ValueError(f"Unknown driver: {driver}")
