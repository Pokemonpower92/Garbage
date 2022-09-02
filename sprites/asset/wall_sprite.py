import pygame
from config import constants


class WallSprite(pygame.sprite.Sprite):
    def __init__(self, tilemap, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

        self.tilemap = tilemap

        self.groups = self.tilemap.all_sprites, self.tilemap.wall_sprites
        self.image = pygame.Surface((constants.TILE_SIZE, constants.TILE_SIZE))
        self.rect = self.image.get_rect()

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image.fill(constants.WALL_COLOR)
        self.tilemap.wall_sprites.add(self)

        self.rect.x = self.x * constants.TILE_SIZE
        self.rect.y = self.y * constants.TILE_SIZE
