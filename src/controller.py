import pygame
from src.button import Button
from src.player import Player

class Controller():
    #The Display 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1600,900))
        self.screen_name = pygame.display.set_caption("Love Message")
        self.STATE = "start"
        
        self.is_running = True

        self.start_image = pygame.image.load('assets/start.png')
        self.help_image = pygame.image.load('assets/help.png')
        self.exit_image = pygame.image.load('assets/exit.png')
        self.title = pygame.image.load('assets/lovemessage.png')
        self.background = pygame.image.load('assets/background.png')

        self.help_button = Button(40,660, self.screen, self.help_image)
        self.start_button = Button(550, 660, self.screen, self.start_image)
        self.exit_button = Button(1050, 660, self.screen, self.exit_image)
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.title, (25,100))
        
        self.player = Player(100,100,self.screen)

    def mainloop(self):
        while self.is_running == True:
            if self.STATE == "start":
                self.start_screen()
            elif self.STATE == "game":
                self.game()
            elif self.STATE == "help":
                self.help()
            elif self.STATE == "exit":
                self.exit_game()
    #Start Screen
    def start_screen(self):
        while self.STATE == "start":
            self.__init__()
            self.start_button.draw()
            self.exit_button.draw()
            self.help_button.draw()
            pygame.display.update()
            pygame.display.flip() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.rect.collidepoint(event.pos):
                        print("start game")
                        self.STATE = "game"
                        print(self.STATE)
                    elif self.help_button.rect.collidepoint(event.pos):
                        print("help game")
                        self.STATE = "help"
                    elif self.exit_button.rect.collidepoint(event.pos):
                        print("exit game")
                        self.STATE = "exit"
                    

    #The actual Game
    def game(self):
        
        while self.STATE == "game":
            self.background = pygame.image.load('assets/background.png')
            clock = pygame.time.Clock()
            Framerate = 60
            clock.tick(Framerate)

            
            self.is_running = False
            # self.player.draw(self.screen)
            # self.player.update()
        
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