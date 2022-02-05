import pygame

class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,1000))
        self.gameState = "start"
    def game(self):
        while self.gameState == "start":
            print("hello")
