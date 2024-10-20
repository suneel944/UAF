from typing import Any

from appium.webdriver.webdriver import WebDriver
from uaf.enums.file_paths import FilePaths
from uaf.enums.mobile_os import MobileOs
from uaf.enums.environments import Environments
from uaf.enums.execution_mode import ExecutionMode
from uaf.enums.mobile_app_type import MobileAppType
from uaf.factories.driver.abstract_factory.abstract_products.abstract_mobile.abstract_mobile import (
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
    Concrete mobile driver factory that produces mobile drivers for both Android and iOS.
    This factory ensures that the drivers returned are compatible with the mobile OS,
    application type, execution mode, and environment.
    """

    def __init__(
        self,
        *,
        os: MobileOs,
        app_type: MobileAppType,
        execution_mode: ExecutionMode,
        environment: Environments,
    ) -> None:
        """Initialize the mobile driver instance.

        Args:
            os (MobileOs): The mobile operating system (e.g., Android, iOS).
            app_type (MobileAppType): The type of mobile application (e.g., native, web, hybrid).
            execution_mode (ExecutionMode): The execution mode for the tests (e.g., local, remote).
            environment (Environments): The environment for the mobile driver (e.g., staging, production).
        """
        self.env = environment
        self.os = os
        self.app_type = app_type
        self.exec_mode = execution_mode

    def get_mobile_driver(
        self, *, capabilities: dict[str, Any]
    ) -> tuple[WebDriver, int]:
        """Fetch or create a mobile driver instance.

        This method launches the Appium service and returns the appropriate mobile driver
        based on the mobile OS (Android or iOS) and the given capabilities. It also handles
        setting up the Appium base URL and port.

        Args:
            capabilities (dict[str, Any]): A dictionary of mobile driver capabilities.

        Returns:
            tuple[WebDriver, int]: A tuple containing the mobile driver instance and the Appium port.
        """
        common_config = YamlParser(FilePaths.COMMON)
        port = CoreUtils.launch_appium_service(self.os, self.app_type)
        remote_url = (
            common_config.get_value(
                "appium",
                (
                    "appium_base_url_local"
                    if self.exec_mode.value == ExecutionMode.LOCAL.value
                    else "appium_base_url_remote"
                ),
            ),
        )[0].replace("${port}", str(port))
        from urllib.parse import urlparse

        host = urlparse(remote_url).hostname
        CoreUtils.wait_for_appium_service_to_load(30, host, port)
        return (
            ConcreteAndroidDriver(remote_url).get_driver(capabilities=capabilities)
            if self.os.value == MobileOs.ANDROID.value
            else ConcreteIOSDriver(remote_url).get_driver(capabilities=capabilities)
        ), port
