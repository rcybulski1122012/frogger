import os.path

import pygame

from colors import *
from objects import Frog, Obstacle


pygame.init()

pygame.display.set_caption("Frogger Game")
BACKGROUND = pygame.image.load(os.path.join("assets", "background.png"))
SURFACE = pygame.display.set_mode((640, 640))
FPS = 60

frog = Frog(SURFACE, 320, 576, 32, 32, 32)

cars = []
car = Obstacle(SURFACE, 615, 490, 150, 50, 2)


def draw_window():
    SURFACE.fill(BLACK)
    SURFACE.blit(BACKGROUND, (0, 0))
    frog.draw()
    car.draw()
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
    car.on_loop()


pygame.quit()
