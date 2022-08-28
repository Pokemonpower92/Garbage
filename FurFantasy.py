import pygame
from sys import exit
import os

from events import listen
from config import constants, environment_resource_paths
from setup import setup_help
from surface.environment.GroundSurface import GroundSurface


def load_surfaces():
    pass


def draw_surfaces():
    pass


def update_gamestate():
    pass


if __name__ == "__main__":
    screen = setup_help.setup_window(
        constants.WINDOW_DIMENSIONS, constants.WINDOW_TITLE
    )
    clock = pygame.time.Clock()
    background = GroundSurface(environment_resource_paths.BACKGROUD_IMAGE_PATH)

    # Main game loop.
    while True:

        try:
            # event loop
            if listen.event_loop() == False:
                exit()

            # draw everything
            screen.blit(background.surface, (background.x, background.y))

            # update everything.
            pygame.display.update()
            clock.tick(60)

        except Exception as e:
            print(f"Exception caught: {e}")
            break
