import pytest
from pytest import mark
from unittest.mock import MagicMock, patch
from uaf.enums.appium_automation_name import AppiumAutomationName
from uaf.enums.browser_make import MobileWebBrowserMake
from uaf.enums.mobile_app_type import MobileAppType
from uaf.enums.execution_mode import ExecutionMode
from uaf.enums.mobile_device_environment_type import MobileDeviceEnvironmentType
from uaf.enums.mobile_os import MobileOs
from uaf.factories.driver.concrete_factory.concrete_factory import (
    ConcreteMobileDriverFactory,
)


@pytest.fixture
def mock_mobile_driver():
    return MagicMock()


def build_capabilities(
    mobile_os: MobileOs,
    mobile_app_type: MobileAppType,
    mobile_browser: MobileWebBrowserMake | None,
    automation_name: AppiumAutomationName,
    no_reset: bool = False,
) -> dict[str, str | bool]:
    capabilities: dict[str, str | bool] = {
        "platformName": mobile_os.value,
        "automationName": automation_name.value,
        "noReset": no_reset,
    }
    if mobile_os == MobileOs.ANDROID:
        if mobile_app_type == MobileAppType.WEB:
            capabilities["browserName"] = (
                mobile_browser.value if mobile_browser else "Chrome"
            )
        elif mobile_app_type in [MobileAppType.NATIVE, MobileAppType.HYBRID]:
            capabilities["appPackage"] = "com.example.android"
            capabilities["appActivity"] = "MainActivity"
            capabilities["autoGrantPermissions"] = True
    elif mobile_os == MobileOs.IOS:
        if mobile_app_type == MobileAppType.NATIVE:
            capabilities["bundleId"] = "com.example.ios"
            capabilities["autoAcceptAlerts"] = True

    return capabilities


@mark.unit_test
@mark.parametrize(
    "mobile_os,mobile_execution_mode,mobile_app_type,mobile_env_type,mobile_automation_name,mobile_browser",
    [
        (
            MobileOs.ANDROID,
            ExecutionMode.LOCAL,
            MobileAppType.WEB,
            MobileDeviceEnvironmentType.PHYSICAL,
            AppiumAutomationName.UIAUTOMATOR2,
            MobileWebBrowserMake.CHROME,
        ),
        (
            MobileOs.IOS,
            ExecutionMode.LOCAL,
            MobileAppType.NATIVE,
            MobileDeviceEnvironmentType.SIMULATOR,
            AppiumAutomationName.XCUITEST,
            None,
        ),
        (
            MobileOs.ANDROID,
            ExecutionMode.LOCAL,
            MobileAppType.HYBRID,
            MobileDeviceEnvironmentType.EMULATOR,
            AppiumAutomationName.UIAUTOMATOR2,
            None,
        ),
        (
            MobileOs.ANDROID,
            ExecutionMode.REMOTE,
            MobileAppType.WEB,
            MobileDeviceEnvironmentType.PHYSICAL,
            AppiumAutomationName.UIAUTOMATOR2,
            MobileWebBrowserMake.CHROME,
        ),
        (
            MobileOs.IOS,
            ExecutionMode.REMOTE,
            MobileAppType.NATIVE,
            MobileDeviceEnvironmentType.SIMULATOR,
            AppiumAutomationName.XCUITEST,
            None,
        ),
        (
            MobileOs.ANDROID,
            ExecutionMode.REMOTE,
            MobileAppType.HYBRID,
            MobileDeviceEnvironmentType.EMULATOR,
            AppiumAutomationName.UIAUTOMATOR2,
            None,
        ),
        (
            MobileOs.IOS,
            ExecutionMode.REMOTE,
            MobileAppType.WEB,
            MobileDeviceEnvironmentType.PHYSICAL,
            AppiumAutomationName.XCUITEST,
            MobileWebBrowserMake.SAFARI,
        ),
        (
            MobileOs.ANDROID,
            ExecutionMode.LOCAL,
            MobileAppType.NATIVE,
            MobileDeviceEnvironmentType.PHYSICAL,
            AppiumAutomationName.UIAUTOMATOR2,
            None,
        ),
        (
            MobileOs.IOS,
            ExecutionMode.LOCAL,
            MobileAppType.HYBRID,
            MobileDeviceEnvironmentType.PHYSICAL,
            AppiumAutomationName.XCUITEST,
            None,
        ),
        (
            MobileOs.ANDROID,
            ExecutionMode.REMOTE,
            MobileAppType.NATIVE,
            MobileDeviceEnvironmentType.EMULATOR,
            AppiumAutomationName.UIAUTOMATOR2,
            None,
        ),
        (
            MobileOs.IOS,
            ExecutionMode.REMOTE,
            MobileAppType.WEB,
            MobileDeviceEnvironmentType.SIMULATOR,
            AppiumAutomationName.XCUITEST,
            MobileWebBrowserMake.SAFARI,
        ),
    ],
)
def test_mobile_driver_factory(
    mock_mobile_driver,
    mobile_os,
    mobile_execution_mode,
    mobile_app_type,
    mobile_env_type,
    mobile_automation_name,
    mobile_browser,
):
    capabilities = build_capabilities(
        mobile_os=mobile_os,
        mobile_app_type=mobile_app_type,
        mobile_browser=mobile_browser,
        automation_name=mobile_automation_name,
    )
    with patch(
        "uaf.factories.driver.concrete_factory.concrete_products.mobile.concrete_mobile_driver.ConcreteMobileDriver.get_mobile_driver",
        return_value=mock_mobile_driver,
    ) as MockGetMobileDriver:
        factory = ConcreteMobileDriverFactory()
        driver = factory.get_mobile_driver(
            os=mobile_os,
            app_type=mobile_app_type,
            execution_mode=mobile_execution_mode,
            environment=mobile_env_type,
            capabilities=capabilities,
        )
        MockGetMobileDriver.assert_called_once_with(capabilities=capabilities)
        assert driver == mock_mobile_driver
