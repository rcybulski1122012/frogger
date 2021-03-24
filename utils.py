import pygame

from models import Direction


def get_move_direction(keys):
    if keys[pygame.K_LEFT]:
        return Direction.LEFT
    elif keys[pygame.K_RIGHT]:
        return Direction.RIGHT
    elif keys[pygame.K_UP]:
        return Direction.UP
    elif keys[pygame.K_DOWN]:
        return Direction.DOWN


def detect_collision(first, second):
    return first.rect.colliderect(second.rect)


