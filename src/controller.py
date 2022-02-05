import pygame
from pyparsing import White
from src.button import Button

class Controller:
    #The Display 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.screen_name = pygame.display.set_caption("Our Game")
        self.game_state = "start"

        self.start_image = pygame.image.load('assets/Next red.png')
        self.end_image = pygame.image.load('assets/Option grey.png')
        self.end_button = Button(450,450, self.screen, self.end_image)
        self.start_button = Button(730, 450, self.screen, self.start_image)

    #Start Screen
    def start_screen(self):
        while self.game_state == "start":
            # self.screen.fill((0,0,0,0))

            self.screen.fill((0,200,240))
            self.start_button.draw()
            self.end_button.draw()
            pygame.display.update() 
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()

    #The actual Game
    def game(self):
        while self.game_state == "game":
            pass 
      
    #Exit the Game
    def exit_game(self):
        pygame.quit()