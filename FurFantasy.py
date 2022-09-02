import pygame
from sys import exit
import os


from config import constants, resource_paths
from sprites.player.player_sprite import PlayerSprite
from tilemap import tilemap
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
        self.level = "a"

    def new(self):
        """Initialize everything we need for a new game."""
        self.load_assets()

    def run(self):
        """Main game loop"""

        self.game_running = True
        while self.game_running:
            self.dt = self.clock.tick(constants.FPS) / 1000
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

        for s in self.tilemap.all_sprites:
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
        self.tilemap.all_sprites.custom_draw(self.player)
        pygame.display.update()

    def load_assets(self):
        """Load the player, walls, enemies, pickups."""
        self.tilemap = tilemap.Tilemap(self)
        self.player = PlayerSprite(self.tilemap)
        self.tilemap.load_wall_map()

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
