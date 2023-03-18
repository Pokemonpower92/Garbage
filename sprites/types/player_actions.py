from enum import Enum, unique

@unique
class PlayerActions(Enum):
    """
    Player actions are the actions a player can take.
    """

    IDLE = "idle"
    WALKING = "walking"
