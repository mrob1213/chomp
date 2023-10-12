import random

import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
tile_size = 64

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('beachside1')

def draw_background(screen):
    water = pygame.image.load('assets/sprites/water.png').convert()
    sand = pygame.image.load('assets/sprites/sand_top.png').convert()
    seagrass = pygame.image.load('assets/sprites/seagrass.png').convert()

    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x,y))

    for x in range(0, screen_width, tile_size):
        screen.blit(sand, (x,screen_height-tile_size))

    for _ in range(7):
        x = random.randint(0, screen_width)
        screen.blit(seagrass, (x,screen_height-tile_size*2))

running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))

    pygame.display.flip()

pygame.quit()

