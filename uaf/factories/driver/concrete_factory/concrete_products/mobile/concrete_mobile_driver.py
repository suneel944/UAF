from typing import Any

from uaf.enums.file_paths import FilePaths
from uaf.enums.mobile_os import MobileOs
from uaf.enums.test_environments import TestEnvironments
from uaf.enums.test_execution_mode import TestExecutionMode
from uaf.factories.driver.abstract_factory.abstract_products.abstract_mobie.abstract_mobile import (
    AbstractMobile,
)
from uaf.factories.driver.concrete_factory.concrete_products.mobile.concrete_android_driver import (
    ConcreteAndroidDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.mobile.concrete_ios_driver import (
    ConcreteIOSDriver,
)
from uaf.utilities.parser.yaml_parser_utils import YamlParser
from uaf.utilities.ui.appium_core.appium_core_utils import CoreUtils


class ConcreteMobileDriver(AbstractMobile):
    """
    Concrete mobile driver factory that produces a family of mobile drivers.

    The factory ensures that the resulting mobile drivers are compatible.
    Note that the signature of the concrete mobile driver factory's methods return an abstract
    mobile driver, while inside the method a concrete product is instantiated.

    Attributes:
        os (MobileOs): The mobile operating system (iOS or Android).
        testExecMode (TestExecutionMode): The test execution mode (Local or Remote).
        testEnv (TestEnvironments): The test environment (Development, QA, Production, etc.).

    Methods:
        __init__(os: MobileOs, test_execution_mode: TestExecutionMode, test_environment: TestEnvironments):
            Initializes the ConcreteMobileDriver with the given OS, execution mode, and environment.
        get_mobile_driver(capabilities: dict[str, Any]):
            Fetches a mobile driver instance configured with the specified capabilities.
    """

    def __init__(
        self,
        *,
        os: MobileOs,
        test_execution_mode: TestExecutionMode,
        test_environment: TestEnvironments,
    ) -> None:
        """
        Initializes a ConcreteMobileDriver instance.

        Args:
            os (MobileOs): The mobile operating system (iOS or Android).
            test_execution_mode (TestExecutionMode): The test execution mode (Local or Remote).
            test_environment (TestEnvironments): The test environment (Development, QA, Production, etc.).
        """
        self.testEnv = test_environment
        self.os = os
        self.testExecMode = test_execution_mode

    def get_mobile_driver(self, *, capabilities: dict[str, Any]):
        """
        Fetches a mobile driver instance configured with the specified capabilities.

        This method creates and returns a WebDriver instance for mobile devices
        (either iOS or Android) configured with the provided capabilities. It also
        launches the Appium service and waits for it to be ready.

        Args:
            capabilities (dict[str, Any]): Dictionary of mobile driver capabilities.

        Returns:
            tuple: A tuple containing the mobile driver instance and the Appium port.

        Example:
            capabilities = {
                "platformName": "iOS",
                "platformVersion": "14.0",
                "deviceName": "iPhone Simulator",
                "app": "/path/to/your/app.app"
            }

            driver, port = ConcreteMobileDriver(
                os=MobileOs.IOS,
                test_execution_mode=TestExecutionMode.LOCAL,
                test_environment=TestEnvironments.DEV
            ).get_mobile_driver(capabilities=capabilities)
        """
        common_config = YamlParser(FilePaths.COMMON)
        # launch appium service
        port = CoreUtils.launch_appium_service()
        # return requested mobile driver
        remote_url = (
            common_config.get_value(
                "appium",
                (
                    "appium_base_url_local"
                    if self.testExecMode.value.__eq__(TestExecutionMode.LOCAL.value)
                    else "appium_base_url_remote"
                ),
            ),
        )[0].replace("${port}", str(port))
        from urllib.parse import urlparse

        host = urlparse(remote_url).hostname
        CoreUtils.wait_for_appium_service_to_load(30, host, port)
        return (
            ConcreteAndroidDriver(remote_url).get_driver(capabilities=capabilities)
            if self.os.value.__eq__(MobileOs.ANDROID.value)
            else ConcreteIOSDriver(remote_url).get_driver(capabilities=capabilities)
        ), port
