from tests.pages.base_page import BasePage
from tests.pages.web.amazon.composition.filter_content import FilterContent
from tests.pages.web.amazon.composition.header_content import HeaderContent
from tests.pages.web.amazon.composition.product_content import ProductContent


class HomePage(BasePage):
    """Page layer for amazon home page"""

    def __init__(self, driver):
        super().__init__(driver)

    # composition

    def get_filter_content(self) -> FilterContent:
        """Retrieves filter content instance

        Returns:
            FilterContent: FilterContent instance
        """
        return FilterContent(self.driver)

    def get_header_content(self) -> HeaderContent:
        """Retrieves header content instance

        Returns:
            HeaderContent: HeaderContent instance
        """
        return HeaderContent(self.driver)

    def get_product_content(self) -> ProductContent:
        """Retrieves product content instance

        Returns:
            ProductContent: ProductContent instance
        """
        return ProductContent(self.driver)

    # page actions
    def go_to(self, url: str) -> "HomePage":
        self.element.launch_url(url)
        return self
