from assetdata.menus import buttons
from assets.assets import Assets
from commands.new_game_command import NewGameCommand
from sprites.menu_sprites.button_sprite import ButtonSprite


class MainMenuAssets(Assets):
    def __init__(self):
        super().__init__()

    def load_assets(self) -> None:
        """
        Load the assets.
        @return: None
        """
        new_game_button = ButtonSprite(buttons.NEW_GAME_BUTTON, NewGameCommand())
        self.button_sprites.add(new_game_button)

    def check_events(self) -> None:
        """
        Check for events in the sprites.
        @return: None
        """
        for button in self.button_sprites:
            button.update()
