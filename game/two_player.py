import random
import pygame
import sys

from pygame import display

from game_parameters import *
from background import draw_background
from game.alien1 import Alien1, aliens1
from game.alien2 import Alien2, aliens2
from game.alien3 import Alien3, aliens3
from player import Player
from player2 import Player2
from game.bullet import Bullet, bullet1
from game.bullet2 import Bullet2, bullet2

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('space')

#LIFE ICONS AND SCORE ICON

life_icon1 = pygame.image.load('../g.assets/sprites/ship.png').convert()
life_icon1.set_colorkey((255,255,255))
life_icon1 = pygame.transform.scale(life_icon1, (25, 25))
lives1 = NUM_LIVES1
life_icon2 = pygame.image.load('../g.assets/sprites/ship2.png').convert()
life_icon2.set_colorkey((255,255,255))
life_icon2 = pygame.transform.scale(life_icon2, (25, 25))
lives2 = NUM_LIVES2
score = 0
score_font = pygame.font.Font('../g.assets/fonts/ArcadeClassic.ttf', 25)
laser = pygame.mixer.Sound('../g.assets/sounds/laser.wav')

clock = pygame.time.Clock()

# INSTRUCTION SCREEN
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False

    instruction_font = pygame.font.Font('../g.assets/fonts/ArcadeClassic.ttf', 25)
    instructions = instruction_font.render('Instructions', True, (255, 225, 255))
    screen.blit(instructions,
                (SCREEN_WIDTH/3,SCREEN_HEIGHT/2))
    instructions = instruction_font.render('ARROW KEYS - RIGHT AND  LEFT', True, (255, 225, 255))
    screen.blit(instructions,
                (SCREEN_WIDTH/5.5,SCREEN_HEIGHT/2+35))
    instructions = instruction_font.render('SPACEBAR - SHOOT', True, (255, 225, 255))
    screen.blit(instructions,
                (SCREEN_WIDTH / 3.25, SCREEN_HEIGHT / 2+70))
    instructions = instruction_font.render('PRESS ENTER TO START!', True, (255, 225, 255))
    screen.blit(instructions,
                (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 + 140))
    instructions = instruction_font.render('GOOD LUCK!', True, (255, 225, 255))
    screen.blit(instructions,
                (SCREEN_WIDTH / 2.65, SCREEN_HEIGHT / 2 + 160))

    title = pygame.image.load("../g.assets/sprites/title.png").convert()
    title.set_colorkey((255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, SCREEN_HEIGHT/4 - title.get_height() / 2))

    pygame.display.flip()

#ADDING ALIENS

running = True
background = screen.copy()
draw_background(background)

for _ in range(1):
        aliens1.add(Alien1(random.randint(0, SCREEN_WIDTH), random.randint(-100,-50)))
for _ in range(1):
        aliens2.add(Alien2(random.randint(0, SCREEN_WIDTH), random.randint(-100,-50)))
for _ in range(1):
        aliens3.add(Alien3(random.randint(0, SCREEN_WIDTH), random.randint(-100,-50)))

#PLAYER LOCATION

player = Player(SCREEN_HEIGHT,SCREEN_HEIGHT)
player2 = Player2(SCREEN_HEIGHT,SCREEN_HEIGHT)

#MAIN LOOP

while running and lives1>0 and lives2>0:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        #player.stop()
                                                #fix issue with both players moving at same time, causing player1 to be unable to move
        if event.type == pygame.KEYDOWN:
            #player1 movement inputs
            if event.key == pygame.K_LEFT:
                #print(f"left key has been pressed")
                player.move_left()
            if event.key == pygame.K_RIGHT:
                #print(f"right key has been pressed")          #FIX STOP WHEN SHOOTING
                player.move_right()
            if event.key == pygame.K_UP:
                player.shoot()
                pygame.mixer.Sound.play(laser)

        #player2 movement inputs
            if event.key == pygame.K_a:
                #print(f"A key has been pressed")
                player2.move_left()
            if event.key == pygame.K_d:
                #print(f"D key has been pressed")
                player2.move_right()
            if event.key == pygame.K_s:
                player2.shoot()
                pygame.mixer.Sound.play(laser)

        #if event.type == pygame.KEYUP:
            #if event.key == pygame.K_a:
                #player2.stop()
            #if event.key == pygame.K_d:
                #player2.stop()

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








# LASER    issues with contact
        resultL1 = pygame.sprite.groupcollide(player.bullets, aliens1, True, True)
        if resultL1:
            print('hit')
            # pygame.mixer.Sound.play(hurt)
            aliens1.add(Alien1(random.randint(0, SCREEN_WIDTH), random.randint(-100, -50)))
            score += len(result)















    screen.blit(background, (0, 0))
    player.update()
    player2.update()


    score_text = score_font.render(f"Score {score}", True, (255, 255, 255))
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
    player.bullets.draw(screen)
    player2.bullets2.draw(screen)
    clock.tick(60)
    pygame.display.flip()

screen.blit(background, (0,0))
message = score_font.render('GAME OVER', True,(255,0,0))
screen.blit(message, (SCREEN_WIDTH/2 - message.get_width()/2, SCREEN_HEIGHT/2 - message.get_height()/2))
score_text = score_font.render(f"Score {score}",True,(255,255,255))
screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, SCREEN_HEIGHT/2 - 3*score_text.get_height()/2))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit

pygame.quit()
sys.exit()
