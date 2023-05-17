from typing import Optional

import pytest

from tests.test_data.appium.capabilities import Capabilities
from uaf.decorators.loggers.logger import log
from uaf.device_farming.device_tasks import release_device, reserve_device
from uaf.enums.appium_automation_name import AppiumAutomationName
from uaf.enums.browser_make import MobileWebBrowserMake, WebBrowserMake
from uaf.enums.driver_executable_paths import DriverExecutablePaths
from uaf.enums.mobile_app_type import MobileAppType
from uaf.enums.mobile_device_environment_type import MobileDeviceEnvironmentType
from uaf.enums.mobile_os import MobileOs
from uaf.enums.test_environments import TestEnvironments
from uaf.enums.test_execution_mode import TestExecutionMode
from uaf.factories.driver.concrete_factory.concrete_factory import ConcreteMobileDriverFactory, ConcreteWebDriverFactory
from uaf.utilities.ui.appium_core.appium_core_utils import CoreUtils


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Specify the test environment")


@log
def __fetch_required_arg_list(arg_mobile_app_type: MobileAppType, arg_mobile_os: MobileOs):
    """Fetch required argument list of capabilities mandated for given mobile app type and mobile os

    Args:
        arg_mobile_app_type (MobileAppType): type of mobile app
        arg_mobile_os (MobileOs): type of mobile os

    Raises:
        ValueError: if invalid mobile app type is provided
    Returns:
        list[str]: list of required mobile app capabilities
    """
    match arg_mobile_app_type.value:
        case MobileAppType.HYBRID.value:
            required_list = [
                "arg_mobile_os",
                "arg_mobile_app_type",
                "arg_automation_name",
                "arg_mobile_device_environment_type",
                "arg_mobile_app_path",
                "arg_mobile_app_activty",
                "arg_mobile_app_package",
            ]
            if arg_mobile_os.value.__eq__(MobileOs.ANDROID.value):
                required_list.append("arg_web_browser_executable_path")
                required_list.append("arg_mobile_web_browser")
            return required_list
        case MobileAppType.NATIVE.value:
            return [
                "arg_mobile_os",
                "arg_mobile_app_type",
                "arg_automation_name",
                "arg_mobile_device_environment_type",
                "arg_mobile_app_path",
                "arg_mobile_app_activty",
                "arg_mobile_app_package",
            ]
        case MobileAppType.WEB.value:
            required_list = [
                "arg_mobile_os",
                "arg_mobile_app_type",
                "arg_automation_name",
                "arg_mobile_device_environment_type",
                "arg_mobile_web_browser",
            ]
            return required_list
        case _:
            raise ValueError("Invalid mobile app type!!")


@log
def __check_required_keys_values_exist(arg_data: pytest.FixtureRequest, arg_required_key_list: list[str]):
    """Checks if required key value dictionary is passed from test layer to fixture

    Args:
        arg_data (FixtureRequest): test arguments
        arg_required_key_list (list[str]): list of required arguments to be passed from test layer

    Raises:
        ValueError: if missing required argument key in dict/if missing required argument value in provided dict
    """
    # key check
    if not all(key in arg_data.param for key in arg_required_key_list):
        raise ValueError("Missing required arguments!! - {}".format(arg_required_key_list))
    # value check
    value_list = [arg_data.param.get(i) for i in arg_required_key_list]
    if None in value_list:
        raise ValueError("Require argument cannot be none type!! - {}".format(arg_required_key_list))


