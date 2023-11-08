import pygame
from pygame.math import Vector2 as vec
from myenv.settings import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP_SPRITE_LOCATION
from myenv.bullet import Bullet
SPACESHIP_START_POSITION = vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


class Spaceship:
    def __init__(self, window):
        """
        Constructor for spaceship
        :param pic:  the pygame image representation for the spaceship
        """
        self.position = SPACESHIP_START_POSITION

        self.image = pygame.image.load(SPACESHIP_SPRITE_LOCATION)
        self.rect = self.image.get_rect(center=self.position)

        self.shot_timer = 0.7
        self.can_shoot = True
        self.lives = True
        # Richtungsvektor initialisieren. Zu beginn zeigt Spaceship nach oben
        # der Punkt (0,0) ist oben links im Screen (nicht wie bei Koordinatensystemen unten rechts)
        self.direction_vector = vec(0, -1)  # (0,-1) nach oben
        # (0,1) nach unten
        # (-1,0) nach links
        # (0,1) nach rechts
        self.speed = 7  # TODO set to 0
        self.rotation_speed = 7  # TODO set to 0 # positive values only
        self.angle = 0
        self.is_alive = True
        self.shot_asteroids = 0

    def move_spaceship(self, direction):
        """
        Calculacte new Poisiton of Spaceship by using vectors
        :param direction:
        :return:
        """

        directions = {
            "forward": 1,
            "backwards": (-1)
        }
        value = directions.get(direction)
        self.position += self.speed * self.direction_vector * value


    def create_bullet(self):
        return Bullet(self.position, self.direction_vector)



