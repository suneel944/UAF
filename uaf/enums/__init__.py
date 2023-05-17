from enum import Enum, unique

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager
from webdriver_manager.opera import OperaDriverManager

__all__ = [
    "Enum",
    "unique",
    "ChromeDriverManager",
    "GeckoDriverManager",
    "IEDriverManager",
    "EdgeChromiumDriverManager",
    "OperaDriverManager",
]
