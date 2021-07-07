
#BUTTON FOR A.I.

import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        #initalize
        self.screen = screen
        black = (20,20,20)
        screen.fill(black)
        self.screen_rect = screen.get_rect()

        #set the dimension size of the button

        self.width = 330
        self.height = 60
        self.button_color = (255, 255, 0)
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font("retro.ttf", 56)
        #self.font = pygame.font.SysFont("halken", 56)

        #build the object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #'prepping' the button
        self.prep_msg(msg)

    def prep_msg(self, msg):
        #write the message itself inside the box/rect
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) # turns text into image; 'True' for anti-aliasing
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        #draw a blank button

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

