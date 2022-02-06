import pygame
from src import button
from src import player

class Controller():
    #The Display 
    def __init__(self):
        self.screen = pygame.display.set_mode((1600,900))
        self.screen_name = pygame.display.set_caption("Love Message")
        self.is_running = True
        self.STATE = "start"

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
        if self.STATE == "start":
            self.start_image = pygame.image.load('assets/start.png')
            self.help_image = pygame.image.load('assets/help.png')
            self.exit_image = pygame.image.load('assets/exit.png')
            self.title = pygame.image.load('assets/lovemessage.png')
            self.background = pygame.image.load('assets/background.png')

            self.start_button = button.Button(550, 660, self.screen, self.start_image)
            self.help_button = button.Button(40,660, self.screen, self.help_image)
            self.exit_button = button.Button(1050, 660, self.screen, self.exit_image)
            self.player = player.Player(500,500,self.screen)
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.title, (25,100))
            self.start_button.draw()
            self.exit_button.draw()
            self.help_button.draw()
            pygame.display.update()
        while self.STATE == "start":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.rect.collidepoint(event.pos):
                        self.STATE = "game"
                        print(self.STATE)
                    elif self.help_button.rect.collidepoint(event.pos):
                        self.STATE = "help"
                        print(self.STATE)
                    elif self.exit_button.rect.collidepoint(event.pos):
                        self.STATE = "exit"
                        self.is_running = False
                        print(self.STATE)
                    
    #The actual Game
    def game(self):
        while self.STATE == "game":
            clock = pygame.time.Clock()
            Framerate = 60
            clock.tick(Framerate)

            self.background = pygame.image.load('assets/background.png')

            self.is_running = False
            self.player.draw(self.screen)
            self.player.update()
            pygame.display.update()
        
    def help(self):
        while self.STATE == "help":
            self.background = pygame.image.load('assets/background.png')
    #Exit the Game
    def exit_game(self):
        self.is_running = False
        pygame.quit()