from typing import Dict, Any, Optional

import pygame

from sprites.menu_sprites import menu_sprite
import gamestate


class TextSprite(menu_sprite.MenuSprite):
    def __init__(self, menu, values) -> None:
        super().__init__()

        self.menu = menu

        self.groups = (self.menu.all_sprites, self.menu.text_sprites)
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.values = values

        self.load_content()

    def load_content(self) -> None:
        """Load the resources for the sprite.
        :return: void
        """
        self.font = pygame.font.SysFont(self.values["font"][0], self.values["font"][1])
        self.content = self.font.render(self.values["text"], 1, self.values["color"])
        self.content_rect = self.content.get_rect()

        self.position = self.values["position"]

    def update(self) -> None:
        """Update the sprite."""
        pass

    def check_mouseover(self) -> None:
        """Check for a mouseover event."""
        pass
