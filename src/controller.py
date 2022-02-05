import pygame

class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,1000))
        self.screen_name =pygame.display.set_caption("Our Game")
        self.game_state = "start"
    def game(self):
        while self.game_state == "start":
            pass
    def start_screen(self):
        while self.game_state == "start":
            self.screen.fill((0,0,0,0))
            self.screen.blit(self.start.image, (self.start.rect.x,self.start.rect.y))
            self.end_button = pygame.Rect()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
    def start(self):
    
    def exit_game(self):
        pygame.quit()
        exit()