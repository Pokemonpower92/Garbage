from commands.command import Command
import pygame
import sys


class ExitGameCommand(Command):
    """
    This command exits the program.
    """

    def execute(self) -> None:
        """
        Exit the program.
        @return: None
        """
        sys.exit()
