import random
import pygame
import sys

from fish import Fish, fishes

pygame.init()

screen_width = 800
screen_height = 600
tile_size = 64

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('beachside1')

clock = pygame.time.Clock()
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
    custom_font = pygame.font.Font('assets/fonts/VOLACROME.ttf', 50)
    text = custom_font.render('Chomp', True, (255,0,0))
    surf.blit(text, (screen_width/2-text.get_width()/2,screen_height/40))

running = True
background = screen.copy()
draw_background(background)

for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*1.5), random.randint(tile_size, screen_height-2*tile_size)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    fishes.update()
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width + 50),
                            random.randint(tile_size, screen_height - 2 * tile_size)))

    fishes.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
