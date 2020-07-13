from typing import List
import random

import gym

from geometry_solver.problem import Problem
from geometry_solver.theorem import Theorem
from geometry_solver.reinforcement_learning.utils import state_encoding, initialize_theorems


class Environment(gym.Env):
    
    def __init__(self, problems: List[Problem], theorems: List[Theorem]=None):
        self.problem_candidates = problems
        if theorems is not None:
            self.theorems = theorems
        else:
            self.theorems = initialize_theorems()
        self.reset()
    
    def reset(self, problem_id=None):
        if problem_id is not None:
            self.problem = self.problem_candidates[problem_id-1]
        else:
            self.problem = random.choice(self.problem_candidates)
        return state_encoding(self.problem)
        
    def step(self, action):
        """action is the index of theorem list."""
        action = int(action)
        theorem = self.theorems[action]
        self.problem.deduct(theorem)
        obs = state_encoding(self.problem)
        done = self.problem.solved
        reward = 100 if done else -1
        info = {}
        return obs, reward, done, info
    
    def render(self, mode='human'):
        """
            - human: show deduction graph.
            - rgb_array: show encoded state.
            - ansi: show plain word answer.
        """
        if self.problem is None:
            print('Problem is not solved!')
        if mode == 'human':
            self.problem.graph.show_graph()
        elif mode == 'rgb_array':
            print(state_encoding(self.problem))
        elif mode == 'ansi':
            print(self.problem.plain_word_answer)
    
    def close(self):
        pass
    
    def seed(self, seed=None):
        """Sets the seed for this env's random number generator(s).
        Note:
            Some environments use multiple pseudorandom number generators.
            We want to capture all such seeds used in order to ensure that
            there aren't accidental correlations between multiple generators.
        Returns:
            list<bigint>: Returns the list of seeds used in this env's random
              number generators. The first value in the list should be the
              "main" seed, or the value which a reproducer should pass to
              'seed'. Often, the main seed equals the provided 'seed', but
              this won't be true if seed=None, for example.
        """
        return

