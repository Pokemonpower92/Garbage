from gamestate.menu.menu import Menu
from gamestate.loop import main_menu_loop


class PauseMenu(Menu):
    def __init__(self, screen, menu_data):
        super().__init__(screen, menu_data)
        self.define_loops()

    def define_loops(self):
        self.load_game_loop = "Load Game Loop"
        self.options_loop = "Options Loop"
        self.main_menu_loop = main_menu_loop.MainMenuLoop()
        self.character_screen_loop = "Character Loop"

        self.loops = {
            "load_game_button": self.load_game_loop,
            "options_button": self.options_loop,
            "main_menu_button": self.main_menu_loop,
            "character_screen_button": self.character_screen_loop,
        }

    def check_events(self):
        for sprite in self.button_sprites:
            clicked, button = sprite.check_mouse_event()

            if clicked:
                self.loops[button].run()
