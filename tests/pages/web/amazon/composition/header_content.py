from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage
from tests.pages.web.amazon.composition.filter_content import FilterContent


class HeaderContent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Elements
    __BTN_HAMBURGER_MENU: tuple[str, str] = (By.XPATH, ".//*[@id='nav-hamburger-menu']")

    def __lnk_left_panel_menu_selection(self, text: str) -> tuple[str, str]:
        return (
            By.XPATH,
            f".//*[@id='hmenu-content']//*[contains(@class,'hmenu-visible')]//*[text()='{text}']",
        )

    def get_filter_content(self) -> FilterContent:
        """Retrieves filter content instance

        Returns:
            FilterContent: FilterContent instance
        """
        return FilterContent(self.driver)

    def click_on_hamburger_menu(self) -> "HeaderContent":
        self.element.click_on_element(self.__BTN_HAMBURGER_MENU)
        return self

    def select_left_menu_specifics(
        self, heading: str, sub_section: str
    ) -> "HeaderContent":
        self.scroller.scroll_to_element(self.__lnk_left_panel_menu_selection(heading))
        self.element.click_on_element(self.__lnk_left_panel_menu_selection(sub_section))
        return self
