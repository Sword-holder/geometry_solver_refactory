from typing import List

import networkx as nx
import matplotlib.pyplot as plt

from geometry_solver.target.target import Target
from geometry_solver.condition import Condition, AttributeValue


class DeductionGraph(object):
    
    def __init__(self, 
            conditions: List[Condition],
            target: Target):
        self.conditions = conditions
        self.attr_value_conds = \
                [c for c in conditions if type(c) == AttributeValue]
        self.target = target
        self.solved = self._target_solved(conditions, target)
        self.target_node = None

    def expand(self, new_condition: Condition):
        """Expand graph after one step deduction.

        :param new_condition: a new condition add to graph.
        """
        self.conditions.append(new_condition)
        if type(new_condition) == AttributeValue:
            self.attr_value_conds.append(new_condition)
        
        if not self.solved \
                and self._target_solved([new_condition], self.target):
            self.target_node = new_condition
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

    def solving_path(self):
        if self.target_node is None:
            return """The problem is solved!"""
        return self._solving_path(self.target_node)

    def _solving_path(self, target_node):
        path_str = ''
        for cond in target_node.from_conditions:
            path_str += self._solving_path(cond) + '\n'
        path_str += str(target_node)
        return path_str

    def show_graph(self):
        self._show_graph(self.conditions)
        
    def _show_graph(self, conditions):
        G = nx.DiGraph()
        for cond in conditions:
            G.add_node(cond)
        for cond in conditions:
            for src in cond.from_conditions:
                G.add_edge(src, cond)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
        
        
    def prune(self):
        if self.target_node is None:
            raise ValueError("The problem is solved!")
        self.conditions = self._prune(self.target_node)
        
    def _prune(self, condition):
        """Prune the graph and return pruned condition list."""
        if not condition.from_conditions:
            return [condition]
        useful_conditions = [condition]
        for cond in condition.from_conditions:
            useful_conditions += self._prune(cond)
        return useful_conditions

