from . import Enum


class DeviceStatus(Enum):
    AVAILABLE = "available"
    TERMINATED = "terminated"
    IN_USE = "in_use"
    FAULTY = "faulty"
