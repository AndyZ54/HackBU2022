from turtle import position
import pygame
# import sys

class Hearts(pygame.sprite.Sprite):
    def __init__(self,x,y, screen, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.screen = screen
        self.screen.blit(self.image, (self.rect.x, self.rect.y))