from commands.command import Command


class RunLoopCommand(Command):
    """
    This command runs whatever loop is given.
    """

    def __init__(self, loop):
        self._loop = loop

    def execute(self) -> None:
        """
        Run the loop.
        @return: None
        """
        self._loop.run()
