import pygame
from pygame.math import Vector2 as vec
from myenv.settings import ASTEROID1_PNG, ASTEROID2_PNG, ASTEROID3_PNG, SCREEN_HEIGHT, SCREEN_WIDTH
import random

# Asteroid will have a veloicty within the range of this attribute
ASTEROID_SPEED_RANGE = (5.0, 8.0)
ASTEROID_SCALES = [30,50,70]

def generate_asteroid():
    """
    Generates an asteroid object
    :return:
    """
    # generate random image
    roid_image = random.choice([ASTEROID1_PNG,ASTEROID2_PNG,ASTEROID3_PNG])
    image = pygame.image.load(roid_image)

    # generate random scale size
    roid_scale_rand = random.choice(ASTEROID_SCALES)
    image = pygame.transform.scale(image, (roid_scale_rand, roid_scale_rand))

    # spawn from random position on edge
    image_width, image_height = image.get_size()
    xPos = random.randint(image_width, SCREEN_WIDTH - image_width)
    yPos = random.randint(image_height, SCREEN_HEIGHT - image_height)

    # One of these values need to be behind the screem, to make the Asteroids spawn on the edge
    # The smaller one of the Random generated values will be behind the screen
    if yPos <= xPos:
        yPos = random.choice([-75,SCREEN_HEIGHT+75])
    else:
        xPos = random.choice([-75,SCREEN_WIDTH+75])
    position_vector = vec(xPos, yPos)
    # give random direction, depending on position
    direction_vector = generate_random_direction_vector(position_vector)

    # give random speed
    speed = random.uniform(ASTEROID_SPEED_RANGE[0], ASTEROID_SPEED_RANGE[1])
    return Asteroid(image, position_vector, direction_vector, speed)


def generate_random_direction_vector(asteroid_position_vector):

    xA = asteroid_position_vector.x
    yA = asteroid_position_vector.y
    xD = 0
    yD = 0
    if xA < 0:
        xD = 1
        yD = random.uniform(-1.0, 1.0)

    elif yA < 0:
        xD = random.uniform(-1.0, 1.0)
        yD = 1
    elif yA > SCREEN_HEIGHT:
        xD = random.uniform(-1.0, 1.0)
        yD = -1
    elif xA > SCREEN_WIDTH:
        xD = -1
        yD = random.uniform(-1.0, 1.0)
    return vec(xD, yD)


class Asteroid:
    """
    Every Asteroid will differ by 3 features
    Image
    Size [Small,Medium,Large] and by
    Velocity-Range: minVelocity,maxVelocity
    """

    def __init__(self, image, position_vector, direction_vector, speed):
        """

        :param image_location: String
        :param position_vector: vec(x,y)
        :param direction_vector: vec(x,y)
        :param speed: int
        :param scale:  tupel
        """
        self.image = image
        self.position = position_vector
        self.direction_vector = direction_vector
        self.speed = speed
        self.is_destroyed = False

    def generate_asteroid(self):
        """
        Generates an asteroid object
        :return:
        """
        image = None
        position = None
        direction_vector = None
        speed = None
        return Asteroid(image, position, direction_vector, speed)


    def move_asteroid(self):
        """
        Changes Asteroid position
        :return:
        """
        self.position += self.speed * self.direction_vector
