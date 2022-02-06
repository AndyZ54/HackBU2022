import pygame
<<<<<<< HEAD
import random 
=======
import random

>>>>>>> b382f6669beaba9cc8067a1d4c62d8a9b435dc4b
class Obstacles:
    #creates and initalizes the obstacle position
    def __init__(self):
        #selects random obstacle
        obstacleNum = random.randrange(1,5)
        if obstacleNum == 1:
            self.image = pygame.image.load('assets/obstacles/obstacle1.png')
        elif obstacleNum == 2:
            self.image = pygame.image.load('assets/obstacles/obstacle2.png')
        elif obstacleNum == 3:
            self.image = pygame.image.load('assets/obstacles/obstacle3.png')
        elif obstacleNum == 4:
            self.image = pygame.image.load('assets/obstacles/obstacle4.png')
        elif obstacleNum == 5:
            self.image = pygame.image.load('assets/obstacles/obstacle5.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1600

    #moves obstacles across the screen
    def update(self):
        self.rect.x -= 60
        #remove obstacle when it is outside of the screen
        if self.x < -self.rect.width:
            self.obstacles.pop()

    #draw the object
<<<<<<< HEAD
    def draw(self, pygame.display.set_mode((1600,900))):
        self.screen.blit(self.image, self.rect())
=======
    def draw(self, screen):
        screen.blit(self.image, self.rect())
>>>>>>> b382f6669beaba9cc8067a1d4c62d8a9b435dc4b
