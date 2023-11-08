import gymnasium as gym
import numpy as np
from myenv.gameimpl import AtariAsteroidsImpl
from gymnasium import spaces
from myenv import gameimpl, settings

from myenv.settings import SCREEN_HEIGHT, SCREEN_WIDTH


class Atari_Asteroids_Env(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"],
                "render_fps": settings.FPS}

    def __init__(self, render_mode):
        """
        Enviroment constructor
        action_space and observation_space are defined here
        :param render_mode:
        """
        # 1. Setup Variables for rendering
        self.gameimpl = AtariAsteroidsImpl(render_mode=render_mode)
        # 2. Define env.action_space + Forward,LeftRotate,RightRotate,Shoot,back,doNothing
        self.action_space = spaces.Discrete(6)
        # 3. Defince env.observation_space   -> our feature space
        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Box(low=np.array([0.0, 0.0]), high=np.array([SCREEN_WIDTH, SCREEN_HEIGHT]),
                                    dtype=float),
                # "Asteroids": spaces.Box(spaces.Box(low=np.array([0.0, 0.0]), high=np.array([SCREEN_WIDTH, SCREEN_HEIGHT]),dtype=float))
            })

    def reset(self, seed=None):
        """
        Reset function
        :return:
        """
        super().reset(seed=seed)
        del self.gameimpl
        self.gameimpl = AtariAsteroidsImpl(render_mode="human")
        observation = self.gameimpl.observe()
        return observation

    def step(self, action):
        """
        step function
        :param action:
        :return: 5-tuple (observation,reward,terminated,truncated,info)
        """
        self.gameimpl.do_action(action)
        obs = self.gameimpl.observe()
        reward = self.gameimpl.evaluate()
        done = self.gameimpl.is_done()
        return obs, reward, done, {}

    def render(self, seed=None):
        """
        render function
        :param seed:
        :return:
        """
        self.gameimpl.view()

    # Close the game and application
    def close(self):
        """
        close function
        :return:
        """
        gameimpl.close()

    def get_obs(self):
        """
        get the observation_space
        :return:
        """
        obs = None  # Needs to be the datatype of our observation, Could be something like a dictonary
        return obs

    def get_info(self):
        """
        get the specfied extra information from the enviroment
        :return:
        """
        info = {}  # Placeholder dictonary
        return info
