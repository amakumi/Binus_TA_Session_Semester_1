#the engine of the game

import sys
from time import sleep  # a delay

import pygame

from bullet import Bullet
from alien import Alien
from button import Button

pygame.mixer.init()

pygame.font.init()
font = pygame.font.SysFont("halken",36)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
# MAIN CONTROL
    # when the key is pressed
    #RIGHT
    if event.key == pygame.K_RIGHT:

        ship.moving_right = True
    #LEFT
    elif event.key == pygame.K_LEFT:

        ship.moving_left = True
    #UP
    elif event.key == pygame.K_UP:

        ship.moving_up = True
    #DOWN
    elif event.key == pygame.K_DOWN:

        ship.moving_down = True

    #SPACE (FIRE BULLETS)
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        gun = pygame.mixer.Sound("gun.wav")
        gun.play()

    #EXIT
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, ship):

    #when the key is not pressed
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def fire_bullet(ai_settings, screen, ship, bullets):
    # you fire bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)



def update_bullets(ai_settings, screen, stats, scr, ship, aliens, bullets):
    # updates bullet positions
    bullets.update()

    # remove the bullets which went out
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # check a contact between bullet and an alien; deletes the alien if it does make one
    check_collisions(ai_settings, screen, stats, scr, ship, aliens, bullets)



def check_collisions(ai_settings, screen, stats, scr, ship, aliens, bullets):
    hit = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # add points
    if hit:
        for aliens in hit.values():
            hi = pygame.mixer.Sound("hi.wav")
            hi.play()
            stats.scr += ai_settings.alien_pts * len(aliens)
            scr.prep_scr()
        check_high_scr(stats, scr) # checks for a high score

    # aliens re-spawn
    if len(aliens) == 0:
        up = pygame.mixer.Sound("up.wav")
        up.play()
        ai_settings.increase_speed() # LEVEL UP!

        # increase the level
        stats.lvl += 1
        scr.prep_lvl()

        create_fleet(ai_settings, screen, ship, aliens) # try againnn


def check_events(ai_settings, screen, stats, scr, play_button, ship, aliens, bullets):

    # how it respond to key-presses and mouse
    #if stats.game_active = True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings, screen, stats, scr, play_button, ship, aliens, bullets, mouse_x, mouse_y)

            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)


def check_play_button(ai_settings, screen, stats, scr, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    # STARTS THE GAME WHEN MOUSE IS PRESSED
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and play_button.rect.collidepoint(mouse_x, mouse_y): # make the button deactivate after clicking
        pygame.mouse.set_visible(False) # hides the cursor
        ai_settings.initialize_dynamic_settings() # reset the difficulty
        stats.reset_stats() # resets the stats/scores
        stats.game_active = True
        pygame.mixer.music.load("battle1.ogg") # bgm (courtesy of UNDERTALE OST by Toby Fox)
        pygame.mixer.music.play(-1)

        # reset the stats, high score, and level
        scr.prep_scr()
        scr.prep_high_scr()
        scr.prep_lvl()
        scr.prep_ships()

        # empties everything
        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.centre_ship() # re-centre the ship


def get_num_aliens_x(ai_settings, alien_width):
    # number of aliens in a COLUMN
    space_x = ai_settings.screen_width - 2 * alien_width #make a gap with the size of an alien
    num_aliens_x = int(space_x / (2 * alien_width))
    return num_aliens_x


def get_num_rows(ai_settings, ship_height, alien_height):
    # number of aliens in each ROW
    space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    num_rows = int(space_y / (2 * alien_height))
    return num_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # create an alien then place it in the row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    # equation
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    #alien.rect.x = alien.x


def create_fleet(ai_settings, screen, ship, aliens):
    # create a fleet of aliens here"

    alien = Alien(ai_settings, screen)
    num_aliens_x = get_num_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_num_rows(ai_settings, ship.rect.height, alien.rect.height)
    #alien_width = alien.rect.width
    #space = ai_settings.screen_width - 2 * alien_width #make a gap with the size of an alien
    #number_aliens = int(space / (2 * alien_width))

    # first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(num_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.edge_check():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    # drop all fleets and change its direction...
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1 #down


def ship_hit(ai_settings, screen, stats, scr, ship, aliens, bullets):
    # what happens if a ship is hit
    ###################################

    ###################################
    if stats.ships_left > 0:
        hit = pygame.mixer.Sound("hit1.wav")
        hit.play()

        stats.ships_left -= 1

        bullets.empty()
        aliens.empty()

        ship.centre_ship()

        # show the decreased number of ships
        scr.prep_ships()
        create_fleet(ai_settings, screen, ship, aliens)

        sleep(2)

    else:
        #GAME OVER :(

        hit = pygame.mixer.Sound("hit1.wav")
        hit.play()
        sleep(2)
        stats.game_active = False
        lose = pygame.mixer.Sound("lose.wav")
        lose.play()
        pygame.mixer.music.load("menu1.ogg")
        pygame.mixer.music.play(-1)
        pygame.mouse.set_visible(True)


def check_bottom(ai_settings, screen, stats, scr, ship, aliens, bullets):
    #check if aliens went to the bottom of the screen
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # use the ship_hit function too!
            ship_hit(ai_settings, screen, stats, scr, ship, aliens, bullets)
            break

def check_high_scr(stats, scr):
    if stats.scr > stats.high_scr:
        #hi = pygame.mixer.Sound("hi.wav")
        #hi.play()
        stats.high_scr = stats.scr
        scr.prep_high_scr()

def update_aliens(ai_settings, screen, stats, scr, ship, aliens, bullets):
    #checks it first, then update the positions of the aliens
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #if ship being hit by aliens
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, scr, ship, aliens, bullets)

    check_bottom(ai_settings, screen, stats, scr, ship, aliens, bullets)

def update_screen(ai_settings, screen, stats, scr, ship, aliens, bullets, play_button):
    # updates the screen and add new images
    # redraw the screen by each loop made

    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    #to REDRAW bullets BEHIND ships and aliens repetitively
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # show/draw the score
    scr.show_score()

    if not stats.game_active:
        play_button = Button(ai_settings, screen, "START GAME!")
        play_button.draw()

    #updates by flipping
    pygame.display.flip()
