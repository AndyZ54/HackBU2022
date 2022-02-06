from turtle import position
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
        self.clicked = False

    def draw(self):

        # self.position = pygame.mouse.get_pos()  

        # if self.rect.collidepoint(self.position):
        #     if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        #         self.clicked = True
        # if pygame.mouse.get_pressed()[0] == 0:
        #     self.clicked = False
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        
