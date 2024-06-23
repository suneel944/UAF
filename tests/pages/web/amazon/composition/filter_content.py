from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage
from tests.pages.web.amazon.composition.product_content import ProductContent


class FilterContent(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def __cbox_left_filter_pane(self, text: str) -> tuple[str, str]:
        return (By.XPATH, f".//*[@id='s-refinements']//*[text()='{text}']/..")

    def select_filter_content_parent_category(
        self, parent_choice_category: str, parent_choice: str
    ) -> "FilterContent":
        self.wait.wait_for_element_presence(
            self.__cbox_left_filter_pane(parent_choice_category)
        )
        self.scroller.scroll_to_element(
            self.__cbox_left_filter_pane(parent_choice_category)
        )
        self.element.click_on_element(self.__cbox_left_filter_pane(parent_choice))
        return self

    def select_filter_content_child_category(
        self, child_choice_category: str, child_choice: str
    ) -> ProductContent:
        self.wait.wait_for_element_presence(
            self.__cbox_left_filter_pane(child_choice_category)
        )
        self.scroller.scroll_to_element(
            self.__cbox_left_filter_pane(child_choice_category)
        )
        self.element.click_on_element(self.__cbox_left_filter_pane(child_choice))
        return ProductContent(self.driver)
