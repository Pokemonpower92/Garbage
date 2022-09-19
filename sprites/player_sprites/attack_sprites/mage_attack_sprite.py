import pygame
from .attack_sprite import AttackSprite
from config import game_constants, player_constants, resource_paths


class FaireFireSprite(AttackSprite):
    def __init__(self, level, direction, damage, x: int = 0, y: int = 0):
        super().__init__(level, x, y)
        self.constants = player_constants.MAGE_CONSTANTS
        self.direction = direction
        self.velocity = self.constants["FAIRE_FIRE_VELOCITY"] * direction
        self.damage = damage

    def move(self):
        """Move the attack."""
        self.hit_box.x += self.velocity.x
        self.check_collisions("x")
        self.hit_box.y += self.velocity.y
        self.check_collisions("y")

        self.rect.center = self.hit_box.center

    def load_resources(self):
        """Load the resources for the faire fire attack."""
        self.image = pygame.Surface(
            (game_constants.TILE_SIZE, game_constants.TILE_SIZE)
        )
        self.image.fill(game_constants.GREEN)
        self.rect = self.image.get_rect()


class Concentration(AttackSprite):
    def __init__(self, level, direction, x: int = 0, y: int = 0):
        super().__init__(level, x, y)
        self.constants = player_constants.MAGE_CONSTANTS
        self.direction = direction

    def move(self):
        """Move the attack. Concentration doesn't move, so simply pass."""
        pass

    def load_resources(self):
        """Load the resources for the mage attack."""
        self.image = pygame.Surface(
            (game_constants.TILE_SIZE, game_constants.TILE_SIZE)
        )
        self.image.fill(game_constants.GREEN)
        self.rect = self.image.get_rect()
