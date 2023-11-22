import pygame
import sys

class Bullet2(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet2,self).__init__()
        #self.width = 4
        #self.height = 4
        #self.size = (self.width,self.height)
        self.image = self.image = pygame.image.load("../g.assets/sprites/laser2.png").convert()
        self.image.set_colorkey((0,0,0)) #pygame.Surface(self.size)
        self.image = pygame.transform.scale(self.image, (30, 30))
        #self.color = ((255,255,255))
        #self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = -7

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
