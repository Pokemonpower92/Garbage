from abc import abstractclassmethod
import pygame
from config import game_constants, player_constants, resource_paths


class PlayerSprite(pygame.sprite.Sprite):
    """Base class for the player sprites.
    PlayerMageSprite, PlayerRogueSprite, ect must implement all passed methods.

    """

    def __init__(
        self, level, x=game_constants.PLAYER_START_X, y=game_constants.PLAYER_START_Y
    ):
        self.level = level
        self.groups = self.level.all_sprites
        self.image = pygame.image.load(resource_paths.TEST_PLAYER)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit_box = self.rect.inflate(0, -26)

        pygame.sprite.Sprite.__init__(self, self.groups)

        # Movement.
        self.direction = pygame.math.Vector2(x=0, y=0)
        self.facing = pygame.math.Vector2(x=0, y=0)

    def load_resources(self):
        """Load the resources for the sprite. Child classes must implement this."""
        pass

    def get_input(self):
        """Get the input for the player."""

        pressed_keys = pygame.key.get_pressed()

        # ABILITIES
        ## Ability 1
        if pressed_keys[pygame.K_SPACE] and self.ability_one.can_cast:
            self.ability_one.cast()

        ## Ability 2
        if pressed_keys[pygame.K_RETURN] and self.ability_two.can_cast:
            self.ability_two.cast()

        ## Ability 3
        if pressed_keys[pygame.K_RSHIFT]:
            self.ability_three.cast()

        # Player moving up/down.
        if pressed_keys[pygame.K_w]:
            self.direction.y = -1
            self.facing.y = -1
            self.facing.x = 0
        elif pressed_keys[pygame.K_s]:
            self.direction.y = 1
            self.facing.y = 1
            self.facing.x = 0
        else:
            self.direction.y = 0

        # Player moving left/right.
        if pressed_keys[pygame.K_d]:
            self.direction.x = 1
            self.facing.x = 1
            self.facing.y = 0
        elif pressed_keys[pygame.K_a]:
            self.direction.x = -1
            self.facing.x = -1
            self.facing.y = 0
        else:
            self.direction.x = 0

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.direction *= self.velocity

        pygame.event.pump()

    def cooldowns(self):
        """Tracks cooldowns for the player."""
        self.ability_one.cooldown()
        self.ability_two.cooldown()
        self.ability_three.cooldown()

    def move(self, dx: int, dy: int):
        """Move the player by dx and dy"""

        self.hit_box.x += dx
        self.check_wall_collision("x")
        self.hit_box.y += dy
        self.check_wall_collision("y")

        self.rect.center = self.hit_box.center

    def check_wall_collision(self, axis):
        """Check if player collides with a wall at a given dx and dy"""

        for wall in self.level.wall_sprites:
            if wall.rect.colliderect(self.hit_box):
                if axis == "x":
                    if self.direction.x > 0:
                        self.hit_box.right = wall.rect.left

                    elif self.direction.x < 0:
                        self.hit_box.left = wall.rect.right

                if axis == "y":
                    if self.direction.y > 0:
                        self.hit_box.bottom = wall.rect.top

                    elif self.direction.y < 0:
                        self.hit_box.top = wall.rect.bottom

    def handle_attack_collison(self, attack):
        print(f"I was hit! for {attack.damage} damage.")

    def update(self):
        self.get_input()
        self.cooldowns()
        self.move(self.direction.x, self.direction.y)
