import random
import pygame
import sys
from pygame import display
from game_parameters import *
from background import draw_background
from game.star import Star1, stars1
from game.alien1 import Alien1, aliens1
from game.alien2 import Alien2, aliens2
from game.alien3 import Alien3, aliens3
from game.boss import Boss1, bosses1
from player import Player
from player2 import Player2
from game.bullet import Bullet, bullet1
from game.bullet2 import Bullet2, bullet2
import random
import pygame
import sys
import time


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('space')

# ICONS,SOUNDS

lives1 = NUM_LIVES1
lives2 = NUM_LIVES2
score = 0
score2 = 0

hurt = pygame.mixer.Sound('../g.assets/sounds/hurt.wav')
laser = pygame.mixer.Sound('../g.assets/sounds/laser.wav')
game_over = pygame.mixer.Sound('../g.assets/sounds/gameover.wav')
alien_hit = pygame.mixer.Sound('../g.assets/sounds/alien.wav')
explosion = pygame.mixer.Sound('../g.assets/sounds/explosion.wav')
fox = pygame.mixer.Sound('../g.assets/sounds/fox.mp3')
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
                (SCREEN_WIDTH/3,SCREEN_HEIGHT/2.5))
    instructions = instruction_font.render('P1 ARROW KEYS - RIGHT AND  LEFT', True, (255, 225, 255))
    screen.blit(instructions,
                (SCREEN_WIDTH/5.5,SCREEN_HEIGHT/2))
    instructions = instruction_font.render('P1 SPACEBAR - SHOOT', True, (255, 225, 255))
    screen.blit(instructions,
                (SCREEN_WIDTH / 3.25, SCREEN_HEIGHT/1.85))
    instructions = instruction_font.render('P2 A D - RIGHT AND  LEFT', True, (255, 225, 255))
    screen.blit(instructions,
                (SCREEN_WIDTH / 3.75, SCREEN_HEIGHT/1.60))
    instructions = instruction_font.render('P2 W - SHOOT', True, (255, 225, 255))
    screen.blit(instructions,
                (SCREEN_WIDTH / 2.5, SCREEN_HEIGHT/1.50))
    instructions = instruction_font.render('PRESS ENTER TO START!', True, (255, 225, 255))
    screen.blit(instructions,
                (SCREEN_WIDTH / 3.75, SCREEN_HEIGHT / 2 + 140))
    instructions = instruction_font.render('GOOD LUCK!', True, (255, 225, 255))
    screen.blit(instructions,
                (SCREEN_WIDTH / 2.50, SCREEN_HEIGHT / 2 + 160))

    title = pygame.image.load("../g.assets/sprites/title.png").convert()
    title.set_colorkey((255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, SCREEN_HEIGHT/4 - title.get_height() / 2))

    pygame.display.flip()

# INSTRUCTION SCREEN2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False

    instruction_font = pygame.font.Font('../g.assets/fonts/ArcadeClassic.ttf', 25)

    instructions = instruction_font.render('BEWARE THE RED MENACE', True, (255, 0, 0))
    screen.blit(instructions,
                (SCREEN_WIDTH/3.75,SCREEN_HEIGHT-50))

    pygame.display.flip()

# ADDING ALIENS / INCREASING DIFFICULTY

background = screen.copy()
running = True
draw_background(background)

for _ in range(40):
    stars1.add(Star1(random.randint(30, SCREEN_WIDTH + 30), random.randint(-10, SCREEN_WIDTH)))

for _ in range(1):
    aliens1.add(Alien1(random.randint(30, SCREEN_WIDTH+30), random.randint(-100,-50)))
for _ in range(1):
    aliens1.add(Alien1(random.randint(30, SCREEN_WIDTH+30), random.randint(-14000,-14000)))
for _ in range(1):
    aliens1.add(Alien1(random.randint(30, SCREEN_WIDTH+30), random.randint(-25000,-25000)))

for _ in range(1):
    aliens2.add(Alien2(random.randint(30, SCREEN_WIDTH+30), random.randint(-100,-50)))
for _ in range(1):
    aliens2.add(Alien2(random.randint(30, SCREEN_WIDTH+30), random.randint(-10000,-10000)))
for _ in range(1):
    aliens2.add(Alien2(random.randint(30, SCREEN_WIDTH+30), random.randint(-21000,-21000)))

for _ in range(1):
    aliens3.add(Alien3(random.randint(30, SCREEN_WIDTH+30), random.randint(-100,-50)))
for _ in range(1):
    aliens3.add(Alien3(random.randint(30, SCREEN_WIDTH+30), random.randint(-6000,-6000)))
for _ in range(1):
    aliens3.add(Alien3(random.randint(30, SCREEN_WIDTH+30), random.randint(-13000,-13000)))

