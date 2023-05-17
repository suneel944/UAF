from . import Enum, unique


@unique
class MobileDeviceEnvironmentType(Enum):
    """Mobile device environment type as constant

    Args:
        Enum (MobileDeviceEnvironmentType): enum
    """

    PHYSICAL = "physical"
    EMULATOR = "emulator"
    CLOUD = "cloud"
    SIMULATOR = "simulator"
