from sprites.menu_sprites import text_sprite
from sprites.menu_sprites import button_sprite


class MenuSpriteFactory:
    def create_menu_sprite(self, sprite_type: str) -> None:
        """Simple factory method.

        :param sprite_type: The type of sprite to create.
        :return: None
        """

        if sprite_type == "text":
            return text_sprite.TextSprite()
        elif sprite_type == "button":
            return button_sprite.ButtonSprite()
        else:
            raise TypeError("No such assets spite type.")
