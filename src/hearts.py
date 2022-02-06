from turtle import position
import pygame
# import sys

class Hearts(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/heart.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.update()
    def update(self):
        self.rect.x -= 10
        if self.rect.right < 100:
            self.kill()
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))