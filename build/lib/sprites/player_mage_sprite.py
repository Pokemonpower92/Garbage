import pygame
from config import game_constants, resource_paths
from player_sprite import PlayerSprite


class PlayterMageSprite(PlayerSprite):
    def __init__(self, tilemap, x=..., y=...):
        super().__init__(tilemap, x, y)

    def cooldowns(self):
        """Cooldowns for the mage class."""
        pass

    def attack(self):
        """Handle attacks for the mage class."""
        print("Attacking!")
