import pygame
from config import constants, resource_paths


class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, tilemap, type, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

        self.tilemap = tilemap

        self.groups = self.tilemap.all_sprites, self.tilemap.wall_sprites
        self.image = self.load_image()
        self.rect = self.image.get_rect()

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.rect.x = self.x
        self.rect.y = self.y

    def load_image():
        return pygame.image.load()
