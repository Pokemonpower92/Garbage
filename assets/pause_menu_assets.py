import assetdata.menus.pause_menu_buttons as buttons
from assets.assets import Assets
from commands.exit_game_command import ExitGameCommand
from sprites.menu_sprites.button_sprite import ButtonSprite


class PauseMenuAssets(Assets):
    def __init__(self):
        super().__init__()

    def load_assets(self):
        # Load all the buttons.
        exit_game_button = ButtonSprite(buttons.EXIT_GAME_BUTTON, ExitGameCommand)
        exit_game_button.set_command(ExitGameCommand())
        self.button_sprites.add(exit_game_button)

    def check_events(self):
        for sprite in self.button_sprites:
            for button in self.button_sprites:
                button.update()
