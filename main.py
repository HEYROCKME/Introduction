import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
        self.walk = [player_walk_1, player_walk_2]
        self.walk_index = 0
        self.image = self.walk[self.walk_index]
        self.rect = self.image.get_rect(midbottom = (200, 300 ))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300: 
            self.rect.bottom = 300
    
    def animation(self):
            # player jumping when off ground
        if self.rect.bottom < 300:
            self.player_surf = self.jump
        else:
        # player walking when on ground
            self.walk_index += 0.1
            if self.walk_index >= len(self.walk):
                self.walk_index = 0
            self.image = self.walk[int(self.walk_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()

class Obstacles(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'fly':
            fly_frame_1 = pygame.image.load('graphics/fly/Fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('graphics/fly/Fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210
        else:
            snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300
        self.animation_index = 0 

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
    
    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation()
        self.rect.x -= 6
        self.destroy()
    
    def destroy(self):
        if self.rect.x <=-100:
            self.kill()




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

# Collisions

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else: return True

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
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.5)

# Frame rate
clock = pygame.time.Clock()

# Fonts
test_font = pygame.font.Font('fonts/Monoton-Regular.ttf', 96)
gui_font = pygame.font.Font(None, 32)

sky_surf = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()


gameOver_surf = test_font.render('GAME OVER', True, "Red")
gameOver_rect = gameOver_surf.get_rect(center = (WIDTH / 2, 200))



# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())
bg_music.play(loops = -1)
obstacle_group = pygame.sprite.Group()



# GUI Setup
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 1.5)
player_stand_rect = player_stand.get_rect(center = (400, 280))

title_surf = test_font.render(f'RUNNER', True, "White").convert_alpha()
title_rect = title_surf.get_rect(center = (400,150))
playAgain_surf = gui_font.render('HIT SPACE TO START', False, 'White')
playAgain_rect = playAgain_surf.get_rect(center = (400, 380))


# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

# Game Loop
while True:
    # Listening for events
    for event in pygame.event.get():
        # Quiting game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Controls
        if game_active == False:         
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks() // 1000
                
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacles(choice(['fly', 'snail', 'snail'])))


    if game_active:
    # draw all elements in sequence
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0, 300))
        
        score = display_score()

        # Player
        player.draw(screen)
        player.update()
        # Obstacle movement
        obstacle_group.draw(screen)
        obstacle_group.update()

        # Collision        
        game_active = collision_sprite()
            


    else: 
        
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        playAgain_rect.midbottom = (80, 300)
        player_gravity = 0
       

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