
#SETTINGS FOR ALIEN INVASION

class Settings():

    def __init__(self):

        self.screen_width = 1100
        self.screen_height = 650
        self.bg_color = (30, 30, 30)

        #ship's speed
        self.ship_speed_factor = 1.5
        #ship's lives
        self.ship_limit = 3

        # settings for bullets
        self.bullet_speed_factor = 1.8
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = 240, 240, 0
        self.bullets_allowed = 10

        # settings for aliens
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 = right / -1 = left

        # SETTINGS FOR GAME PLAY
        self.speedup_scale = 1.25 # increase in difficulty

        # ALIEN PTS INCREASE
        self.score_scale = 1.25

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # difficulty modifier
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.2

        # fleet movements; 1 = right / -1 = left
        self.fleet_direction = 1

        # points
        self.alien_pts = 50

    def increase_speed(self):
        # you said it
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        # count and display score
        self.alien_pts = int(self.alien_pts * self.score_scale)
        #print(self.alien_pts)
