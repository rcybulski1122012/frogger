import pygame

from enum import Enum


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


class GameObject:
    def __init__(self, surface, x, y, width, height, velocity):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity

    def move(self, direction):
        if direction == Direction.LEFT:
            self.x -= self.velocity
        elif direction == Direction.RIGHT:
            self.x += self.velocity
        elif direction == Direction.UP:
            self.y -= self.velocity
        elif direction == Direction.DOWN:
            self.y += self.velocity


class Frog(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._jump_delay = 0

    def draw(self):
        pygame.draw.rect(self.surface, (128, 128, 128), pygame.Rect(self.x, self.y, self.width, self.height))

    def control(self, keys):
        direction = self._get_move_direction(keys)
        if self._jump_delay == 0 and direction:
            self.move(direction)
            self._jump_delay += 1
        elif self._jump_delay == 20:
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
