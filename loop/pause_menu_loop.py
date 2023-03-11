import pygame

from events import listen

from loop.menu_loop import MenuLoop
from assets.pause_menu_assets import PauseMenuAssets


class PauseMenuLoop(MenuLoop):
    def __init__(self, game_loop):
        super().__init__()
        self.game_loop = game_loop
        self.load_assets()

    def load_assets(self):
        self.assets = PauseMenuAssets()

    def event_loop(self):
        listen.event_loop()

        if self.can_interact():
            self.assets.check_events()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_p]:
                self.running = False
