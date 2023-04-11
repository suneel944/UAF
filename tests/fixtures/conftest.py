from pytest import fixture, FixtureRequest
from uaf.enums.mobile_os import MobileOs
from uaf.enums.mobile_app_type import MobileAppType
from uaf.enums.test_execution_mode import TestExecutionMode
from uaf.enums.appium_automation_name import AppiumAutomationName
from uaf.enums.test_environments import TestEnvironments
from uaf.enums.mobile_device_environment_type import MobileDeviceEnvironmentType
from uaf.enums.browser_make import WebBrowserMake, MobileWebBrowserMake
from uaf.utilities.appium.appium_utils import AppiumUtils
from uaf.factories.driver.concrete_factory.concrete_factory import (
    ConcreteWebDriverFactory,
    ConcreteMobileDriverFactory,
)
from uaf.enums.driver_executable_paths import DriverExecutablePaths
from tests.test_data.appium.capabilities import Capabilities
from typing import Optional
from uaf.device_farming.device_tasks import reserve_device, release_device
from uaf.decorators.loggers.logger import log


@log
def __fetch_required_arg_list(
    arg_mobile_app_type: MobileAppType, arg_mobile_os: MobileOs
):
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
def __check_required_keys_values_exist(
    arg_data: FixtureRequest, arg_required_key_list: list[str]
):
    # key check
    if not all(key in arg_data.param for key in arg_required_key_list):
        raise ValueError(
            "Missing required arguments!! - {}".format(arg_required_key_list)
        )
    # value check
    value_list = [arg_data.param.get(i) for i in arg_required_key_list]
    if None in value_list:
        raise ValueError(
            "Require argument cannot be none type!! - {}".format(arg_required_key_list)
        )


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
            raise TypeError("Invalid mobile app type!")


@log
@fixture(scope="function")
def mobile_driver(request: FixtureRequest):
    __check_required_keys_values_exist(
        request,
        __fetch_required_arg_list(
            request.param.get("arg_mobile_app_type"), request.param.get("arg_mobile_os")
        ),
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
    AppiumUtils.purge_appium_node(port)
    release_device.delay(device_id, session_id).get(timeout=10)


@fixture(scope="function")
def web_driver(request: FixtureRequest):
    driver = (ConcreteWebDriverFactory()).get_web_driver(
        browser_make=request.param.get("arg_browser_make"),
        options=request.param.get("arg_capabilities"),
    )
    yield driver
    driver.quit()
