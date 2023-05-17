from typing import Any

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement as MobileElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from uaf.decorators.loggers.logger import log


class LocatorUtils:
    def __init__(self, driver):
        self.driver = driver

    def __perform_by_to_element_conversion(self, by_locator) -> Any:
        locator_type, locator_value = by_locator  # type: ignore
        return self.driver.find_element(locator_type, locator_value)  # type: ignore

    @log
    def by_locator_to_web_element(self, by_locator: tuple[By, str]) -> WebElement:
        """Convert by_locator to web_element

        Args:
            by_locator (tuple[By,str]): (locatory type, locator value)

        Returns:
            webelement: webelement instance
        """
        return self.__perform_by_to_element_conversion(by_locator)

    @log
    def by_locator_to_mobile_element(self, by_locator: tuple[AppiumBy, str]) -> MobileElement:
        """Convert by_locator to mobile version of webelement

        Args:
            by_locator (tuple[AppiumBy, str]): (locator type, locator value)

        Returns:
            MobileElement: appium webelement instance
        """
        return self.__perform_by_to_element_conversion(by_locator)

    @log
    def by_locator_to_web_elements(self, by_locator: tuple[str]) -> list[WebElement]:
        """Convert by_locator to list of web_elements

        Args:
            by_locator (tuple[str]): (locator type, locator value)

        Returns:
            list[webelement]: list of webelement instance
        """
        locator_type, locator_value = by_locator  # type: ignore
        return self.driver.find_elements(locator_type, locator_value)  # type: ignore
