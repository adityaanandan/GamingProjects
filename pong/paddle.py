import pygame
from random import randint
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect() 
    def moveup(self, velocity):
        self.rect.y -= velocity
        if self.rect.y <0:
            self.rect.y = 0 
    def movedown(self, velocity):
        self.rect.y += velocity
        if self.rect. y > 400:
            self.rect.y = 400
