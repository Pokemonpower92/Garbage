from commands.run_loop_command import RunLoopCommand
from unittest.mock import patch
import unittest


class MockLoop:

    def run(self):
        assert True

class TestNewGameCommand(unittest.TestCase):

    def test_execute(self):
        """
        Test if the loop's run method is called.
        @return: None
        """
        command = RunLoopCommand(MockLoop())
        command.execute()
