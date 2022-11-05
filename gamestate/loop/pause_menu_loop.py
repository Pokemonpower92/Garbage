import pygame
from sys import exit
import os

from config import menu_data
from events import listen

from gamestate.loop.loop import Loop
from gamestate.menu.pause_menu import PauseMenu


class PauseMenuLoop(Loop):
    def __init__(self):
        super().__init__()
        self.load_assets()
        self.time_since_loop_started = pygame.time.get_ticks()
        self.can_exit = False

    def draw(self):
        self.menu.draw_background()
        self.menu.draw_text_sprites()
        self.menu.draw_button_sprites()

    def load_assets(self):
        self.menu = PauseMenu(self.screen, menu_data.PAUSE_MENU)

    def update(self):
        pygame.display.update()

    def run(self):
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
            self.can_exit = True

    def event_loop(self):

        listen.event_loop()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_ESCAPE]:
            if self.can_exit:
                self.running = False
