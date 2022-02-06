import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        vec = pygame.math.Vector2
        ACC = 0.3
        FRIC = -0.10
        super().__init__()

        self.screen = screen
        self.vx = 0
        self.pos = vec((340,240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = "Right"

        self.jumping = False
        self.doubleJumping = False
        self.running = False
        self.dying = False
        self.move_frame = 0

        self.health = 5
        self.collection = 0

        self.x = x
        self.y = y

        self.running_sprites = []
        self.death_sprites = []

        for i in range(1,16):
            player_image = pygame.image.load(f"assets/theboy/Run ({i}).png")
            player_image = pygame.transform.scale(player_image, (int(player_image.get_width() * 0.4), int(player_image.get_height() * 0.4)))
            self.running_sprites.append(player_image)

        self.current_image = 0
        self.image = self.running_sprites[self.current_image]
        self.rect = self.image.get_rect(center = (self.x, self.y))
        
    def animate(self):
        self.current_image += 0.8
        if self.current_image >= len(self.running_sprites):
            self.current_image = 0
        
        self.image = self.running_sprites[int(self.current_image)]

    def update(self):
        self.animate()

    def draw(self, screen):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        
        
