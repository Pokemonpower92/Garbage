import pygame
from sys import exit
import os

from config import game_constants, level_data, menu_data
from utils import setup
from events import listen
from config import game_constants, level_data

from gamestate.loop.loop import Loop
from gamestate.loop.main_menu_loop import MainMenuLoop
from gamestate.menu.menu import Menu


class TitleScreenLoop(Loop):
    def __init__(self):
        super().__init__()
        self.load_assets()
        self.main_menu_loop = MainMenuLoop()

    def draw(self):
        self.menu.draw_background()
        self.menu.draw_text_sprites()
        self.menu.draw_button_sprites()

    def load_assets(self):
        self.menu = Menu(self.screen, menu_data.TITLE_SCREEN)

    def update(self):
        pygame.display.update()

    def run(self):

        self.running = True
        while self.running:
            self.event_loop()
            self.update()
            self.draw()

    def event_loop(self):
        listen.event_loop(self)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_RETURN]:
            self.main_menu_loop.run()
