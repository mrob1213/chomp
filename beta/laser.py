import pygame
import sys

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("../g.assets/sprites/laser.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))

    def update(self):
        self.rect.y += 5