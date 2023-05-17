from uaf.enums.file_paths import FilePaths
from uaf.utilities.parser.yaml_parser_utils import YamlParser
from uaf.utilities.ui.element.element_utils import ElementUtils
from uaf.utilities.ui.locator.locator_utils import LocatorUtils
from uaf.utilities.ui.scroller.scroll import ScrollUtils
from uaf.utilities.ui.swipe.swipe_utils import SwipeUtils
from uaf.utilities.ui.waiter.waits import Waits
from uaf.utilities.ui.window.window_utils import WindowUtils


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.element = ElementUtils(driver)
        self.scroller = ScrollUtils(driver)
        self.config = YamlParser(FilePaths.COMMON)
        self.wait = Waits(driver)
        self.locator = LocatorUtils(driver)
        self.window = WindowUtils(driver)
        self.swipe = SwipeUtils(driver)
