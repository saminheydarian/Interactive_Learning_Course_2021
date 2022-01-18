from amalearn.agent import AgentBase
from abc import abstractmethod
from queue import Queue
from amalearn.social import Message

class SocialAgent(AgentBase):
    def __init__(self, id: str, container, environment, queue_max_size=100):
        super(SocialAgent, self).__init__(id, environment)
        if container is None:
            raise Exception('The container cannot be None.')
        self.container = container
        self.container.register_agent(self, environment.id)
        self.inbox = Queue(queue_max_size)
        self.observables = []

    # DO NOT CHANGE THIS METHOD
    def request_observation(self, agent_id, env_id):
        pass
    
    # DO NOT CHANGE THIS METHOD
    def cancel_observation(self, agent_id, env_id):
        pass

    # DO NOT CHANGE THIS METHOD
    def send_message(self, message: Message):
        self.container.enqueue_message(message)

