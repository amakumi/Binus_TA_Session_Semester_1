
#THIS IS THE SHIP FOR ALIEN INVASION GAME

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen): # initialize the ship and its start position
        self.screen = screen
        self.ai_settings = ai_settings

        super(Ship, self).__init__()


        #loading the image
        #rect = rectangles!
        self.image = pygame.image.load("pod.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        #start the ship ON THE BOTTOM of the screen

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #stores a decimal value of the ship's center
        self.center = float(self.rect.centerx)

        #initial conditions
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # updates the ship's position to move anywhere
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # limiting the range of the ship to explore
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # limiting the range of the ship to explore
            self.center -= self.ai_settings.ship_speed_factor

        # to update the whole thing
        self.rect.centerx = self.center

    def centre_ship(self):
        self.center = self.screen_rect.centerx

    def blitme(self):

        # to DRAW the ship at the current location (or specified by self_rect)
        self.screen.blit(self.image, self.rect)




