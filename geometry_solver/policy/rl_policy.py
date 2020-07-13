import numpy as np

from geometry_solver.policy.base_policy import BasePolicy
from geometry_solver.reinforcement_learning.utils import state_encoding


class RLPolicy(BasePolicy):

    def __init__(self, agent):
        super().__init__()
        self.agent = agent

    def chose_theorem(self, problem):
        obs = state_encoding(problem)
        theorem_id = self.agent(obs)
        return theorem_id

