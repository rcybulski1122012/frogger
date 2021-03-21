import os.path

import pygame

from colors import *
from objects import Frog, Obstacle, Direction


pygame.init()

pygame.display.set_caption("Frogger Game")
BACKGROUND = pygame.image.load(os.path.join("assets", "background.png"))
SURFACE = pygame.display.set_mode((640, 640))
FPS = 60

frog = Frog(SURFACE, 320, 576, 32, 32, 32)
water_area = Obstacle(SURFACE, 0, 97, 640, 191, 0)

cars = [
    Obstacle(SURFACE, 640, 490, 75, 50, 2),
    Obstacle(SURFACE, 1100, 490, 75, 50, 2),
    Obstacle(SURFACE, 1450, 490, 75, 50, 2),


    Obstacle(SURFACE, -150, 426, 150, 50, 2, direction=Direction.RIGHT),
    Obstacle(SURFACE, -500, 426, 150, 50, 2, direction=Direction.RIGHT),
    Obstacle(SURFACE, -1000, 426, 150, 50, 2, direction=Direction.RIGHT),

    Obstacle(SURFACE, 640, 362, 150, 50, 2),
    Obstacle(SURFACE, 1100, 362, 150, 50, 2),
    Obstacle(SURFACE, 1450, 362, 150, 50, 2),
]

logs = [
    Obstacle(SURFACE, 640, 98, 300, 32, 2),
    Obstacle(SURFACE, 640, 131, 300, 32, 2),
    Obstacle(SURFACE, 640, 164, 300, 32, 2),
    Obstacle(SURFACE, 640, 197, 300, 32, 2),
    Obstacle(SURFACE, 640, 230, 300, 31, 2),
    Obstacle(SURFACE, 640, 262, 300, 25, 2),
]


def draw_window():
    SURFACE.fill(BLACK)
    SURFACE.blit(BACKGROUND, (0, 0))

    # water_area.draw()
    for car in cars:
        car.draw()

    for log in logs:
        log.draw()

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

    # cars actions: collisions, moving to default position then beyond the screen
    for car in cars:
        car.on_loop()
        if car.beyond_the_screen:
            car.set_position(car.starting_x, car.starting_y)
            car.beyond_the_screen = False

        if frog.check_collision(car):
            frog.set_position(frog.starting_x, frog.starting_y)

    for log in logs:
        log.on_loop()
        if log.beyond_the_screen:
            log.set_position(log.starting_x, log.starting_y)
            log.beyond_the_screen = False

    if frog.check_collision(water_area) and not any([log.check_collision(frog) for log in logs]):
        frog.set_position(frog.starting_x, frog.starting_y)

    draw_window()


pygame.quit()
