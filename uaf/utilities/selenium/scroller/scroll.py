import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from uaf.decorators.loggers.logger import log
from uaf.utilities.selenium.locator.locator_utils import LocatorUtils
from uaf.utilities.selenium.waiter.waits import Waits


class Scroll:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = Waits(driver)
        self.locator = LocatorUtils(driver)

    @log
    def scroll_to_element(self, by_locator):
        """Scroll to element

        Args:
            by_locator (tuple): (locator_type, locator_value)
        """
        element = self.locator.by_locator_to_web_element(by_locator)  # type: ignore
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    @log
    def scroll_to_bottom(self):
        """Scrolls to bottom of the page"""
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.END)

    @log
    def scroll_to_top(self):
        """Scrolls to page top"""
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.HOME)

    @log
    def is_bottom_reached(self):
        """Check if bottom reached during scrolling

        Returns:
            bool: True/False
        """
        return self.driver.execute_script(
            "return (window.innerHeight + window.pageYOffset) >= document.body.scrollHeight;"
        )

    @log
    def is_scroll_paused(self):
        """Checks if scrolling is paused

        Returns:
            bool: True/False
        """
        initial_position = self.driver.execute_script("return window.pageYOffset;")
        time.sleep(0.5)  # Adjust the delay as needed
        final_position = self.driver.execute_script("return window.pageYOffset;")
        return initial_position == final_position

    @log
    def scroll_to_bottom_with_pause(self, pause_duraton=1):
        """Scrolls to bottom of the page with pause

        Args:
            pause_duraton (int, optional): Duration for which scroll action is halted. Defaults to 1.
        """
        while not self.is_bottom_reached():
            self.scroll_to_bottom()
            time.sleep(pause_duraton)
