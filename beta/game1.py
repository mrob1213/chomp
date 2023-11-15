import random
import pygame
import sys
from game_parameters import *
from background import draw_background
from beta.alien1 import Alien1, aliens1
from beta.alien2 import Alien2, aliens2
from beta.alien3 import Alien3, aliens3
from player import Player
from player2 import Player2

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('space')

clock = pygame.time.Clock()

running = True
background = screen.copy()
draw_background(background)

for _ in range(1):
        aliens1.add(Alien1(random.randint(SCREEN_WIDTH, int(SCREEN_WIDTH * 1.5)), random.randint(0, SCREEN_HEIGHT)))
for _ in range(1):
        aliens2.add(Alien2(random.randint(SCREEN_WIDTH, int(SCREEN_WIDTH * 1.5)), random.randint(0, SCREEN_HEIGHT)))
for _ in range(1):
        aliens3.add(Alien3(random.randint(SCREEN_WIDTH, int(SCREEN_WIDTH * 1.5)), random.randint(0, SCREEN_HEIGHT)))

player = Player(SCREEN_HEIGHT,SCREEN_HEIGHT)
player2 = Player2(SCREEN_HEIGHT,SCREEN_HEIGHT)

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        player.stop()
        player2.stop()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print(f"left key has been pressed")
                player.move_left()
            if event.key == pygame.K_RIGHT:
                print(f"right key has been pressed")
                player.move_right()

            if event.key == pygame.K_a:                         #A and D keys dont work, but up and down do?
                print(f"A key has been pressed")
                player2.move_left()
            if event.key == pygame.K_d:
                print(f"D key has been pressed")
                player2.move_right()

    screen.blit(background, (0, 0))
    aliens1.update()
    player.update()
    player2.update()


    for alien in aliens1:
        if alien.rect.x < -alien.rect.width:
            aliens1.remove(alien)
            aliens1.add(Alien1(random.randint(SCREEN_WIDTH, SCREEN_WIDTH+50), random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))
    aliens1.draw(screen)
    aliens2.update()
    for alien2 in aliens2:
        if alien2.rect.x < -alien2.rect.width:
            aliens2.remove(alien2)
            aliens2.add(Alien2(random.randint(SCREEN_WIDTH, SCREEN_WIDTH+50), random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))
    aliens2.draw(screen)
    aliens3.update()
    for alien3 in aliens3:
        if alien3.rect.x < -alien3.rect.width:
            aliens3.remove(alien3)
            aliens3.add(Alien3(random.randint(SCREEN_WIDTH, SCREEN_WIDTH+50), random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))
    aliens3.draw(screen)

    player.draw(screen)
    player2.draw(screen)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()
