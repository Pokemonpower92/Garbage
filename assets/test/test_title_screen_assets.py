from unittest.mock import patch

import unittest
import pygame
import logging

from assets.title_screen_assets import TitleScreenAssets

@patch("pygame.display")
class TestTitleScreenAssets(unittest.TestCase):

    def setUp(self) -> None:
        pygame.init()

    def test_create_asset(self, mock_pygame):
        asset = TitleScreenAssets()
        assert asset

    def test_load_assets(self, mock_pygame):
        asset = TitleScreenAssets()
        asset.load_assets()

    def test_check_events(self, mock_pygame):
        asset = TitleScreenAssets()
        asset.load_assets()
        asset.check_events()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
