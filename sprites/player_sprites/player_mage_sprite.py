import pygame
from config import game_constants, player_constants, resource_paths
from .player_sprite import PlayerSprite
from ..attack_sprites import mage_attack_sprite


class PlayerMageSprite(PlayerSprite):
    def __init__(self, tilemap, x=..., y=...):
        super().__init__(
            tilemap,
        )

        self.constants = player_constants.MAGE_CONSTANTS

        # Ability Configuration.
        self.attack_cooldown = self.constants["PLAYER_WALK_SPEED"]

        # Movement configuration.
        self.velocity = self.constants["PLAYER_WALK_SPEED"]
        self.player_run_speed = self.constants["PLAYER_RUN_SPEED"]
        self.player_sneak_speed = self.constants["PLAYER_SNEAK_SPEED"]
        self.player_walk_speed = self.constants["PLAYER_WALK_SPEED"]

        self.attacks = []

    def cooldowns(self):
        """Cooldowns for the mage class."""

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time_since_attack
        if delta_time >= self.constants["PLAYER_ATTACK_COOLDOWN"]:
            self.can_attack = True

    def attack(self):
        """Handle attacks for the mage class."""
        print("Attacking!")
        mage_attack_sprite.MageAttackSprite(
            self.level, self.facing, self.rect.x, self.rect.y
        )
        self.can_attack = False
