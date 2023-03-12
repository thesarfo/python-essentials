
import pygame
pygame.init()

# screen details
screen_height = 600
screen_width = 800

# colors
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
black = 0, 0, 0
white = 255, 255, 255

# plaer a information
player_a_width = 20
player_a_xpos = 350
player_a_height = 100
player_a_ypos = 550

# player b information
player_b_width = 20
player_b_xpos = 350
player_b_height = 100
player_b_ypos = 20
conf_screen_width = 720

# ball information
ball_height = 20
ball_width = 20
ball_xpos = 400
ball_ypos = 300
vel = 0.5

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong Game")

# game loop and keypresses
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # detecting keypresses 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player_a_xpos < conf_screen_width - player_a_width - vel:
        player_a_xpos += vel
    if keys[pygame.K_LEFT] and player_a_xpos > vel:
        player_a_xpos -= vel
    if keys[pygame.K_d] and  player_b_xpos < conf_screen_width - player_b_width - vel:
        player_b_xpos += vel
    if keys[pygame.K_a] and player_b_xpos > vel :
        player_b_xpos -= vel
    # player and ball draw, screen fill and screen update   
    screen.fill(green)
    player_a_draw = pygame.draw.rect((screen), red, (player_a_xpos, player_a_ypos, player_a_height, player_a_width))
    player_b_draw = pygame.draw.rect((screen), blue, (player_b_xpos, player_b_ypos, player_b_height, player_b_width))
    ball = pygame.draw.rect((screen), white, (ball_xpos, ball_ypos, ball_height, ball_width))
    pygame.display.update()

    
    
