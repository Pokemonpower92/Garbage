import unittest
import pygame
import logging

from assets.main_menu_assets import MainMenuAssets
from unittest.mock import patch


@patch("pygame.display")
class TestMainMenuAssets(unittest.TestCase):

    def setUp(self) -> None:
        pygame.init()

    def test_create_asset(self, mock_pytest):
        asset = MainMenuAssets()
        assert asset


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
