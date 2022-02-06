from re import X
import pygame
from src import button
from src import player
from src import hearts

class Controller():
    #The Display 
    def __init__(self):
        self.screen = pygame.display.set_mode((1600,900))
        self.screen_name = pygame.display.set_caption("Love Message")
        self.is_running = True
        self.font = pygame.font.SysFont("Minecraft", 70)
        self.STATE = "start"

    def mainloop(self):
        while self.is_running == True:
            if self.STATE == "start":
                self.start_screen()
            elif self.STATE == "game":
                self.game()
            elif self.STATE == "help":
                self.help()
            elif self.STATE == "end":
                self.end_screen()
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
            self.music = pygame.mixer.music
            self.music.load('assets/music/music.mp3')
            self.music.set_volume(0.3)
            self.music.play(loops=1)

            self.start_button = button.Button(550, 660, self.screen, self.start_image)
            self.help_button = button.Button(40,660, self.screen, self.help_image)
            self.exit_button = button.Button(1050, 660, self.screen, self.exit_image)
            self.player = player.Player(300,740,self.screen)
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
        x = 0
        x_sky = 0
        x_house = 0
        x_house1 = 0
        x_house2 = 0
        x_fb = 0
        x_umb = 0
        x_road = 0
        jumping = False
        gravity = 0.5

        self.sky = pygame.image.load('assets/city/Sky.png').convert()
        self.house = pygame.image.load('assets/city/houses.png').convert_alpha()
        self.house1 = pygame.image.load('assets/city/houses1.png').convert_alpha()
        self.house2 = pygame.image.load('assets/city/houses2.png').convert_alpha()
        self.fountain = pygame.image.load('assets/city/fountainbush.png').convert_alpha()
        self.umbrella = pygame.image.load('assets/city/umbrellapolicebox.png').convert_alpha()
        self.road = pygame.image.load('assets/city/road.png').convert_alpha()

        self.score = 0
        self.health = 0
        self.display_score = self.font.render('Hearts Collected : ' + str(self.score), False , (225, 215, 0))
        self.display_health = self.font.render('Health : ' + str(self.health), False , (225, 215, 0))

        self.heart_sprite = pygame.sprite.Group()
        # for i in range(5):
        #     x , y = 700 , random.randrange(700, 1400)
        self.heart_sprite.add(hearts.Hearts(700, 1400, self.screen, 'assets/heart.png'))

        while self.STATE == "game":
            
            self.player.y_velocity += gravity
            if self.player.y_velocity > 10:
                self.player.y_velocity = 10
            self.player.rect.y += self.player.y_velocity
            if self.player.rect.bottom + self.player.rect.y > 1450:
                self.player.rect.y = 1450 - (self.player.rect.bottom)
                self.player.y_velocity = 0
                self.player.airborne = False

            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    self.STATE = "exit"
                if  keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                    self.player.jumping = True
                else:
                    self.player.jumping = False
            print(self.player.jumping)
                
                
            clock = pygame.time.Clock()
            Framerate = 60
            clock.tick(Framerate)

            rel_x_sky = x_sky % self.sky.get_rect().width
            self.screen.blit(self.sky,(rel_x_sky - self.sky.get_rect().width,0))
            if rel_x_sky < 1600:
                self.screen.blit(self.sky,(rel_x_sky,0))
            x_sky -= 4
            
            rel_x = x % self.house.get_rect().width
            self.screen.blit(self.house,(rel_x - self.house.get_rect().width,0))
            if rel_x < 1600:
                self.screen.blit(self.house,(rel_x,0))
            x_house -= 4

            rel_x_house2 = x_house2 % self.house2.get_rect().width
            self.screen.blit(self.house2,(rel_x_house2 - self.house2.get_rect().width,0))
            if rel_x_house2 < 1600:
                self.screen.blit(self.house2,(rel_x_house2,0))
            x_house2 -= 5

            rel_fb = x_fb % self.fountain.get_rect().width
            self.screen.blit(self.fountain,(rel_fb - self.fountain.get_rect().width,0))
            if rel_fb < 1600:
                self.screen.blit(self.fountain,(rel_fb,0))
            x_fb -= 6

            rel_x_house1 = x_house1 % self.house1.get_rect().width
            self.screen.blit(self.house1,(rel_x_house1 - self.house1.get_rect().width,0))
            if rel_x_house1 < 1600:
                self.screen.blit(self.house1,(rel_x_house1,0))
            x_house1 -= 6

            rel_umb = x_umb % self.umbrella.get_rect().width
            self.screen.blit(self.umbrella,(rel_umb - self.umbrella.get_rect().width,0))
            if rel_umb < 1600:
                self.screen.blit(self.umbrella,(rel_umb,0))
            x_umb -= 7

            rel_road = x_road % self.road.get_rect().width
            self.screen.blit(self.road,(rel_road - self.road.get_rect().width,0))
            if rel_road < 1600:
                self.screen.blit(self.road,(rel_road,0))
            x_road -= 7

            self.player.move()
            self.player.draw(self.screen)
            self.player.update()     
            self.screen.blit(self.display_health, (1370, 50))
            self.screen.blit(self.display_score, (10, 50))
            self.heart_sprite.draw(self.screen)

            pygame.display.flip()

    def end_screen(self):
        pass
        
    def help(self):
        while self.STATE == "help":
            self.background = pygame.image.load('assets/background.png')
    #Exit the Game
    def exit_game(self):
        self.is_running = False
        pygame.quit()