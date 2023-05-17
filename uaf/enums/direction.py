from . import Enum, unique


@unique
class Direction(Enum):
    DOWN = ("down",)
    UP = ("up",)
    RIGHT = ("right",)
    LEFT = "left"
