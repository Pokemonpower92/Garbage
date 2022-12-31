import pygame
from typing import List


class AnimationSet:
    """This is a wrapper for working with lists of animation images."""

    def __init__(self, image_set: List):
        self.image_set = image_set
        self.current_image = 0

    def advance(self) -> pygame.image:
        """Cycle the image to be rendered."""
        image = pygame.image.load(self.image_set[self.current_image])
        self.current_image += 1

        if self.current_image == len(self.image_set):
            self.current_image = 0

        return image
