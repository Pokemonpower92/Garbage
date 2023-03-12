import pygame
from config import game_constants


class globalTimers:
    """Here's the global cooldown singleton."""

    _instance = None

    def __init__(self):
        if globalTimers._instance:
            raise Exception("Cannot instantiate multiple globalTimers")
        else:
            globalTimers._instance = self
            self.globalCooldowns = globalCooldowns()

    @staticmethod
    def get_instance():
        if not globalTimers._instance:
            globalTimers()
        return globalTimers._instance

    def check_button_cooldown(self):
        return self.globalCooldowns.check_buttons()

    def set_button_timer(self):
        self.globalCooldowns.set_button_timer()

    def get_button_time(self):
        self.globalCooldowns.get_button_time()

    def check_animation_cooldown(self):
        return self.globalCooldowns.check_animation()

    def set_animation_timer(self):
        self.globalCooldowns.set_animation_timer()

    def get_animation_time(self):
        self.globalCooldowns.get_animation_time()


class globalCooldowns:
    def __init__(self):
        self.buttonClickTime = genericTimer()
        self.animationTime = genericTimer()

    def check_buttons(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.buttonClickTime.get_time()

        return delta_time > game_constants.MENU_BUTTON_COOLDOWN

    def check_animation(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.animationTime.get_time()

        return delta_time > game_constants.ANIMATION_SPEED

    def set_button_timer(self):
        self.buttonClickTime.set_time()

    def set_animation_timer(self):
        self.animationTime.set_time()

    def get_button_time(self):
        return self.buttonClickTime.get_time()

    def get_animation_time(self):
        return self.animationTime.get_time()


class genericTimer:
    def __init__(self):
        self.timeSince = pygame.time.get_ticks()

    def set_time(self):
        self.timeSince = pygame.time.get_ticks()

    def get_time(self):
        return self.timeSince
