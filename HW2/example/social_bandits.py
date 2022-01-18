import numpy as np

from amalearn.container import Container
from amalearn.environment import MutliArmedBanditEnvironment
from amalearn.reward import GaussianReward
from amalearn.agent import RandomBanditAgent, SocialAgent
from amalearn.social import Message

class SocialBanditAgent(SocialAgent):
    def __init__(self, id, environment, container):
        super(SocialBanditAgent, self).__init__(id, container, environment)

    def take_action(self) -> (object, float, bool, object):
        # checking inbox:
        print('inbox of agent {}'.format(self.id))
        while not self.inbox.empty():
            msg = self.inbox.get_nowait()
            print(msg)
        available_actions = self.environment.available_actions()
        action = np.random.choice(available_actions)
        obs, r, d, i = self.environment.step(action)
        if r > 0:
            msg = Message(self.id, 'ag1', 'I got positive reward!')
            self.send_message(msg)
        print(obs, r, d, i)
        self.environment.render()
        return obs, r, d, i


means = [1, 2, -10, -5]
stds = [0.2, 0.1, 0.5, 0.4]
rewards = [GaussianReward(mean, std) for mean, std in zip(means, stds)]

cont = Container('cont1')
env1 = MutliArmedBanditEnvironment(rewards, 10, 'env1', cont)
env2 = MutliArmedBanditEnvironment(rewards, 10, 'env2', cont)

agent1 = SocialBanditAgent('ag1', env1, cont)
agent2 = SocialBanditAgent('ag2', env2, cont)

cont.simulate()
