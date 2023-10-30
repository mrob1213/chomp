import pygame
import random
from game_parameters import *
from fish import Fish, fishes
from enemy import Enemy, enemies
def draw_background(surf):
    water = pygame.image.load('../assets/sprites/water.png').convert()
    sand = pygame.image.load('../assets/sprites/sand_top.png').convert()
    seagrass = pygame.image.load('../assets/sprites/seagrass.png').convert()

    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            surf.blit(water, (x,y))

    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        surf.blit(sand, (x,SCREEN_HEIGHT-TILE_SIZE))

    for _ in range(7):
        x = random.randint(0, SCREEN_WIDTH)
        surf.blit(seagrass, (x,SCREEN_HEIGHT-TILE_SIZE*2))
    custom_font = pygame.font.Font('../assets/fonts/VOLACROME.ttf', 50)
    text = custom_font.render('Chomp', True, (255,0,0))
    surf.blit(text, (SCREEN_WIDTH/2-text.get_width()/2,SCREEN_HEIGHT/40))

def add_fish(num_fish):
    for _ in range(num_fish):
        fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 1.5),
                        random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

def add_enemies(num_enemies):
    for _ in range(num_enemies):
        enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 1.5),
                        random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))