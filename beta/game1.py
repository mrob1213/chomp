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
        aliens1.add(Alien1(random.randint(5,895),
                        random.randint(5,970)))
for _ in range(1):
        aliens2.add(Alien2(random.randint(5,895),
                        random.randint(5,970)))
for _ in range(1):
        aliens3.add(Alien3(random.randint(5,895),
                        random.randint(5,970)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    aliens1.update()
    for alien in aliens1:
        if alien.rect.x < -alien.rect.width:
            aliens1.remove(alien)
            aliens1.add(Alien1(random.randint(910,910), random.randint(5,790)))
    aliens1.draw(screen)
    aliens2.update()
    for alien2 in aliens2:
        if alien2.rect.x < -alien2.rect.width:
            aliens2.remove(alien2)
            aliens2.add(Alien1(random.randint(910,910), random.randint(5,790)))
    aliens2.draw(screen)
    aliens3.update()
    for alien3 in aliens3:
        if alien3.rect.x < -alien3.rect.width:
            aliens3.remove(alien3)
            aliens3.add(Alien1(random.randint(910,910), random.randint(5,790)))
    aliens3.draw(screen)

    pygame.display.flip()



pygame.quit()
sys.exit()
