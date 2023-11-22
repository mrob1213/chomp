import pygame
import random
from game_parameters import *
class Alien1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = alien1 = pygame.image.load('../g.assets/sprites/alien1.png').convert()
        alien1.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, space):
        space.blit(self.image, (self.rect.x, self.rect.y))

aliens1 = pygame.sprite.Group()
