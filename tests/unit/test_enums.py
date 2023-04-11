from pytest import mark
from uaf.enums.browser_make import WebBrowserMake
from uaf.enums.file_paths import FilePaths
from uaf.enums.mobile_os import MobileOs
from uaf.enums.test_environments import TestEnvironments
from uaf.enums.test_execution_mode import TestExecutionMode


@mark.parametrize(
    "arg_browser_enum",
    [
        WebBrowserMake.BRAVE,
        WebBrowserMake.CHROME,
        WebBrowserMake.CHROMIUM,
        WebBrowserMake.IE,
        WebBrowserMake.MSEDGE,
        WebBrowserMake.FIREFOX,
    ],
)
def test_browser_enum(arg_browser_enum: WebBrowserMake):
    assert isinstance(arg_browser_enum.value, str)


@mark.parametrize(
    "arg_filepath_enum",
    [
        FilePaths.COMMON,
        FilePaths.TEST_CONFIG_DEV,
        FilePaths.TEST_CONFIG_PROD,
        FilePaths.TEST_CONFIG_QA,
        FilePaths.TEST_CONFIG_STAGE,
    ],
)
def test_filepath_enum(arg_filepath_enum: FilePaths):
    assert isinstance(arg_filepath_enum.value, str)


@mark.parametrize("arg_mobileOs_enum", [MobileOs.ANDROID, MobileOs.IOS])
def test_mobileOs_enum(arg_mobileOs_enum: MobileOs):
    assert isinstance(arg_mobileOs_enum.value, str)


@mark.parametrize(
    "arg_test_env_enum",
    [
        TestEnvironments.DEVELOPMENT,
        TestEnvironments.PRODUCTION,
        TestEnvironments.QA,
        TestEnvironments.STAGE,
    ],
)
def test_test_environment_enum(arg_test_env_enum: TestEnvironments):
    assert isinstance(arg_test_env_enum.value, str)


@mark.parametrize(
    "arg_test_exec_mode", [TestExecutionMode.LOCAL, TestExecutionMode.REMOTE]
)
def test_test_execution_mode_enum(arg_test_exec_mode: TestExecutionMode):
    assert isinstance(arg_test_exec_mode.value, str)
