from commands.exit_game_command import ExitGameCommand
from unittest.mock import patch
import unittest


class TestNewGameCommand(unittest.TestCase):

    @patch("commands.exit_game_command.sys.exit")
    @patch("pygame.display")
    def test_execute(self, mock_pygame, mock_exit_game):
        """
        Test if start_new_game() is called when execute() is.
        @return: None
        """
        command = ExitGameCommand()
        command.execute()
        self.assertTrue(mock_exit_game.called)
