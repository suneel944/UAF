from appium.webdriver.common.appiumby import AppiumBy

from tests.pages.base_page import BasePage
from tests.pages.mobile.amazon.composition.category_content import CategoryContent
from tests.pages.mobile.amazon.composition.product_content import ProductContent


class HeaderContent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Elements
    __BTN_HAMBURGER_MENU: tuple[str, str] = (AppiumBy.XPATH, ".//*[@id='nav-hamburger-menu']")
    __ELE_FILTER_MENU: tuple[str, str] = (AppiumBy.XPATH, ".//*[@data-csa-c-content-id='s-all-filters']")
    __LNK_SHOW_RESULTS: tuple[str, str] = (AppiumBy.XPATH, "//*[contains(text(),'result')]//parent::a")

    def __tab_filter_panel_selection(self, tab_name: str) -> tuple[str, str]:
        return (AppiumBy.XPATH, f".//*[@id='{tab_name}']//*[@data-action='s-vtab-action']")

    def __lnk_left_panel_menu_selection(self, text: str) -> tuple[str, str]:
        return (AppiumBy.XPATH, f".//*[@id='hmenu-content']//*[contains(@class,'hmenu-visible')]//*[text()='{text}']")

    def __lnk_sort_by(self, type: str):
        return (AppiumBy.XPATH, f".//*[contains(@id,'sort/')]//*[text()='{type}']")

    def get_category_content(self) -> CategoryContent:
        """Retrieves filter content instance

        Returns:
            FilterContent: filter content instance
        """
        return CategoryContent(self.driver)

    def get_product_content(self):
        """Retrieves product content instance

        Returns:
            ProductContent: product content instance
        """
        return ProductContent(self.driver)

    def filter_product_based_on_specifics(self, tab_name: str, filter_specific: str):
        self.element.click_on_element(self.__ELE_FILTER_MENU)
        self.wait.wait_for_element_visibility(self.__tab_filter_panel_selection(tab_name))
        self.element.click_on_element(self.__tab_filter_panel_selection(tab_name))
        self.element.click_on_element(self.__lnk_sort_by(filter_specific))
        self.element.click_on_element(self.__LNK_SHOW_RESULTS)
        return self

    def click_on_hamburger_menu(self) -> "HeaderContent":
        self.element.click_on_element(self.__BTN_HAMBURGER_MENU)
        return self

    def select_left_menu_specifics(self, heading: str, sub_section: str) -> "HeaderContent":
        self.scroller.scroll_to_element(self.__lnk_left_panel_menu_selection(heading))
        self.element.click_on_element_using_js(self.__lnk_left_panel_menu_selection(sub_section))
        return self
