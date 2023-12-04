import pygame
import random
from game import player
from game_parameters import *

class Star1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../g.assets/sprites/star.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (3,3))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(STAR_SPEED1, STAR_SPEED2)
        self.rect.center = (x,y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, space):
        space.blit(self.image, self.rect) #(self.rect.x, self.rect.y))



stars1 = pygame.sprite.Group()

