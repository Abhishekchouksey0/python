import pygame
import random

# initialize the game engine
pygame.init()

# set screen width and height
screen_width = 1000
screen_height = 800

# create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# set the title of the window
pygame.display.set_caption("Action Game")

# player properties
player_width = 50
player_height = 50
player_x = (screen_width / 2) - (player_width / 2)
player_y = (screen_height - player_height) - 10

# enemy properties
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = 0
enemy_speed = 5

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update player position based on key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    # keep player within screen bounds
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width

    # update enemy position
    enemy_y += enemy_speed

    # check for collision
    if enemy_y + enemy_height >= player_y and enemy_x < player_x + player_width and enemy_x + enemy_width > player_x:
        print("Game Over")
        running = False

    # keep enemy within screen bounds
    if enemy_y > screen_height:
        enemy_y = 0
        enemy_x = random.randint(0, screen_width - enemy_width)

    # fill the screen with white color
    screen.fill((255, 255, 255))

    # draw the player
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))

    # draw the enemy
    pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, enemy_width, enemy_height))

    # update the screen
    pygame.display.update()

# deinitialize the game engine
pygame.quit()
