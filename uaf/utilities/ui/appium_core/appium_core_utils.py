import socket
import time
import requests
from . import (
    FakerUtils,
    FilePaths,
    MobileDeviceEnvironmentType,
    Optional,
    YamlParser,
    MobileAppType,
    MobileOs,
    AppiumService,
)


class CoreUtils:
    """Utility class for Appium"""

    def __init__(self) -> None:
        """Constructor"""
        pass

    @staticmethod
    def execute_commands(command: list[str], check_output: bool = False):
        """Executes command in a terminal/cmd/bash

        Args:
            command (list[str]): list of commnd strings
            check_output (bool, optional): to indicate whether commandline execution result is required/or not. Defaults to False.

        Returns:
            Popen|bytes: process instance| byte data
        """
        import subprocess

        if check_output:
            return subprocess.Popen(command)
        else:
            return subprocess.check_output(command).decode("utf-8")

    @staticmethod
    def launch_appium_service(mobile_os: MobileOs, app_type: MobileAppType) -> int:
        """Launches Appium service based on the mobile OS and app type.

        Args:
            mobile_os (MobileOs): The mobile OS type, either 'android' or 'ios'
            app_type (MobileAppType): The app type, either 'native', 'hybrid', or 'web'

        Raises:
            Exception: if unable to find port availability or start Appium service

        Returns:
            int: Port number.
        """
        config = YamlParser(FilePaths.COMMON)
        min_port = config.get_value("ports", "appipum_service_min_port_band")
        max_port = config.get_value("ports", "appium_service_max_port_band")

        port = CoreUtils._find_free_port(min_port, max_port)
        CoreUtils._start_appium_service(port, mobile_os, app_type)

        return port

    @staticmethod
    def _find_free_port(min_port: int, max_port: int) -> int:
        """Finds an available port within the given range

        Args:
            min_port (int): Minimum port number in the range
            max_port (int): Maximum port number in the range

        Raises:
            Exception: If no free port is found within the range

        Returns:
            int: Available port number.
        """
        for port in range(min_port, max_port + 1):
            if CoreUtils._is_port_available(port):
                return port
        raise Exception(
            f"Unable to find a free port within the range {min_port}-{max_port}"
        )

    @staticmethod
    def _is_port_available(port: int) -> bool:
        """Checks if a given port is available

        Args:
            port (int): Port number to check

        Returns:
            bool: True if the port is available, False otherwise
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(("localhost", port)) != 0

    @staticmethod
    def _start_appium_service(
        port: int, mobile_os: MobileOs, app_type: MobileAppType
    ) -> AppiumService:
        """Starts the Appium service on the given port using the custom AppiumService class.

        Args:
            port (int): Port number on which Appium service should be started
            mobile_os (MobileOs): The mobile OS type, either 'android' or 'ios'
            app_type (MobileAppType): The app type, either 'native', 'hybrid', or 'web'

        Returns:
            AppiumService: The AppiumService instance for the started Appium service

        Raises:
            Exception: If the Appium service fails to start
        """
        appium_service = AppiumService()

        # Build arguments list based on mobile OS and app type
        args = ["--port", str(port), "--log-timestamp", "--local-timezone"]

        if mobile_os == MobileOs.ANDROID:
            args.extend(["--allow-insecure", "chromedriver_autodownload"])
            if app_type in [MobileAppType.HYBRID, MobileAppType.WEB]:
                args.extend(["--chromedriver-port", str(port + 1)])
        elif mobile_os == MobileOs.IOS:
            if app_type in [MobileAppType.HYBRID, MobileAppType.WEB]:
                args.extend(["--webkit-debug-proxy-port", str(port + 2)])

        try:
            appium_service.start(args=args)
            return appium_service
        except Exception as e:
            raise Exception(f"Failed to start Appium service: {str(e)}")

    @staticmethod
    def wait_for_appium_service_to_load(
        max_wait_time: int, host: str, port: int
    ) -> bool:
        """Waits for an Appium service to load for a specified amount of time.

        Args:
            max_wait_time (int): Maximum wait time in seconds.
            host (str): Host address.
            port (int): Port number.

        Returns:
            bool: True if the service starts within the specified time, False otherwise.
        """
        start_time = time.time()
        while not CoreUtils._is_service_running(host, port):
            elapsed_time = time.time() - start_time
            if elapsed_time >= max_wait_time:
                return False
            time.sleep(1)
        return True

    @staticmethod
    def _is_service_running(host: str, port: int) -> bool:
        """Checks if a service is running on the specified host and port.

        Args:
            host (str): Host address.
            port (int): Port number.

        Returns:
            bool: True if the service is running, False otherwise.
        """
        try:
            response = requests.get(f"http://{host}:{port}/status", timeout=1)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    @staticmethod
    def purge_appium_node(port: int):
        """Terminate/kill specified appium port

        Args:
            port (int): port number
        """
        from psutil import AccessDenied, NoSuchProcess, ZombieProcess, process_iter

        for proc in process_iter():
            try:
                for cons in proc.connections(kind="inet"):
                    if cons.laddr.port == port:
                        proc.kill()
            except (NoSuchProcess, AccessDenied, ZombieProcess):
                pass

    @staticmethod
    def create_ios_simulator(simulator_name: str, package: str):
        """
        Create ios simulator with user required name and system image a.ka package\n

        Ex: AppiumUtils.create_ios_simulator("test_simulator_01", "com.apple.CoreSimulator.SimRuntime.iOS-15-0")
        """
        if simulator_name.__contains__(" "):
            raise Exception("No white spaces allowed in emulator name")
        CoreUtils.execute_commands(
            [
                "xcrun",
                "simctl",
                "create",
                f"{simulator_name}",
                f"{package}",
            ]
        )

    @staticmethod
    def purge_ios_simulator(simulator_name: str):
        """Delete specified ios simulator

        Args:
            simulator_name (str): name of the simulator
        """
        CoreUtils.execute_commands(["xcrun", "simctl", "delete", f"{simulator_name}"])

    @staticmethod
    def create_android_emulator(
        emulator_name: Optional[str] = None, package: Optional[str] = None
    ):
        """Creates an android emulator with user required name and system image a.k.a package\n

        Ex: AppiumUtils.create_android_emulator("test_emulator_1", "system-images;android-31;google_apis;x86_64")
        Note :
            i.  If package details are not known then follow the below steps\n
                    1.  Execute the command "sdkmanager --list"\n
                    2.  Select any from the entry and provide that as an package argument for above method\n
            ii. Follow the [package installing instruction](https://developer.android.com/studio/command-line
            /sdkmanager#install)
            , if no packages/system images are installed yet in system

        Args:
            emulator_name (Optional[str], optional): name of the emulator. Defaults to None.
            package (Optional[str], optional): installing android package information. Defaults to None.

        Raises:
            Exception: if white spaces are provided in emulator name
        """
        if emulator_name is None:
            faker = FakerUtils.get_instance()
            emulator_name = (
                f"Test_Auto_Emulator_{faker.random_int(min_val=0, max_val=999999)}"
                f"_{faker.random_float(min_val=10, max_val=2993092)}_{faker.random_str(length=4)}"
            )
        if emulator_name.__contains__(" "):
            raise Exception("No white spaces allowed in emulator name")
        CoreUtils.execute_commands(
            [
                "avdmanager",
                "--verbose",
                "create",
                "avd",
                "--force",
                "--name",
                f'"{emulator_name}"',
                "--package",
                f'"{package}"',
                "--tag",
                '"google_apis"',
                "--abi",
                '"x86_64"',
            ]
        )

    @staticmethod
    def purge_android_emulator(emulator_name: str):
        """Delete specified android emulator

        Args:
            emulator_name (str): name of the emulator
        """
        CoreUtils.execute_commands(
            ["avdmanager", "delete", "avd", "-n", f"{emulator_name}"]
        )

    @staticmethod
    def fetch_connected_android_devices_ids(
        mobile_device_environment: MobileDeviceEnvironmentType,
        emulator_name: Optional[str] = None,
        package: Optional[str] = None,
    ):
        """Fetch connected android devices

        Args:
            mobile_device_environment (MobileDeviceEnvironmentType): mobile device environment type enum
            emulator_name (Optional[str], optional): name of the emulator. Defaults to None.
            package (Optional[str], optional): installing android package information. Defaults to None.

        Raises:
            RuntimeError: if no physical devices are connected at the moment
            TypeError: if unknown/unsupported device environment type is specified

        Returns:
            list[str]: list of connected android device ids
        """
        cmd_output = CoreUtils.execute_commands(["adb", "devices"])
        device_ids: list[str] = [
            line.split()[0]
            for line in cmd_output.splitlines()[1:]
            if line and not line.startswith("*")
        ]
        match mobile_device_environment.value:
            case MobileDeviceEnvironmentType.PHYSICAL.value:
                if device_ids.__len__() == 0:
                    raise RuntimeError(
                        "No physical device(s) connected/available at the moment!"
                    )
                return list(filter(lambda x: "emulator" not in x, device_ids))
            case MobileDeviceEnvironmentType.EMULATOR.value:
                if device_ids.__len__() == 0:
                    CoreUtils.create_android_emulator(emulator_name, package)
                list(filter(lambda x: "emulator" in x, device_ids))
            case _:
                raise TypeError("Supports only physical and emulator type!!")

    @staticmethod
    def fetch_connected_ios_devices_ids(
        mobile_device_environment: MobileDeviceEnvironmentType,
    ) -> list[str]:
        """Fetch connected ios devices list

        Args:
            mobile_device_environment (MobileDeviceEnvironmentType): mobile device environment type enum

        Raises:
            TypeError: if provided invalid mobile device environment type

        Returns:
            list[str]: list of connected ios device ids
        """
        match mobile_device_environment.value:
            case MobileDeviceEnvironmentType.PHYSICAL.value:
                cmd_output = CoreUtils.execute_commands(["idevice_id", "-l"])
                return list(cmd_output.strip().split("\n"))
            case MobileDeviceEnvironmentType.SIMULATOR.value:
                cmd_output = CoreUtils.execute_commands(["xcrun", "simctl", "list"])
                return [
                    line.split("(")[1].split(")")[0] for line in cmd_output.split("\n")
                ]
            case _:
                raise TypeError("Supports only physical and simulator type!!")
