import pygame


class Bird:
    def __init__(self, fb_game):
        self.screen = fb_game.screen
        self.settings = fb_game.settings
        
        self.raw_image = pygame.image.load('imgs/bird.png')
        self.image = pygame.transform.scale(self.raw_image, self.settings.bird_scale)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 165, 260

        # store exact vertical position of the bird
        self.y = float(self.rect.y)

        # gravity physics
        self.gravity = 1
        self.jump_height = 15
        self.velocity = self.jump_height

        # if this is True the bird will jump
        self.jumping = False

    def update(self):
        if self.jumping:
            self.y -= self.velocity
            self.velocity -= self.gravity
            if self.velocity < -self.jump_height:
                self.jumping = False
                self.velocity = self.jump_height
        
        self.rect.y = self.y


    def blitme(self):
        self.screen.blit(self.image, self.rect)