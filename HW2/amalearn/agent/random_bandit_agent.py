import numpy as np
from amalearn.agent import AgentBase

class RandomBanditAgent(AgentBase):
    def __init__(self, id, environment):
        super(RandomBanditAgent, self).__init__(id, environment)

    def take_action(self) -> (object, float, bool, object):
        available_actions = self.environment.available_actions()
        action = np.random.choice(available_actions)
        obs, r, d, i = self.environment.step(action)
        print(obs, r, d, i)
        self.environment.render()
        return obs, r, d, i
