from curses import KEY_ENTER
import pygame
from config import constants


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, tilemap, x=constants.PLAYER_START_X, y=constants.PLAYER_START_Y):
        self.direction = pygame.math.Vector2(x=0, y=0)
        self.velocity = constants.PLAYER_WALK_SPEED
        self.sneaking = 0
        self.sprinting = 0

        self.tilemap = tilemap

        self.groups = self.tilemap.all_sprites
        self.image = pygame.Surface((constants.TILE_SIZE, constants.TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image.fill(constants.PLAYER_COLOR)

    def get_input(self):
        """Get the input for the player."""

        pressed_keys = pygame.key.get_pressed()

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
            self.velocity = constants.PLAYER_RUN_SPEED
        elif pressed_keys[pygame.K_RSHIFT]:
            self.velocity = constants.PLAYER_SNEAK_SPEED
        else:
            self.velocity = constants.PLAYER_WALK_SPEED

        self.direction *= self.velocity
        self.move(self.direction.x, self.direction.y)

    def move(self, dx: int, dy: int):
        """Move the player by dx and dy"""

        self.rect.x += dx
        self.check_wall_collision("x")
        self.rect.y += dy
        self.check_wall_collision("y")

    def check_wall_collision(self, axis):
        """Check if player collides with a wall at a given dx and dy"""

        for wall in self.tilemap.wall_sprites:
            if wall.rect.colliderect(self.rect):
                if axis == "x":
                    # Moving right.
                    if self.direction.x > 0:
                        self.rect.right = wall.rect.left

                    elif self.direction.x < 0:
                        self.rect.left = wall.rect.right

                if axis == "y":
                    if self.direction.y > 0:
                        self.rect.bottom = wall.rect.top

                    elif self.direction.y < 0:
                        self.rect.top = wall.rect.bottom

    def update(self):
        self.get_input()
