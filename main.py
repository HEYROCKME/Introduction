import pygame
from sys import exit


# Pygame init
pygame.init()
# seting up a display surface

# Set window size in pixels
HEIGHT = 450
WIDTH = 800

# Colors
text_color = (64,64,64)
boxcolor = '#c0e8ec' 

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
score_surface = test_font.render('THE GAME', True, (64,64,64))
score_rect = score_surface.get_rect(center = (400, 100))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(700, 300))
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
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            if player_rect.collidepoint((event.pos)):
                print("collison")
    
    # draw all elements in sequence 
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, boxcolor, score_rect)
    pygame.draw.rect(screen, boxcolor, score_rect, 10)
    # pygame.draw.line(screen,'Blue', (0,0), pygame.mouse.get_pos(), 3)
    pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200,100,100))
    screen.blit(score_surface, score_rect)
    # moving items
    snail_rect.x -= 5
    if snail_rect.right <= -1:
        snail_rect.x = 800
    screen.blit(snail_surface, snail_rect)
    player_rect.left +=1
    screen.blit(player_surface, player_rect)
    # Collision

    # if player_rect.colliderect(snail_rect):
    #    print('collsion')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
        
    
    # update everything
    pygame.display.update()
    
    # Max frame rate
    clock.tick(60)