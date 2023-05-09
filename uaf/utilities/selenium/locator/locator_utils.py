from selenium.webdriver.remote.webelement import WebElement

from uaf.decorators.loggers.logger import log


class LocatorUtils:
    def __init__(self, driver):
        self.driver = driver

    @log
    def by_locator_to_web_element(self, by_locator: tuple[str]) -> WebElement:
        """Convert by_locator to web_element

        Args:
            by_locator (tuple[str]): (locatory type, locator value)

        Returns:
            webelement: webelement instance
        """
        locator_type, locator_value = by_locator  # type: ignore
        return self.driver.find_element(locator_type, locator_value)  # type: ignore

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
