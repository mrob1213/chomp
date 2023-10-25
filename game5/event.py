import random
import pygame
import sys

from background import draw_background
from game_parameters import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('beachside1')

running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print(f"up key has been pressed")
            if event.key == pygame.K_DOWN:
                print(f"down key has been pressed")
            if event.key == pygame.K_LEFT:
                print(f"left key has been pressed")
            if event.key == pygame.K_RIGHT:
                print(f"right key has been pressed")


    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()

