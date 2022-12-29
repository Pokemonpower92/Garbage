import pygame
from config import game_constants, resource_paths
from sprites.menu_sprites import text_sprite, menu_sprite_factory
from sprites.menu_sprites import button_sprite
from utils import data_management


class Menu:
    def __init__(self, screen, menu_data):

        self.menu_data = menu_data
        self.screen = screen

        self.sprite_factory = menu_sprite_factory.MenuSpriteFactory(self)

        # Create all the sprites for the menu.
        self.button_sprites = ButtonSpriteGroup(self.screen)
        self.text_sprites = TextSpriteGroup(self.screen)
        self.background_surface = None

        self.load_menu()

    def load_menu(self):
        """Loads the menu and creates all the sprites."""

        self.background_surface = pygame.image.load(self.menu_data["background_path"])

        # A menu may have multiple text and button sprites.
        for type, sprites in self.menu_data["sprites"].items():
            for values in sprites:
                self.sprite_factory.create_menu_sprite(type).load_content(values)

    def draw_background(self):
        self.screen.blit(self.background_surface, [0, 0])

    def draw_text_sprites(self):
        self.text_sprites.custom_draw()

    def draw_button_sprites(self):
        self.button_sprites.custom_draw()

    def check_events(self):
        for sprite in self.button_sprites:
            clicked, button = sprite.check_mouse_event()

            if clicked:
                self.loops[button].run()


class TextSpriteGroup(pygame.sprite.Group):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def custom_draw(self):
        for sprite in self.sprites():
            self.screen.blit(sprite.content, sprite.position)


class ButtonSpriteGroup(pygame.sprite.Group):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def custom_draw(self):
        for sprite in self.sprites():
            sprite.draw()
