import pygame

from gamestate.level.level import Level
from gamestate.loop import loop
from gamestate.loop.pause_menu_loop import PauseMenuLoop

from config import game_constants, level_data
from sprites.player_sprites.player_mage_sprite import PlayerMageSprite
from events import listen


class GameLoop(loop.Loop):
    def __init__(self):
        super().__init__()
        self.load_assets()
        self.time_unpaused = 0

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(game_constants.FPS)
            self.event_loop()
            self.player.get_input()
            self.update()
            self.draw()

    def event_loop(self):
        listen.event_loop()

        self.time_before_pause = pygame.time.get_ticks()
        delta_time = self.time_before_pause - self.time_unpaused

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_ESCAPE] and delta_time >= 500:
            PauseMenuLoop().run()
            self.time_unpaused = pygame.time.get_ticks()

    def update(self):
        for s in self.level.all_sprites:
            s.update()

    def draw(self):
        self.screen.fill(game_constants.BACKGROUND_COLOR)
        self.level.all_sprites.custom_draw(self.player)
        pygame.display.update()

    def load_assets(self):
        """Load the player and level."""
        self.level = Level(self, level_data.LEVEL_0)
        self.player = PlayerMageSprite(self.level)

        self.level.load_level()
