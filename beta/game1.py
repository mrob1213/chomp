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

life_icon1 = pygame.image.load('../g.assets/sprites/ship.png').convert()
life_icon1.set_colorkey((255,255,255))
life_icon1 = pygame.transform.scale(life_icon1, (35, 35))
lives1 = NUM_LIVES1
life_icon2 = pygame.image.load('../g.assets/sprites/ship2.png').convert()
life_icon2.set_colorkey((255,255,255))
life_icon2 = pygame.transform.scale(life_icon2, (35, 35))
lives2 = NUM_LIVES2
score = 0
score_font = pygame.font.Font('../g.assets/fonts/ArcadeClassic.ttf', 25)

clock = pygame.time.Clock()

running = True
background = screen.copy()
draw_background(background)

for _ in range(1):
        aliens1.add(Alien1(random.randint(0, SCREEN_WIDTH), random.randint(-100,-50)))
for _ in range(1):
        aliens2.add(Alien2(random.randint(0, SCREEN_WIDTH), random.randint(-100,-50)))
for _ in range(1):
        aliens3.add(Alien3(random.randint(0, SCREEN_WIDTH), random.randint(-100,-50)))

#location of player1/2
player = Player(SCREEN_HEIGHT,SCREEN_HEIGHT)
player2 = Player2(SCREEN_HEIGHT,SCREEN_HEIGHT)

while running and lives1>0 and lives2>0:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        player.stop()
                                                #fix issue with both players moving at same time, causing player1 to be unable to move
        if event.type == pygame.KEYDOWN:
            #player1 movement inputs
            if event.key == pygame.K_LEFT:
                #print(f"left key has been pressed")
                player.move_left()
            if event.key == pygame.K_RIGHT:
                #print(f"right key has been pressed")
                player.move_right()

        #player2 movement inputs
            if event.key == pygame.K_a:
                #print(f"A key has been pressed")
                player2.move_left()
            if event.key == pygame.K_d:
                #print(f"D key has been pressed")
                player2.move_right()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player2.stop()
            if event.key == pygame.K_d:
                player2.stop()

        #Player1 lives
        result = pygame.sprite.spritecollide(player, aliens1, True)
        print(result)
        if result:
            #pygame.mixer.Sound.play(hurt)
            aliens1.add(Alien1(random.randint(0, SCREEN_WIDTH), random.randint(-100, -50)))
            lives1 -= len(result)
        result = pygame.sprite.spritecollide(player, aliens2, True)
        print(result)
        if result:
            # pygame.mixer.Sound.play(hurt)
            aliens2.add(Alien2(random.randint(0, SCREEN_WIDTH), random.randint(-100, -50)))
            lives1 -= len(result)
        result = pygame.sprite.spritecollide(player, aliens3, True)
        print(result)
        if result:
            # pygame.mixer.Sound.play(hurt)
            aliens3.add(Alien3(random.randint(0, SCREEN_WIDTH), random.randint(-100, -50)))
            lives1 -= len(result)

        #Player2 lives
        result2 = pygame.sprite.spritecollide(player2, aliens1, True)
        print(result2)
        if result2:
            # pygame.mixer.Sound.play(hurt)
            aliens1.add(Alien1(random.randint(0, SCREEN_WIDTH), random.randint(-100, -50)))
            lives2 -= len(result2)
        result2 = pygame.sprite.spritecollide(player2, aliens2, True)
        print(result2)
        if result2:
            # pygame.mixer.Sound.play(hurt)
            aliens2.add(Alien2(random.randint(0, SCREEN_WIDTH), random.randint(-100, -50)))
            lives2 -= len(result2)
        result2 = pygame.sprite.spritecollide(player2, aliens3, True)
        print(result2)
        if result2:
            # pygame.mixer.Sound.play(hurt)
            aliens3.add(Alien3(random.randint(0, SCREEN_WIDTH), random.randint(-100, -50)))
            lives2 -= len(result2)


    screen.blit(background, (0, 0))
    player.update()
    player2.update()
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text,
                (385,20))

    aliens1.update()
    for alien in aliens1:
        if alien.rect.y > SCREEN_HEIGHT:
            aliens1.remove(alien)
            aliens1.add(Alien1(random.randint(0, SCREEN_WIDTH), random.randint(-100,-50)))
    aliens1.draw(screen)

    aliens2.update()
    for alien2 in aliens2:
        if alien2.rect.y > SCREEN_HEIGHT:
            aliens2.remove(alien2)
            aliens2.add(Alien2(random.randint(0, SCREEN_WIDTH), random.randint(-100, -50)))
    aliens2.draw(screen)

    aliens3.update()
    for alien3 in aliens3:
        if alien3.rect.y > SCREEN_HEIGHT:
            aliens3.remove(alien3)
            aliens3.add(Alien3(random.randint(0, SCREEN_WIDTH), random.randint(-100, -50)))
    aliens3.draw(screen)

    for i in range(lives1):
        screen.blit(life_icon1, (i*TILE_SIZE+325, SCREEN_HEIGHT-TILE_SIZE))
    for i in range(lives2):
        screen.blit(life_icon2, (i*TILE_SIZE+10, SCREEN_HEIGHT-TILE_SIZE))

    player.draw(screen)
    player2.draw(screen)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()
