from abc import ABC, abstractmethod

class RewardBase(ABC):
    def __init__(self):
        super(RewardBase, self).__init__()

    @abstractmethod
    def get_reward(self):
        # This method must return a SINGLE NUMBER.
        pass