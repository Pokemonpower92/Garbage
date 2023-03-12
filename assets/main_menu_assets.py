from assetdata.menus import buttons
from assets.assets import Assets
from commands.new_game_command import NewGameCommand


class MainMenuAssets(Assets):
    def __init__(self):
        super().__init__()

    def load_assets(self):
        # Load all the buttons.
        new_game_button = self.sprite_factory.create_menu_sprite("button")
        new_game_button.load_content(buttons.NEW_GAME_BUTTON)
        new_game_button.set_command(NewGameCommand())
        #self.button_sprites.add(new_game_button)

    def check_events(self):
        for button in self.button_sprites:
            button.update()
