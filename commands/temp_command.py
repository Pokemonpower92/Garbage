from commands.command import Command


class TempCommand(Command):
    """
    This command serves as a temporary command for buttons with no implementation.
    """

    def execute(self) -> None:
        """
        Run the loop.
        @return: None
        """
        pass
