import pygame
from sys import exit
import os


from config import game_constants, level_data
from sprites.player_sprites.player_mage_sprite import PlayerMageSprite
from gamestate.level.level import Level
from events import listen
from . import loop


class GameLoop(loop.Loop):
    def __init__(self, gamestate):
        """Initialize the game."""
        super().__init__(gamestate)

        self.new()

    def new(self):
        """Initialize everything we need for a new game."""
        self.load_assets()

    def run(self):
        """Main game loop"""

        self.running = True
        while self.running:
            self.clock.tick(game_constants.FPS)
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

        w = game_constants.WINDOW_DIMENSIONS[0]
        h = game_constants.WINDOW_DIMENSIONS[1]
        ts = game_constants.TILE_SIZE

        for x in range(0, w, ts):
            pygame.draw.line(self.screen, game_constants.GRID_COLOR, (x, 0), (x, h))
        for y in range(0, h, ts):
            pygame.draw.line(self.screen, game_constants.GRID_COLOR, (0, y), (w, y))

    def draw(self):
        """Draw our sprites."""

        self.screen.fill(game_constants.BACKGROUND_COLOR)
        self.draw_grid()
        self.level.all_sprites.custom_draw(self.player)
        pygame.display.update()

    def load_assets(self):
        """Load the player and level."""
        self.level = Level(self, level_data.LEVEL_0)
        self.player = PlayerMageSprite(self.level)

        self.level.load_level()

    def show_start_screen(self):
        pass

    def show_main_menu(self):
        pass

    def show_pause_screen(self):
        pass
