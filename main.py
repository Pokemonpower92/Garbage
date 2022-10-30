from gamestate.loop.title_screen_loop import TitleScreenLoop
import pygame

if __name__ == "__main__":
    pygame.init()
    tsl = TitleScreenLoop()

    tsl.run()
