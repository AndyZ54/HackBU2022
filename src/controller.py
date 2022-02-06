import pygame
from src.button import Button

class Controller:
    #The Display 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.screen_name = pygame.display.set_caption("Our Game")
        self.STATE = "start"
        
        self.is_running = True

        self.start_image = pygame.image.load('assets/Next red.png')
        self.help_image = pygame.image.load('assets/Option grey.png')
        self.exit_image = pygame.image.load('assets/Cross green.png')

        self.help_button = Button(450,450, self.screen, self.help_image)
        self.start_button = Button(730, 450, self.screen, self.start_image)
        self.exit_button = Button(590, 450, self.screen, self.exit_image)

    def mainloop(self):
        '''
        The main loop that changes state based on what is occuring on screen
        args: none
        return: none
        '''
        while self.is_running:
            if self.STATE == "start":
                self.start_screen()
            elif self.STATE == "game":
                self.game()
            elif self.STATE == "help":
                self.help()
            # elif self.STATE == "end":
            #     self.endloop()
            elif self.STATE == "exit":
                self.exit_game()
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
                        self.STATE = "exit"
                    

    #The actual Game
    def game(self):
        while self.STATE == "game":
            # Placeholders for Now
            self.is_running = False
            self.STATE = "boi"
            print(self.STATE)
            pygame.quit()

    def help(self):
        while self.STATE == "help":
            # Placeholders for Now
            self.is_running = False
            self.STATE = "boi"
            print(self.STATE)
            pygame.quit()
    #Exit the Game
    def exit_game(self):
        while self.STATE == "exit":
            # Placeholders for Now
            self.STATE = "boi"
            print(self.STATE)
            self.is_running = False
            pygame.quit()