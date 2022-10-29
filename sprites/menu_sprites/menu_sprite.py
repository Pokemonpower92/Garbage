from typing import Dict, Any

import pygame


class MenuSprite(pygame.sprite.Sprite):
    """Menu sprites are any sprite that
    menus require to function. Cosmetic
    sprites are seperate.
    """

    def __init__(self):
        pass

    def load_content(self):
        """Load the resources for the sprite."""
        pass

    def update(self):
        """Update the sprite."""
        pass

    def check_mouseover(self):
        """Check for a mouseover event."""
        pass
