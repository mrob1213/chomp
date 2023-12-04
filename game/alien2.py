import pygame
import random
from game_parameters import *


class Alien2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../g.assets/sprites/alien2.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(ALIEN2a, ALIEN2b)
        self.rect.center = (x,y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, space):
        space.blit(self.image, (self.rect.x, self.rect.y))

aliens2 = pygame.sprite.Group()
