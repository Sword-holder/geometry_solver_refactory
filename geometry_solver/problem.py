from typing import List

from geometry_solver.entity import Entity
from geometry_solver.condition import Condition
from geometry_solver.target import Target


class Problem(object):
    
    def __init__(self, entity: Entity, conditions: List[Condition], target: Target):
        if len(entity.children) == 0:
            raise ValueError("Problem entity is empty!")
        self.entity = entity
        self.conditions = conditions
        self.target = target
    
    def set_entity(self, entity: Entity) -> None:
        self.entity = entity

    def set_conditions(self, conditions: List[Condition]) -> None:
        self.conditions = conditions
        
