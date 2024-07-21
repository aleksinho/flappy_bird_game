import sys
import pygame



class FlappyBird:
    """ Overal   class to manage game assets and behavior """
    
    def __init__(self):
        """ Initialize tha game and create game resources """
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((720, 480))
        pygame.display.set_caption("Flappy Bird")

        self.bg_color = (84, 168, 50)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()
            self.clock.tick(60)
            print(self.clock.get_fps())



if __name__ == "__main__":
    fb = FlappyBird()
    fb.run_game()