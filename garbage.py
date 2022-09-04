import pygame
from sys import exit
import os


from config import constants, level_data
from sprites.player_sprite import PlayerSprite
from level import Level
from utils import setup
from events import listen


class Game:
    def __init__(self):
        """Initialize the game."""

        pygame.init()

        self.screen = setup.setup_window(
            constants.WINDOW_DIMENSIONS,
            constants.WINDOW_TITLE,
        )

        self.clock = pygame.time.Clock()

    def new(self):
        """Initialize everything we need for a new game."""
        self.load_assets()

    def run(self):
        """Main game loop"""

        self.game_running = True
        while self.game_running:
            self.clock.tick(constants.FPS)
            listen.event_loop(self)
            self.player.get_input()
            self.update()
            self.draw()

    def quit(self):
        """Quit the game."""

        pygame.quit()
        exit()

    def update(self):
        """Update all the objects."""

        for s in self.level.all_sprites:
            s.update()

    def draw_grid(self):
        """Draw the grid."""

        w = constants.WINDOW_DIMENSIONS[0]
        h = constants.WINDOW_DIMENSIONS[1]
        ts = constants.TILE_SIZE

        for x in range(0, w, ts):
            pygame.draw.line(self.screen, constants.GRID_COLOR, (x, 0), (x, h))
        for y in range(0, h, ts):
            pygame.draw.line(self.screen, constants.GRID_COLOR, (0, y), (w, y))

    def draw(self):
        """Draw our sprites."""

        self.screen.fill(constants.BACKGROUND_COLOR)
        self.draw_grid()
        self.level.all_sprites.custom_draw(self.player)
        pygame.display.update()

    def load_assets(self):
        """Load the player, walls, enemies, pickups."""
        self.level = Level(self, level_data.LEVEL_0)
        self.player = PlayerSprite(self.level)

        self.level.load_level()

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
