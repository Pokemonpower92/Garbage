import pygame
from config import constants


def event_loop(game):
    """
    This checks for all types of player input.

    Returns:
        Boolean for if the game quits.
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        game.player.move(0, -1)
    if keys[pygame.K_a]:
        game.player.move(-1, 0)
    if keys[pygame.K_s]:
        game.player.move(0, 1)
    if keys[pygame.K_d]:
        game.player.move(1, 0)
