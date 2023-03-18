import copy
from unittest import TestCase
from unittest.mock import patch

from sprites.animation.player_animation_group import PlayerAnimationGroup
from sprites.types.direction import Direction
from sprites.types.player_actions import PlayerActions
from config.animation_sets import PLAYER_MAGE_ANIMATION_SETS


@patch("gamestate.globalTimers.globalTimers.globalTimers.check_animation_cooldown", return_value=True)
class TestPlayerAnimationGroup(TestCase):

    def setUp(self):
        self.image_set = copy.deepcopy(PLAYER_MAGE_ANIMATION_SETS)
        self.expected_image_set = [
            '/Users/pooch/PycharmProjects/Garbage/resources/graphics/player/mage/walking/down/down3.png',
            '/Users/pooch/PycharmProjects/Garbage/resources/graphics/player/mage/walking/down/down2.png',
            '/Users/pooch/PycharmProjects/Garbage/resources/graphics/player/mage/walking/down/down1.png',
            '/Users/pooch/PycharmProjects/Garbage/resources/graphics/player/mage/walking/down/down4.png'
        ]

    def test_create_player_animation_group(self, mock_timer):
        pag = PlayerAnimationGroup()

    def test_load_animation_sets(self, mock_timer):
        pag = PlayerAnimationGroup()
        pag.load_animation_sets(self.image_set)

    def test_change_current_set(self, mock_timer):
        pag = PlayerAnimationGroup()
        pag.load_animation_sets(self.image_set)

        pag.change_current_set(PlayerActions.WALKING, Direction.DOWN)
        assert pag.current_animation_set.image_set == self.expected_image_set
