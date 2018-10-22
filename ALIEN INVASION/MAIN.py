
import sys
import pygame

from pygame.sprite import Group
from settings import Settings #initialize settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien

import game_functions as gf

#FPS
FPS = 60
fpClock = pygame.time.Clock()

# set colours
white = (255, 255, 255)
bg_color = (230, 230, 230)
black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
green1 = (0, 150, 150)
red = (255, 0, 0)
maroon = (80, 0, 20)
purple = (255, 0, 255)
gray = (70, 70, 70)

def text_format(msg, text_color):
    new_font = pygame.font = pygame.font("retro.ttf", 56)
    new_text = new_font.render(msg, 0 ,text_color)

    return new_text

def run_game():

    # to start the game and to configure the screen res.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION") #title!
    game_icon = pygame.image.load("pod.png")

    pygame.display.set_icon(game_icon)

    # CREATE A BUTTON!
    play_button = Button(ai_settings, screen, "START GAME")

    # ESTABLISH A STAT
    stats = GameStats(ai_settings)

    # scoreboard
    scr = Scoreboard(ai_settings, screen, stats)

    # THE SHIP ITSELF...
    ship = Ship(ai_settings, screen)
    bullets = Group() #make a group consisting of bullets
    aliens = Group()

    # create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # aliens!
    alien = Alien(ai_settings, screen)

    # bgm (courtesy of UNDERTALE OST by Toby Fox)
    pygame.mixer.music.load("menu1.ogg")
    pygame.mixer.music.play(-1)


    # contents and main loop
    while True:

        # PARAMETERS FROM FUNCTIONS -> def

        gf.check_events(ai_settings, screen, stats, scr, play_button, ship, aliens, bullets)

        bullets.update()
        # remove bullets when leaving the screen

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        for event in pygame.event.get():
            # close window
            if event.type == pygame.QUIT:
                sys.exit()
        # display screen visible

        pygame.display.flip()

        # mandatory stuff

        if stats.game_active: # as long as the game is still active/ongoing (esp. if Esc is pressed)
            ship.update() # updates every changes that happen in the ship.py (controls)
            gf.update_bullets(ai_settings, screen, stats, scr, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, scr, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, scr, ship, aliens, bullets, play_button)
        # screen.fill(ai_settings.bg_color)  # bg colour *UPDATE: IN SETTINGS.PY
        # ship.blitme()  # the ship itself, putting this above screen.fill would put it 'inside' the background



fpClock.tick(FPS)

run_game()
