from sprites.animation.animation_set import AnimationSet
from sprites.animation.animation_group import AnimationGroup
import pygame

from config import game_constants, level_data, animation_sets


class PlayerAnimationGroup(AnimationGroup):
    def __init__(self) -> None:
        super().__init__()

    def load_animation_sets(self, image_sets) -> AnimationSet:
        """Load the animation sets for the group into the animation_sets dictionary."""

        a = image_sets.copy()

        for action, directions in image_sets.items():
            for direction, image_set in directions.items():
                a[action][direction] = AnimationSet([x for x in image_set])

        self.current_animation_set = a["idle"]["down"]

        return self

    def advance_animation(self) -> pygame.image:
        """Cycle the current animation group."""

        return self.current_animation_set.advance()

    def change_animation_set(self, action: str, direction: str) -> None:
        """Swap to the appropriate animation set for the direction and action."""

        self.current_animation_set = self.animation_sets[action][direction]
