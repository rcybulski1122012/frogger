from dataclasses import dataclass
from enum import Enum
from typing import Union

import pygame


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


@dataclass
class BasicGameObject:
    x: Union[int, float]
    y: Union[int, float]
    width: int
    height: int

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class GameObject(BasicGameObject):
    def __init__(self, x, y, width, height, velocity, sprite):
        super().__init__(x, y, width, height)
        self.starting_x = x
        self.starting_y = y
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

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))

    def move_to_starting_position(self):
        self.move_to_position(self.starting_x, self.starting_y)

    def move_to_position(self, x, y):
        self.x, self.y = x, y

    def move_by_value(self, direction, value):
        if direction == Direction.LEFT:
            self.x -= value
        elif direction == Direction.RIGHT:
            self.x += value
        elif direction == Direction.UP:
            self.y -= value
        elif direction == Direction.DOWN:
            self.y += value


class Frog(GameObject):
    def __init__(self, x, y, width, height, velocity, sprite, jump_frequency=15):
        super().__init__(x, y, width, height, velocity, sprite)
        self._jump_delay = 0
        self._jump_frequency = jump_frequency

    def move(self, direction):
        if self._jump_delay == 0 and direction:
            super().move(direction)
            self._jump_delay += 1
        elif self._jump_delay == self._jump_frequency:
            self._jump_delay = 0
        elif self._jump_delay != 0:
            self._jump_delay += 1

    def is_beyond_the_surface_after_move(self, direction, surface):
        if direction == Direction.LEFT:
            return self.x - self.velocity < 0
        elif direction == Direction.RIGHT:
            return self.x + self.width + self.velocity > surface.get_width()
        elif direction == Direction.UP:
            return self.y - self.velocity < 0
        elif direction == Direction.DOWN:
            return self.y + self.velocity + self.width > surface.get_height()


class MovingObject(GameObject):
    def __init__(self, x, y, width, height, velocity, sprite, direction=Direction.LEFT):
        super().__init__(x, y, width, height, velocity, sprite)
        self.direction = direction

    def move(self, *args):
        super().move(self.direction)

    def is_beyond_the_surface(self, surface):
        if (
            self.direction == Direction.LEFT
            and self.x + self.width < 0
            or self.direction == Direction.RIGHT
            and self.x - self.width > surface.get_width()
        ):
            return True

        return False
