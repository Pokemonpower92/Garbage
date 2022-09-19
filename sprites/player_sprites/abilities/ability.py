import abc
import pygame


class Ability(abc.ABC):
    """This is the base class for all abilities.

    All entity abilities will eventualy inherit from this class.
    """

    def __init__(self, player):
        self.player = player
        self.can_cast = True
        self.time_since_last_cast = 0

    def cast(self):
        """Cast this particular ability."""
        pass

    def cooldown(self):
        """Handle the cooldown for this particular ability."""
        pass
