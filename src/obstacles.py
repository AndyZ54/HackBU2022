import pygame

class Obstacles:
    #creates and initalizes the obstacle position
    def__init__(self):
        #selects random obstacle
        obstacleNum = random.randrange(1,5)
        if obstacleNum == 1:
            self.image = pygame.image.load('assets/obstacle1.png')
        elif obstacleNum == 2:
            self.image = pygame.image.load('assets/obstacle2.png')
        elif obstacleNum == 3:
            self.image = pygame.image.load('assets/obstacle3.png')
        elif obstacleNum == 4:
            self.image = pygame.image.load('assets/obstacle4.png')
        elif obstacleNum == 5:
            self.image = pygame.image.load('assets/obstacle5.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1600

    #moves obstacles across the screen
    def update(self):
        self.rect.x -= 60
        #remove obstacle when it is outside of the screen
        if self.x < -self.rect.width:
            self.obstacles.pop()

    #draw the object
    def draw(self, pygame.display.set_mode((1600,900))):
        screen.blit(self.image, self.rect())
