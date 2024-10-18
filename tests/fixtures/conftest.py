import pytest

from uaf.decorators.loggers.logger import log
from appium.webdriver.webdriver import WebDriver
from tests.test_data.appium.capabilities import Capabilities
from uaf.device_farming.device_tasks import release_device, reserve_device
from uaf.enums.appium_automation_name import AppiumAutomationName
from uaf.enums.browser_make import MobileWebBrowserMake
from uaf.enums.mobile_app_type import MobileAppType
from uaf.enums.mobile_app_status import MobileAppStatus
from uaf.enums.mobile_device_environment_type import MobileDeviceEnvironmentType
from uaf.enums.mobile_os import MobileOs
from uaf.enums.test_environments import TestEnvironments
from uaf.enums.test_execution_mode import TestExecutionMode
from uaf.factories.driver.concrete_factory.concrete_factory import (
    ConcreteMobileDriverFactory,
    ConcreteWebDriverFactory,
)
from uaf.utilities.ui.appium_core.appium_core_utils import CoreUtils


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Specify the test environment"
    )


@log
def __fetch_required_arg_list(
    arg_mobile_app_type: MobileAppType,
    arg_mobile_os: MobileOs,
    arg_mobile_app_status: MobileAppStatus,
):
    """Fetch required argument list of capabilities mandated for given mobile app type, mobile os, and app status.

    Args:
        arg_mobile_app_type (MobileAppType): type of mobile app
        arg_mobile_os (MobileOs): type of mobile os
        arg_mobile_app_status (MobileAppStatus): status of the mobile app (existing or requires installation)

    Raises:
        ValueError: if invalid mobile app type is provided

    Returns:
        list[str]: list of required mobile app capabilities
    """
    required_list = [
        "arg_mobile_os",
        "arg_mobile_app_type",
        "arg_mobile_app_status",
        "arg_automation_name",
        "arg_mobile_device_environment_type",
        "arg_print_page_source_on_find_failure",
    ]
    if arg_mobile_app_status == MobileAppStatus.EXISTING:
        required_list.append("arg_no_reset")
    else:
        required_list.append("arg_full_reset")
        required_list.append("arg_mobile_app_path")
    match arg_mobile_app_type:
        case MobileAppType.HYBRID:
            match arg_mobile_os:
                case MobileOs.ANDROID:
                    required_list.extend(
                        [
                            "arg_web_browser_executable_path",
                            "arg_mobile_web_browser",
                            "arg_mobile_app_activity",
                            "arg_mobile_app_package",
                            "arg_auto_grant_permission",
                        ]
                    )
                case MobileOs.IOS:
                    required_list.extend(
                        ["arg_mobile_bundle_id", "arg_auto_accept_alerts"]
                    )
        case MobileAppType.NATIVE:
            match arg_mobile_os:
                case MobileOs.ANDROID:
                    required_list.extend(
                        [
                            "arg_mobile_app_activity",
                            "arg_mobile_app_package",
                            "arg_auto_grant_permission",
                        ]
                    )
                case MobileOs.IOS:
                    required_list.extend(
                        ["arg_mobile_bundle_id", "arg_auto_accept_alerts"]
                    )
        case MobileAppType.WEB:
            required_list.extend(["arg_mobile_web_browser", "arg_no_reset"])
        case _:
            raise ValueError("Invalid mobile app type!")

    return required_list


@log
def __check_required_keys_values_exist(
    arg_data: pytest.FixtureRequest, arg_required_key_list: list[str]
):
    """Checks if required key value dictionary is passed from test layer to fixture

    Args:
        arg_data (FixtureRequest): test arguments
        arg_required_key_list (list[str]): list of required arguments to be passed from test layer

    Raises:
        ValueError: if missing required argument key in dict/if missing required argument value in provided dict
    """
    # key check
    if not all(key in arg_data.param for key in arg_required_key_list):
        raise ValueError(f"Missing required arguments!! - {arg_required_key_list}")
    # value check
    value_list = [arg_data.param.get(i) for i in arg_required_key_list]
    if None in value_list:
        raise ValueError(
            f"Require argument cannot be none type!! - {arg_required_key_list}"
        )


