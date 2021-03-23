import pygame

from colors import *
from enum import Enum


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


class GameObject:
    def __init__(self, surface, x, y, width, height, velocity, sprite):
        self.surface = surface
        self.starting_x = x
        self.starting_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.sprite = sprite

    def move(self, direction):
        if direction == Direction.LEFT:
            self.x -= self.velocity
        elif direction == Direction.RIGHT:
            self.x += self.velocity
        elif direction == Direction.UP:
            self.y -= self.velocity
        elif direction == Direction.DOWN:
            self.y += self.velocity

    def draw(self):
        self.surface.blit(self.sprite, (self.x, self.y))

    def move_to_starting_position(self):
        self.move_to_position(self.starting_x, self.starting_y)

    def move_to_position(self, x, y):
        self.x, self.y = x, y

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision(self, other):
        return self.rect.colliderect(other.rect)


class Frog(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._jump_delay = 0

    def control(self, keys):
        direction = self._get_move_direction(keys)
        if self._jump_delay == 0 and direction:
            self.move(direction)
            self._jump_delay += 1
        elif self._jump_delay == 15:
            self._jump_delay = 0
        elif self._jump_delay != 0:
            self._jump_delay += 1

    @staticmethod
    def _get_move_direction(keys):
        if keys[pygame.K_LEFT]:
            return Direction.LEFT
        elif keys[pygame.K_RIGHT]:
            return Direction.RIGHT
        elif keys[pygame.K_UP]:
            return Direction.UP
        elif keys[pygame.K_DOWN]:
            return Direction.DOWN

        return None

    def move(self, direction):
        if not self._is_beyond_the_border_after_move(direction):
            super().move(direction)

    def _is_beyond_the_border_after_move(self, direction):
        if direction == Direction.LEFT:
            return self._left_border()
        elif direction == Direction.RIGHT:
            return self._right_border()
        elif direction == Direction.UP:
            return self._top_border()
        elif direction == Direction.DOWN:
            return self._bottom_border()

    def _right_border(self):
        return self.x + self.width + self.velocity > self.surface.get_width()

    def _left_border(self):
        return self.x - self.velocity < 0

    def _top_border(self):
        return self.y - self.velocity < 0

    def _bottom_border(self):
        return self.y + self.velocity + self.width > self.surface.get_height()


class Obstacle(GameObject):
    def __init__(self, *args, direction=Direction.LEFT, **kwargs):
        super().__init__(*args, **kwargs)
        self.beyond_the_screen = False
        self.direction = direction

    def move(self, *args):
        super().move(self.direction)

    def is_beyond_screen(self):
        if self.direction == Direction.LEFT:
            if self.x + self.width < 0:
                return True
            return False
        elif self.direction == Direction.RIGHT:
            if self.x - self.width > self.surface.get_width():
                return True
            return False

