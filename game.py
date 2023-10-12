import pygame
import sys

#initalize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600

#define colors
BLUE = (0, 0, 255)
BROWN = (224, 161, 52)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('beachside')

#MainLoop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)
    rectangle_height = 200
    pygame.draw.rect(screen, BROWN, (0, screen_height-rectangle_height, screen_width, rectangle_height))

    pygame.display.flip()

