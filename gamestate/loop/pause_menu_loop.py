import pygame
import os

from config import menu_data
from events import listen

from gamestate.loop.menu_loop import MenuLoop
from gamestate.menu.pause_menu import PauseMenu


class PauseMenuLoop(MenuLoop):
    def __init__(self):
        super().__init__()

    def load_assets(self):
        self.menu = PauseMenu(self.screen, menu_data.PAUSE_MENU)

    def event_loop(self):
        listen.event_loop()

        if self.can_interact:
            self.menu.check_events()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_ESCAPE]:
                self.running = False
