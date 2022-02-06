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
            self.running_sprites.append(player_image)

        self.current_image = 0
        self.image = self.running_sprites[self.current_image]
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def animate(self):
        self.current_image += 1
        if self.current_image > 14:
            self.current_image = 0
        
        self.image = self.running_sprites[self.current_image]

    def update(self):
        self.animate()

    def draw(self, screen):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        
        
