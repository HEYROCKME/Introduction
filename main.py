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
sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = test_font.render('THE GAME', True, 'black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
print(snail_surface)
snail_x_position = 600

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))

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
    # moving items
    snail_x_position -= 5
    if snail_x_position <= -72:
        snail_x_position = 800
    screen.blit(snail_surface, (snail_x_position, 265))
    screen.blit(player_surface, player_rect)

    # update everything
    pygame.display.update()
    
    # Max frame rate
    clock.tick(60)