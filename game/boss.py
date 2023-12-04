import pygame
import random
from game import player
from game_parameters import *

class Boss1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../g.assets/sprites/boss.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (65,65))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(BOSS_SPEED1, BOSS_SPEED2)
        self.rect.center = (x,y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, space):
        space.blit(self.image, self.rect) #(self.rect.x, self.rect.y))



bosses1 = pygame.sprite.Group()

