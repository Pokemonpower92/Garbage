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
        self.can_interact = False

    def draw(self):
        self.menu.draw_background()
        self.menu.draw_text_sprites()
        self.menu.draw_button_sprites()

    def load_assets(self):
        self.menu = Menu(self.screen, menu_data.TITLE_SCREEN)

    def update(self):
        pygame.display.update()

    def run(self):
        self.time_since_loop_started = pygame.time.get_ticks()
        self.running = True
        while self.running:
            self.cooldown()
            self.event_loop()
            self.update()
            self.draw()

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time_since_loop_started

        if delta_time >= 500:
            self.can_interact = True

    def event_loop(self):
        listen.event_loop()

        if self.can_interact:
            self.menu.check_events()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_RETURN]:
                MainMenuLoop().run()
