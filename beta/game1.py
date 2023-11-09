import random
import pygame
from beta.alien1 import Alien1, aliens1
from beta.alien2 import Alien2, aliens2
from beta.alien3 import Alien3, aliens3
import sys

pygame.init()

screen_width = 900
screen_height = 975
tile_size = 64

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('space')

def draw_background(screen):
    space = pygame.image.load('../g.assets/sprites/space.png')

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(space, (x,y))

running = True
background = screen.copy()
draw_background(background)

for _ in range(1):
        aliens1.add(Alien1(random.randint(screen_height, screen_height),
                        random.randint(tile_size, screen_height - 2 * tile_size)))
for _ in range(1):
        aliens2.add(Alien2(random.randint(screen_height, screen_height),
                        random.randint(tile_size, screen_height - 2 * tile_size)))
for _ in range(1):
        aliens3.add(Alien3(random.randint(screen_height, screen_height),
                        random.randint(tile_size, screen_height - 2 * tile_size)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    aliens1.update()
    for alien in aliens1:
        if alien.rect.x < -alien.rect.width:
            aliens1.remove(alien)
            aliens1.add(Alien1(random.randint(screen_height, screen_height + 50), random.randint(tile_size, screen_height - 2 * tile_size)))
    aliens1.draw(screen)
    aliens2.update()
    for alien in aliens2:
        if alien.rect.x < -alien.rect.width:
            aliens2.remove(alien)
            aliens2.add(Alien1(random.randint(screen_height, screen_height + 50), random.randint(tile_size, screen_height - 2 * tile_size)))
    aliens2.draw(screen)
    aliens3.update()
    for alien in aliens3:
        if alien.rect.x < -alien.rect.width:
            aliens3.remove(alien)
            aliens3.add(Alien1(random.randint(screen_height, screen_height + 50), random.randint(tile_size, screen_height - 2 * tile_size)))
    aliens3.draw(screen)

    pygame.display.flip()



pygame.quit()
sys.exit()
