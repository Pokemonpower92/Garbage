from abc import abstractclassmethod
import pygame
from config import game_constants, resource_paths


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(
        self, tilemap, x=game_constants.PLAYER_START_X, y=game_constants.PLAYER_START_Y
    ):
        self.tilemap = tilemap
        self.groups = self.tilemap.all_sprites
        self.image = pygame.image.load(resource_paths.TEST_PLAYER)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit_box = self.rect.inflate(0, -26)

        pygame.sprite.Sprite.__init__(self, self.groups)

        # Movement.
        self.direction = pygame.math.Vector2(x=0, y=0)
        self.velocity = game_constants.PLAYER_WALK_SPEED
        self.sneaking = False
        self.sprinting = False

        # Abilities.
        self.attacking = False
        self.attack_cooldown = game_constants.PLAYER_ATTACK_COOLDOWN
        self.time_since_attack = 0

    def get_input(self):
        """Get the input for the player."""

        pressed_keys = pygame.key.get_pressed()

        # Player is attacking.
        if pressed_keys[pygame.K_SPACE]:
            self.attack()

        # Player moving up/down.
        if pressed_keys[pygame.K_w]:
            self.direction.y = -1
        elif pressed_keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # Player moving up/down.
        if pressed_keys[pygame.K_d]:
            self.direction.x = 1
        elif pressed_keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # Player is sprinting
        if pressed_keys[pygame.K_RETURN]:
            self.velocity = game_constants.PLAYER_RUN_SPEED
            self.sprinting = True
            self.sneaking = False

        # Player is sneaking
        elif pressed_keys[pygame.K_RSHIFT]:
            self.velocity = game_constants.PLAYER_SNEAK_SPEED
            self.sneaking = True

        # Player is walking normally
        else:
            self.velocity = game_constants.PLAYER_WALK_SPEED
            self.sprinting = False
            self.sneaking = False

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.direction *= self.velocity

        pygame.event.pump()

    def cooldowns(self):
        """Tracks cooldowns for the player."""
        pass

    def attack(self):
        """Performs an attack based on the class."""
        pass

    def move(self, dx: int, dy: int):
        """Move the player by dx and dy"""

        self.hit_box.x += dx
        self.check_wall_collision("x")
        self.hit_box.y += dy
        self.check_wall_collision("y")

        self.rect.center = self.hit_box.center

    def check_wall_collision(self, axis):
        """Check if player collides with a wall at a given dx and dy"""

        for wall in self.tilemap.wall_sprites:
            if wall.rect.colliderect(self.hit_box):
                if axis == "x":
                    # Moving right.
                    if self.direction.x > 0:
                        self.hit_box.right = wall.rect.left

                    elif self.direction.x < 0:
                        self.hit_box.left = wall.rect.right

                if axis == "y":
                    if self.direction.y > 0:
                        self.hit_box.bottom = wall.rect.top

                    elif self.direction.y < 0:
                        self.hit_box.top = wall.rect.bottom

    def update(self):
        self.get_input()
        self.cooldowns()
        self.move(self.direction.x, self.direction.y)
