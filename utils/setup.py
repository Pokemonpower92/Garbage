import pygame
from typing import Tuple


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
