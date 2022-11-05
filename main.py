from gamestate.loop.title_screen_loop import TitleScreenLoop
from gamestate.loop.pause_menu_loop import PauseMenuLoop
from gamestate.loop.main_menu_loop import MainMenuLoop
import pygame

if __name__ == "__main__":
    pygame.init()
    MainMenuLoop().run()
