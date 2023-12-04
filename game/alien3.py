import pygame
import random
from game_parameters import *

class Alien3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #alien1
        self.image = pygame.image.load('../g.assets/sprites/alien3.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(ALIEN3a, ALIEN3b)
        self.rect.center = (x,y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, space):
        space.blit(self.image, (self.rect.x, self.rect.y))

aliens3 = pygame.sprite.Group()