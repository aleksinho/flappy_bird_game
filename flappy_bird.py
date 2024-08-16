import sys

import pygame

from settings import Settings
from bird import Bird


class FlappyBird:
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Flappy Bird")
        self.bg_color = self.settings.bg_color

        self.bird = Bird(self)

    
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.bird.update()

    
    def _check_events(self):
        """ Respond to keypresses and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.QUIT:
                sys.exit()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.bird.jump = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_SPACE:
            self.bird.jump = False


    def _update_screen(self):
        # fps
        self.clock.tick(60)
        # background color
        self.screen.fill(self.bg_color)
        # draw the bird
        self.bird.blitme()

        pygame.display.flip()



if __name__ == "__main__":
    fp = FlappyBird()
    fp.run_game()