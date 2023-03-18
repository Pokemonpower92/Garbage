from typing import List

from sprites.animation.animation_set import AnimationSet
from sprites.animation.animation_group import AnimationGroup
from sprites.types.player_actions import PlayerActions
from sprites.types.direction import Direction

import pygame



class PlayerAnimationGroup(AnimationGroup):
    def __init__(self) -> None:
        super().__init__()
        self.current_animation_set = None
        self.all_sets = None

    def load_animation_sets(self, image_sets: List[str]) -> AnimationSet:
        """
        Load the animation sets for the group into the animation_sets dictionary.
        @param image_sets: A list of paths to all animations for the group.
        @return: The created AnimationSet.
        """

        self.all_sets = image_sets.copy()

        for action, directions in image_sets.items():
            for direction, image_set in directions.items():
                self.all_sets[action][direction] = AnimationSet([x for x in image_set])

        self.change_current_set(PlayerActions.IDLE, Direction.DOWN)

        return self

    def change_current_set(self, action: PlayerActions, direction: Direction) -> None:
        """
        Change the currently cycling animation set.
        @param action: The action to take.
        @param direction: The direction that the action happens in.
        @return: None
        """
        self.current_animation_set = self.all_sets[action.value][direction.value]

    def advance_animation(self) -> pygame.image:
        """
        Cycle the current animation group.
        @return: The current image to render in the animation cycle.
        """

        return self.current_animation_set.advance()
