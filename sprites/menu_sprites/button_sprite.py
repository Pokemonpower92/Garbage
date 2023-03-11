from typing import Dict, Any

import pygame
from sprites.menu_sprites import menu_sprite
from gamestate.globalTimers.globalTimers import globalTimers


class ButtonSprite(menu_sprite.MenuSprite):
    def __init__(self, menu):
        pygame.sprite.Sprite.__init__(self)
        self.contentFactory = ButtonSpriteContentFactory()

        self.mouseover = False
        self.clicked = False

    def load_content(self, values):
        """Load the resources for the sprite."""
        self.content = self.contentFactory.create_button_sprite_content(values)

    def draw(self, screen: pygame.Surface):
        """Draw the button's content"""
        self.content.draw_content(screen, self.mouseover)

    def update(self):
        """Update the sprite."""
        pass

    def check_mouse_event(self):
        """Check for a mouse events."""
        mouse_pos = pygame.mouse.get_pos()

        if self.content.button_rect.collidepoint(mouse_pos):
            self.mouseover = True
            if pygame.mouse.get_pressed()[0]:
                if globalTimers.get_instance().check_button_cooldown():
                    self.clicked = True
                    globalTimers.get_instance().set_button_timer()
        else:
            self.mouseover = False
            self.clicked = False

        return self.clicked, self.content.name


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
        """Unpack the button's content configuration from values. and set up the TextContent"""
        for name, value in values.items():
            setattr(self, name, value)

        self.width = self.dimensions[0]
        self.height = self.dimensions[1]

        self.button_rect = pygame.Rect(0, 0, self.width, self.height)
        self.button_rect.center = self.position

        self.font = pygame.font.SysFont(self.font[0], self.font[1])
        self.text_content = self.font.render(self.text, 1, self.text_color)
        self.text_rect = self.text_content.get_rect()
        self.text_rect.center = self.position

        self.hover_text_color = self.hover_text_color
        self.hover_color = self.hover_color
        self.border_radius = self.border_radius

    def draw_content(self, screen, mouseover):
        if mouseover:
            self.text_content = self.font.render(self.text, 1, self.hover_text_color)
            pygame.draw.rect(
                screen,
                self.hover_color,
                self.button_rect,
                border_radius=self.border_radius,
            )
            screen.blit(self.text_content, self.text_rect.topleft)
        else:
            self.text_content = self.font.render(self.text, 1, self.text_color)
            pygame.draw.rect(
                screen, self.color, self.button_rect, border_radius=self.border_radius
            )
            screen.blit(self.text_content, self.text_rect.topleft)


class IconContent:
    def __init__(self, values):
        self.values = values

    def draw_content(self, scale):
        return self.content
