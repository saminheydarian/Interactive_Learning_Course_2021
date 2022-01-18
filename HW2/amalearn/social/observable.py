from abc import ABC, abstractmethod
from queue import Queue

class Observable(ABC):
    def __init__(self, observed_id, observer_id, max_observations_queue=100):
        self.observed_id = observed_id
        self.observer_id = observer_id
        self.observations = Queue(max_observations_queue)

    # raises Full exception when the queue is full. you should handle it yourself
    def add_observation(self, obs):
        self.observations.put_nowait(obs)
    
    # raises Empty exception when the queue is full. you should handle it yourself
    def observe(self):
        return self.observations.get_nowait()

