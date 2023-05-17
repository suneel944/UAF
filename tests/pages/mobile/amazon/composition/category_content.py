from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage
from tests.pages.mobile.amazon.composition.product_content import ProductContent


class CategoryContent(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def get_product_content(self) -> ProductContent:
        """Retrieves product content instance

        Returns:
            ProductContent: product content instance
        """
        return ProductContent(self.driver)

    def __img_category_grid(self, text: str) -> tuple[str, str]:
        return (By.XPATH, f".//*[@alt='{text}']")

    def select_category_grid(self, category: str):
        """Select category grid

        Args:
            category (str): name of category

        Returns:
            CategoryContent: category content instance
        """
        self.scroller.scroll_to_element(self.__img_category_grid(category))
        self.element.click_on_element(self.__img_category_grid(category))
        return self
