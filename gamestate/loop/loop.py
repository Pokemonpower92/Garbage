import abc
from typing import Tuple
import pygame
from utils import setup

from config import game_constants


class Loop(abc.ABC):
    """Loops are where all interation with the game from uses occurs."""

    def __init__(self):
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
    def draw(self) -> None:
        """Draw all of the sprites associated with the loop."""
        pass

    @abc.abstractmethod
    def load_assets(self) -> None:
        """Load the assets that belong to the loop."""
        pass

    @abc.abstractmethod
    def update(self):
        """Update the screen"""
        pass

    @abc.abstractmethod
    def run(self) -> None:
        """Run the loop."""
        pass

    def draw_text(
        self,
        text: str,
        font: pygame.font,
        color: Tuple,
        surface: pygame.surface,
        pos: Tuple,
    ) -> None:
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.midtop = pos
        surface.blit(textobj, textrect)

    def quit(self) -> None:
        """Quit the loop."""

        pygame.quit()
        exit()
