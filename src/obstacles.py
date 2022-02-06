import pygame
import random 
class Obstacles(pygame.sprite.Sprite):
    #creates and initalizes the obstacle position
    def __init__(self, x, y):
        #selects random obstacle
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        obstacleNum = random.randrange(1,5)
        if obstacleNum == 1:
            player_image = pygame.image.load('assets/obstacles/obstacle1.png')
            self.image = pygame.transform.scale(player_image, (int(player_image.get_width() * 0.4), int(player_image.get_height() * 0.4)))
        elif obstacleNum == 2:
            player_image = pygame.image.load('assets/obstacles/obstacle2.png')
            self.image = pygame.transform.scale(player_image, (int(player_image.get_width() * 0.4), int(player_image.get_height() * 0.4)))
        elif obstacleNum == 3:
            player_image = pygame.image.load('assets/obstacles/obstacle3.png')
            self.image = pygame.transform.scale(player_image, (int(player_image.get_width() * 0.4), int(player_image.get_height() * 0.4)))
        elif obstacleNum == 4:
            player_image = pygame.image.load('assets/obstacles/obstacle4.png')
            self.image = pygame.transform.scale(player_image, (int(player_image.get_width() * 0.4), int(player_image.get_height() * 0.4)))
        elif obstacleNum == 5:
            player_image = pygame.image.load('assets/obstacles/obstacle5.png')
            self.image = pygame.transform.scale(player_image, (int(player_image.get_width() * 0.4), int(player_image.get_height() * 0.4)))
        self.rect = self.image.get_rect()

    #moves obstacles across the screen
    def update(self):
        self.rect.x -= 12
        #remove obstacle when it is outside of the screen
        if self.rect.right < 100:
            self.kill()

    #draw the object
    def draw(self, screen):
        self.screen.blit(self.image, self.rect())
