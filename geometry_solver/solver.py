from typing import List
import time

import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

from geometry_solver.entity.entity import Entity
from geometry_solver.condition.condition import Condition
from geometry_solver.graph.deduction_graph import DeductionGraph
from geometry_solver.target.target import Target
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.policy import BasePolicy, RandomPolicy


class Solver(object):

    def __init__(self, 
            entity: Entity=None,
            target: Target=None,
            conditions: List[Condition]=None,
            policy: BasePolicy=None):
        if len(entity.children) == 0:
            raise ValueError("Problem entity is empty!")
        self.entity = entity
        self.target = target
        self.conditions = conditions
        if policy is None:
            policy = RandomPolicy()
        self.policy = policy

    def set_entity(self, entity: Entity) -> None:
        self.entity = entity

    def set_conditions(self, conditions: List[Condition]) -> None:
        self.conditions = conditions

    def solve(self, 
            show_answer=True,
            show_process=True,
            show_graph=True,
            prune=True) -> None:
        """Solve the problem.

        :param show_answer: 
            if true, final answer will be printed through standard output.
        :param show_process: 
        if true, solving process will be printed through standard output.
        :param show_graph: 
            if true, deduction graph will be shown after solved.
        :prune_graph: 
            if true, the deduction graph will be pruned to remove unneccessary step.
        """
        
        # Initialize deduction graph.
        graph = DeductionGraph(self.conditions, self.target)
        
        # Build indexer
        indexer = Indexer(self.entity, graph)

        begin = time.time()
        trial_times = 0
        # Adopt policy until solve the problem.
        while not graph.solved:
            theorem = self.policy.chose_theorem()
            if show_process:
                print("trial {}: chose {}".format(trial_times, theorem.name))
            # Traverse all [sources, target] pair that meet requirement of theorem.
            for srcs, tg in theorem.index(indexer):
                srcs, tg = theorem.deduct(srcs, tg)
                graph.expand(tg)
                tg.from_conditions = srcs
                tg.from_theorem = theorem
                indexer.update_index(tg)
            trial_times += 1
        end = time.time()
        time_usage = end - begin

        solving_steps_before_prune = graph.solving_steps()
        solving_steps_after_prune = None

        if prune:
            graph.prune()
            solving_steps_after_prune = graph.solving_steps()
        
        if show_process:
            print('Problem solved succesfully!')
        
        plain_word_answer = graph.plain_word_answer()
        if show_answer:
            print(plain_word_answer)

        if show_graph:
            graph.show_graph()
        
        result = {
            "plain_word_answer": plain_word_answer,
            "solving_steps_before_prune": solving_steps_before_prune,
            "solving_steps_after_prune": solving_steps_after_prune,
            "trial_times": trial_times,
            "time_usage": time_usage
        }
        return result

