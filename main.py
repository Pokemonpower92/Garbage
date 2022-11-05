from gamestate.loop.title_screen_loop import TitleScreenLoop
from gamestate.loop.pause_menu_loop import PauseMenuLoop
import pygame

if __name__ == "__main__":
    pygame.init()
    TitleScreenLoop().run()
