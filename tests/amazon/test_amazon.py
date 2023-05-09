from pytest import mark

from tests.fixtures.conftest import web_driver  # type: ignore
from tests.pages.amazon.home_page import HomePage
from tests.pages.amazon.product_page import ProductPage
from uaf.enums.browser_make import WebBrowserMake
from uaf.enums.file_paths import FilePaths
from uaf.utilities.parser.yaml_parser_utils import YamlParser

config = YamlParser(FilePaths.TEST_CONFIG_DEV)


@mark.web_test
@mark.parametrize(
    "web_driver",
    [
        {"arg_browser_make": WebBrowserMake.CHROME},
    ],
    indirect=True,
)
def test_amazon_product_search_01(web_driver):
    home_page = HomePage(web_driver)
    product_page = ProductPage(web_driver)
    home_page.go_to(
        config.get_value("urls", "amazon")
    ).get_header_content().click_on_hamburger_menu().select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_heading"),
    ).select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_choice"),
    ).get_filter_content().select_filter_content_parent_category(
        config.get_value("amazon", "filter_section_parent_category"),
        config.get_value("amazon", "filter_section_parent_choice"),
    ).select_filter_content_child_category(
        config.get_value("amazon", "filter_section_child_category"),
        config.get_value("amazon", "filter_section_child_choice"),
    ).sort_product(
        config.get_value("amazon", "sort_product_based_on")
    ).click_on_the_desired_product(
        config.get_value("amazon", "desired_product_index")
    )

    assert isinstance(product_page.get_product_text_content(), str)


@mark.web_test
@mark.parametrize(
    "web_driver",
    [
        {"arg_browser_make": WebBrowserMake.CHROME},
    ],
    indirect=True,
)
def test_amazon_product_search_02(web_driver):
    home_page = HomePage(web_driver)
    product_page = ProductPage(web_driver)
    home_page.go_to(
        config.get_value("urls", "amazon")
    ).get_header_content().click_on_hamburger_menu().select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_heading"),
    ).select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_choice"),
    ).get_filter_content().select_filter_content_parent_category(
        config.get_value("amazon", "filter_section_parent_category"),
        config.get_value("amazon", "filter_section_parent_choice"),
    ).select_filter_content_child_category(
        config.get_value("amazon", "filter_section_child_category"),
        config.get_value("amazon", "filter_section_child_choice"),
    ).sort_product(
        config.get_value("amazon", "sort_product_based_on")
    ).click_on_the_desired_product(
        config.get_value("amazon", "desired_product_index")
    )

    assert isinstance(product_page.get_product_text_content(), str)


@mark.web_test
@mark.parametrize(
    "web_driver",
    [
        {"arg_browser_make": WebBrowserMake.CHROME},
    ],
    indirect=True,
)
def test_amazon_product_search_03(web_driver):
    home_page = HomePage(web_driver)
    product_page = ProductPage(web_driver)
    home_page.go_to(
        config.get_value("urls", "amazon")
    ).get_header_content().click_on_hamburger_menu().select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_heading"),
    ).select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_choice"),
    ).get_filter_content().select_filter_content_parent_category(
        config.get_value("amazon", "filter_section_parent_category"),
        config.get_value("amazon", "filter_section_parent_choice"),
    ).select_filter_content_child_category(
        config.get_value("amazon", "filter_section_child_category"),
        config.get_value("amazon", "filter_section_child_choice"),
    ).sort_product(
        config.get_value("amazon", "sort_product_based_on")
    ).click_on_the_desired_product(
        config.get_value("amazon", "desired_product_index")
    )

    assert isinstance(product_page.get_product_text_content(), str)


@mark.web_test
@mark.parametrize(
    "web_driver",
    [
        {"arg_browser_make": WebBrowserMake.CHROME},
    ],
    indirect=True,
)
def test_amazon_product_search_04(web_driver):
    home_page = HomePage(web_driver)
    product_page = ProductPage(web_driver)
    home_page.go_to(
        config.get_value("urls", "amazon")
    ).get_header_content().click_on_hamburger_menu().select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_heading"),
    ).select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_choice"),
    ).get_filter_content().select_filter_content_parent_category(
        config.get_value("amazon", "filter_section_parent_category"),
        config.get_value("amazon", "filter_section_parent_choice"),
    ).select_filter_content_child_category(
        config.get_value("amazon", "filter_section_child_category"),
        config.get_value("amazon", "filter_section_child_choice"),
    ).sort_product(
        config.get_value("amazon", "sort_product_based_on")
    ).click_on_the_desired_product(
        config.get_value("amazon", "desired_product_index")
    )

    assert isinstance(product_page.get_product_text_content(), str)


