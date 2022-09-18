import pygame
from config import game_constants, resource_paths


class FloorSprite(pygame.sprite.Sprite):
    def __init__(self, level, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

        self.level = level

        self.groups = self.level.all_sprites, self.level.wall_sprites
        self.image = pygame.image.load(resource_paths.TEST_ROCK)
        self.rect = self.image.get_rect()

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.level.wall_sprites.add(self)

        self.rect.x = self.x * game_constants.TILE_SIZE
        self.rect.y = self.y * game_constants.TILE_SIZE
