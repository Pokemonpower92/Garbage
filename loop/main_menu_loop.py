from loop.menu_loop import MenuLoop
from assets.main_menu_assets import MainMenuAssets

from config import menu_data
from events import listen


class MainMenuLoop(MenuLoop):
    def __init__(self):
        super().__init__()
        self.load_assets()

    def load_assets(self):
        self.assets = MainMenuAssets(menu_data.MAIN_MENU)

    def event_loop(self):
        listen.event_loop()
        self.assets.check_events()
