import pygame
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()

        self.screen = screen
        self.pos = vec(300,740)
        self.vel = vec(0,0)
        self.accel = vec(0,0)

        self.acceleration = 0.5
        self.friction = -0.12
        self.gravity = 0.8


        self.airborne = False
        self.jumping = False
        self.doubleJumping = False
        self.running = False
        self.dying = False
        self.move_frame = 0

        self.health = 5
        self.collection = 0

        self.alive = True

        self.x = x
        self.y = y
        self.y_velocity = 0

        self.running_sprites = []
        self.jumping_sprites = []
        self.death_sprites = []

        for i in range(1,16):
            player_image = pygame.image.load(f"assets/theboy/Run ({i}).png")
            player_image = pygame.transform.scale(player_image, (int(player_image.get_width() * 0.4), int(player_image.get_height() * 0.4)))
            self.running_sprites.append(player_image)

        for i in range(1,16):
            jumping_image = pygame.image.load(f"assets/theboy/Jump ({i}).png")
            jumping_image = pygame.transform.scale(player_image, (int(jumping_image.get_width() * 0.4), int(jumping_image.get_height() * 0.4)))
            self.jumping_sprites.append(jumping_image)

        self.current_image = 0
        self.current_jumping_image = 0
        self.image = self.running_sprites[self.current_image]
        self.jumping_image = self.jumping_sprites[self.current_jumping_image]
        self.rect = self.image.get_rect(center = (self.x, self.y))
        
    def animate(self):
        
        self.current_image += 1
        if self.current_image >= len(self.running_sprites):
            self.current_image = 0
        self.image = self.running_sprites[int(self.current_image)]

    def move(self):
        change_x = 0
        change_y = 0
        if self.jumping == True and self.airborne == False:
            self.y_velocity = -15
            self.jump = False
            self.airborne = True
        
        self.rect.x += change_x
        self.rect.y += change_y

    def update(self):
        self.animate()

    def draw(self, screen):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        
        
