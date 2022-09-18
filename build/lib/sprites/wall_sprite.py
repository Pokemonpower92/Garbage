import pygame
from config import game_constants, resource_paths


class WallSprite(pygame.sprite.Sprite):
    def __init__(self, tilemap, image_path, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

        self.tilemap = tilemap

        self.groups = self.tilemap.all_sprites, self.tilemap.wall_sprites
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.rect.x = self.x
        self.rect.y = self.y
