import random
from myenv.settings import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame

BULLET_WIDTH, BULLET_HEIGHT = 7, 7
BULLET_SPEED = 14
BULLET_COLOR = (255, 255, 255)


class Bullet:

    def __init__(self, position_vector, direction_vector):
        self.position_vector = position_vector
        self.direction_vector = direction_vector
        self.bullet_speed = BULLET_SPEED
        self.color = BULLET_COLOR

        self.rect = pygame.Rect(0, 0, BULLET_WIDTH, BULLET_HEIGHT)
        self.rect.center = position_vector

    def move_bullet(self):
        self.rect.center += self.bullet_speed * self.direction_vector
