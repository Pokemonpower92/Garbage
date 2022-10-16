from gamestate import gamestate
import pygame

if __name__ == "__main__":
    pygame.init()
    gs = gamestate.Gamestate()
    gs.run_title_screen()
