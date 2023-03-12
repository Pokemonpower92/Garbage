import unittest
import pygame
import logging

from assets.pause_menu_assets import PauseMenuAssets


class TestPauseMenuAssets(unittest.TestCase):

    def setUp(self) -> None:
        pygame.init()

    def test_create_asset(self):
        asset = PauseMenuAssets()
        assert asset


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
