from unittest import TestCase
from unittest.mock import patch

from sprites.animation.animation_set import AnimationSet
from sprites.types.direction import Direction
from sprites.types.player_actions import PlayerActions
from config.animation_sets import PLAYER_MAGE_ANIMATION_SETS

@patch("gamestate.globalTimers.globalTimers.globalTimers.check_animation_cooldown", return_value=True)
class TestAnimationSet(TestCase):

    def setUp(self):
        self.image_set = PLAYER_MAGE_ANIMATION_SETS[PlayerActions.IDLE.value][Direction.DOWN.value]


    def create_animation_set(self):
        animation_set = AnimationSet(self.image_set)
        assert animation_set.current_image == 0
        assert len(animation_set.image_set) == 4

        return animation_set

    def test_create_animation_set(self, mock_timer):
        a_set = self.create_animation_set()

    def test_advance_animation_set(self, mock_timer):
        a_set = self.create_animation_set()

        for i in range(len(a_set.image_set)):
            assert a_set.current_image == i
            a_set.advance()

        # ensure a complete cycle gets us back to image 0.
        assert a_set.current_image == 0
