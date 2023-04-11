from typing import Any
from uaf.utilities.appium.appium_utils import AppiumUtils
from uaf.utilities.parser.yaml_parser_utils import YamlParser
from uaf.enums.test_environments import TestEnvironments
from uaf.enums.test_execution_mode import TestExecutionMode
from uaf.enums.mobile_os import MobileOs
from uaf.enums.file_paths import FilePaths
from uaf.factories.driver.abstract_factory.abstract_products.abstract_mobie.abstract_mobile import (
    AbstractMobile,
)
from uaf.factories.driver.concrete_factory.concrete_products.mobile.concrete_android_driver import (
    ConcreteAndroidDriver,
)
from uaf.factories.driver.concrete_factory.concrete_products.mobile.concrete_ios_driver import (
    ConcreteIOSDriver,
)


class ConcreteMobileDriver(AbstractMobile):
    """
    Concrete mobile browser factory produce a family of web browsers that belong to
    web variant. The factory gurantees that resulting web browsers are compaitible.
    Note that signature of the concrete mobile browser factory's methods return an abstract
    web browser, while inside the method a concrete product is instantiated.
    """

    def __init__(
        self,
        *,
        os: MobileOs,
        test_execution_mode: TestExecutionMode,
        test_environment: TestEnvironments,
    ) -> None:
        """Concrete implementation of mobile driver instance creation

        Args:
            os (MobileOs): _description_
            test_execution_mode (TestExecutionMode): _description_
            test_environment (TestEnvironments): _description_
        """
        self.testEnv = test_environment
        self.os = os
        self.testExecMode = test_execution_mode

    def get_mobile_driver(self, *, capabilities: dict[str, Any]):
        """Concrete implementation of fetching mobile driver

        Args:
            capabilities (dict[str, Any]): _description_

        Returns:
            tuple[WebDriver, int]: (mobile driver instance, appium port)
        """
        common_config = YamlParser(FilePaths.COMMON)
        # launch appium service
        port = AppiumUtils.launch_appium_service()
        # return requested mobile driver
        remote_url = (
            common_config.get_value(
                "appium",
                "appium_base_url_local"
                if self.testExecMode.value.__eq__(TestExecutionMode.LOCAL.value)
                else "appium_base_url_remote",
            ),
        )[0].replace("${port}", str(port))
        from urllib.parse import urlparse

        host = urlparse(remote_url).hostname
        AppiumUtils.wait_for_appium_service_to_load(30, host, port)
        return (
            ConcreteAndroidDriver(remote_url).get_driver(capabilities=capabilities)
            if self.os.value.__eq__(MobileOs.ANDROID.value)
            else ConcreteIOSDriver(remote_url).get_driver(capabilities=capabilities)
        ), port
