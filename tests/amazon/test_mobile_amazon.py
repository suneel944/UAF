from pytest import mark

from tests.fixtures.conftest import mobile_driver  # type: ignore
from tests.pages.mobile.amazon.home_page import HomePage
from tests.pages.mobile.amazon.product_page import ProductPage
from uaf.enums.appium_automation_name import AppiumAutomationName
from uaf.enums.browser_make import MobileWebBrowserMake
from uaf.enums.file_paths import FilePaths
from uaf.enums.mobile_app_type import MobileAppType
from uaf.enums.mobile_device_environment_type import MobileDeviceEnvironmentType
from uaf.enums.mobile_os import MobileOs
from uaf.utilities.parser.yaml_parser_utils import YamlParser

config = YamlParser(FilePaths.TEST_CONFIG_DEV)


@mark.mobile_test
@mark.parametrize(
    "mobile_driver",
    [
        {
            "arg_mobile_os": MobileOs.ANDROID,
            "arg_mobile_app_type": MobileAppType.WEB,
            "arg_mobile_device_environment_type": MobileDeviceEnvironmentType.PHYSICAL,
            "arg_automation_name": AppiumAutomationName.UIAUTOMATOR2,
            "arg_mobile_web_browser": MobileWebBrowserMake.CHROME,
        }
    ],
    indirect=True,
)
def test_mobile_web_amazon_product_search(mobile_driver):  # noqa
    home_page = HomePage(mobile_driver)
    product_page = ProductPage(mobile_driver)
    home_page.go_to(
        config.get_value("urls", "amazon")
    ).get_header_content().click_on_hamburger_menu().select_left_menu_specifics(
        config.get_value("amazon", "mobile_hamburger_menu_panel_heading"),
        config.get_value("amazon", "mobile_hamburger_menu_panel_sub_heading"),
    ).get_category_content().select_category_grid(
        config.get_value("amazon", "mobile_category_parent")
    ).select_category_grid(
        config.get_value("amazon", "mobile_category_child")
    ).get_product_content().click_on_product(
        config.get_value("amazon", "mobile_desired_product_index")
    ).get_product_page()

    assert isinstance(product_page.get_product_text_content(), str)
