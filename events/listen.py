import pygame
import sys
from config import game_constants


def event_loop():
    """This checks for all types of player input."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
