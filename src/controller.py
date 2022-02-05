import pygame
from src.button import Button

class Controller:
    #The Display 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.screen_name = pygame.display.set_caption("Our Game")
        self.STATE = "start"

        self.start_image = pygame.image.load('assets/Next red.png')
        self.help_image = pygame.image.load('assets/Option grey.png')
        self.exit_image = pygame.image.load('assets/Cross green.png')

        self.help_button = Button(450,450, self.screen, self.help_image)
        self.start_button = Button(730, 450, self.screen, self.start_image)
        self.exit_button = Button(640, 600, self.screen, self.exit_image)


    #Start Screen
    def start_screen(self):
        while self.STATE == "start":
            # self.screen.fill((0,0,0,0))

            self.screen.fill((0,200,240))
            self.start_button.draw()
            self.exit_button.draw()
            self.help_button.draw()

            pygame.display.update() 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.rect.collidepoint(event.pos):
                        print("start game")
                        self.STATE = "game"
                    if self.help_button.rect.collidepoint(event.pos):
                        print("help game")
                        self.STATE = "help"
                    if self.exit_button.rect.collidepoint(event.pos):
                        print("exit game")
                        self.STATE = "help"
                    

    #The actual Game
    def game(self):
        while self.STATE == "game":
            pass

      
    #Exit the Game
    def exit_game(self):
        pygame.quit()