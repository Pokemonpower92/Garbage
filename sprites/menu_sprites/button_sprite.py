from typing import Dict, Any

import pygame
from sprites.menu_sprites import menu_sprite
import gamestate


class ButtonSprite(menu_sprite.MenuSprite):
    def __init__(self, menu):
        self.menu = menu

        self.groups = self.menu.button_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.contentFactory = ButtonSpriteContentFactory()

    def load_content(self, values):
        """Load the resources for the sprite."""
        self.content = self.contentFactory.create_button_sprite_content(values)

    def draw(self):
        """Draw the button's content"""
        self.content.draw_content(self.menu.screen)

    def update(self):
        """Update the sprite."""
        pass

    def check_mouseover(self):
        """Check for a mouseover event."""
        pass


class ButtonSpriteContentFactory:
    def create_button_sprite_content(self, values):

        if values["type"] == "text":
            return TextContent(values)
        elif values["type"] == "icon":
            return IconContent(values)
        else:
            pass


class TextContent:
    def __init__(self, values):
        self.width = values["dimensions"][0]
        self.height = values["dimensions"][1]
        self.color = values["color"]
        self.text = values["text"]

        self.button_rect = pygame.Rect(0, 0, self.width, self.height)
        self.button_rect.center = values["position"]

        self.font = pygame.font.SysFont(values["font"][0], values["font"][1])
        self.text = self.font.render(values["text"], 1, values["text_color"])
        self.text_rect = self.text.get_rect()
        self.text_rect.center = values["position"]

    def draw_content(self, screen):
        pygame.draw.rect(screen, self.color, self.button_rect)
        screen.blit(self.text, self.text_rect.topleft)


class IconContent:
    def __init__(self, values):
        self.values = values

    def draw_content(self, scale):
        return self.content