@log
def __build_mobile_capabilities(
    arg_mobile_os: MobileOs,
    arg_mobile_app_type: MobileAppType,
    arg_mobile_device_environment_type: MobileDeviceEnvironmentType,
    arg_automation_name: AppiumAutomationName,
    arg_mobile_app_path: str | None = None,
    arg_mobile_web_browser: MobileWebBrowserMake | None = None,
    arg_mobile_app_activity: str | None = None,
    arg_mobile_app_package: str | None = None,
    arg_no_reset: bool = False,
    arg_full_reset: bool = False,
    arg_print_page_source_on_find_failure: bool = True,
    arg_auto_accept_alerts: bool = False,
    arg_auto_grant_permission: bool = False,
    arg_mobile_bundle_id: str | None = None,
):
    """Generates mobile capabilities for user-specified mobile app type and mobile OS.

    Args:
        arg_mobile_os (MobileOs): mobile os in which script has to be invoked
        arg_mobile_app_type (MobileAppType): type of mobile app in which script has to be executed
        arg_mobile_device_environment_type (MobileDeviceEnvironmentType): type of mobile device environment in which script has to be executed
        arg_automation_name (AppiumAutomationName): appium automation name
        arg_mobile_app_path (Optional[str], optional): path of mobile app where it is stored. Defaults to None.
        arg_mobile_web_browser (Optional[MobileWebBrowserMake], optional): mobile web browser in which automation has to be executed. Defaults to None.
        arg_mobile_app_activity (Optional[str], optional): mobile app activity. Defaults to None.
        arg_mobile_app_package (Optional[str], optional): mobile app package. Defaults to None.
        arg_no_reset (bool): indicates if the app should not be reset between sessions. Defaults to False.
        arg_full_reset (bool): indicates if the app should be fully reset between sessions. Defaults to False.
        arg_print_page_source_on_find_failure (bool): flag to print the page source on find failure. Defaults to True.
        arg_auto_accept_alerts (bool): whether to auto accept alerts in iOS apps. Defaults to False.
        arg_auto_grant_permission (bool): whether to auto grant permissions in Android apps. Defaults to False.
        arg_mobile_bundle_id (Optional[str]): the bundle ID for iOS apps. Defaults to None.

    Raises:
        ValueError: if invalid mobile app type is provided

    Returns:
        dict[str, Any]: mobile app capabilities dictionary
    """
    caps = Capabilities.get_instance()
    device_id, session_id = reserve_device.delay(arg_mobile_os.value).get(timeout=10)
    common_caps = {
        "platform_name": arg_mobile_os,
        "device_name": f"Test_AUTO_DEVICE_{arg_mobile_app_type.name}",
        "device_id": device_id,
        "automation_name": arg_automation_name,
        "no_reset": arg_no_reset,
        "full_reset": arg_full_reset,
        "print_page_source_on_find_failure": arg_print_page_source_on_find_failure,
    }
    match arg_mobile_app_type:
        case MobileAppType.HYBRID:
            match arg_mobile_os:
                case MobileOs.ANDROID:
                    caps.set_mobile_hybrid_app_capabilities(
                        **common_caps,
                        app=arg_mobile_app_path,
                        app_activity=arg_mobile_app_activity,
                        app_package=arg_mobile_app_package,
                        auto_grant_permissions=arg_auto_grant_permission,
                        browser_name=arg_mobile_web_browser,
                    )
                case MobileOs.IOS:
                    caps.set_mobile_hybrid_app_capabilities(
                        **common_caps,
                        app=arg_mobile_app_path,
                        app_activity=arg_mobile_app_activity,
                        app_package=arg_mobile_app_package,
                        browser_name=arg_mobile_web_browser,
                        bundle_id=arg_mobile_bundle_id,
                        auto_accept_alerts=arg_auto_accept_alerts,
                    )
            return caps.get_mobile_hybrid_app_capabilities(), device_id, session_id
        case MobileAppType.NATIVE:
            match arg_mobile_os:
                case MobileOs.ANDROID:
                    caps.set_mobile_native_app_capabilities(
                        **common_caps,
                        app=arg_mobile_app_path,
                        app_activity=arg_mobile_app_activity,
                        app_package=arg_mobile_app_package,
                        auto_grant_permissions=arg_auto_grant_permission,
                    )
                case MobileOs.IOS:
                    caps.set_mobile_native_app_capabilities(
                        **common_caps,
                        app=arg_mobile_app_path,
                        app_activity=arg_mobile_app_activity,
                        app_package=arg_mobile_app_package,
                        bundle_id=arg_mobile_bundle_id,
                        auto_accept_alerts=arg_auto_accept_alerts,
                    )
            return caps.get_mobile_native_app_capabilities(), device_id, session_id
        case MobileAppType.WEB:
            caps.set_mobile_web_browser_capabilities(
                **common_caps,
                browser_name=arg_mobile_web_browser,
            )
            return caps.get_mobile_web_browser_capabilities(), device_id, session_id

        case _:
            raise ValueError("Invalid mobile app type!")


