import pygame.sprite as sprite
#HIGH SCORES AND STATS OF THE GAME

class GameStats():

    def __init__(self, ai_settings):
        #start the stats counting
        self.ai_settings = ai_settings
        self.reset_stats()

        # make the game ALIVE!!!
        # START THE GAME FROM THE MENU
        self.game_active = False

        # HIGH SCORES - never be deleted/reset
        self.high_scr = 0

    def reset_stats(self):
        # make so the stats could change
        self.ships_left = self.ai_settings.ship_limit
        self.scr = 0
        self.lvl = 0 # level


