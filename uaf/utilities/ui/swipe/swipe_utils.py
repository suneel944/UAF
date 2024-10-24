from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.pointer_input import PointerInput

from uaf.enums.direction import Direction
from uaf.utilities.ui.locator.locator_utils import LocatorUtils


class SwipeUtils:
    """Swipe utils which mimics swiping action using w3c actions \n
    **Note:** Works only on native context and webview context is out of focus,
    consider using javascript \n
    Reference: issue : https://github.com/appium/python-client/issues/867
    """

    def __init__(self, driver) -> None:
        self.driver = driver
        self.finger = PointerInput(POINTER_TOUCH, "finger")
        self.locator = LocatorUtils(driver)
        self.actions = ActionChains(driver)

    def __build_w3c_actions(self, start_x, start_y, end_x, end_y):
        self.actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        self.actions.w3c_actions.pointer_action.pointer_down()
        self.actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        self.actions.w3c_actions.pointer_action.release()

    def swipe(self, start_x, start_y, end_x, end_y, iterate_times=1):
        while iterate_times > 0:
            self.__build_w3c_actions(start_x, start_y, end_x, end_y)
            self.actions.perform()
            iterate_times -= 1

    def long_swipe(self, direction: Direction):
        start_x, start_y, end_x, end_y = 0, 0, 0, 0
        view_port = self.driver.get_window_size()
        match direction.value:
            case Direction.UP.value:
                start_x = view_port["width"] // 2
                start_y = int(view_port["height"] * 0.10)
                end_x = view_port["width"] // 2
                end_y = int(view_port["height"] * 0.8)
            case Direction.DOWN.value:
                start_x = view_port["width"] // 2
                start_y = int(view_port["height"] * 0.8)
                end_x = view_port["width"] // 2
                end_y = int(view_port["height"] * 0.10)
            case _:
                raise ValueError("Invalid direction!")
        self.__build_w3c_actions(start_x, start_y, end_x, end_y)
        self.actions.perform()

    def short_swipe(self, direction: Direction):
        start_x, start_y, end_x, end_y = 0, 0, 0, 0
        view_port = self.driver.get_window_size()
        match direction.value:
            case Direction.UP.value:
                start_x = view_port["width"] // 2
                start_y = int(view_port["height"] * 0.10)
                end_x = view_port["width"] // 2
                end_y = int(view_port["height"] * 0.45)
            case Direction.DOWN.value:
                start_x = view_port["width"] // 2
                start_y = int(view_port["height"] * 0.45)
                end_x = view_port["width"] // 2
                end_y = int(view_port["height"] * 0.10)
            case _:
                raise ValueError("Invalid direction!")
        self.__build_w3c_actions(start_x, start_y, end_x, end_y)
        self.actions.perform()

    def swipe_till_text_visibility(self, text: str, direction: Direction, max_swipe=10):
        if max_swipe <= 0:
            raise ValueError("max_swipe must be greater than 0")

        start_x, start_y, end_x, end_y = 0, 0, 0, 0
        view_port = self.driver.get_window_size()
        match direction.value:
            case Direction.LEFT.value:
                start_x = view_port["width"] // 2
                start_y = view_port["height"] // 2
                end_x = int(view_port["width"] * 0.90)
                end_y = view_port["height"] // 2
            case Direction.UP.value:
                start_x = view_port["width"] // 2
                start_y = int(view_port["height"] * 0.15)
                end_x = view_port["width"] // 2
                end_y = int(view_port["height"] * 0.45)
            case Direction.RIGHT.value:
                start_x = view_port["width"] // 2
                start_y = view_port["height"] // 2
                end_x = int(view_port["width"] * 0.10)
                end_y = view_port["height"] // 2
            case Direction.DOWN.value:
                start_x = view_port["width"] // 2
                start_y = int(view_port["height"] * 0.45)
                end_x = view_port["width"] // 2
                end_y = int(view_port["height"] * 0.10)
            case _:
                raise ValueError("Invalid direction!")

        while max_swipe > 0:
            if text in self.driver.page_source:
                return
            self.__build_w3c_actions(start_x, start_y, end_x, end_y)
            self.actions.perform()
            max_swipe -= 1

        raise NoSuchElementException(
            f"Text '{text}' not found after {max_swipe} swipes"
        )
