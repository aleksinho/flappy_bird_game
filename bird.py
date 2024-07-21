import pygame



class Bird:
    def __init__(self, fb_game):
        """ Initialize the ship and set its starting position """
        self.screen = fb_game.screen
        self.screen_rect = fb_game.screen.get_rect()

        # load the bird image and get its rect
        self.original_image = pygame.image.load('images/flappy_bird.png')
        # changing the size of the bird image
        bird_size = (200/4, 111/4)
        self.resized_image = pygame.transform.scale(self.original_image, bird_size)
        # get the bird rect
        self.rect = self.resized_image.get_rect()

        # giving its starting position
        self.rect.x = 60
        self.rect.y = 240

    def blitme(self):
        """ Drawing the ship """
        self.screen.blit(self.resized_image, self.rect)