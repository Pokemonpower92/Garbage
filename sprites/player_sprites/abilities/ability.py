import abc
import pygame


class Ability(abc.ABC):
    def __init__(self, player):
        self.player = player
        self.can_cast = True
        self.time_since_last_cast = 0

    def cast(self):
        pass

    def cooldown(self):
        pass
