import pygame

from config import menu_data
from events import listen

from gamestate.loop.menu_loop import MenuLoop
from gamestate.loop.main_menu_loop import MainMenuLoop
from gamestate.menu.menu import Menu


class TitleScreenLoop(MenuLoop):
    def __init__(self):
        super().__init__()

    def load_assets(self):
        self.menu = Menu(self.screen, menu_data.TITLE_SCREEN)

    def event_loop(self):
        listen.event_loop()

        if self.can_interact:
            self.menu.check_events()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_RETURN]:
                MainMenuLoop().run()
