from typing import Any

from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __TXT_PRODUCT_DETAILS: tuple[str, str] = (By.XPATH, ".//*[@id='featureSeeMore']//*[@id='feature-bullets']")

    def get_product_text_content(self) -> str | Any:
        self.window.switch_to_succeeding_window()
        self.scroller.scroll_to_element(self.__TXT_PRODUCT_DETAILS)
        return self.element.get_text_from_element(self.__TXT_PRODUCT_DETAILS)
