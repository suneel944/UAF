from uaf.enums.file_paths import FilePaths
from uaf.utilities.parser.yaml_parser_utils import YamlParser
from uaf.utilities.selenium.element.element_utils import ElementUtils
from uaf.utilities.selenium.locator.locator_utils import LocatorUtils
from uaf.utilities.selenium.scroller.scroll import Scroll
from uaf.utilities.selenium.waiter.waits import Waits
from uaf.utilities.selenium.window.window_utils import WindowUtils


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.element_util = ElementUtils(driver)
        self.scroller = Scroll(driver)
        self.config = YamlParser(FilePaths.COMMON)
        self.wait = Waits(driver)
        self.locator = LocatorUtils(driver)
        self.window = WindowUtils(driver)
