from assets.assets import Assets
from assetdata.menus.texts import TITLE_SCREEN_MESSAGE
from sprites.menu_sprites.menu_sprite_factory import MenuSpriteFactory

class TitleScreenAssets(Assets):
    def __init__(self):
        super().__init__()

    def load_assets(self):
        message = self.sprite_factory.create_menu_sprite("text")
        message.load_content(TITLE_SCREEN_MESSAGE)
        self.text_sprites.add(message)

    def check_events(self):
        for sprite in self.button_sprites:
            for button in self.button_sprites:
                button.update()