@log
def __build_mobile_capabilities(
    arg_mobile_os: MobileOs,
    arg_mobile_app_type: MobileAppType,
    arg_mobile_device_environment_type: MobileDeviceEnvironmentType,
    arg_automation_name: AppiumAutomationName,
    arg_mobile_app_path: Optional[str] = None,
    arg_mobile_web_browser: Optional[MobileWebBrowserMake] = None,
    arg_mobile_app_activty: Optional[str] = None,
    arg_mobile_app_package: Optional[str] = None,
):
    """Generates mobile capabilities for user specified mobile app type and mobile os

    Args:
        arg_mobile_os (MobileOs): mobile os in which script has to be invoked
        arg_mobile_app_type (MobileAppType): type of mobile app in which script has to be executed
        arg_mobile_device_environment_type (MobileDeviceEnvironmentType): type of mobile device environment in which script has to be executed
        arg_automation_name (AppiumAutomationName): appium automation name
        arg_mobile_app_path (Optional[str], optional): path of mobile app where it is stored. Defaults to None.
        arg_mobile_web_browser (Optional[MobileWebBrowserMake], optional): mobile web browser in which automation has to be executed. Defaults to None.
        arg_mobile_app_activty (Optional[str], optional): mobile app activity. Defaults to None.
        arg_mobile_app_package (Optional[str], optional): mobile app package. Defaults to None.

    Raises:
        ValueError: if invalid mobile app type is provided

    Returns:
        dict[str, Any]: mobile app capabilities dictionary
    """
    caps = Capabilities.get_instance()
    device_id, session_id = reserve_device.delay(arg_mobile_os.value).get(timeout=10)
    match arg_mobile_app_type.value:
        case MobileAppType.HYBRID.value:
            caps.set_mobile_hybrid_app_capabilities(
                platform_name=arg_mobile_os,
                app=arg_mobile_app_path,
                device_name="Test_AUTO_DEVICE_HYBRID",
                device_id=device_id,
                app_activity=arg_mobile_app_activty,
                app_package=arg_mobile_app_package,
                auto_grant_permissions=True,
                automation_name=arg_automation_name,
                browser_name=arg_mobile_web_browser,
            )
            return caps.get_mobile_hybrid_app_capabilities(), device_id, session_id
        case MobileAppType.NATIVE.value:
            caps.set_mobile_native_app_capabilities(
                platform_name=arg_mobile_os,
                app=arg_mobile_app_path,
                device_name="Test_AUTO_DEVICE_NATIVE",
                device_id=device_id,
                app_activity=arg_mobile_app_activty,
                app_package=arg_mobile_app_package,
                auto_grant_permissions=True,
                automation_name=arg_automation_name,
            )
            return caps.get_mobile_native_app_capabilities(), device_id, session_id
        case MobileAppType.WEB.value:
            caps.set_mobile_web_browser_capabilities(
                platform_name=arg_mobile_os,
                device_name="Test_AUTO_DEVICE_WEB",
                device_id=device_id,
                browser_name=arg_mobile_web_browser,
                auto_grant_permissions=True,
                automation_name=arg_automation_name,
            )
            return caps.get_mobile_web_browser_capabilities(), device_id, session_id
        case _:
            raise ValueError("Invalid mobile app type!")


@log
@pytest.fixture(scope="function")
def mobile_driver(request: pytest.FixtureRequest):
    """Mobile driver fixture, responsible for yielding user requested mobile driver instance and clean up activity

    Args:
        request (FixtureRequest): test arguments

    Yields:
        AppiumDriver : returns user requested mobile driver instance
    """
    __check_required_keys_values_exist(
        request,
        __fetch_required_arg_list(request.param.get("arg_mobile_app_type"), request.param.get("arg_mobile_os")),
    )
    capabilities, device_id, session_id = __build_mobile_capabilities(
        request.param.get("arg_mobile_os"),
        request.param.get("arg_mobile_app_type"),
        request.param.get("arg_mobile_device_environment_type"),
        request.param.get("arg_automation_name"),
        request.param.get("arg_mobile_app_path"),
        request.param.get("arg_mobile_web_browser"),
        request.param.get("arg_mobile_app_activity"),
        request.param.get("arg_mobile_app_package"),
    )
    driver, port = (ConcreteMobileDriverFactory()).get_mobile_driver(
        os=request.param.get("arg_mobile_os"),
        test_execution_mode=TestExecutionMode.LOCAL,
        test_environment=TestEnvironments.DEVELOPMENT,
        capabilities=capabilities,
    )
    yield driver
    driver.quit()
    CoreUtils.purge_appium_node(port)
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
