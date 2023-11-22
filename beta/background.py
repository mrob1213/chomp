import pygame
from game_parameters import *
def draw_background(screen):
    space = pygame.image.load('../g.assets/sprites/space.png')

    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(space, (x,y))

