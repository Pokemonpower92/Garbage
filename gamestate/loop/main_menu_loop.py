import pygame

from gamestate.loop.menu_loop import MenuLoop
from gamestate.menu.main_menu import MainMenu

from config import menu_data


class MainMenuLoop(MenuLoop):
    def __init__(self):
        super().__init__()

    def load_assets(self):
        self.menu = MainMenu(self.screen, menu_data.MAIN_MENU)
