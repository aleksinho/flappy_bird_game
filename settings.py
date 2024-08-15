class Settings:
    """ A class to store all the settings for Flappy Bird """
    
    def __init__(self):

        # screen settings
        self.screen_width = 580
        self.screen_height = 600
        self.bg_color = (52, 180, 235)

        # bird settings
        self.bird_scale = (75, 41.625)