from re import X
import pygame
import random
import time
from src import button
from src import player
from src import hearts
from src import obstacles


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
            elif self.STATE == "win":
                self.win()
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
                        
                    elif self.help_button.rect.collidepoint(event.pos):
                        self.STATE = "help"
                        
                    elif self.exit_button.rect.collidepoint(event.pos):
                        self.STATE = "exit"
                        self.is_running = False
                        
                    
    #The actual Game
    def game(self):
        self.end_one = []
        for i in range(1,4):
                image = pygame.image.load(f"assets/win/end1/Win ({i}).png")
                self.end_one.append(image)
        for i in self.end_one:
                self.screen.blit(i,(0,0))
                pygame.display.update()
                pygame.time.delay(1500)
        x = 0
        x_sky = 0
        x_house = 0
        x_house1 = 0
        x_house2 = 0
        x_fb = 0
        x_umb = 0
        x_road = 0
        jumping = False
        gravity = 0.53

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
        self.display_health = self.font.render('Health : ' + str(self.player.health), False , (225, 215, 0))
        self.all_heart_sprites = pygame.sprite.Group()
        self.all_obstacles = pygame.sprite.Group()
        for i in range(10):
            x, y = random.randrange(2000, 20000), random.randrange(600, 700)
            self.all_heart_sprites.add(hearts.Hearts(x, y))

        for j in range(20):
            x_obs, y_obs = random.randrange(2000, 20000), 700
            randoNumbo = random.randrange(1,6)
            self.all_obstacles.add(obstacles.Obstacles(x_obs, y_obs, randoNumbo))

        while self.STATE == "game":
            self.display_score = self.font.render('Envelope Collected : ' + str(self.score), False , (225, 215, 0))
            self.display_health = self.font.render('Health : ' + str(self.player.health), False , (225, 215, 0))
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

            if self.player.health > 0:
                player_hit = pygame.sprite.spritecollide(self.player, self.all_heart_sprites, True, pygame.sprite.collide_circle_ratio(0.4))
                player_hit_by_obstacle = pygame.sprite.spritecollide(self.player, self.all_obstacles, True, pygame.sprite.collide_circle_ratio(0.4))
                if player_hit:
                    envelope = pygame.mixer.Sound('assets/music/love.mp3')
                    pygame.mixer.Sound.play(envelope)
                    self.score += 1
                    
                    
                if player_hit_by_obstacle:
                    ouch = pygame.mixer.Sound('assets/music/ouch.mp3')
                    pygame.mixer.Sound.play(ouch)
                    self.player.health -= 1
                
                if len(self.all_obstacles) < 20:
                    new_obx, new_oby = random.randrange(2000, 20000), 700
                    randoNumbo2 = random.randrange(1,6)
                    new_boy = obstacles.Obstacles(new_obx, new_oby, randoNumbo2)
                    self.all_obstacles.add(new_boy)

                if len(self.all_heart_sprites) < 10:
                    new_x, new_y = random.randrange(2000, 20000), random.randrange(600, 700)
                    self.all_heart_sprites.add(hearts.Hearts(new_x, new_y))
            else:
                self.STATE = "end"

            self.all_heart_sprites.update()
            self.all_heart_sprites.draw(self.screen)

            self.all_obstacles.update()
            self.all_obstacles.draw(self.screen)

            self.player.move()
            self.player.draw(self.screen)
            self.player.update()     
            self.screen.blit(self.display_health, (1370, 50))
            self.screen.blit(self.display_score, (10, 50))
            
            if self.score == 2:     
                self.STATE = "win"
            pygame.display.flip()

    def end_screen(self):
        self.screen.fill((0,0,0))
        self.end_background = pygame.image.load('assets/endscreen/darkBackground.png')
        self.end_menu = pygame.image.load('assets/endscreen/darkMenu.png')
        self.end_quit = pygame.image.load('assets/endscreen/darkQuit.png')
        self.end_restart = pygame.image.load('assets/endscreen/darkRestart.png')
        self.end_gameover = pygame.image.load('assets/endscreen/gameOver.png')
        self.screen.blit(self.end_background, (0, 0))
        self.screen.blit(self.end_gameover, (0,0))
        self.end_menu_button= button.Button(400, 570, self.screen, self.end_menu)
        self.end_quit_button = button.Button(400, 740, self.screen, self.end_quit)
        self.end_restart_button = button.Button(400, 370, self.screen, self.end_restart)
        self.end_menu_button.draw()
        self.end_quit_button.draw()
        self.end_restart_button.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.STATE = "exit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.end_menu_button.rect.collidepoint(event.pos):
                    self.STATE = "start"
                elif self.end_quit_button.rect.collidepoint(event.pos):
                    self.STATE = "exit"
                elif self.end_restart_button.rect.collidepoint(event.pos):
                    self.STATE = "start"

    def help(self):
        while self.STATE == "help":
            self.screen.fill((0,0,0))
            self.menu_background = pygame.image.load('assets/help/menuBackground.png')
            self.instructions = pygame.image.load('assets/help/instructions.png')
            self.back_button = pygame.image.load('assets/help/back.png')
            self.screen.blit(self.menu_background, (0,0))
            self.screen.blit(self.instructions, (0,0))
            self.back_button = button.Button(400, 740, self.screen, self.back_button)
            self.back_button.draw()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.rect.collidepoint(event.pos):
                        self.STATE = "start"
    def win(self):
        self.end_two = []
        for i in range(1,9):
            image = pygame.image.load(f"assets/win/end2/Win ({i}).png")
            self.end_two.append(image)
        if self.STATE == "win":
            for i in self.end_two:
                self.screen.blit(i, (0,0))
                pygame.time.delay(1000)
                pygame.display.update()
            next_image = pygame.image.load("assets/win/end2/Win (8).png")
            self.screen.blit(next_image, (0,0))
            pygame.time.delay(5000)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                        self.STATE = "start"

    #Exit the Game
    def exit_game(self):
        self.is_running = False
        pygame.quit()