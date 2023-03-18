from enum import Enum, unique


@unique
class EnemyActions(Enum):
    ATTACKING = "attacking"
    TRACKING = "tracking"
    IDLE = "idle"
