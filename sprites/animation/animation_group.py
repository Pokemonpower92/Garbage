import pygame


class AnimationGroup:
    def __init__(self) -> None:
        pass

    def load_animation_sets(self, animation_sets):
        """Load the animation sets for the group into the animation_sets dictionary."""
        pass

    def advance_animation(self) -> pygame.image:
        """Cycle the current animation group."""

        if self.current_animation_set.end():
            self.current_animation_set.restart()
        else:
            self.current_animation_set.advance()

    def change_animation_set(self, direction: str, action: str) -> None:
        """Swap to the appropriate animation set for the direction and action."""
        pass
