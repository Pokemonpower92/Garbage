from typing import Dict, Any, Optional

import pygame

from sprites.menu_sprites import menu_sprite
import gamestate


class TextSprite(menu_sprite.MenuSprite):
    def __init__(self, menu) -> None:
        super().__init__()

        self.menu = menu

        self.groups = self.menu.text_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

    def load_content(self, values) -> None:
        """Load the resources for the sprite.
        :return: void
        """
        self.font = pygame.font.SysFont(values["font"][0], values["font"][1])
        self.content = self.font.render(values["text"], 1, values["color"])
        self.content_rect = self.content.get_rect()

        self.position = values["position"]

    def update(self) -> None:
        """Update the sprite."""
        pass

    def check_mouseover(self) -> None:
        """Check for a mouseover event."""
        pass
