
#BAD GUYS
#same concept as making the ship; difference in positions

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        #initialize
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the image
        self.image = pygame.image.load("lol.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()


        #start each alien at the top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store its position
        self.x = float(self.rect.x)

    def edge_check(self): #if aliens move right or left (hits the edge)
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        #ALIENS MOVE RIGHT OR LEFT
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        #DRAW the whole thing in its location
        self.screen.blit(self.image, self.rect)

    #def update_aliens(aliens):
        #update the positions of the aliens
    #   aliens.update()

