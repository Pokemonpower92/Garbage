from commands.command import Command
from loop.game_loop import GameLoop


class NewGameCommand(Command):
    """
    This command runs whatever loop is given.
    """
    def __init__(self):
        self._loop = GameLoop()

    def execute(self) -> None:
        """
        Run the loop.
        @return: None
        """
        self._loop.start_new_game()
