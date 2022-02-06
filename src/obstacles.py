import pygame
import random 
class Obstacles(pygame.sprite.Sprite):
    #creates and initalizes the obstacle position
    def __init__(self, x, y, obstacleNum):
        #selects random obstacle
        pygame.sprite.Sprite.__init__(self)
        
        
        if obstacleNum == 1:
            the_image = pygame.image.load('assets/obstacle/cone.png')
            the_image = pygame.transform.scale(the_image, (int(the_image.get_width() * 0.5), int(the_image.get_height() * 0.5)))
            self.image = the_image
        elif obstacleNum == 2:
            the_image = pygame.image.load('assets/obstacle/dog.png')
            the_image = pygame.transform.scale(the_image, (int(the_image.get_width() * 0.5), int(the_image.get_height() * 0.5)))
            self.image = the_image
        elif obstacleNum == 3:
            the_image = pygame.image.load('assets/obstacle/garbage.png')
            the_image = pygame.transform.scale(the_image, (int(the_image.get_width() * 0.5), int(the_image.get_height() * 0.5)))
            self.image = the_image
        elif obstacleNum == 4:
            the_image = pygame.image.load('assets/obstacle/hyrant.png')
            the_image = pygame.transform.scale(the_image, (int(the_image.get_width() * 0.5), int(the_image.get_height() * 0.5)))
            self.image = the_image
        elif obstacleNum == 5:
            the_image = pygame.image.load('assets/obstacle/poop.png')
            the_image = pygame.transform.scale(the_image, (int(the_image.get_width() * 1), int(the_image.get_height() * 1)))
            self.image = the_image
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.update()

    #moves obstacles across the screen
    def update(self):
        self.rect.x -= 12
        #remove obstacle when it is outside of the screen
        if self.rect.right < 100:
            self.kill()

    #draw the object
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
