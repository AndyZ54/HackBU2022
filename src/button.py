import pygame
# import sys

class Button():
    def __init__(self,x,y, screen, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x = x
        self.y = y
        self.rect.topleft = (x,y)

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        
