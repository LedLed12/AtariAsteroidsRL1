import tokenize
import random

import pygame

from myenv.asteroid import Asteroid
from myenv.asteroid import generate_asteroid
from myenv.settings import *
from myenv.spaceship import Spaceship
from myenv.token import Token
from threading import Timer
from myenv.bullet import Bullet
import myenv.token


def calcPosi(point, d_vector):
    """
    Utility function
    Returns a vector, given a distance vector and a point
    :param point:
    :param d_vector:
    :return:
    """
    vect = vec(point + 100 * d_vector)
    return vect





class AtariAsteroidsImpl:

    def __init__(self, render_mode):
        """
        constructor for game initialization
        gets called by enviroment
        :param render_mode:
        """

        self.window = None  # Our Screen
        self.clock = None  # Time tracking
        self.render_mode = render_mode
        self.spaceship = Spaceship(self.window)
        self.shooting_cooldown = 220
        # This should be a list
        self.asteroids = []
        self.asteroids_shot_prev = 0
        self.asteroids_shot = 0
        self.tokens_collected_prev = 0
        self.token_collected = 0

        self.bullets = []
        self.token = myenv.token.generate_token()
        self.asteroid_spawn_rate = 1000
        self.time_since_last_asteroid_drawn = 1000  # 5000 Millisceonds -> 1 second
        self.time_since_last_bullet_shot = 500  # 0.5 seconds
        self.score_int = 0

    def view(self):
        """
        gets called by atari_env.render()
        here is the game loop and rendering implemented
        :return:
        """

        if self.window is None and self.render_mode == "human":
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.clock is None and self.render_mode == "human":
            self.clock = pygame.time.Clock()

        self.window.fill(BACKGROUND_COLOR)
        if self.render_mode == "human":
            pygame.event.pump()
            self.clock.tick(FPS)
            # self.spaceship.move_spaceship(self.spaceship.direction_vector, self.spaceship.speed)

            # Handle key inputs
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.spaceship.move_spaceship(
                    "forward")  # moves spaceship differentiate bewtween forwards and backwards
            elif keys[pygame.K_a]:
                self.spaceship.angle += self.spaceship.rotation_speed
            elif keys[pygame.K_s]:
                self.spaceship.move_spaceship("backwards")
            elif keys[pygame.K_d]:
                self.spaceship.angle -= self.spaceship.rotation_speed
            elif keys[pygame.K_SPACE]:
                self.shoot_bullet()

            if not self.spaceship.is_alive:
                return

            self.check_spaceship_collision()
            self.check_bullet_collision()
            self.draw_spaceship(self.spaceship.angle, self.spaceship.position)
            self.update_bullets()
            self.spawn_asteroid()
            self.destroy_asteroid()
            self.draw_Asteroids()
            self.draw_token()
            self.draw_background()
            self.update_score()
            #(f"Evaluation {self.evaluate()}")

            pygame.display.update()

    def do_action(self, action_index):
        """
        action_index -> [Forward=0,Left=1,Right=2,Backwards=3,Shoot=4]
        :param action_index:
        :return:
        """
        if action_index == 0:  # Move Forward
            self.spaceship.speed += 7
        if action_index == 1:  # Left Rotate
            self.spaceship.rotation_speed += 7
        if action_index == 2:  # Right Rotate
            self.spaceship.rotation_speed -= 7
        if action_index == 3:  # Move Back
            self.spaceship.speed -= 7
        if action_index == 4:  # Do Shoot
            pass
        if action_index == 5:  # Do nothing
            pass

    def evaluate(self):
        """
        gets the reward
        :return:
        """
        reward = 0
        if not self.spaceship.is_alive:
            reward -= 1000
        if self.asteroids_shot_prev < self.asteroids_shot:  # TODO check this
            print("bullet shot: reward +20")
            reward += 20
            self.asteroids_shot_prev = self.asteroids_shot
        if self.tokens_collected_prev < self.token_collected:
            reward += 20
            print("bullet shot: token collected reward +20")
            self.tokens_collected_prev = self.token_collected
        return reward

    def observe(self):
        """
        gets_the observation space
        :return:
        """
        obs = None
        return obs

    def close(self):
        """
        close
        :return:
        """
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()

    def rotate_spaceship_center(self, angle):
        """
        Rotates the spaceship depending on the direction point
        Rotates the image along the direction-vector
        :return:
        """
        # Rotate the distance_vector
        v1 = vec(0, -1)
        v1 = v1.rotate(-angle)
        self.spaceship.direction_vector = v1
        # pygame.draw.line(self.window, (150, 200, 10), self.spaceship.position,calcPosi(self.spaceship.position, self.spaceship.direction_vector))

        rotate_spaceship = pygame.transform.rotate(self.spaceship.image, angle)
        rect = rotate_spaceship.get_rect(center=self.spaceship.rect.center)
        return rotate_spaceship, rect

    def draw_spaceship(self, angle, position_vector):  # image,x,y
        """
        Draw a spaceship and blit it to the screen
        This function, turns the spaceship to the given angle and position vector
        :param position_vector:
        :param angle:
        :return:
        """
        rotate_spaceship, rect = self.rotate_spaceship_center(angle)

        # move spaceship to position vector
        # move spaceship rect_center to position vector
        rect.center = position_vector

        # draw a line to show our moving vector

        self.window.blit(rotate_spaceship, rect)

    def is_done(self):
        """
        Check if game is over
        :return:
        """
        if not self.spaceship.is_alive:
            return True
        return False

    def draw_Asteroids(self):
        for asteroid in self.asteroids:
            asteroid.move_asteroid()
        for asteroid in self.asteroids:
            self.window.blit(asteroid.image, asteroid.position)

    def spawn_asteroid(self):
        # TODO increase spawn frequency
        if len(self.asteroids) > 8:
            return
        self.time_since_last_asteroid_drawn += self.clock.get_time()
        if self.time_since_last_asteroid_drawn < self.asteroid_spawn_rate:  # 5000 milliseconds = 5 seconds
            return

        if self.asteroid_spawn_rate >= 200:
            self.asteroid_spawn_rate -= 20
        print(self.asteroid_spawn_rate)
        self.time_since_last_asteroid_drawn = 0
        asteroid = generate_asteroid()
        self.asteroids.append(asteroid)

    def destroy_asteroid(self):
        copy_asteroids = self.asteroids.copy()
        for asteroid in copy_asteroids:
            if asteroid.position.x > SCREEN_WIDTH + 80:
                self.asteroids.remove(asteroid)

            if asteroid.position.y > SCREEN_HEIGHT + 80:
                self.asteroids.remove(asteroid)
            if asteroid.position.x < -80:
                self.asteroids.remove(asteroid)
            if asteroid.position.y < -80:
                self.asteroids.remove(asteroid)

    def check_spaceship_collision(self):
        """
        this function checks, if the spaceship is colliding with the border
        or if it collided with an asteroid
        """
        for asteroid in self.asteroids:
            roid_rect = asteroid.image.get_rect()
            roid_rect.x, roid_rect.y = asteroid.position

            space_rect = self.spaceship.image.get_rect()
            space_rect.center = self.spaceship.position

            #pygame.draw.rect(self.window, (0, 0, 0), roid_rect)
            # apygame.draw.rect(self.window, (0, 0, 100), space_rect)


            # Asteroid collision
            if pygame.Rect.colliderect(roid_rect, space_rect):
                self.spaceship.is_alive = False

            # Token collision
            if pygame.Rect.colliderect(space_rect, self.token.rect):
                self.token_collected += 1
                self.token = myenv.token.generate_token()

            # border collision
            if space_rect.x <= 0:
                self.spaceship.position = vec(0 + self.spaceship.image.get_rect().size[0] / 2,
                                              self.spaceship.position.y)
            if space_rect.y <= 0:
                self.spaceship.position = vec(self.spaceship.position.x,
                                              0 + self.spaceship.image.get_rect().size[1] / 2)
            if space_rect.x >= SCREEN_WIDTH - space_rect.size[0]:
                self.spaceship.position = vec(SCREEN_WIDTH - self.spaceship.image.get_rect().size[0] / 2,
                                              self.spaceship.position.y)

            if space_rect.y >= SCREEN_HEIGHT - space_rect.size[1]:
                self.spaceship.position = vec(self.spaceship.position.x,
                                              SCREEN_HEIGHT - self.spaceship.image.get_rect().size[1] / 2)

    def shoot_bullet(self):
        self.time_since_last_bullet_shot += self.clock.get_time()

        if self.time_since_last_bullet_shot < self.shooting_cooldown:  # 5000 milliseconds = 5 seconds
            return
        self.time_since_last_bullet_shot = 0
        bullet = self.spaceship.create_bullet()
        self.bullets.append(bullet)

    def update_score(self):
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render(f"Score: {self.score_int}", True, (255, 255, 255))
        self.score_int += 1
        self.window.blit(score_text, (20, 20))

    def update_bullets(self):
        for bullet in self.bullets:
            pygame.draw.rect(self.window, bullet.color, bullet.rect)
        for bullet in self.bullets:
            if bullet.rect.x > SCREEN_WIDTH + 80:
                self.bullets.remove(bullet)

            if bullet.rect.y > SCREEN_HEIGHT + 80:
                self.bullets.remove(bullet)
            if bullet.rect.x < -80:
                self.bullets.remove(bullet)
            if bullet.rect.y < -80:
                self.bullets.remove(bullet)
            bullet.move_bullet()

    def draw_token(self):
        pygame.draw.circle(self.window, self.token.color, self.token.rect.center, myenv.token.TOKEN_RADIUS)

    def check_bullet_collision(self):
        bullets_copy = self.bullets.copy()
        asteroids_copy = self.asteroids.copy()

        for bullet in bullets_copy:
            for asteroid in asteroids_copy:

                roid_rect = asteroid.image.get_rect()
                roid_rect.x, roid_rect.y = asteroid.position

                if pygame.Rect.colliderect(bullet.rect, roid_rect):
                    self.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)
                    self.asteroids_shot += 1

    def draw_background(self):
        for dot in BACKGROUND_DOTS:
            pygame.draw.circle(self.window, (255, 255, 255), dot, 1)
