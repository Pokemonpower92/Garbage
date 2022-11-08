from sprites.animation.animation_set import AnimationSet
from sprites.animation.animation_group import AnimationGroup
import pygame


class PlayerAnimationGroup(AnimationGroup):
    def __init__(self) -> None:
        super().__init__()

    def load_animation_sets(self, animation_sets) -> AnimationSet:
        """Load the animation sets for the group into the animation_sets dictionary."""

        for action, directions in animation_sets.items():
            for direction, set in directions.items():
                animation_sets[action][direction] = AnimationSet(set)

        self.current_animation_set = animation_sets["idle"]["down"]

        return self

    def advance_animation(self) -> pygame.image:
        """Cycle the current animation group."""

        return self.current_animation_set.advance()

    def change_animation_set(self, action: str, direction: str) -> None:
        """Swap to the appropriate animation set for the direction and action."""

        self.current_animation_set = self.animation_sets[action][direction]
