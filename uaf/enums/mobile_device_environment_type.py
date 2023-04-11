from . import Enum


class MobileDeviceEnvironmentType(Enum):
    PHYSICAL = "physical"
    EMULATOR = "emulator"
    CLOUD = "cloud"
    SIMULATOR = "simulator"
