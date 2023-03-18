from assets.assets import Assets
from assetdata.menus.texts import TITLE_SCREEN_MESSAGE
from menu_sprites.text_sprite import TextSprite


class TitleScreenAssets(Assets):
    def __init__(self):
        super().__init__()

    def load_assets(self):
        message = TextSprite(TITLE_SCREEN_MESSAGE)
        self.text_sprites.add(message)

    def check_events(self):
        for sprite in self.button_sprites:
            for button in self.button_sprites:
                button.update()
