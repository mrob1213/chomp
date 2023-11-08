import pygame
import random
import sys

from game_parameters import *
from fish import Fish, fishes
from background import draw_background, add_fish, add_enemies
from player import Player
from enemy import Enemy, enemies


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('beachside1')

chomp = pygame.mixer.Sound('../assets/sounds/chomp.wav')
hurt = pygame.mixer.Sound('../assets/sounds/hurt.wav')
bubbles = pygame.mixer.Sound('../assets/sounds/bubbles.wav')

#transparency for images with black background
life_icon = pygame.image.load('../assets/sprites/orange_fish_alt.png').convert()
life_icon.set_colorkey((0,0,0))

lives = NUM_LIVES


clock = pygame.time.Clock()

running = True
background = screen.copy()
draw_background(background)

add_fish(5)
add_enemies(3)

player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

score = 0
score_font = pygame.font.Font('../assets/fonts/VOLACROME.ttf', 40)

while running and lives>0:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        player.stop()                  #comment out to get diagonal motion

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print(f"up key has been pressed")
                player.move_up()
            if event.key == pygame.K_DOWN:
                print(f"down key has been pressed")
                player.move_down()
            if event.key == pygame.K_LEFT:
                print(f"left key has been pressed")
                player.move_left()
            if event.key == pygame.K_RIGHT:
                print(f"right key has been pressed")
                player.move_right()


    screen.blit(background, (0, 0))
    fishes.update()
    enemies.update()
    player.update()

    result = pygame.sprite.spritecollide(player, fishes, True)
    print(result)
    if result:
        pygame.mixer.Sound.play(chomp)
        score += len(result)
        print(score)

        add_fish(len(result))

    result = pygame.sprite.spritecollide(player, enemies, True)
    print(result)
    if result:
        pygame.mixer.Sound.play(hurt)
        add_enemies(len(result))
        lives -= len(result)

    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            add_fish(1)

    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)
            add_enemies(1)

    fishes.draw(screen)
    enemies.draw(screen)
    player.draw(screen)
    text = score_font.render(f'{score}', True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH-TILE_SIZE, 0))

    for i in range(lives):
        screen.blit(life_icon, (i*TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE))

    clock.tick(60)
    pygame.display.flip()

screen.blit(background, (0,0))
message = score_font.render('GAME OVER', True,(255,0,0))
screen.blit(message, (SCREEN_WIDTH/2 - message.get_width()/2, SCREEN_HEIGHT/2 - message.get_height()/2))
score_text = score_font.render(f"Score: {score}",True,(255,0,255))
screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, SCREEN_HEIGHT/2 - 3*score_text.get_height()/2))

pygame.display.flip()
pygame.mixer.Sound(bubbles)

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit

pygame.quit()
sys.exit()
