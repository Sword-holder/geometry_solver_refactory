from typing import List

from geometry_solver.target.target import Target
from geometry_solver.condition.condition import Condition


class DeductionGraph(object):
    
    def __init__(self, 
            conditions: List[Condition],
            target: Target):
        self.conditions = conditions
        self.target = target
        self.solved = self._target_solved(conditions, target)

    def expand(self, new_condition: Condition):
        """Expand graph after one step deduction.

        :param new_condition: a new condition add to graph.
        """
        self.conditions.append(new_condition)
        if not self.solved \
                and self._target_solved([new_condition], self.target):
            self.solved = True

    def _target_solved(self, 
            conditions: List[Condition], 
            target: Target):
        """Traversal the conditions, find if there is a condition match target.
        
        Return true if there is a condition match the target.
        """
        for cond in conditions:
            if cond.match(target):
                return True
        return False

