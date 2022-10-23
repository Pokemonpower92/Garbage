import pygame
from config import game_constants, resource_paths
from sprites.environment_sprites.wall_sprite import WallSprite
from sprites.enemy_sprites.enemy_sprite import EnemySprite
from utils import data_management


class Menu:
    def __init__(self, screen, menu_data):

        self.menu_data = menu_data
        self.screen = screen

        # Create all the sprites for the menu.
        self.all_sprites = MenuSpriteGroup(screen, menu_data)
        self.button_sprites = pygame.sprite.Group()
        self.text_sprites = pygame.sprite.Group()
        self.background_surface = None

    def load_menu(self):
        """Loads the menu and creates all the sprites."""
        pass


class MenuSpriteGroup(pygame.sprite.Group):
    def __init__(self, screen, menu_data):

        super().__init__()
        self.screen = screen
        self.menu_data = menu_data
        # The background.
        self.background_surface = pygame.image.load(self.menu_data["background_path"])

    def custom_draw(self):

        self.screen.blit(self.background_surface, [0, 0])
