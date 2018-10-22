
#SCORES

import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    #report scoring info
    def __init__(self, ai_settings, screen, stats):
        # initialize
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # font settings
        self.text_color = (255, 255, 255)
        self.text_color1 = (0, 255, 0)
        self.text_color2 = (60, 60, 60)
        self.font = pygame.font.Font("retro.ttf", 48)
        #self.font = pygame.font.SysFont("halken outline", 48)

        # to prepare/execute
        self.prep_scr()
        self.prep_high_scr()
        self.prep_lvl()
        self.prep_ships()

    def prep_scr(self):

        #turn the score into a 'rendered' image

        # rounding the score and adding ','
        rounded_scr = int(round(self.stats.scr, -1))
        scr_str = "{:,}".format(rounded_scr)

        scr_str = str(self.stats.scr)
        self.scr_image = self.font.render(scr_str, True, self.text_color1, self.ai_settings.bg_color)

        # display the scores
        self.scr_rect = self.scr_image.get_rect()
        # put it to the right
        self.scr_rect.right = self.screen_rect.right - 20
        self.scr_rect.top = 20

    def prep_high_scr(self):
        # turn high score into rendered image
        high_scr = int(round(self.stats.high_scr, -1))
        high_scr_str = "{:,}".format(high_scr) # add a ','

        # turn the high scr into a rendered image
        self.high_scr_image = self.font.render(high_scr_str, True, self.text_color, self.ai_settings.bg_color)

        # put the high score on the CENTER
        self.high_scr_rect = self.high_scr_image.get_rect()
        self.high_scr_rect.centerx = self.screen_rect.centerx
        self.high_scr_rect.top = self.scr_rect.top

    def prep_lvl(self):
        # turn the level into a rendered image
        self.lvl_image = self.font.render(str(self.stats.lvl), True, self.text_color2, self.ai_settings.bg_color)

        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.right = self.scr_rect.right
        self.lvl_rect.top = self.scr_rect.bottom + 10

    def prep_ships(self):
        # show how many ships are left
        self.ships = Group()

        for ship_num in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_num * ship.rect.width # set the coordinate of the ship number side by side (10 spaces per ship)
            ship.rect.y = 10 # set the coordinate (10 pixels down) to line up with the rest of the scores
            self.ships.add(ship)

    def show_score(self):
        # to show the score via the rendered one
        self.screen.blit(self.scr_image, self.scr_rect)
        self.screen.blit(self.high_scr_image, self.high_scr_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.ships.draw(self.screen)