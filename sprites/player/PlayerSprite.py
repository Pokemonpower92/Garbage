from asyncio import constants
import pygame
from config import constants


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, game):
        self.x = 0
        self.y = 0
        self.game = game

        self.groups = self.game.all_sprites
        self.image = pygame.Surface((constants.TILE_SIZE, constants.TILE_SIZE))
        self.rect = self.image.get_rect()

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image.fill("Yellow")
        self.groups.add(self)

    def move(self, dx: int, dy: int):
        """Move the player by dx and dy"""
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * constants.TILE_SIZE
        self.rect.y = self.y * constants.TILE_SIZE