@mark.web_test
@mark.parametrize(
    "web_driver",
    [
        {"arg_browser_make": WebBrowserMake.CHROME},
    ],
    indirect=True,
)
def test_amazon_product_search_05(web_driver):
    home_page = HomePage(web_driver)
    product_page = ProductPage(web_driver)
    home_page.go_to(
        config.get_value("urls", "amazon")
    ).get_header_content().click_on_hamburger_menu().select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_heading"),
    ).select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_choice"),
    ).get_filter_content().select_filter_content_parent_category(
        config.get_value("amazon", "filter_section_parent_category"),
        config.get_value("amazon", "filter_section_parent_choice"),
    ).select_filter_content_child_category(
        config.get_value("amazon", "filter_section_child_category"),
        config.get_value("amazon", "filter_section_child_choice"),
    ).sort_product(
        config.get_value("amazon", "sort_product_based_on")
    ).click_on_the_desired_product(
        config.get_value("amazon", "desired_product_index")
    )

    assert isinstance(product_page.get_product_text_content(), str)


@mark.web_test
@mark.parametrize(
    "web_driver",
    [
        {"arg_browser_make": WebBrowserMake.CHROME},
    ],
    indirect=True,
)
def test_amazon_product_search_06(web_driver):
    home_page = HomePage(web_driver)
    product_page = ProductPage(web_driver)
    home_page.go_to(
        config.get_value("urls", "amazon")
    ).get_header_content().click_on_hamburger_menu().select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_heading"),
    ).select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_choice"),
    ).get_filter_content().select_filter_content_parent_category(
        config.get_value("amazon", "filter_section_parent_category"),
        config.get_value("amazon", "filter_section_parent_choice"),
    ).select_filter_content_child_category(
        config.get_value("amazon", "filter_section_child_category"),
        config.get_value("amazon", "filter_section_child_choice"),
    ).sort_product(
        config.get_value("amazon", "sort_product_based_on")
    ).click_on_the_desired_product(
        config.get_value("amazon", "desired_product_index")
    )

    assert isinstance(product_page.get_product_text_content(), str)


@mark.web_test
@mark.parametrize(
    "web_driver",
    [
        {"arg_browser_make": WebBrowserMake.CHROME},
    ],
    indirect=True,
)
def test_amazon_product_search_07(web_driver):
    home_page = HomePage(web_driver)
    product_page = ProductPage(web_driver)
    home_page.go_to(
        config.get_value("urls", "amazon")
    ).get_header_content().click_on_hamburger_menu().select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_heading"),
    ).select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_choice"),
    ).get_filter_content().select_filter_content_parent_category(
        config.get_value("amazon", "filter_section_parent_category"),
        config.get_value("amazon", "filter_section_parent_choice"),
    ).select_filter_content_child_category(
        config.get_value("amazon", "filter_section_child_category"),
        config.get_value("amazon", "filter_section_child_choice"),
    ).sort_product(
        config.get_value("amazon", "sort_product_based_on")
    ).click_on_the_desired_product(
        config.get_value("amazon", "desired_product_index")
    )

    assert isinstance(product_page.get_product_text_content(), str)


@mark.web_test
@mark.parametrize(
    "web_driver",
    [
        {"arg_browser_make": WebBrowserMake.CHROME},
    ],
    indirect=True,
)
def test_amazon_product_search_08(web_driver):
    home_page = HomePage(web_driver)
    product_page = ProductPage(web_driver)
    home_page.go_to(
        config.get_value("urls", "amazon")
    ).get_header_content().click_on_hamburger_menu().select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_heading"),
    ).select_left_menu_specifics(
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_heading"),
        config.get_value("amazon", "hamburger_menu_panel_sub_section_extension_choice"),
    ).get_filter_content().select_filter_content_parent_category(
        config.get_value("amazon", "filter_section_parent_category"),
        config.get_value("amazon", "filter_section_parent_choice"),
    ).select_filter_content_child_category(
        config.get_value("amazon", "filter_section_child_category"),
        config.get_value("amazon", "filter_section_child_choice"),
    ).sort_product(
        config.get_value("amazon", "sort_product_based_on")
    ).click_on_the_desired_product(
        config.get_value("amazon", "desired_product_index")
    )

    assert isinstance(product_page.get_product_text_content(), str)
