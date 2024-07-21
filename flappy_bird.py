import sys
import pygame



class FlappyBird:
    """ Overal   class to manage game assets and behavior """
    
    def __init__(self):
        """ Initialize tha game and create game resources """
        pygame.init()

        self.screen = pygame.display.set_mode((720, 480))
        pygame.display.set_caption("Flappy Bird")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == "__main__":
    fb = FlappyBird()
    fb.run_game()