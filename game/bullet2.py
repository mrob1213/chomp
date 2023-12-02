import pygame
import sys

class Bullet2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.image = pygame.image.load("../g.assets/sprites/laser2.png").convert()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = -7

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def draw(self, space):
        space.blit(self.image, self.rect)

bullet2 = pygame.sprite.Group()
