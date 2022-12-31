import pygame
from config import game_constants, resource_paths
from sprites.menu_sprites import text_sprite, menu_sprite_factory
from sprites.menu_sprites import button_sprite
from utils import data_management
from gamestate.menu import menu

from gamestate.loop import game_loop


class MainMenu(menu.Menu):
    def __init__(self, screen, menu_data):
        super().__init__(screen, menu_data)

    def check_events(self):
        for sprite in self.button_sprites:
            clicked, button = sprite.check_mouse_event()

            if clicked:
                if button == "new_game_button":
                    game_loop.GameLoop().start_new_game()
