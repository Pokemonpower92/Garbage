import pygame


def event_loop():
    """
    This checks for all types of player input.

    Returns:
        Boolean for if the game quits.
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
