from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __TXT_PRODUCT_CONTENT: tuple = (By.ID, "feature-bullets")

    def get_product_text_content(self) -> str:
        self.window.switch_to_succeeding_window()
        self.scroller.scroll_to_element(self.__TXT_PRODUCT_CONTENT)
        return self.element_util.get_text_from_element(self.__TXT_PRODUCT_CONTENT)
