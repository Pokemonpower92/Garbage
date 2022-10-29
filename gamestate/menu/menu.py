import pygame
from config import game_constants, resource_paths
from sprites.menu_sprites import text_sprite, button_sprite, menu_sprite_factory
from utils import data_management


class Menu:
    def __init__(self, screen, menu_data):

        self.menu_data = menu_data
        self.screen = screen

        self.sprite_factory = menu_sprite_factory.MenuSpriteFactory(self)

        # Create all the sprites for the menu.
        self.all_sprites = MenuSpriteGroup(screen, menu_data)
        self.button_sprites = pygame.sprite.Group()
        self.text_sprites = pygame.sprite.Group()
        self.background_surface = None

        self.load_menu()

    def load_menu(self):
        """Loads the menu and creates all the sprites."""

        # A menu may have multiple text and button sprites.
        for type, sprites in self.menu_data["sprites"].items():
            for values in sprites:
                self.sprite_factory.create_menu_sprite(type).load_content(values)


class MenuSpriteGroup(pygame.sprite.Group):
    def __init__(self, screen, menu_data):

        super().__init__()
        self.screen = screen
        self.menu_data = menu_data
        # The background.
        self.background_surface = pygame.image.load(self.menu_data["background_path"])

    def custom_draw(self):

        self.screen.blit(self.background_surface, [0, 0])
        for sprite in self.sprites():
            self.screen.blit(sprite.content, sprite.position)
