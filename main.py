import os.path

import pygame

from colors import *
from objects import Frog, Obstacle, Direction


pygame.init()

pygame.display.set_caption("Frogger Game")

BACKGROUND = pygame.image.load(os.path.join("assets", "background.png"))
FROG_IMG = pygame.image.load(os.path.join("assets", "frog.png"))
CAR1_IMG = pygame.image.load(os.path.join("assets", "car1.png"))
CAR2_IMG = pygame.image.load(os.path.join("assets", "car2.png"))
CAR3_IMG = pygame.image.load(os.path.join("assets", "car3.png"))
CAR5_IMG = pygame.image.load(os.path.join("assets", "car4.png"))


SCREEN_WIDTH = SCREEN_HEIGHT = 640
SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60

frog = Frog(SURFACE, 320, 576, 32, 32, 32, FROG_IMG)
water_area = Obstacle(SURFACE, 0, 160, 640, 192, 0, None)

cars = [
    Obstacle(SURFACE, 150, 544, 32, 32, 1.2, CAR1_IMG),
    Obstacle(SURFACE, 350, 544, 32, 32, 1.2, CAR1_IMG),
    Obstacle(SURFACE, 550, 544, 32, 32, 1.2, CAR1_IMG),

    Obstacle(SURFACE, 550, 512, 32, 32, 0.8, CAR2_IMG, direction=Direction.RIGHT),
    Obstacle(SURFACE, 350, 512, 32, 32, 0.8, CAR2_IMG, direction=Direction.RIGHT),
    Obstacle(SURFACE, 150, 512, 32, 32, 0.8, CAR2_IMG, direction=Direction.RIGHT),

    Obstacle(SURFACE, 200, 480, 32, 32, 1, CAR3_IMG),
    Obstacle(SURFACE, 400, 480, 32, 32, 1, CAR3_IMG),
    Obstacle(SURFACE, 600, 480, 32, 32, 1, CAR3_IMG),

    Obstacle(SURFACE, 450, 448, 32, 32, 0.9, CAR2_IMG, direction=Direction.RIGHT),
    Obstacle(SURFACE, 100, 448, 32, 32, 0.9, CAR2_IMG, direction=Direction.RIGHT),

    Obstacle(SURFACE, 100, 416, 64, 32, 0.7, CAR5_IMG),
    Obstacle(SURFACE, 250, 416, 64, 32, 0.7, CAR5_IMG),
    Obstacle(SURFACE, 450, 416, 64, 32, 0.7, CAR5_IMG),
    Obstacle(SURFACE, 600, 416, 64, 32, 0.7, CAR5_IMG),

    Obstacle(SURFACE, 640, 384, 32, 32, 1.2, CAR1_IMG),
    Obstacle(SURFACE, 850, 384, 32, 32, 1.2, CAR1_IMG),
    Obstacle(SURFACE, 1050, 384, 32, 32, 1.2, CAR1_IMG),
]

logs = [
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

    for car in cars:
        car.move()

        if car.is_beyond_screen():
            if car.direction == Direction.RIGHT:
                car.move_to_position(-car.width, car.y)
            elif car.direction == Direction.LEFT:
                car.move_to_position(SCREEN_WIDTH, car.y)

        if frog.check_collision(car):
            frog.move_to_starting_position()

    if frog.check_collision(water_area) and not any([log.check_collision(frog) for log in logs]):
        frog.move_to_starting_position()

    draw_window()


pygame.quit()
