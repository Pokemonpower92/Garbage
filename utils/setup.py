import pygame
from typing import Tuple
from config.game_constants import WINDOW_DIMENSIONS, WINDOW_TITLE

class Window:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Window, cls).__new__(cls)
            cls._window = setup_window(WINDOW_DIMENSIONS, WINDOW_TITLE)
        return cls.instance

    def get_window(self):
        return self._window


def setup_window(dimensions: Tuple, title: str) -> pygame.display:
    """
    Sets up the game window.

    Parameters:
        dimensions: A tuple of the form (width, height)
        title: the title of the window.

    Returns:
        The display.
    """
    pygame.init()
    screen = pygame.display.set_mode(dimensions)
    pygame.display.set_caption(title)

    return screen