@log
@pytest.fixture(scope="function")
def mobile_driver(request: pytest.FixtureRequest):
    """Mobile driver fixture, responsible for yielding user requested mobile driver instance and clean up activity.

    Args:
        request (FixtureRequest): test arguments

    Yields:
        AppiumDriver: returns user requested mobile driver instance
    """
    __check_required_keys_values_exist(
        request,
        __fetch_required_arg_list(
            request.param.get("arg_mobile_app_type"),
            request.param.get("arg_mobile_os"),
            request.param.get("arg_mobile_app_status"),
        ),
    )
    capabilities, device_id, session_id = __build_mobile_capabilities(
        arg_mobile_os=request.param.get("arg_mobile_os"),
        arg_mobile_app_type=request.param.get("arg_mobile_app_type"),
        arg_mobile_device_environment_type=request.param.get(
            "arg_mobile_device_environment_type"
        ),
        arg_automation_name=request.param.get("arg_automation_name"),
        arg_mobile_app_path=request.param.get("arg_mobile_app_path"),
        arg_mobile_web_browser=request.param.get("arg_mobile_web_browser"),
        arg_mobile_app_activity=request.param.get("arg_mobile_app_activity"),
        arg_mobile_app_package=request.param.get("arg_mobile_app_package"),
        arg_no_reset=request.param.get("arg_no_reset"),
        arg_full_reset=request.param.get("arg_full_reset"),
        arg_print_page_source_on_find_failure=request.param.get(
            "arg_print_page_source_on_find_failure"
        ),
        arg_auto_accept_alerts=request.param.get("arg_auto_accept_alerts"),
        arg_auto_grant_permission=request.param.get("arg_auto_grant_permission"),
        arg_mobile_bundle_id=request.param.get("arg_mobile_bundle_id"),
    )
    capabilities = {k: v for k, v in capabilities.items() if v is not None}
    data: tuple[WebDriver, int] = (ConcreteMobileDriverFactory()).get_mobile_driver(
        os=request.param.get("arg_mobile_os"),
        app_type=request.param.get("arg_mobile_app_type"),
        test_execution_mode=TestExecutionMode.LOCAL,
        test_environment=TestEnvironments.DEVELOPMENT,
        capabilities=capabilities,
    )
    yield data[0]
    data[0].quit()
    CoreUtils.purge_appium_node(data[1])
    release_device.delay(device_id, session_id).get(timeout=10)


@log
@pytest.fixture(scope="function")
def web_driver(request: pytest.FixtureRequest):
    """WebDriver fixture, responsible for yielding user requested web driver instance and clean up activity

    Args:
        request (FixtureRequest): test arguments

    Yields:
        WebDriver: requested webdriver instance
    """
    driver = (ConcreteWebDriverFactory()).get_web_driver(
        browser_make=request.param.get("arg_browser_make"),
        options=request.param.get("arg_capabilities"),
    )
    yield driver
    driver.quit()
