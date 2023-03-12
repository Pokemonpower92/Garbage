import pygame

from config import resource_paths
from sprites.menu_sprites import menu_sprite_factory


class Assets:
    def __init__(self):
        self.sprite_factory = menu_sprite_factory.MenuSpriteFactory()

        # Create all the sprites for the assets.
        self.button_sprites = ButtonSpriteGroup()
        self.text_sprites = TextSpriteGroup()
        self.background_surface = pygame.image.load(resource_paths.TITLE_SCREEN)
        self.load_assets()

    def load_assets(self):
        """Loads the assets and creates all the sprites."""
        pass

    def draw_background(self, screen: pygame.Surface) -> None:
        """
        Blits the background image to the specified screen.
        @param screen: pygame.Surface: the surface to draw to.
        @return: None
        """
        screen.blit(self.background_surface, [0, 0])

    def draw_text_sprites(self, screen: pygame.Surface) -> None:
        """Draws any text sprites for the assets."""
        self.text_sprites.custom_draw(screen)

    def draw_button_sprites(self, screen: pygame.Surface) -> None:
        """Draws any button sprites for the assets."""
        self.button_sprites.custom_draw(screen)


class TextSpriteGroup(pygame.sprite.Group):
    """TextSpriteGroup is a compendium of all text sprites in the assets."""
    def __init__(self):
        super().__init__()

    def custom_draw(self, screen: pygame.Surface) -> None:
        """
        Draws the test sprite to the specified screen.
        @param screen: pygame.Surface: the surface to draw to.
        @return: None
        """
        for sprite in self.sprites():
            screen.blit(sprite.content, sprite.position)


class ButtonSpriteGroup(pygame.sprite.Group):
    """ButtonSpriteGroup is a compendium of all button sprites in the assets."""
    def __init__(self):
        super().__init__()

    def custom_draw(self, screen: pygame.Surface):
        """
        Draw the button sprite.
        @return: None
        """
        for sprite in self.sprites():
            sprite.draw(screen)
