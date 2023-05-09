from selenium.webdriver.common.by import By

from tests.pages.amazon.composition.filter_content import FilterContent
from tests.pages.base_page import BasePage


class HeaderContent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Elements
    __BTN_HAMBURGER_MENU: tuple = (By.ID, "nav-hamburger-menu")

    def __lnk_left_panel_menu_selection(self, text: str) -> tuple:
        return (By.XPATH, f".//*[@id='hmenu-content']//*[contains(@class,'hmenu-visible')]//*[text()='{text}']")

    def get_filter_content(self) -> FilterContent:
        """Retrieves filter content instance

        Returns:
            FilterContent: FilterContent instance
        """
        return FilterContent(self.driver)

    def click_on_hamburger_menu(self) -> "HeaderContent":
        self.element_util.click_on_element(self.__BTN_HAMBURGER_MENU)
        return self

    def select_left_menu_specifics(self, heading: str, sub_section: str) -> "HeaderContent":
        self.scroller.scroll_to_element(self.__lnk_left_panel_menu_selection(heading))
        self.element_util.click_on_element(self.__lnk_left_panel_menu_selection(sub_section))
        return self
