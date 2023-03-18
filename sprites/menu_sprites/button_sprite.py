from __future__ import annotations
from typing import Dict, Any
import pygame

from commands.command import Command
from sprites.menu_sprites import menu_sprite
from gamestate.globalTimers.globalTimers import globalTimers


class ButtonSprite(menu_sprite.MenuSprite):
    def __init__(self, content, command):
        pygame.sprite.Sprite.__init__(self)
        self.contentFactory = ButtonSpriteContentFactory()
        self._content = self.set_content(content)
        self._command = self.set_command(command)
        self.mouseover = False
        self.clicked = False

    def _check_mouse_event(self):
        """Check for a mouse events."""
        mouse_pos = pygame.mouse.get_pos()

        if self._content.button_rect.collidepoint(mouse_pos):
            self.mouseover = True
            if pygame.mouse.get_pressed()[0]:
                if globalTimers.get_instance().check_button_cooldown():
                    self.clicked = True
                    self._press_button()
                    globalTimers.get_instance().set_button_timer()
        else:
            self.mouseover = False
            self.clicked = False

    def _press_button(self):
        """
        Execute the command associated with the button.
        @return: None
        """
        self._command.execute()

    def set_content(self, content: Dict[str, Any]) -> ButtonContent:
        """
        Set the button's content.
        @param content: The content to set.
        @return: ButtonSprite
        """
        self._content = self.contentFactory.create_button_sprite_content(content)
        return self._content

    def set_command(self, command: Command) -> ButtonSprite:
        """
        Sets the button's command.
        @param command: ButtonCommand: The command to be executed when pressed.
        @return: None
        """
        self._command = command
        return self._command

    def draw(self, screen: pygame.Surface):
        """Draw the button's content"""
        self._content.draw_content(screen, self.mouseover)

    def update(self):
        """Update the sprite."""
        self._check_mouse_event()


class ButtonSpriteContentFactory:
    def create_button_sprite_content(self, values):

        if values["type"] == "text":
            return TextContent(values)
        elif values["type"] == "icon":
            return IconContent(values)
        else:
            pass


class ButtonContent:

    def draw_content(self) -> None:
        """
        Draw the content.
        @return: None
        """

class TextContent(ButtonContent):
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


class IconContent(ButtonContent):
    def __init__(self, values):
        self.values = values

    def draw_content(self, scale):
        return self.content
