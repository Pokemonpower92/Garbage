from typing import Dict, Any

import pygame
from sprites.menu_sprites import menu_sprite
import gamestate


class ButtonSprite(menu_sprite.MenuSprite):
    def __init__(self, menu, values):
        self.menu = menu

        self.groups = (self.menu.all_sprites, self.menu.text_sprites)
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.values = values

    def load_content(self):
        """Load the resources for the sprite."""
        pass

    def update(self):
        """Update the sprite."""
        pass

    def check_mouseover(self):
        """Check for a mouseover event."""
        pass
