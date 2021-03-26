import os.path

import pygame

from models import Frog, MovingObject, Direction, GameObject
from utils import get_move_direction, detect_collision
from timer import Timer
from best_score import BestScore


class Frogger:
    def __init__(self):
        self._init_pygame()
        self._load_images()
        self.SURFACE = pygame.display.set_mode((640, 640))
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.timer = Timer(25, 25, 200, 25, (255, 0, 0), 30, self.FPS)
        self.best_score_manager = BestScore('frogger.txt')
        self.best_score = self.best_score_manager.get()
        self.font = pygame.font.SysFont('Comic Sans MS', 35)
        self.frog = Frog(320, 576, 32, 32, 32, self.FROG_IMG)
        self.cars = [
            MovingObject(150, 544, 32, 32, 1.2, self.CAR1_IMG),
            MovingObject(350, 544, 32, 32, 1.2, self.CAR1_IMG),
            MovingObject(550, 544, 32, 32, 1.2, self.CAR1_IMG),

            MovingObject(550, 512, 32, 32, 0.8, self.CAR2_IMG, direction=Direction.RIGHT),
            MovingObject(350, 512, 32, 32, 0.8, self.CAR2_IMG, direction=Direction.RIGHT),
            MovingObject(150, 512, 32, 32, 0.8, self.CAR2_IMG, direction=Direction.RIGHT),

            MovingObject(200, 480, 32, 32, 1, self.CAR3_IMG),
            MovingObject(400, 480, 32, 32, 1, self.CAR3_IMG),
            MovingObject(600, 480, 32, 32, 1, self.CAR3_IMG),

            MovingObject(450, 448, 32, 32, 0.9, self.CAR4_IMG, direction=Direction.RIGHT),
            MovingObject(100, 448, 32, 32, 0.9, self.CAR4_IMG, direction=Direction.RIGHT),

            MovingObject(100, 416, 64, 32, 0.7, self.CAR5_IMG),
            MovingObject(250, 416, 64, 32, 0.7, self.CAR5_IMG),
            MovingObject(450, 416, 64, 32, 0.7, self.CAR5_IMG),
            MovingObject(600, 416, 64, 32, 0.7, self.CAR5_IMG),

            MovingObject(200, 384, 32, 32, 1.2, self.CAR1_IMG),
            MovingObject(400, 384, 32, 32, 1.2, self.CAR1_IMG),
            MovingObject(600, 384, 32, 32, 1.2, self.CAR1_IMG),
        ]
        self.water_area = GameObject(0, 161, 640, 190, None, None)
        self.blocks = [
            MovingObject(0, 161, 128, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT),
            MovingObject(215, 161, 128, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT),
            MovingObject(430, 161, 128, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT),
            MovingObject(655, 161, 128, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT),

            MovingObject(0, 225, 192, 31, 1.2, self.BLOCK6_IMG, direction=Direction.RIGHT),
            MovingObject(400, 225, 192, 31, 1.2, self.BLOCK6_IMG, direction=Direction.RIGHT),

            MovingObject(0, 257, 96, 31, 0.8, self.BLOCK3_IMG, direction=Direction.RIGHT),
            MovingObject(350, 257, 96, 31, 0.8, self.BLOCK3_IMG, direction=Direction.RIGHT),
            MovingObject(700, 257, 96, 31, 0.8, self.BLOCK3_IMG, direction=Direction.RIGHT),

            MovingObject(150, 321, 128, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT),
            MovingObject(450, 321, 128, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT),
            MovingObject(700, 321, 128, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT),
        ]
        self.turtles = [

            MovingObject(0, 193, 32, 31, 1.1, self.TURTLE_IMG),
            MovingObject(35, 193, 32, 31, 1.1, self.TURTLE_IMG),

            MovingObject(150, 193, 32, 31, 1.1, self.TURTLE_IMG),
            MovingObject(185, 193, 32, 31, 1.1, self.TURTLE_IMG),

            MovingObject(300, 193, 32, 31, 1.1, self.TURTLE_IMG),
            MovingObject(335, 193, 32, 31, 1.1, self.TURTLE_IMG),

            MovingObject(450, 193, 32, 31, 1.1, self.TURTLE_IMG),
            MovingObject(485, 193, 32, 31, 1.1, self.TURTLE_IMG),

            MovingObject(215, 289, 32, 31, 0.9, self.TURTLE_IMG),
            MovingObject(250, 289, 32, 31, 0.9, self.TURTLE_IMG),
            MovingObject(285, 289, 32, 31, 0.9, self.TURTLE_IMG),

            MovingObject(500, 289, 32, 31, 0.9, self.TURTLE_IMG),
            MovingObject(535, 289, 32, 31, 0.9, self.TURTLE_IMG),
            MovingObject(570, 289, 32, 31, 0.9, self.TURTLE_IMG),

            MovingObject(700, 289, 32, 31, 0.9, self.TURTLE_IMG),
            MovingObject(735, 289, 32, 31, 0.9, self.TURTLE_IMG),
            MovingObject(770, 289, 32, 31, 0.9, self.TURTLE_IMG),
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
        self.TURTLE_IMG = pygame.image.load(os.path.join("assets", "turtle.png"))

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self._handle_input()
            self._process_game_logic()
            self._draw_game_elements()

            self._handle_game_ending()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        direction = get_move_direction(keys)

        if not self.frog.is_beyond_the_surface_after_move(direction, self.SURFACE):
            self.frog.move(direction)

    def _process_game_logic(self):
        self._process_objects_movement()
        self._process_frog_with_cars_collisions()
        self._process_frog_with_blocks_and_turtles_collisions()
        self.timer.tick()

    def _process_objects_movement(self):
        for moving_object in self._get_all_moving_objects():
            moving_object.move()

            if moving_object.is_beyond_the_surface(self.SURFACE):
                self._move_obstacle_to_opposite_side(moving_object)

    def _get_all_moving_objects(self):
        return [*self.cars, *self.blocks, *self.turtles]

    def _move_obstacle_to_opposite_side(self, moving_object):
        if moving_object.direction == Direction.RIGHT:
            moving_object.move_to_position(-moving_object.width, moving_object.y)
        elif moving_object.direction == Direction.LEFT:
            moving_object.move_to_position(self.SURFACE.get_width(), moving_object.y)

    def _process_frog_with_cars_collisions(self):
        for car in self.cars:
            if detect_collision(self.frog, car):
                self.frog.move_to_starting_position()

    def _process_frog_with_blocks_and_turtles_collisions(self):
        colliding_object = None
        for moving_object in [*self.blocks, *self.turtles]:
            if detect_collision(self.frog, moving_object):
                colliding_object = moving_object

        if detect_collision(self.frog, self.water_area) and colliding_object is None:
            self.frog.move_to_starting_position()
        elif colliding_object:
            self.frog.move_by_value(colliding_object.direction, colliding_object.velocity)

    def _draw_game_elements(self):
        self.SURFACE.blit(self.BACKGROUND, (0, 0))

        for moving_object in self._get_all_moving_objects():
            moving_object.draw(self.SURFACE)

        self.timer.draw(self.SURFACE)
        self.frog.draw(self.SURFACE)

        self.SURFACE.blit(self._get_score_surface(), (400, 25))

        pygame.display.update()

    def _get_score_surface(self):
        return self.font.render(f'Best score: {self.best_score}', False, (255, 255, 255))

    def _handle_game_ending(self):
        if self.timer.end_of_time():
            pygame.quit()


if __name__ == '__main__':
    game = Frogger()
    game.run()