for _ in range(1):
    bosses1.add(Boss1(random.randint(30, SCREEN_WIDTH + 30), random.randint(-27500, -27500)))
for _ in range(1):
    bosses1.add(Boss1(random.randint(30, SCREEN_WIDTH + 30), random.randint(-50000, -50000)))

# PLAYER LOCATION

player = Player(SCREEN_HEIGHT,SCREEN_HEIGHT)
player2 = Player2(SCREEN_HEIGHT,SCREEN_HEIGHT)

# BACKGROUND MUSIC
pygame.mixer.Sound.play(fox)

# MAIN LOOP

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# MOVEMENT INPUTS

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_UP:
                player.shoot()
                pygame.mixer.Sound.play(laser)

            if event.key == pygame.K_a:
                player2.move_left()
            if event.key == pygame.K_d:
                player2.move_right()
            if event.key == pygame.K_w:
                player2.shoot()
                pygame.mixer.Sound.play(laser)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.stop()
            if event.key == pygame.K_RIGHT:
                player.stop()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player2.stop()
            if event.key == pygame.K_d:
                player2.stop()

# PLAYER LIVES

    result = pygame.sprite.spritecollide(player, aliens1, True)
    if result:
        pygame.mixer.Sound.play(hurt)
        aliens1.add(Alien1(random.randint(30, SCREEN_WIDTH-30), random.randint(-100, -50)))
        lives1 -= len(result)
    result = pygame.sprite.spritecollide(player, aliens2, True)
    if result:
        pygame.mixer.Sound.play(hurt)
        aliens2.add(Alien2(random.randint(30, SCREEN_WIDTH-30), random.randint(-100, -50)))
        lives1 -= len(result)
    result = pygame.sprite.spritecollide(player, aliens3, True)
    if result:
        pygame.mixer.Sound.play(hurt)
        aliens3.add(Alien3(random.randint(30, SCREEN_WIDTH-30), random.randint(-100, -50)))
        lives1 -= len(result)
    result = pygame.sprite.spritecollide(player, bosses1, True)
    if result:
        pygame.mixer.Sound.play(hurt)
        bosses1.add(Alien3(random.randint(30, SCREEN_WIDTH - 30), random.randint(-5000, -50)))
        lives1 -= 3

# PLAYER2 LIVES

    result = pygame.sprite.spritecollide(player2, aliens1, True)
    if result:
        pygame.mixer.Sound.play(hurt)
        aliens1.add(Alien1(random.randint(30, SCREEN_WIDTH-30), random.randint(-100, -50)))
        lives2 -= len(result)
    result = pygame.sprite.spritecollide(player2, aliens2, True)
    if result:
        pygame.mixer.Sound.play(hurt)
        aliens2.add(Alien2(random.randint(30, SCREEN_WIDTH-30), random.randint(-100, -50)))
        lives2 -= len(result)
    result = pygame.sprite.spritecollide(player2, aliens3, True)
    if result:
        pygame.mixer.Sound.play(hurt)
        aliens3.add(Alien3(random.randint(30, SCREEN_WIDTH-30), random.randint(-100, -50)))
        lives2 -= len(result)
    result = pygame.sprite.spritecollide(player, bosses1, True)
    if result:
        pygame.mixer.Sound.play(hurt)
        bosses1.add(Alien3(random.randint(30, SCREEN_WIDTH - 30), random.randint(-5000, -50)))
        lives2 -= 3

# LASER

    resultL1 = pygame.sprite.groupcollide(player.bullets, aliens1, True, True)
    if resultL1:
        pygame.mixer.Sound.play(alien_hit)
        aliens1.add(Alien1(random.randint(30, SCREEN_WIDTH-30), random.randint(-100, -50)))
        score += 10
    resultL1 = pygame.sprite.groupcollide(player.bullets, aliens2, True, True)
    if resultL1:
        pygame.mixer.Sound.play(alien_hit)
        aliens2.add(Alien2(random.randint(30, SCREEN_WIDTH-30), random.randint(-100, -50)))
        score += 10
    resultL1 = pygame.sprite.groupcollide(player.bullets, aliens3, True, True)
    if resultL1:
        pygame.mixer.Sound.play(alien_hit)
        aliens3.add(Alien3(random.randint(30, SCREEN_WIDTH-30), random.randint(-100, -50)))
        score += 10

    screen.blit(background, (0, 0))
    player.update()

# LASER2

    resultL2 = pygame.sprite.groupcollide(player2.bullets2, aliens1, True, True)
    if resultL2:
        pygame.mixer.Sound.play(alien_hit)
        aliens1.add(Alien1(random.randint(30, SCREEN_WIDTH - 30), random.randint(-100, -50)))
        score2 += 10
    resultL2 = pygame.sprite.groupcollide(player2.bullets2, aliens2, True, True)
    if resultL2:
        pygame.mixer.Sound.play(alien_hit)
        aliens2.add(Alien2(random.randint(30, SCREEN_WIDTH - 30), random.randint(-100, -50)))
        score2 += 10
    resultL2 = pygame.sprite.groupcollide(player2.bullets2, aliens3, True, True)
    if resultL2:
        pygame.mixer.Sound.play(alien_hit)
        aliens3.add(Alien3(random.randint(30, SCREEN_WIDTH - 30), random.randint(-100, -50)))
        score2 += 10

    screen.blit(background, (0, 0))
    player2.update()


