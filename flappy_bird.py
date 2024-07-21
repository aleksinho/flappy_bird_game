import sys
import pygame
from settings import Settings
from bird import Bird



class FlappyBird:
    """ Overal   class to manage game assets and behavior """
    
    def __init__(self):
        """ Initialize tha game and create game resources """
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Flappy Bird")

        self.bird = Bird(self)

        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            self.bird.blitme()

            pygame.display.flip()
            self.clock.tick(60)
            print(self.clock.get_fps())



if __name__ == "__main__":
    fb = FlappyBird()
    fb.run_game()