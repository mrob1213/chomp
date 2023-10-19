import random

import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
tile_size = 64

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('beachside1')

custom_font = pygame.font.Font('assets/fonts/VOLACROME.ttf', 50)

def draw_background(surf):
    water = pygame.image.load('assets/sprites/water.png').convert()
    sand = pygame.image.load('assets/sprites/sand_top.png').convert()
    seagrass = pygame.image.load('assets/sprites/seagrass.png').convert()

    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,y))

    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x,screen_height-tile_size))

    for _ in range(7):
        x = random.randint(0, screen_width)
        surf.blit(seagrass, (x,screen_height-tile_size*2))

    text = custom_font.render('Chomp', True, (255,0,0))
    surf.blit(text, (screen_width/2-text.get_width()/2,screen_height/40))

def draw_fishes(surf):
    green_fish = pygame.image.load('assets/sprites/green_fish.png').convert()
    green_fish = pygame.transform.flip(green_fish, True, False)
    green_fish.set_colorkey((0,0,0))
    for _ in range(3):
        x = random.randint(0, screen_width-tile_size)
        y = random.randint(0, screen_height-tile_size*2)
        surf.blit(green_fish, (x,y))
    orange_fish = pygame.image.load('assets/sprites/orange_fish.png').convert()
    orange_fish.set_colorkey((0, 0, 0))
    for _ in range(3):
        x = random.randint(0, screen_width - tile_size)
        y = random.randint(0, screen_height-tile_size*2)
        surf.blit(orange_fish, (x, y))
    puffer_fish = pygame.image.load('assets/sprites/puffer_fish.png').convert()
    puffer_fish.set_colorkey((0, 0, 0))
    for _ in range(3):
        x = random.randint(0, screen_width - tile_size)
        y = random.randint(0, screen_height-tile_size*2)
        surf.blit(puffer_fish, (x, y))

running = True
background = screen.copy()
draw_background(background)
draw_fishes(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))



    pygame.display.flip()

pygame.quit()



