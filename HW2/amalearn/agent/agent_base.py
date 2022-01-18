from abc import ABC, abstractmethod

class AgentBase:
    def __init__(self, id, environment=None):
        self.id = id
        self.environment = environment

    def set_environment(self, env):
        self.environment = env

    @abstractmethod
    def take_action(self) -> (object, float, bool, object):
        # in this method, you MUST call the `step` method of 
        # the environment and observe the results and return them like:
        # return observation, reward, done, info
        pass