import gymnasium as gym
from gymnasium.envs.registration import register
from gymnasium.utils.play import play
import time
import random

register(
    id="Atari-v0",
    entry_point="myenv.atari_env:Atari_Asteroids_Env",
    max_episode_steps=2000,
)
KEYMAP = {
    "w": "",
    "a": "",
    "s": "",
    "d": ""
}

env = gym.make("Atari-v0", render_mode="rgb_array")


# gym.utils.play.play(env, keys_to_action=KEYMAP)


done = False
env.reset()
while True:
    action = env.action_space.sample()  # Replace with your desired action selection strategy
    env.render()
    if done:
        break
env.close()