# RECYCLING ALIENS

    aliens1.update()
    for alien in aliens1:
        if alien.rect.y > SCREEN_HEIGHT:
            aliens1.remove(alien)
            aliens1.add(Alien1(random.randint(20, SCREEN_WIDTH-20), random.randint(-100,-50)))
    aliens1.draw(screen)

    aliens2.update()
    for alien2 in aliens2:
        if alien2.rect.y > SCREEN_HEIGHT:
            aliens2.remove(alien2)
            aliens2.add(Alien2(random.randint(20, SCREEN_WIDTH-20), random.randint(-100, -50)))
    aliens2.draw(screen)

    aliens3.update()
    for alien3 in aliens3:
        if alien3.rect.y > SCREEN_HEIGHT:
            aliens3.remove(alien3)
            aliens3.add(Alien3(random.randint(20, SCREEN_WIDTH-20), random.randint(-100, -50)))
    aliens3.draw(screen)


    bosses1.update()
    for boss1 in bosses1:
        if boss1.rect.y > SCREEN_HEIGHT:
            bosses1.remove(boss1)
            bosses1.add(Boss1(random.randint(20, SCREEN_WIDTH - 20), random.randint(-5000,-50)))
    bosses1.draw(screen)

# STAR BACKGROUND

    stars1.update()
    for star1 in stars1:
        if star1.rect.y > SCREEN_HEIGHT:
            stars1.remove(star1)
            stars1.add(Star1(random.randint(20, SCREEN_WIDTH - 20), random.randint(-5000, -50)))
    stars1.draw(screen)

# SCORE AND LIVES DISPLAY

    score_font = pygame.font.Font('../g.assets/fonts/ArcadeClassic.ttf', 25)
    life_icon1 = pygame.image.load('../g.assets/sprites/ship.png').convert()
    life_icon1.set_colorkey((255, 255, 255))
    life_icon1 = pygame.transform.scale(life_icon1, (25, 25))

    life_icon2 = pygame.image.load('../g.assets/sprites/ship2.png').convert()
    life_icon2.set_colorkey((255, 255, 255))
    life_icon2 = pygame.transform.scale(life_icon2, (25, 25))

    score_text = score_font.render(f"Score {score}", True, (72, 181, 217))
    screen.blit(score_text,
                (360, 20))

    score2_text = score_font.render(f"Score {score2}", True, (135, 233, 165))
    screen.blit(score2_text,
                (40, 20))

    for i in range(lives1):
        screen.blit(life_icon1, (i*TILE_SIZE+320, SCREEN_HEIGHT-TILE_SIZE/1.5))
    lives1_text = score_font.render(f"PLAYER 1", True, (255, 255, 255))
    screen.blit(lives1_text,(350, SCREEN_HEIGHT-TILE_SIZE-5))


    for i in range(lives2):
        screen.blit(life_icon2, (i * TILE_SIZE+30, SCREEN_HEIGHT - TILE_SIZE / 1.5))
    lives2_text = score_font.render(f"PLAYER 2", True, (255, 255, 255))
    screen.blit(lives2_text, (60, SCREEN_HEIGHT - TILE_SIZE-5))

# CHECK PLAYER LIVES
    if lives1 > 0:
        player.draw(screen)
        player.bullets.draw(screen)
    else:
        player.kill()
    if lives2 > 0:
        player2.draw(screen)
        player2.bullets2.draw(screen)
    else:
        player2.kill()

    if lives1==0 or lives2==0:
        break

    clock.tick(60)
    pygame.display.flip()

# GAME OVER SCREEN

screen.blit(background, (0,0))
message = score_font.render('GAME OVER', True,(255,0,0))
pygame.mixer.Sound.play(game_over)
screen.blit(message, (SCREEN_WIDTH/2 - message.get_width()/2, SCREEN_HEIGHT/2 - message.get_height()/1.25))
score_text = score_font.render(f"Score {score}",True,(72, 181, 217))
screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, SCREEN_HEIGHT/2 - 3*score_text.get_height()+80))
score_text2 = score_font.render(f"Score {score2}",True,(135, 233, 165))
screen.blit(score_text2, (SCREEN_WIDTH/2 - score_text.get_width()/2, SCREEN_HEIGHT/2 - 3*score_text2.get_height()+105))

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit

pygame.quit()
sys.exit()