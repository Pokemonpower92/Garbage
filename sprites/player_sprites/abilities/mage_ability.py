import pygame
from .ability import Ability
from ..attack_sprites import mage_attack_sprite


class FaireFire(Ability):
    def __init__(self, player):
        super().__init__(player)

    def cast(self):
        print("Casting Faire Fire")
        mage_attack_sprite.FaireFireSprite(
            self.player.level,
            self.player.facing,
            self.player.rect.x,
            self.player.rect.y,
        )

        self.time_since_last_cast = pygame.time.get_ticks()
        self.can_cast = False

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time_since_last_cast
        if delta_time >= self.player.constants["PLAYER_ATTACK_COOLDOWN"]:
            self.can_cast = True


class Concentration(Ability):
    def __init__(self, player):
        super().__init__(player)

    def cast(self):
        print("Casting Concentration")

    def cooldown(self):
        pass


class Teleport(Ability):
    def __init__(self, player):
        super().__init__(player)

    def cast(self):
        print("Casting Teleport")

    def cooldown(self):
        pass
