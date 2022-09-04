import pygame
from config import constants


def event_loop(game):
    """This checks for all types of player input."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.quit()
