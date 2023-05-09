import time

from selenium.webdriver.support.select import Select

from uaf.decorators.loggers.logger import log
from uaf.utilities.selenium.locator.locator_utils import LocatorUtils
from uaf.utilities.selenium.waiter.waits import Waits


class ElementUtils:
    """Selenium wrapper utiity for element interactions"""

    def __init__(self, driver):
        """Constructor

        Args:__wait_for_title
            driver (webdriver): webdriver instance
        """
        self.driver = driver
        self.wait = Waits(self.driver)
        self.locator = LocatorUtils(driver)

    @log
    def click_on_element(self, by_locator: tuple[str]):
        """Clicks on a element which is interactable"""
        self.wait.wait_for_element_to_be_clickable(by_locator).click()  # type: ignore
        return self

    @log
    def launch_url(self, url: str):
        """Launch a url

        Args:
            url (str): website page address
        """
        self.driver.get(url)
        self.wait.wait_for_page_load()
        return self

    @log
    def fetch_title(self, title: str):
        """Fetches title of the current active/in-foucs webpage

        Args:
            title (str): title of website

        Returns:
            str: actual title of website
        """
        self.wait.wait_for_title(title)  # type: ignore
        return self.driver.title

    @log
    def send_keys(self, by_locator: tuple[str], text: str, enter_char_by_char: bool = False):
        """Send text to edit field

        Args:
            by_locator (_type_): by locator
            text (str): text to be entered
            enter_char_by_char (bool, optional): if True, enters texts character by character. Defaults to False.
        """
        if not enter_char_by_char:
            self.locator.by_locator_to_web_element(by_locator).send_keys(text)  # type: ignore
        else:
            for i in text:
                self.locator.by_locator_to_web_element(by_locator).send_keys(i)  # type: ignore
                time.sleep(0.5)  # introduced forced delay to mimic user typing
        return self

    @log
    def get_text_from_element(self, by_locator: tuple[str]):
        return self.locator.by_locator_to_web_element(by_locator).text  # type: ignore

    @log
    def select_from_drop_down(self, by_locator: tuple[str], value: str):
        element = self.locator.by_locator_to_web_element(by_locator)  # type: ignore
        select = Select(element)
        select.select_by_value(value)
        return self
