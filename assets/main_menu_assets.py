from assets.assets import Assets
from loop import game_loop


class MainMenuAssets(Assets):
    def __init__(self, menu_data):
        super().__init__(menu_data)

    def check_events(self):
        for sprite in self.button_sprites:
            clicked, button = sprite.check_mouse_event()

            if clicked:
                if button == "new_game_button":
                    game_loop.GameLoop().start_new_game()
