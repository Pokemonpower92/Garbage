import pygame
from config import player_constants, animation_sets
from .player_sprite import PlayerSprite
from .abilities import mage_ability

from sprites.animation.player_animation_group import PlayerAnimationGroup
import copy


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

        self.faire_fire_base_damage = self.constants["FAIRE_FIRE_BASE_DAMAGE"]
        self.faire_fire_actual_damage = self.faire_fire_base_damage
        self.concentration_damage_modifier = self.constants[
            "CONCENTRATION_DAMAGE_MODIFIER"
        ]
        self.concentration_effect_active = False

        # Movement configuration.
        self.velocity = self.constants["PLAYER_WALK_SPEED"]

        self.load_resources()

    def load_resources(self):
        """Load resources for the sprite."""
        self.animation_group = PlayerAnimationGroup().load_animation_sets(
            copy.deepcopy(animation_sets.PLAYER_MAGE_ANIMATION_SETS)
        )
