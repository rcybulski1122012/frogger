import pygame

from frogger.game import Frogger

try:
    game = Frogger()
    game.run()
except pygame.error:
    pass
