import pygame
from typing import List
from gamestate.globalTimers.globalTimers import globalTimers

class AnimationSet:
    """This is a wrapper for working with lists of animation images."""

    def __init__(self, image_set: List):
        self.image_set = image_set
        self.current_image = 0

    def advance(self) -> pygame.image:
        """Cycle the image to be rendered."""
        image = pygame.image.load(self.image_set[self.current_image])

        if globalTimers.get_instance().check_animation_cooldown():
            self.current_image += 1
            if self.current_image == len(self.image_set):
                self.current_image = 0
            globalTimers.get_instance().set_animation_timer()

        return image
