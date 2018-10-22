#make bullets!

import pygame
from pygame.sprite import Sprite #a dedicated feature

class Bullet(Sprite):

    #to manage bullets from the ship
    def __init__(self, ai_settings, screen, ship):
        #to create bullets from the ship's position
        super(Bullet, self).__init__() #to use/summon Sprite's module
        self.screen = screen

        #setting the bullet at (0,0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx #to set the bullet's location right at the TOP of the ship
        self.rect.top = ship.rect.top

        #store the bullet's pos using decimal PLUS configuring its speed
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #to move the bullet upwards in the screen!

        self.y -= self.speed_factor #update the decimal position of the bullet, which goes UP
        #the x coordinate DO NOT change because the bullet only moves up in one direction

        self.rect.y = self.y #update the rectangle position


    def draw_bullet(self):
        #draws the bullet onto the screen
        pygame.draw.rect(self.screen, self.color, self.rect)


