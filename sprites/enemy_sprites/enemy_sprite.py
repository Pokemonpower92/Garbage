import pygame
from sprites.enemy_sprites.enemy_actions import EnemyActions


class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, level, type, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

        self.level = level
        self.type = type

        self.groups = (
            self.level.all_sprites,
            self.level.enemy_sprites,
            self.level.entity_sprites,
        )
        self.image = self.load_image()
        self.rect = self.image.get_rect()

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.rect.x = self.x
        self.rect.y = self.y
        self.hit_box = self.rect.inflate(0, -26)

        self.action = EnemyActions.IDLE
        self.distance = None
        self.direction = None

    def handle_attack_collision(self, attack):
        print(f"Enemy Hit for {attack.damage} damage")
        self.kill()

    def load_image(self):
        """Load an image for the enemy sprite"""
        image_path = self.level.level_data["graphics_paths"]["enemies"][self.type]
        return pygame.image.load(image_path)

    def take_action(self) -> None:
        """
        Take whatever action for the frame.
        @return: None
        """

        if self.action == EnemyActions.ATTACKING:
            print("Attacking")

        if self.action == EnemyActions.TRACKING:
            print("Tracking")
            new_position = self.direction.normalize()*4
            self.rect.x += new_position.x
            self.rect.y += new_position.y
            self.hit_box.center = self.rect.center

    def choose_action(self) -> None:
        """
        Chooses the appropriate action for the frame.
        @return: None
        """
        player_position = pygame.math.Vector2(self.level.player.rect.center)
        enemy_position = pygame.math.Vector2(self.rect.center)
        self.direction = (player_position - enemy_position)
        self.distance = self.direction.magnitude()

        self.action = EnemyActions.IDLE

        if self.distance and self.distance < 500:
            self.action = EnemyActions.TRACKING

        if self.distance and self.distance < 50:
            self.action = EnemyActions.ATTACKING

    def update(self) -> None:
        """
        Update the enemy sprite.
        @return: None
        """
        self.choose_action()
        self.take_action()
