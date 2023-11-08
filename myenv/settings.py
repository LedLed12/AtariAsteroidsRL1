from pygame.math import Vector2 as vec

"""

Here are some constants our game needs
We can adjust some ingame settings here

"""

# Screen
FPS = 30
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (0,0,0)  # RGB Tupel

# Spaceship
SPACESHIP_START_POSITION = vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
SPACESHIP_SPRITE_LOCATION = "spaceship_sprite.png"  # this location is seen by main.py // so it is not "../spaceship_sprite.png"

ASTEROID1_PNG = "asteroid1.png"
ASTEROID2_PNG = "asteroid2.png"
ASTEROID3_PNG = "asteroid3.png"

file_path = SPACESHIP_SPRITE_LOCATION  # Replace with the path to the file you want to check

BACKGROUND_DOTS = [(235, 248),
                   (685, 166),
                   (636, 311),
                   (198, 349),
                   (654, 120),
                   (448, 388),
                   (255, 80),
                   (228, 98),
                   (154, 154),
                   (109, 271),
                   (187, 397),
                   (580, 192),
                   (168, 115),
                   (255, 259),
                   (71, 222),
                   (491, 28),
                   (455, 59),
                   (293, 18),
                   (319, 71),
                   (679, 318),
                   (469, 138),
                   (166, 201),
                   (134, 53),
                   (185, 44),
                   (26, 55),
                   (247, 241),
                   (342, 485),
                   (649, 491),
                   (685, 320),
                   (201, 266),
                   (700, 76),
                   (667, 76),
                   (560, 486),
                   (468, 352),
                   (666, 266),
                   (279, 247),
                   (40, 180),
                   (507, 266),
                   (553, 153),
                   (191, 315),
                   (204, 86),
                   (632, 83),
                   (519, 448),
                   (494, 232),
                   (238, 36),
                   (695, 338),
                   (260, 387),
                   (374, 161),
                   (556, 176),
                   (458, 381)]
