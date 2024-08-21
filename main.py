import pygame
from sys import exit


# Pygame init
pygame.init()
# seting up a display surface

# Set window size in pixels
HEIGHT = 450
WIDTH = 800
 
# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Runner')

# Frame rate
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill('gold')

# Game Loop
while True:
    for event in pygame.event.get():
        # Quiting game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface, (200,100))
    # draw all elements 
    # update everything
    pygame.display.update()
    
    # Max frame rate
    clock.tick(60)