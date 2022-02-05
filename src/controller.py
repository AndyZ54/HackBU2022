import pygame
from src.button import Button

class Controller:
    #The Display 
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,1000))
        self.screen_name =pygame.display.set_caption("Our Game")
        self.game_state = "start"
        self.start_button = Button(100,400, 'assets/Next red.png')
        self.end_button = Button(450, 200, 'assets/Cross red.png')

    #Start Screen
    def start_screen(self):
        while self.game_state == "start":
            self.screen.fill((0,0,0,0))
            self.screen.blit(self.start.image, (self.start.rect.x,self.start.rect.y))

            self.start_button.draw()
            self.end_button.draw()

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
        exit()