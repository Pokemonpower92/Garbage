from enum import Enum, unique

@unique
class Direction(Enum):
    """
    Directions.
    """

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

