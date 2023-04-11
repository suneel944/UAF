from . import FakerUtils, FilePaths, MobileDeviceEnvironmentType, Optional, YamlParser


class AppiumUtils:
    def __init__(self) -> None:
        pass

    @staticmethod
    def execute_commands(command: list[str], check_output: bool = False):
        import subprocess

        if check_output:
            return subprocess.Popen(command)
        else:
            return subprocess.check_output(command).decode("utf-8")

    @staticmethod
    def launch_appium_service() -> int:
        import socket

        config = YamlParser(FilePaths.COMMON)

        def find_free_port():
            for port in range(
                config.get_value("ports", "appipum_service_min_port_band"),
                config.get_value("ports", "appium_service_max_port_band") + 1,
            ):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    # if port is available, return it
                    if s.connect_ex(("localhost", port)) != 0:
                        return port
            # if no free port is found, raise an exception
            raise Exception(
                "Unable to find a free port within the range {}-{}".format(
                    config.get_value("ports", "appipum_service_min_port_band"),
                    config.get_value("ports", "appium_service_max_port_band"),
                )
            )

        port: int = find_free_port()
        AppiumUtils.execute_commands(
            [
                "appium",
                "-p",
                f"{port}",
                "--allow-insecure",
                "chromedriver_autodownload",
            ],
            True,
        )
        return port

    @staticmethod
    def wait_for_appium_service_to_load(max_wait_time: int, host: str, port: int):
        import socket
        import time

        start_time = time.time()
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.settimeout(max_wait_time)
                    s.connect((host, port))
                    break
                except OSError:
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= max_wait_time:
                        raise TimeoutError("Timed out waiting for Appium server to start")
                    else:
                        time.sleep(1)

    @staticmethod
    def purge_appium_node(port: int):
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
        AppiumUtils.execute_commands(
            [
                "xcrun",
                "simctl",
                "create",
                "{}".format(simulator_name),
                "{}".format(package),
            ]
        )

    @staticmethod
    def purge_ios_simulator(simulator_name: str):
        AppiumUtils.execute_commands(["xcrun", "simctl", "delete", "{}".format(simulator_name)])

    @staticmethod
    def create_android_emulator(emulator_name: Optional[str] = None, package: Optional[str] = None):
        """
        Creates an android emulator with user required name and system image a.k.a package\n

        Ex: AppiumUtils.create_android_emulator("test_emulator_1", "system-images;android-31;google_apis;x86_64")
        Note :
            i.  If package details are not known then follow the below steps\n
                    1.  Execute the command "sdkmanager --list"\n
                    2.  Select any from the entry and provide that as an package argument for above method\n
            ii. Follow the [package installing instruction](https://developer.android.com/studio/command-line
            /sdkmanager#install)
            , if no packages/system images are installed yet in system
        """
        if emulator_name is None:
            faker = FakerUtils.get_instance()
            emulator_name = (
                f"Test_Auto_Emulator_{faker.random_int(min_val=0, max_val=999999)}"
                f"_{faker.random_float(min_val=10, max_val=2993092)}_{faker.random_str(length=4)}"
            )
        if emulator_name.__contains__(" "):
            raise Exception("No white spaces allowed in emulator name")
        AppiumUtils.execute_commands(
            [
                "avdmanager",
                "--verbose",
                "create",
                "avd",
                "--force",
                "--name",
                '"{}"'.format(emulator_name),
                "--package",
                '"{}"'.format(package),
                "--tag",
                '"google_apis"',
                "--abi",
                '"x86_64"',
            ]
        )

    @staticmethod
    def purge_android_emulator(emulator_name: str):
        AppiumUtils.execute_commands(["avdmanager", "delete", "avd", "-n", "{}".format(emulator_name)])

    @staticmethod
    def fetch_connected_android_devices_ids(
        mobile_device_environment: MobileDeviceEnvironmentType,
        emulator_name: Optional[str] = None,
        package: Optional[str] = None,
    ):
        cmd_output = AppiumUtils.execute_commands(["adb", "devices"])
        device_ids: list[str] = [
            line.split()[0] for line in cmd_output.splitlines()[1:] if line and not line.startswith("*")
        ]
        match mobile_device_environment.value:
            case MobileDeviceEnvironmentType.PHYSICAL.value:
                if device_ids.__len__() == 0:
                    raise RuntimeError("No physical device(s) connected/available at the moment!")
                return list(filter(lambda x: "emulator" not in x, device_ids))
            case MobileDeviceEnvironmentType.EMULATOR.value:
                if device_ids.__len__() == 0:
                    AppiumUtils.create_android_emulator(emulator_name, package)
                list(filter(lambda x: "emulator" in x, device_ids))
            case _:
                raise TypeError("Supports only physical and emulator type!!")

    @staticmethod
    def fetch_connected_ios_devices_ids(
        mobile_device_environment: MobileDeviceEnvironmentType,
    ) -> list[str]:
        match mobile_device_environment.value:
            case MobileDeviceEnvironmentType.PHYSICAL.value:
                cmd_output = AppiumUtils.execute_commands(["idevice_id", "-l"])
                return list(cmd_output.strip().split("\n"))
            case MobileDeviceEnvironmentType.SIMULATOR.value:
                cmd_output = AppiumUtils.execute_commands(["xcrun", "simctl", "list"])
                return [line.split("(")[1].split(")")[0] for line in cmd_output.split("\n")]
            case _:
                raise TypeError("Supports only physical and simulator type!!")
