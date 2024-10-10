import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player variables
player_pos = [400, 300]
player_size = 50
player_speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.flip()

pygame.quit()
