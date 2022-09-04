import pygame
from config import resource_paths, constants
from sprites.wall_sprite import WallSprite
from utils import data_management


class Level:
    def __init__(self, game, level_data):

        self.game = game
        self.level_data = level_data

        # Create all the sprites for the level.
        self.all_sprites = YSortedSpriteGroup(self.game.screen, level_data)
        self.wall_sprites = pygame.sprite.Group()
        self.route_sprites = pygame.sprite.Group()
        self.floor_sprites = pygame.sprite.Group()

    def load_level(self):
        """Loads the level and creates all the sprites."""

        for type, layout in self.level_data["tiles"].items():
            for row_index, row in enumerate(layout):
                for column_index, value in enumerate(row):
                    x = column_index * constants.TILE_SIZE
                    y = row_index * constants.TILE_SIZE

                    if value != "-1":
                        if type == "wall":
                            WallSprite(
                                self,
                                self.level_data["wall_path"] + value + ".png",
                                x,
                                y,
                            )


class YSortedSpriteGroup(pygame.sprite.Group):
    def __init__(self, screen, level_data):

        super().__init__()
        self.screen = screen

        self.half_width = constants.WINDOW_DIMENSIONS[0] // 2
        self.half_height = constants.WINDOW_DIMENSIONS[1] // 2
        self.offset = pygame.math.Vector2()

        # The floor.
        self.floor_surface = pygame.image.load(level_data["floor_path"])
        self.floor_rect = self.floor_surface.get_rect(topleft=(0, 0))

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_position = self.floor_rect.topleft - self.offset
        self.screen.blit(self.floor_surface, floor_offset_position)

        for sprite in sorted(self.sprites(), key=lambda x: x.rect.y):
            offset_position = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_position)
