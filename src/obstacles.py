import pygame

class Obstacles:
    #creates and initalizes the obstacle position
    def__init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = #Screen width

    #moves obstacles across the screen
    def update(self):
        self.rect.x -= #speed of game
        #remove obstacle when it is outside of the screen
        if self.x < -self.rect.width:
            self.obstacles.pop()

    #draw the object
    def draw(self,)
