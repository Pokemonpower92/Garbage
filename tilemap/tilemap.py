import pygame
from config import resource_paths, constants
from resources.tilemaps.prototype import walls
from sprites.asset import wall_sprite


class Tilemap:
    def __init__(self, game, wall_map_path=""):

        self.game = game
        self.all_sprites = YSortedSpriteGroup(self.game.screen)
        self.wall_sprites = pygame.sprite.Group()
        self.route_sprites = pygame.sprite.Group()

    def load_wall_map(self, wall_map_path=""):
        for row_index, row in enumerate(walls.WALL_MAP):
            for col_index, col in enumerate(row):
                if col == "1":
                    wall_sprite.WallSprite(self, col_index, row_index)


class YSortedSpriteGroup(pygame.sprite.Group):
    def __init__(self, screen):

        super().__init__()
        self.screen = screen

        self.half_width = constants.WINDOW_DIMENSIONS[0] // 2
        self.half_height = constants.WINDOW_DIMENSIONS[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key=lambda x: x.rect.y):
            offset_position = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_position)
