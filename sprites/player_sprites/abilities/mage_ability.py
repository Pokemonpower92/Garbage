import pygame
from .ability import Ability
from ..attack_sprites import mage_attack_sprite


class FaireFire(Ability):
    """Faire Fire is the player mage class's damaging ability.
    It hits for high alpha, and has a long cooldown.
    """

    def __init__(self, player):
        super().__init__(player)

    def cast(self):
        print("Casting Faire Fire")

        mage_attack_sprite.FaireFireSprite(
            self.player.level,
            self.player.facing,
            self.player.faire_fire_actual_damage,
            self.player.rect.x,
            self.player.rect.y,
        )

        # Just always reset faire_fire_damage.
        self.player.faire_fire_actual_damage = self.player.faire_fire_base_damage

        self.time_since_last_cast = pygame.time.get_ticks()
        self.can_cast = False

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time_since_last_cast
        if delta_time >= self.player.constants["FAIRE_FIRE_COOLDOWN"]:
            self.can_cast = True


class Concentration(Ability):
    """Concentration boosts the damage of the mage's
    next cast faire fire.
    """

    def __init__(self, player):
        super().__init__(player)

    def cast(self):
        print("Casting Concentration")

        # Right now the mage can concentrate as many times
        # as they want between casts of Faire Fire.
        self.player.faire_fire_actual_damage *= (
            self.player.concentration_damage_modifier
        )
        self.time_since_last_cast = pygame.time.get_ticks()
        self.can_cast = False

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time_since_last_cast
        if delta_time >= self.player.constants["CONCENTRATION_COOLDOWN"]:
            self.can_cast = True


class Teleport(Ability):
    def __init__(self, player):
        super().__init__(player)

    def cast(self):
        destination = self.player.direction * self.player.constants["TELEPORT_VELOCITY"]
        self.player.move(destination.x, destination.y)
        self.time_since_last_cast = pygame.time.get_ticks()
        self.can_cast = False


    def cooldown(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time_since_last_cast
        if delta_time >= self.player.constants["TELEPORT_COOLDOWN"]:
            self.can_cast = True
