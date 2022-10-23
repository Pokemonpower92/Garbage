from gamestate.loop import title_screen_loop, main_menu_loop


class Gamestate:
    """This is the controller for the game loops."""

    def __init__(self) -> None:
        self.title_screen_loop = title_screen_loop.TitleScreenLoop(self)
        self.main_menu_loop = main_menu_loop.MainMenuLoop(self)

    def run_title_screen(self):
        self.title_screen_loop.run()

    def run_game_loop(self):
        self.main_menu_loop.run()
