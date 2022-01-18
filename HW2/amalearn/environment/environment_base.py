import gym
from abc import ABC, abstractmethod

class EnvironmentBase(ABC, gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, action_space, state_space, id, container=None):
        super(EnvironmentBase, self).__init__()
        self.action_space = action_space
        self.observation_space = state_space
        self.state = None
        self.id = id
        self.agents = {}

        if container != None:
            container.register_environment(self)

    def register_agent(self, agent):
        if type(agent.id) != str:
            raise Exception('Agent id must be a valid string.')
        if agent.id in self.agents.keys():
            raise Exception('An agent with the same id already exists.')
        
        self.agents[agent.id] = agent

    @abstractmethod
    def calculate_reward(self, action):
        pass

    # determine if the episode is terminated based on the current state
    @abstractmethod
    def terminated(self):
        pass

    # return the observation using self.state
    @abstractmethod
    def observe(self):
        pass

    # any info
    def get_info(self, action):
        return {}

    @abstractmethod
    def next_state(self, action):
        # This method sets the next state based on the current state and the action just taken.
        pass

    # Feel free to override this method. However, YOU MUST IMPLEMENT THE FOLLOWING METHODS AND USE THOHSE IN THIS METHOD:
    #   - calculate_reward
    #   - observe
    #   - get_info (optional)
    #   - next_state
    def step(self, action):
        err_msg = "%r (%s) invalid" % (action, type(action))
        assert self.action_space.contains(action), err_msg

        reward = self.calculate_reward(action)
        info = self.get_info(action)
        self.next_state(action)
        done = self.terminated()
        observation = self.observe()
        return observation, reward, done, info
    
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def render(self, mode='human'):
        pass

    @abstractmethod
    def close(self):
        pass




