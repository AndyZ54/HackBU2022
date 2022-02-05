import pygame

class Start(pygame.sprite.Sprite):
    def __init__(self,fn):
        self.initial_image = pygame.image.load('assets/Next red.png')
        self.rect = self.image.get_rect()
        self.rect.x = 615
        self.rect.y = 470