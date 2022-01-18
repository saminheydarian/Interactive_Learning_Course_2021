import numpy as np

from amalearn.environment import MutliArmedBanditEnvironment
from amalearn.reward import GaussianReward
from amalearn.agent import RandomBanditAgent

means = [1, 2, -10, -5]
stds = [0.2, 0.1, 0.5, 0.4]

rewards = [GaussianReward(mean, std) for mean, std in zip(means, stds)]
env = MutliArmedBanditEnvironment(rewards, 10, '1')
agent = RandomBanditAgent('1', env)

for step in range(10):
    o, r, d, i = agent.take_action()

