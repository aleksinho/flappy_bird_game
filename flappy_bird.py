import sys
import pygame



class FlappyBird:
    """ Overal   class to manage game assets and behavior """
    
    def __init__(self):
        """ Initialize tha game and create game resources """
        pygame.init()

        self.screen = pygame.display.set_mode((720, 480))
        pygame.display.set_caption("Flappy Bird")