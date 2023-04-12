from pytest import mark

from tests.fixtures.conftest import mobile_driver, web_driver  # type: ignore
from uaf.enums.appium_automation_name import AppiumAutomationName
from uaf.enums.browser_make import MobileWebBrowserMake, WebBrowserMake
from uaf.enums.mobile_app_type import MobileAppType
from uaf.enums.mobile_device_environment_type import MobileDeviceEnvironmentType
from uaf.enums.mobile_os import MobileOs


# TODO: Improvise the existing dockerfile and compose to accomodate the same
@mark.skip(reason="require infrastructure to support to run this test case and is resource intensive")
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
def test_mobile_driver_factory(mobile_driver):
    mobile_driver.get("https://www.google.co.in/")
    title = mobile_driver.title
    assert isinstance(title, str) and title.lower().__eq__("google")


@mark.parametrize(
    "web_driver",
    [
        {"arg_browser_make": WebBrowserMake.CHROME},
        {"arg_browser_make": WebBrowserMake.BRAVE},
        {"arg_browser_make": WebBrowserMake.FIREFOX},
        {"arg_browser_make": WebBrowserMake.MSEDGE},
    ],
    indirect=True,
)
def test_web_driver_factory(web_driver):
    web_driver.get("https://www.google.co.in/")
    title = web_driver.title
    assert isinstance(title, str) and title.lower().__eq__("google")
