import pygame
from .ability import Ability


class DaggerStrike(Ability):
    def cast(self):
        print("Casting dagger Strike")


class Sprint(Ability):
    def cast(self):
        self.velocity = self.player_run_speed
        self.sprinting = True
        self.sneaking = False


class Sneak(Ability):
    def cast(self):
        self.velocity = self.player_sneak_speed
        self.sneaking = True
