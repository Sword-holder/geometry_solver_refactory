from typing import List

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
            show_graph=False,
            prune_graph=False) -> None:
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

        # Adopt policy until solve the problem.
        while not graph.solved:
            theorem = self.policy.chose_theorem()
            # Traverse all [sources, target] pair that meet requirement of theorem.
            for srcs, tg in theorem.index(indexer):
                srcs, tg = theorem.deduct(srcs, tg)
                graph.expand(tg)
                tg.from_conditions = srcs
        
        print('Problem solved succesfully!')
        print(graph.solving_path())
        graph.show_graph()
        
        return graph

