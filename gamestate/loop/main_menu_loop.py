import pygame

from gamestate.loop.menu_loop import MenuLoop
from gamestate.menu.main_menu import MainMenu
from gamestate.globalTimers.globalTimers import globalTimers

from config import menu_data
from events import listen


class MainMenuLoop(MenuLoop):
    def __init__(self):
        super().__init__()
        self.load_assets()

    def load_assets(self):
        self.menu = MainMenu(self.screen, menu_data.MAIN_MENU)

    def event_loop(self):
        listen.event_loop()
        self.menu.check_events()
