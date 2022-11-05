import pygame

from gamestate.loop.loop import Loop

from events import listen


class MenuLoop(Loop):
    def __init__(self):
        super().__init__()
        self.load_assets()
        self.can_interact = False

    def draw(self):
        """Draw the assets associated with the menu."""
        self.menu.draw_background()
        self.menu.draw_text_sprites()
        self.menu.draw_button_sprites()

    def load_assets(self):
        """Load the particular assets for the menu"""
        pass

    def update(self):
        pygame.display.update()

    def run(self):
        """ "Run the menu."""
        self.time_since_loop_started = pygame.time.get_ticks()
        self.running = True
        while self.running:
            self.cooldown()
            self.event_loop()
            self.update()
            self.draw()

    def cooldown(self):
        """Handle the cooldown for interacting with the menu."""
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time_since_loop_started

        if delta_time >= 500:
            self.can_interact = True

    def event_loop(self):
        """Handle events for the menu."""
        listen.event_loop()

        if self.can_interact:
            self.menu.check_events()
