from gamestate.menu.menu import Menu
from gamestate.loop import main_menu_loop

import pygame


class PauseMenu(Menu):
    def __init__(self, screen, menu_data, game_loop, pause_menu_loop):
        super().__init__(screen, menu_data)
        self.game_loop = game_loop
        self.pause_menu_loop = pause_menu_loop
        self.define_loops()

    def define_loops(self):
        self.new_game_loop = "New Game Loop"
        self.load_game_loop = "Load Game Loop"
        self.options_loop = "Options Loop"
        self.character_screen_loop = "Character Loop"
        self.save_game_menu_loop = main_menu_loop.MainMenuLoop()
        self.exit_game_menu_loop = main_menu_loop.MainMenuLoop()

        self.loops = {
            "new_game_loop": self.new_game_loop,
            "load_game_button": self.load_game_loop,
            "options_button": self.options_loop,
            "character_screen_button": self.character_screen_loop,
            "save_game_button": self.save_game_menu_loop,
            "exit_game_button": self.exit_game_menu_loop,
        }

    def check_events(self):
        for sprite in self.button_sprites:
            clicked, button = sprite.check_mouse_event()

            if clicked:
                # If we exit the game we need to end both loops.
                if button == "exit_game_button":
                    self.game_loop.running = False
                    self.pause_menu_loop.running = False
                    return

                self.loops[button].run()
