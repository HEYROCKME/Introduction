import pygame
from sys import exit


# Pygame init
pygame.init()
# seting up a display surface
HEIGHT = 600
WIDTH = 800
 
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Runner')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # draw all elements 
    # update everything
    pygame.display.update()