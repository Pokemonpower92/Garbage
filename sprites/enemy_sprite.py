import pygame
from config import constants, resource_paths, level_data


class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, level, type, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

        self.level = level
        self.type = type

        self.groups = self.level.all_sprites, self.level.enemy_sprites
        self.image = self.load_image()
        self.rect = self.image.get_rect()

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.rect.x = self.x
        self.rect.y = self.y

    def load_image(self):
        image_path = self.level.level_data["graphics_paths"]["enemies"][self.type]
        return pygame.image.load(image_path)
