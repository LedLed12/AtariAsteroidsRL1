import pygame
from pygame.math import Vector2 as vec
import random
from myenv.settings import SCREEN_HEIGHT, SCREEN_WIDTH

TOKEN_RADIUS = 15
COLOR = (100, 200, 50)


def generate_token():
    x_pos = random.randint(10, SCREEN_WIDTH - 10)
    y_pos = random.randint(10, SCREEN_HEIGHT - 10)

    return Token(vec(x_pos, y_pos))


class Token:

    def __init__(self, position_vector):
        self.rect = pygame.Rect(position_vector.x, position_vector.y, TOKEN_RADIUS * 2, TOKEN_RADIUS * 2)
        self.color = COLOR
