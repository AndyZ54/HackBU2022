import pygame

class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,1000))
        self.gameState = "start"
    def game(self):
        while self.gameState == "start":
            pass
    def startScreen(self):
        while self.gameState == "start":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitGame()
    def exitGame(self):
        pygame.quit()
        exit()
