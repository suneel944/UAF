from . import Enum, unique


@unique
class DeviceStatus(Enum):
    """Device status as constant

    Args:
        Enum (_type_): _description_
    """

    AVAILABLE = "available"
    TERMINATED = "terminated"
    IN_USE = "in_use"
    FAULTY = "faulty"
