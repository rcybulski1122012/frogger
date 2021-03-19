import pygame

pygame.init()

pygame.display.set_caption("Frogger Game")
screen = pygame.display.set_mode((640, 640))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
