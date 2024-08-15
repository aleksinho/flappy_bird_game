import pygame


class Bird:
    def __init__(self, fb_game):
        self.screen = fb_game.screen
        self.settings = fb_game.settings
        
        self.raw_image = pygame.image.load('imgs/bird.png')
        self.image = pygame.transform.scale(self.raw_image, self.settings.bird_scale)
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = 30, 240

    def blitme(self):
        self.screen.blit(self.image, self.rect)