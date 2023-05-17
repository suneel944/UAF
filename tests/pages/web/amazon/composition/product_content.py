from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class ProductContent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_product_page(self):
        """Retrieves product page instance

        Returns:
            _type_: _description_
        """
        from tests.pages.web.amazon.product_page import ProductPage

        return ProductPage(self.driver)

    __TXT_PRODUCT_PRICE = (By.XPATH, "//span[@class='a-price-whole'][1]")
    __SLT_PRODUCT_SORT = (By.XPATH, ".//*[@id='s-result-sort-select']")

    def sort_product(self, value):
        self.wait.wait_for_page_load()
        self.element.select_from_drop_down(self.__SLT_PRODUCT_SORT, value)
        return self

    def click_on_the_desired_product(self, product_index):
        self.element.click_on_element(self.__TXT_PRODUCT_PRICE)
        # return product page instance
        return self.get_product_page()
