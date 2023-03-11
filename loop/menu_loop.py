import pygame

import utils.setup
from loop.loop import Loop

from events import listen


class MenuLoop(Loop):
    """Menu loops run when menus are evoked. Each should implement its own assets class to load."""

    def __init__(self):
        super().__init__()

    def draw(self, screen: pygame.Surface):
        """Draw the assets associated with the assets."""
        self.assets.draw_background(screen)
        self.assets.draw_text_sprites(screen)
        self.assets.draw_button_sprites(screen)

    def load_assets(self):
        """Load the particular assets for the assets"""
        pass

    def update(self):
        """Update the display."""
        pygame.display.update()

    def run(self):
        """Run the assets."""
        self.time_since_loop_started = pygame.time.get_ticks()
        self.running = True
        while self.running:
            self.event_loop()
            self.update()
            self.draw(utils.setup.Window().get_window())

    def event_loop(self):
        """Handle events for the loop."""

        # Listen for top-level events like closing the window.
        listen.event_loop()
        # Check events associated with all assets.
        self.assets.check_events()

    def can_interact(self):
        """Internal cooldown for interacting with menus."""
        delta_time = pygame.time.get_ticks() - self.time_since_loop_started
        return delta_time > 500
