import pygame
from sys import exit
from random import randint



def display_score():
    current_time = int(pygame.time.get_ticks() // 1000) - start_time
    score_surf = test_font.render(f'{current_time}', False, TEXT_COLOR)
    score_rect = score_surf.get_rect(center = (400,100))
    screen.blit(score_surf, score_rect)
    return current_time

def display_gameOver():
    screen.fill(TEXT_COLOR)
    screen.blit(gameOver_surf, gameOver_rect)
    playAgain_surf = gui_font.render('HIT SPACE TO START', False, 'White')
    playAgain_rect = playAgain_surf.get_rect(center = (400, 350))
    screen.blit(playAgain_surf, playAgain_rect)


# Pygame init
pygame.init()
# seting up a display surface

# Set window size in pixels
HEIGHT = 450
WIDTH = 800

# Colors
TEXT_COLOR = (64,64,64)
boxcolor = '#c0e8ec' 

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Runner')

# Game play
game_active = True
start_time = 0
score = 0

# Frame rate
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Monoton-Regular.ttf', 96)
gui_font = pygame.font.Font(None, 32)

# test_surf = pygame.Surface((100,200))
# test_surf.fill('gold')
sky_surf = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()

# score_surf = test_font.render('THE GAME', True, (64,64,64))
# score_rect = score_surf.get_rect(center = (WIDTH / 2, 100))


gameOver_surf = test_font.render('GAME OVER', True, "Red")
gameOver_rect = gameOver_surf.get_rect(center = (WIDTH / 2, 200))


# Enemies
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_rect = snail_surf.get_rect(midbottom=(700, 300))
fly_surf = pygame.image.load('graphics/fly/Fly1.png').convert_alpha()
# fly_rect = fly_surf.get_rect(midbottom=(700, 200))




obstacle_rect_list = []

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else: 
                screen.blit(fly_surf, obstacle_rect)
        # Remove rectangles that are of screen
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x >= -100 ]
        return obstacle_list
    else: return []

# Player
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (100, 300))
player_gravity = 0
# Intro Screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 1.5)
player_stand_rect = player_stand.get_rect(center = (400, 280))

title_surf = test_font.render(f'RUNNER', True, "White").convert_alpha()
title_rect = title_surf.get_rect(center = (400,150))
playAgain_surf = gui_font.render('HIT SPACE TO START', False, 'White')
playAgain_rect = playAgain_surf.get_rect(center = (400, 380))


# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

# Game Loop
while True:
    # Listening for events
    for event in pygame.event.get():
        # Quiting game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Controls
        if game_active:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

        else:       
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    
                    game_active = True
                    start_time = pygame.time.get_ticks() // 1000
                    print(game_active)
        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright=( randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright=( randint(900, 1100), 100)))

    if game_active:
    # draw all elements in sequence 
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0, 300))
        # pygame.draw.rect(screen, boxcolor, score_rect)
        # pygame.draw.rect(screen, boxcolor, score_rect, 10)
        # pygame.draw.line(screen,'Blue', (0,0), pygame.mouse.get_pos(), 3)
        # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200,100,100))
        # screen.blit(score_surf, score_rect)
        score = display_score()
        # moving items
        # snail_rect.x -= 5
        # if snail_rect.right <= -1:
        #     snail_rect.x = 800
        # screen.blit(snail_surf, snail_rect)
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom=300    
        screen.blit(player_surf, player_rect)


        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)


        # Collision
        # if snail_rect.colliderect(player_rect):
        #   game_active = False
            

        # if player_rect.colliderect(snail_rect):
        #    print('collsion')

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint((mouse_pos)):
            
        
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')
    else: 
        # display_gameOver()
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = gui_font.render(f'Your score: {score}', False, 'white')
        score_message_rect = score_message.get_rect(center=(400, player_stand_rect.bottom + 10))
        screen.blit(title_surf, title_rect)
        if score == 0:
            screen.blit(playAgain_surf, playAgain_rect)
        else:
            screen.blit(score_message, score_message_rect)
            screen.blit(playAgain_surf, playAgain_rect)

    # update everything
    pygame.display.update()
    
    # Max frame rate
    clock.tick(60)