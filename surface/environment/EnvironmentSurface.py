import pygame


class EnvironmentSurface:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.sprite = ""
        self.surface = None

    def load_sprite(self, path: str) -> pygame.image:
        """
        Load the surface's sprite from the path.

        Parameters:
            path: the path to the sprite's image.

        Returns:
            A pygame.image object.
        """
        pass

    def set_coordinates(self, x: int, y: int):
        """
        Set the surface's x and y coordinates.

        Parameters:
            x: the x coordinate.
            y: the y coordinate.
        """
        pass
