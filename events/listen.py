import pygame
import sys


def event_loop():
    """This checks for top level events, like 'x'ing' out of the game window."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
