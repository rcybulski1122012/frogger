class Obstacle(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.to_remove = False

    def on_loop(self):
        self.move(Direction.LEFT)
        self.check_to_remove()

    def draw(self):
        pygame.draw.rect(self.surface, (10, 128, 200), pygame.Rect(self.x, self.y, 25, 25))

    def check_to_remove(self):
        if (self._right_border() or self._left_border() or
                self._top_border() or self._bottom_border()):
            self.to_remove = True

    def _right_border(self):
        return self.x > self.surface.get_width()

    def _left_border(self):
        return self.x + self.width < 0

    def _top_border(self):
        return self.y + self.height < 0

    def _bottom_border(self):
        return self.y > self.surface.get_height()
