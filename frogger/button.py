import pygame

from frogger.models import BasicGameObject


class Button(BasicGameObject):
    def __init__(
        self, x, y, width, height, text, font, bg_color=(0, 0, 0), color=(255, 255, 255)
    ):
        super().__init__(x, y, width, height)
        self.bg_color = bg_color
        self.color = color
        self.text = text
        self.font = font

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)
        text_surf = self.font.render(self.text, False, self.color)
        surface.blit(text_surf, (self.x, self.y))

    def is_mouse_over(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
