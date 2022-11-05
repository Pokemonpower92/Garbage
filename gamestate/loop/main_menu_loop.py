import pygame
from sys import exit
import os

from gamestate.loop import game_loop, pause_menu_loop
from gamestate.loop.loop import Loop
from gamestate.menu.main_menu import MainMenu

from config import menu_data
from events import listen


class MainMenuLoop(Loop):
    def __init__(self):
        super().__init__()
        self.load_assets()

    def draw(self):
        self.menu.draw_background()
        self.menu.draw_text_sprites()
        self.menu.draw_button_sprites()

    def load_assets(self):
        self.menu = MainMenu(self.screen, menu_data.MAIN_MENU)

    def update(self):
        pygame.display.update()

    def run(self):

        self.running = True
        while self.running:
            self.event_loop()
            self.update()
            self.draw()

    def event_loop(self):
        listen.event_loop()
        self.menu.check_events()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            game_loop.GameLoop().run()
