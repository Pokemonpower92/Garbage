import pygame

from gamestate.loop.loop import Loop
from gamestate.globalTimers import globalTimers

from events import listen


class MenuLoop(Loop):
    """Menu loops run when menus are evoked. Each should implement its own menu class to load."""

    def __init__(self):
        super().__init__()

    def draw(self):
        """Draw the assets associated with the menu."""
        self.menu.draw_background()
        self.menu.draw_text_sprites()
        self.menu.draw_button_sprites()

    def load_assets(self):
        """Load the particular assets for the menu"""
        pass

    def update(self):
        """Update the display."""
        pygame.display.update()

    def run(self):
        """ "Run the menu."""
        self.time_since_loop_started = pygame.time.get_ticks()
        self.running = True
        while self.running:
            self.event_loop()
            self.update()
            self.draw()

    def event_loop(self):
        """Handle events for the menu."""
        listen.event_loop()
        self.menu.check_events()

    def can_interact(self):
        delta_time = pygame.time.get_ticks() - self.time_since_loop_started

        return delta_time > 500
