import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class ActionOnly(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.k = 10
    self.reward_std = 1

    self.qstar = np.random.normal(0,1,self.k)
    self.action_space = spaces.Discrete(self.k)
    
  def _step(self, action):
    reward = np.random.normal(self.qstar[action], self.reward_std)
    return None, reward, False, {}

  def _reset(self):
    return None

  def _render(self, mode='human', close=False):
    pass