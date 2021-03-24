import os.path

import pygame

from models import Frog, Obstacle, Direction
from utils import get_move_direction, detect_collision


class Frogger:
    def __init__(self):
        self._init_pygame()
        self._load_images()
        self.SURFACE = pygame.display.set_mode((640, 640))
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.frog = Frog(320, 576, 32, 32, 32, self.FROG_IMG)
        self.cars = [
            Obstacle(150, 544, 32, 32, 1.2, self.CAR1_IMG),
            Obstacle(350, 544, 32, 32, 1.2, self.CAR1_IMG),
            Obstacle(550, 544, 32, 32, 1.2, self.CAR1_IMG),

            Obstacle(550, 512, 32, 32, 0.8, self.CAR2_IMG, direction=Direction.RIGHT),
            Obstacle(350, 512, 32, 32, 0.8, self.CAR2_IMG, direction=Direction.RIGHT),
            Obstacle(150, 512, 32, 32, 0.8, self.CAR2_IMG, direction=Direction.RIGHT),

            Obstacle(200, 480, 32, 32, 1, self.CAR3_IMG),
            Obstacle(400, 480, 32, 32, 1, self.CAR3_IMG),
            Obstacle(600, 480, 32, 32, 1, self.CAR3_IMG),

            Obstacle(450, 448, 32, 32, 0.9, self.CAR4_IMG, direction=Direction.RIGHT),
            Obstacle(100, 448, 32, 32, 0.9, self.CAR4_IMG, direction=Direction.RIGHT),

            Obstacle(100, 416, 64, 32, 0.7, self.CAR5_IMG),
            Obstacle(250, 416, 64, 32, 0.7, self.CAR5_IMG),
            Obstacle(450, 416, 64, 32, 0.7, self.CAR5_IMG),
            Obstacle(600, 416, 64, 32, 0.7, self.CAR5_IMG),

            Obstacle(200, 384, 32, 32, 1.2, self.CAR1_IMG),
            Obstacle(400, 384, 32, 32, 1.2, self.CAR1_IMG),
            Obstacle(600, 384, 32, 32, 1.2, self.CAR1_IMG),
        ]

    @staticmethod
    def _init_pygame():
        pygame.init()
        pygame.display.set_caption("Frogger Clone")

    def _load_images(self):
        self.BACKGROUND = pygame.image.load(os.path.join("assets", "background.png"))
        self.FROG_IMG = pygame.image.load(os.path.join("assets", "frog.png"))
        self.CAR1_IMG = pygame.image.load(os.path.join("assets", "car1.png"))
        self.CAR2_IMG = pygame.image.load(os.path.join("assets", "car2.png"))
        self.CAR3_IMG = pygame.image.load(os.path.join("assets", "car3.png"))
        self.CAR4_IMG = pygame.image.load(os.path.join("assets", "car4.png"))
        self.CAR5_IMG = pygame.image.load(os.path.join("assets", "car5.png"))
        self.BLOCK3_IMG = pygame.image.load(os.path.join("assets", "block3.png"))
        self.BLOCK4_IMG = pygame.image.load(os.path.join("assets", "block4.png"))
        self.BLOCK6_IMG = pygame.image.load(os.path.join("assets", "block6.png"))
        self.TURTLE = pygame.image.load(os.path.join("assets", "turtle.png"))

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self._handle_input()
            self._process_game_logic()
            self._draw_game_elements()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        direction = get_move_direction(keys)

        if not self.frog.is_beyond_the_surface_after_move(direction, self.SURFACE):
            self.frog.move(direction)

    def _process_game_logic(self):
        for car in self.cars:
            if detect_collision(self.frog, car):
                self.frog.move_to_starting_position()

            car.move()

            if car.is_beyond_the_surface(self.SURFACE):
                if car.direction == Direction.RIGHT:
                    car.move_to_position(-car.width, car.y)
                elif car.direction == Direction.LEFT:
                    car.move_to_position(self.SURFACE.get_width(), car.y)

    def _draw_game_elements(self):
        self.SURFACE.blit(self.BACKGROUND, (0, 0))
        for car in self.cars:
            car.draw(self.SURFACE)
        self.frog.draw(self.SURFACE)
        pygame.display.update()


if __name__ == '__main__':
    game = Frogger()
    game.run()
