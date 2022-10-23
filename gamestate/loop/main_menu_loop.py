import pygame
from sys import exit
import os

from gamestate.loop import game_loop
from gamestate.loop.loop import Loop
from gamestate.level.level import Level

from config import game_constants, level_data
from utils import setup
from events import listen


class MainMenuLoop(Loop):
    def __init__(self, gamestate):
        super().__init__(gamestate)
        self.game_loop = game_loop.GameLoop(gamestate)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_text(
            "main menu", self.font, (255, 255, 255), self.screen, self.title_position
        )
        self.draw_text(
            "Press 'space'",
            self.font,
            (255, 255, 255),
            self.screen,
            self.message_position,
        )

    def load_assets(self):
        self.level = Level(self, level_data.MAIN_MENU)

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

        if pressed_keys[pygame.K_SPACE]:
            self.game_loop.run()
