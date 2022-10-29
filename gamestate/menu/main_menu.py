import pygame
from config import game_constants, resource_paths
from sprites.menu_sprites import text_sprite, menu_sprite_factory
from sprites.menu_sprites import button_sprite
from utils import data_management
from gamestate.menu import menu


class MainMenu(menu.Menu):
    def __init__(self, screen, menu_data):
        super().__init__(screen, menu_data)
        self.define_loops()

    def define_loops(self):
        self.new_game_loop = "New Game Loop"
        self.load_game_loop = "Load Game Loop"
        self.options_loop = "Options Loop"

        self.loops = {
            "new_game_button": self.new_game_loop,
            "load_game_button": self.load_game_loop,
            "options_button": self.options_loop,
        }

    def check_events(self):
        for sprite in self.button_sprites:
            clicked, button = sprite.check_mouse_event()

            if clicked:
                self.loops[button].run()
