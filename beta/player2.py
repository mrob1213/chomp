import pygame
from game_parameters import *


class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../g.assets/sprites/ship2.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.image = self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_left(self):
        self.x_speed = -1 * PLAYER2_SPEED

    def move_right(self):
        self.x_speed = PLAYER2_SPEED

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > SCREEN_WIDTH - TILE_SIZE:
            self.x = SCREEN_WIDTH - TILE_SIZE
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.y > SCREEN_HEIGHT - 2 * TILE_SIZE:
            self.y = SCREEN_HEIGHT - 2 * TILE_SIZE
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, space):
        space.blit(self.image, self.rect)
