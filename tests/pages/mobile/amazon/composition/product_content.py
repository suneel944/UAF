from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class ProductContent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # locators
    def __ele_product_tile(self, product_index: int):
        return (
            By.XPATH,
            f".//*[@data-component-type='s-search-result'][{product_index}]",
        )

    # composition
    def get_product_page(self):
        """Retrieves product page instance

        Returns:
            _type_: _description_
        """
        from tests.pages.mobile.amazon.product_page import ProductPage

        return ProductPage(self.driver)

    # page actions

    def click_on_product(self, product_index: int):
        """Select product

        Args:
            product_index (int): product index

        Returns:
            ProductPage: product page instance
        """
        self.wait.wait_for_element_visibility(self.__ele_product_tile(product_index))
        self.scroller.scroll_to_element(self.__ele_product_tile(product_index))
        self.element.click_on_element(self.__ele_product_tile(product_index))
        return self
