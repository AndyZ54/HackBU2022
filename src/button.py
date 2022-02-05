import pygame
# import sys

class Button():
    def __init__(self,x,y, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (x,y)

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        
