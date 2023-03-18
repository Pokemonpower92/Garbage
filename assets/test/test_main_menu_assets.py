import unittest
from unittest.mock import patch

import pygame
import logging

from assets.main_menu_assets import MainMenuAssets

@patch("pygame.display")
@patch("pygame.mouse.get_pos", return_value=(0,0))
class TestMainMenuAssets(unittest.TestCase):

    def setUp(self) -> None:
        pygame.init()

    def test_create_asset(self, mock_display, mock_mouse):
        asset = MainMenuAssets()
        assert asset

    def test_load_assets(self, mock_display, mock_mouse):
        asset = MainMenuAssets()
        asset.load_assets()

    def test_check_events(self, mock_display, mock_mouse):
        asset = MainMenuAssets()
        asset.load_assets()
        asset.check_events()

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
