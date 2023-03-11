import pygame

from events import listen

from loop.menu_loop import MenuLoop
from loop.main_menu_loop import MainMenuLoop
from assets.title_screen_assets import TitleScreenAssets


class TitleScreenLoop(MenuLoop):
    def __init__(self):
        super().__init__()
        self.load_assets()

    def load_assets(self):
        self.assets = TitleScreenAssets()

    def event_loop(self):
        listen.event_loop()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RETURN]:
            MainMenuLoop().run()
