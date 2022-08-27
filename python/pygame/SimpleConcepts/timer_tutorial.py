import pygame, sys

# Setting up Pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

current_time = 0
button_press_time = 0

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.exit()
            sys.quit()
        if e.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
            screen.fill((255, 255, 255))

        current_time = pygame.time.get_ticks()
        if current_time -button_press_time > 2000:
            screen.fill((0, 0, 0))

        pygame.display.flip()
        clock.tick(60)