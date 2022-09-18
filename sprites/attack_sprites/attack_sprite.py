import pygame
from config import game_constants, resource_paths


class AttackSprite(pygame.sprite.Sprite):
    def __init__(self, level, x: int = 0, y: int = 0):
        self.level = level
        self.load_resources()
        self.groups = self.level.all_sprites, self.level.attack_sprites
        self.rect.x = x
        self.rect.y = y
        self.hit_box = self.rect.inflate(0, -26)

        pygame.sprite.Sprite.__init__(self, self.groups)

    def move(self):
        """Move the attack."""
        pass

    def load_resources(self):
        pass

    def check_collisions(self, axis):
        """Check if attack collides with an entity"""

        for sprite in self.level.wall_sprites:
            if sprite.rect.colliderect(self.hit_box):
                self.kill()

        for sprite in self.level.entity_sprites:
            if sprite.rect.colliderect(self.hit_box):
                if axis == "x":
                    # Moving right.
                    if self.direction.x > 0:
                        self.hit_box.right = sprite.rect.left

                    elif self.direction.x < 0:
                        self.hit_box.left = sprite.rect.right

                if axis == "y":
                    if self.direction.y > 0:
                        self.hit_box.bottom = sprite.rect.top

                    elif self.direction.y < 0:
                        self.hit_box.top = sprite.rect.bottom

                print("It's a hit!")
                self.kill()

    def update(self):
        """Update the attack sprite."""
        self.move()
