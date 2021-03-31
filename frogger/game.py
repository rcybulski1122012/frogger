import pygame

from frogger.best_score import BestScore
from frogger.button import Button
from frogger.models import Direction, Frog, GameObject, MovingObject
from frogger.score_counter import ScoreCounter
from frogger.timer import Timer
from frogger.utils import detect_collision, get_img_path, get_move_direction


class Frogger:
    def __init__(self, seconds_per_frog=30, lives=3):
        self._init_pygame()
        self._load_images()

        self.font = pygame.font.SysFont("Comic Sans MS", 35)
        self.SURFACE = pygame.display.set_mode((640, 640))
        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.best_score_manager = BestScore("frogger.txt")
        self.best_score = self.best_score_manager.get()
        self.score_counter = ScoreCounter()
        self.starting_lives = lives
        self.lives = lives

        self.reset_game_button = Button(
            250, 300, 60, 30, " YES", self.font, (0, 255, 0)
        )
        self.quit_game_button = Button(350, 300, 60, 30, "  NO", self.font, (255, 0, 0))
        self.choice_area = GameObject(210, 100, 240, 250, None, None)
        self.reset_or_quit_text = self.font.render(
            "RESET GAME?", False, (255, 255, 255)
        )

        self.seconds_per_frog = seconds_per_frog
        self.timer = Timer(25, 25, 200, 25, (255, 0, 0), seconds_per_frog, self.FPS)
        self.frog = Frog(320, 576, 32, 32, 32, self.FROG_IMG)
        self._init_game_objects()

    @staticmethod
    def _init_pygame():
        pygame.init()
        pygame.display.set_caption("Frogger Clone")

    def _load_images(self):
        self.BACKGROUND = pygame.image.load(get_img_path("background.png"))
        self.FROG_IMG = pygame.image.load(get_img_path("frog.png"))
        self.CAR1_IMG = pygame.image.load(get_img_path("car1.png"))
        self.CAR2_IMG = pygame.image.load(get_img_path("car2.png"))
        self.CAR3_IMG = pygame.image.load(get_img_path("car3.png"))
        self.CAR4_IMG = pygame.image.load(get_img_path("car4.png"))
        self.CAR5_IMG = pygame.image.load(get_img_path("car5.png"))
        self.BLOCK3_IMG = pygame.image.load(get_img_path("block3.png"))
        self.BLOCK4_IMG = pygame.image.load(get_img_path("block4.png"))
        self.BLOCK6_IMG = pygame.image.load(get_img_path("block6.png"))
        self.TURTLE_IMG = pygame.image.load(get_img_path("turtle.png"))

    def _init_game_objects(self):
        self.cars = [
            MovingObject(150, 544, 32, 32, 1.2, self.CAR1_IMG),
            MovingObject(350, 544, 32, 32, 1.2, self.CAR1_IMG),
            MovingObject(550, 544, 32, 32, 1.2, self.CAR1_IMG),
            MovingObject(
                550, 512, 32, 32, 0.8, self.CAR2_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                350, 512, 32, 32, 0.8, self.CAR2_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                150, 512, 32, 32, 0.8, self.CAR2_IMG, direction=Direction.RIGHT
            ),
            MovingObject(200, 480, 32, 32, 1, self.CAR3_IMG),
            MovingObject(400, 480, 32, 32, 1, self.CAR3_IMG),
            MovingObject(600, 480, 32, 32, 1, self.CAR3_IMG),
            MovingObject(
                450, 448, 32, 32, 0.9, self.CAR4_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                100, 448, 32, 32, 0.9, self.CAR4_IMG, direction=Direction.RIGHT
            ),
            MovingObject(100, 416, 64, 32, 0.7, self.CAR5_IMG),
            MovingObject(250, 416, 64, 32, 0.7, self.CAR5_IMG),
            MovingObject(450, 416, 64, 32, 0.7, self.CAR5_IMG),
            MovingObject(600, 416, 64, 32, 0.7, self.CAR5_IMG),
            MovingObject(200, 384, 32, 32, 1.2, self.CAR1_IMG),
            MovingObject(400, 384, 32, 32, 1.2, self.CAR1_IMG),
            MovingObject(600, 384, 32, 32, 1.2, self.CAR1_IMG),
        ]
        self.water_area = GameObject(0, 161, 640, 190, None, None)
        self.grass_area = GameObject(0, 97, 640, 62, None, None)
        self.frog_homes = [
            GameObject(64, 129, 33, 30, None, None),
            GameObject(160, 129, 33, 30, None, None),
            GameObject(254, 129, 33, 30, None, None),
            GameObject(352, 129, 33, 30, None, None),
            GameObject(448, 129, 33, 30, None, None),
            GameObject(544, 129, 33, 30, None, None),
        ]
        self.blocks = [
            MovingObject(
                0, 161, 126, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                215, 161, 126, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                430, 161, 126, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                655, 161, 126, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                0, 225, 188, 31, 1.2, self.BLOCK6_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                400, 225, 188, 31, 1.2, self.BLOCK6_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                0, 257, 92, 31, 0.8, self.BLOCK3_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                350, 257, 92, 31, 0.8, self.BLOCK3_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                600, 257, 92, 31, 0.8, self.BLOCK3_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                150, 321, 126, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                450, 321, 126, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT
            ),
            MovingObject(
                700, 321, 126, 31, 1, self.BLOCK4_IMG, direction=Direction.RIGHT
            ),
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
        self._process_objects_movement()
        self._process_frog_with_cars_collisions()
        self._process_frog_with_blocks_and_turtles_collisions()
        self._process_frog_homes()
        self._process_game_conditions()
        self._handle_end_of_time()
        self.timer.tick()

    def _process_objects_movement(self):
        for obj in self._get_all_moving_objects():
            obj.move()

            if obj.is_beyond_the_surface(self.SURFACE):
                self._move_object_to_opposite_side(obj)

    def _get_all_moving_objects(self):
        return [*self.cars, *self.blocks, *self.turtles]

    def _move_object_to_opposite_side(self, obj):
        if obj.direction == Direction.RIGHT:
            obj.move_to_position(-obj.width, obj.y)
        elif obj.direction == Direction.LEFT:
            obj.move_to_position(self.SURFACE.get_width(), obj.y)

    def _process_frog_with_cars_collisions(self):
        for car in self.cars:
            if detect_collision(self.frog, car):
                self.frog.move_to_starting_position()
                self._lose_live()

    def _lose_live(self):
        self.frog.move_to_starting_position()
        self.lives -= 1
        self.timer.reset()

    def _process_frog_with_blocks_and_turtles_collisions(self):
        colliding_object = None
        for obj in [*self.blocks, *self.turtles]:
            if detect_collision(self.frog, obj):
                colliding_object = obj

        if detect_collision(self.frog, self.water_area) and colliding_object is None:
            self._lose_live()
        elif (
            colliding_object
            and not self.is_beyond_the_surface_after_moving_object_move(
                colliding_object, self.SURFACE
            )
        ):
            self.frog.move_by_value(
                colliding_object.direction, colliding_object.velocity
            )

    def is_beyond_the_surface_after_moving_object_move(self, moving_object, surface):
        return (
            self.frog.x + moving_object.velocity < 0
            or self.frog.x + self.frog.width + moving_object.velocity
            > surface.get_width()
        )

    def _process_frog_homes(self):
        colliding_object = None
        index = None
        for i, obj in enumerate(self.frog_homes):
            if detect_collision(self.frog, obj):
                colliding_object = obj
                index = i

        if detect_collision(self.frog, self.grass_area) and colliding_object is None:
            self._lose_live()
        elif colliding_object:
            self.frog_homes.pop(index)
            self._frog_in_home()

    def _frog_in_home(self):
        self.score_counter.add_points_for_arriving()
        self.score_counter.add_points_for_unused_time(self.timer.seconds)
        self.frog.move_to_starting_position()
        self.timer.reset()

    def _process_game_conditions(self):
        if self.lives < 0:
            self._end_game()
        elif len(self.frog_homes) == 0:
            self.score_counter.add_points_for_saving_all_frogs()
            self.score_counter.add_points_for_preserved_lives(self.lives)
            self._end_game()

    def _end_game(self):
        if self.score_counter.score > self.best_score:
            self.best_score_manager.set(self.score_counter.score)

        self._reset_or_quit_game()

    def _reset_or_quit_game(self):
        self._draw_reset_or_quit_buttons()

        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.reset_game_button.is_mouse_over(mouse_pos):
                        self._reset_game()
                        running = False
                    elif self.quit_game_button.is_mouse_over(mouse_pos):
                        pygame.quit()
                if event.type == pygame.QUIT:
                    pygame.quit()

    def _draw_reset_or_quit_buttons(self):
        pygame.draw.rect(self.SURFACE, (0, 0, 0), self.choice_area.rect)
        self.reset_game_button.draw(self.SURFACE)
        self.quit_game_button.draw(self.SURFACE)
        self.SURFACE.blit(self.reset_or_quit_text, (240, 150))
        pygame.display.update()

    def _reset_game(self):
        self.__init__(self.seconds_per_frog, self.starting_lives)

    def _handle_end_of_time(self):
        if self.timer.end_of_time():
            self._lose_live()

    def _draw_game_elements(self):
        self.SURFACE.blit(self.BACKGROUND, (0, 0))

        for obj in self._get_all_moving_objects():
            obj.draw(self.SURFACE)

        for obj in self.frog_homes:
            pygame.draw.rect(self.SURFACE, (24, 48, 172), obj.rect)

        self.timer.draw(self.SURFACE)
        self.frog.draw(self.SURFACE)

        self._draw_game_info()

        pygame.display.update()

    def _draw_game_info(self):
        self.SURFACE.blit(self._get_best_score_surface(), (400, 25))
        self.SURFACE.blit(self._get_lives_number_surface(), (400, 60))
        self.SURFACE.blit(self._get_current_score_surface(), (25, 60))

    def _get_best_score_surface(self):
        return self.font.render(
            f"Best score: {self.best_score}", False, (255, 255, 255)
        )

    def _get_lives_number_surface(self):
        return self.font.render(f"Lives: {self.lives}", False, (255, 255, 255))

    def _get_current_score_surface(self):
        return self.font.render(
            f"Current score: {self.score_counter.score}", False, (255, 255, 255)
        )


if __name__ == "__main__":
    game = Frogger(lives=3)
    game.run()
