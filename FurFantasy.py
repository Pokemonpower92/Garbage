import pygame
from sys import exit
import os


from config import constants, environment_resource_paths
from sprites.player import PlayerSprite
from setup import setup_help
from events import listen


class Game:
    def __init__(self):
        """Initialize the game."""

        pygame.init()

        self.screen = setup_help.setup_window(
            constants.WINDOW_DIMENSIONS,
            constants.WINDOW_TITLE,
        )
        self.clock = pygame.time.Clock()

    def new(self):
        """Initialize everything we need for a new game."""

        self.all_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()
        self.player = PlayerSprite.PlayerSprite(self)

    def run(self):
        """Main game loop"""
        self.game_running = True
        while self.game_running:
            self.dt = self.clock.tick(constants.FPS) / 1000
            listen.event_loop(self)
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        exit()

    def update(self):
        for s in self.all_sprites:
            s.update()

    def draw_grid(self):
        w = constants.WINDOW_DIMENSIONS[0]
        h = constants.WINDOW_DIMENSIONS[1]
        ts = constants.TILE_SIZE

        for x in range(0, w, ts):
            pygame.draw.line(self.screen, "Grey", (x, 0), (x, h))
        for y in range(0, h, ts):
            pygame.draw.line(self.screen, "Grey", (0, y), (w, y))

    def draw(self):
        self.screen.fill("White")
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.update()

    def show_start_screen(self):
        pass

    def show_main_menu(self):
        pass

    def show_pause_screen(self):
        pass


if __name__ == "__main__":
    ff = Game()
    ff.show_start_screen()

    # Run the main game loop.
    while True:
        ff.new()
        ff.run()
