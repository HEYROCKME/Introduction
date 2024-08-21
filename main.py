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
test_font = pygame.font.Font('fonts/Monoton-Regular.ttf', 96)

# test_surface = pygame.Surface((100,200))
# test_surface.fill('gold')
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('THE GAME', True, 'black')

# Game Loop
while True:
    # Listening for events
    for event in pygame.event.get():
        # Quiting game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # draw all elements in sequence 
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (150, 20))
    # update everything
    pygame.display.update()
    
    # Max frame rate
    clock.tick(60)