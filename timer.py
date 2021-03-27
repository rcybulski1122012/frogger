import pygame


class Timer:
    def __init__(self, x, y, width, height, color, seconds, fps):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.seconds = seconds
        self._px_per_sec = width / seconds
        self._second_per_tick = 1 / fps

    def tick(self):
        if self.seconds > 0:
            self.seconds -= self._second_per_tick

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         pygame.Rect(self.x, self.y, self._px_per_sec * self.seconds, self.height))

    def end_of_time(self):
        return self.seconds <= 0