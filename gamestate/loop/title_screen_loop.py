import pygame
from sys import exit
import os

from config import game_constants, level_data
from utils import setup
from events import listen
from config import game_constants, level_data

from .loop import Loop


class TitleScreenLoop(Loop):
    def __init__(self, gamestate):
        super().__init__(gamestate)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_text(
            "Title", self.font, (255, 255, 255), self.screen, self.title_position
        )
        self.draw_text(
            "Press 'enter'",
            self.font,
            (255, 255, 255),
            self.screen,
            self.message_position,
        )

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
            self.gamestate.run_game_loop()
