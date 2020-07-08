from typing import List
import random

import gym

from geometry_solver.problem import Problem
from geometry_solver.theorem import Theorem

class Environment(gym.Env):
    
    def __init__(self, problems: List[Problem], theorems: List[Theorem]):
        self.problem_candidates = problems
        self.theorems = theorems
        self.reset()
    
    def reset(self):
        self.problem = random.choice(self.problem_candidates)
        
    def step(self, action):
        """action is the index of theorem list."""
        theorem = self.theorems[action]
        
