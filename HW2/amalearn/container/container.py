from amalearn.environment import EnvironmentBase
from amalearn.social import Message, Observable
from queue import Queue

class Container:
    def __init__(self, id):
        self.id = id
        self.envs = {}
        self.agents = {}
        self.pending_messages = []

    def register_environment(self, env: EnvironmentBase):
        if env.id in self.envs.keys():
            raise Exception('An environment with the same ID already exists in container {}.'.format(self.id))
        self.envs[env.id] = env

    # env_id is the id of the environment the agent wishes to interact with
    def register_agent(self, agent, env_id):
        if agent.id in self.agents.keys():
            raise Exception('An agent with the same ID already exists in container {}.'.format(self.id))
        self.agents[agent.id] = agent
        self.envs[env_id].register_agent(agent)

    def enqueue_message(self, message: Message):
        self.pending_messages.append(message)

    def deliver_message(self, message: Message):
        try:
            self.agents[message.receiver_id].inbox.put_nowait(message)
        except Exception:
            print('Error delivering message from agent#{} to agent#{}'
                        .format(message.sender_id, message.receiver_id))

    def observe_agent(self, observer_id, observed_id):
        obs = Observable(observed_id, observer_id, 100)
        return obs

    def simulate_environment(self, env):
        env_done = False
        for id, agent in env.agents.items():
            obs, reward, done, info = agent.take_action()
            env_done = env_done or done
        
        return env_done

    # Single thread simulation. The interaction of agents within
    # a single environment is performed in a turn-based manner.
    def simulate(self):

        for id, env in self.envs.items():
            if len(env.agents) == 0:
                raise Exception('Environment {} has no registered agent. Either remove the environment or registe at least an agent in it.'.format(id))

        env_done = {env_id: 0 for env_id in self.envs.keys()}
        while True:
            for id, env in self.envs.items():
                if env_done[id] == 0:
                    done = self.simulate_environment(env)
                    env_done[id] = done

            for msg in self.pending_messages:
                self.deliver_message(msg)

            self.pending_messages = list()

            simulate_done = True
            for done in env_done.values():
                simulate_done = simulate_done and done
            if simulate_done:
                break
        
        # reset all the environments
        for _, env in self.envs.items():
            env.reset()

