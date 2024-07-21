import pygame




class Settings:
    def __init__(self):
        # screen size
        self.screen_width = 720
        self.screen_height = 480

        # background color
        self.bg_color = (52, 192, 235)

        # bird image
        self.bird_image = 'images/flappy_bird.png' 

        # bird size
        self.bird_size = (200/4, 111/4)

        # bird starting position
        self.x_start = 60
        self.y_start = 240