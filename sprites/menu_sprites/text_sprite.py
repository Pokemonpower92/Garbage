from __future__ import annotations
from typing import Dict, Any, Optional

import pygame

from sprites.menu_sprites import menu_sprite
import gamestate


class TextSprite(menu_sprite.MenuSprite):
    def __init__(self, content: Dict[str, Any]) -> None:
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.position = None
        self.content_rect = None
        self.font = None

        self.content = self.set_content(content)

    def set_content(self, content: Dict[str, Any]) -> pygame.font:
        """
        Set the sprite's content.
        @param content: The content to set.
        @return: TextSprite
        """
        self.font = pygame.font.SysFont(content["font"][0], content["font"][1])
        self.content = self.font.render(content["text"], 1, content["color"])
        self.content_rect = self.content.get_rect()

        self.position = content["position"]

        return self.content

    def update(self) -> None:
        """Update the sprite."""
        pass

    def check_mouseover(self) -> None:
        """Check for a mouseover event."""
        pass
