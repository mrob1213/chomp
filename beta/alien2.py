import pygame
import random

MIN_SPEED = 0.2
MAX_SPEED = 0.5
class Alien2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #alien1
        self.image = alien2 = pygame.image.load('../g.assets/sprites/alien2.png').convert()
        alien2.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, space):
        space.blit(self.image, self.rect)

aliens2 = pygame.sprite.Group()
