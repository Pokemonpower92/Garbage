import pygame
from config import game_constants, player_constants, resource_paths
from .player_sprite import PlayerSprite
from .abilities import mage_ability


class PlayerMageSprite(PlayerSprite):
    def __init__(self, tilemap, x=..., y=...):
        super().__init__(
            tilemap,
        )

        self.constants = player_constants.MAGE_CONSTANTS

        # Ability Configuration.
        self.ability_one = mage_ability.FaireFire(self)
        self.ability_two = mage_ability.Concentration(self)
        self.ability_three = mage_ability.Teleport(self)

        # Movement configuration.
        self.velocity = self.constants["PLAYER_WALK_SPEED"]
