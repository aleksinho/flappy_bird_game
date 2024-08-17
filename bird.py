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

        # setting physics variables
        self.gravity = 0.5
        self.current_velocity = 0
        self.max_velocity = -10
        self.max_fall_speed = 10

        # if this is true the bird will jump
        self.jumping = False

    def jump(self):
        if self.jumping:
            self.current_velocity = self.max_velocity
            self.jumping = False
        
        # applying the gravity
        self.current_velocity += self.gravity

        # Limit the fall speed
        if self.current_velocity > self.max_fall_speed:
            self.current_velocity = self.max_fall_speed

        self.y += self.current_velocity
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)