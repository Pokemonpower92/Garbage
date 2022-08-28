import pygame
from .EnvironmentSurface import EnvironmentSurface


class GroundSurface(EnvironmentSurface):
    def __init__(self, path: str):
        """
        Builds a GroundSurface object and loads the image in path.

        Parameters:
            path: the path to the GroundSurface resource.
        """
        super().__init__()
        self.surface = self.load_sprite(path)

    def load_sprite(self, path: str):
        return pygame.image.load(path)
