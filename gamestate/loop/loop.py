import abc
import pygame
from utils import setup

from config import game_constants


class Loop(abc.ABC):
    def __init__(self, gamestate):
        self.gamestate = gamestate

        self.screen = setup.setup_window(
            game_constants.WINDOW_DIMENSIONS,
            game_constants.WINDOW_TITLE,
        )

        self.font = pygame.font.SysFont(None, 75)
        
        self.clock = pygame.time.Clock()
        self.title_position = pygame.math.Vector2(
            game_constants.WINDOW_DIMENSIONS[0] // 2, 0
        )
        self.message_position = pygame.math.Vector2(
            game_constants.WINDOW_DIMENSIONS[0] // 2,
            game_constants.WINDOW_DIMENSIONS[1]
            - (game_constants.WINDOW_DIMENSIONS[1] // 5),
        )

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def load_assets(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

    def draw_text(self, text, font, color, surface, pos):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.midtop = pos
        surface.blit(textobj, textrect)

    def quit(self):
        """Quit the game."""

        pygame.quit()
        exit()
