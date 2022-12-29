import pygame


class globalTimers:
    """Here's the global cooldown singleton."""

    _instance = None

    def __init__(self):
        if globalTimers._instance:
            raise Exception("Cannot instantiate mulitple globalTimers")
        else:
            globalTimers._instance = self
            self.buttons = globalCooldowns()

    @staticmethod
    def get_instance():
        if not globalTimers._instance:
            globalTimers()
        return globalTimers._instance

    def check_button_cooldown(self):
        return self.buttons.check_buttons()

    def set_button_timer(self):
        self.buttons.set_button_timer()

    def get_button_time(self):
        self.buttons.get_button_time()


class globalCooldowns:
    def __init__(self):
        self.buttonClickTime = buttonClickTime()

    def check_buttons(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.buttonClickTime.get_time()

        return delta_time > 500

    def set_button_timer(self):
        self.buttonClickTime.set_time()

    def get_button_time(self):
        return self.buttonClickTime.get_time()


class buttonClickTime:
    def __init__(self):
        self.timeSinceLastClick = pygame.time.get_ticks()

    def set_time(self):
        self.timeSinceLastClick = pygame.time.get_ticks()

    def get_time(self):
        return self.timeSinceLastClick
