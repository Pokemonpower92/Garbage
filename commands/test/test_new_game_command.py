from commands.new_game_command import NewGameCommand
from unittest.mock import patch
import unittest


class TestNewGameCommand(unittest.TestCase):

    @patch("commands.new_game_command.GameLoop.start_new_game")
    @patch("pygame.display")
    def test_execute(self, mock_pygame, mock_start_new_game):
        """
        Test if start_new_game() is called when execute() is.
        @return: None
        """
        command = NewGameCommand()
        command.execute()
        self.assertTrue(mock_start_new_game.called)
