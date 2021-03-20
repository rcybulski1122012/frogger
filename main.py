import pygame

from colors import *
from objects import Frog


pygame.init()

pygame.display.set_caption("Frogger Game")
SURFACE = pygame.display.set_mode((640, 640))
FPS = 60

frog = Frog(SURFACE, 320, 550, 25, 25, 25)


def draw_window():
    SURFACE.fill(BLACK)
    frog.draw()
    pygame.display.update()


running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    frog.control(keys)

    draw_window()

pygame.quit()
