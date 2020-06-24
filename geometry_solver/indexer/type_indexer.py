from typing import Union

from geometry_solver.indexer.base_indexer import BaseIndexer
from geometry_solver.entity import (Entity, Point, Line, 
        Angle, Area, Triangle)
from geometry_solver.relationship import (Relationship, Collineation, 
        CommonVertexAngle, NAngleSector, NLineSector, OppositeVerticalAngle,
        Parallel, Perpendicular, SimilarTriangle, SupplementaryAngle, 
        IsRightTriangle, IsIsoscelesTriangle, IsEquilateralTriangle)
from geometry_solver.graph.deduction_graph import DeductionGraph
from geometry_solver.condition import RelationshipBased
from geometry_solver.condition.condition import Condition


class TypeIndexer(BaseIndexer):
    
    def __init__(self,
            entity: Entity, 
            graph: DeductionGraph):
        # In this table, key is entity/relationship type, and value 
        # is a list of entities/relationships of this type.
        self.table = {
            Point: [],
            Line: [],
            Angle: [],
            Area: [],
            Triangle: [],
            Collineation: [],
            CommonVertexAngle: [],
            NAngleSector: [],
            NLineSector: [],
            OppositeVerticalAngle: [],
            Parallel: [],
            Perpendicular: [],
            SimilarTriangle: [],
            SupplementaryAngle: [],
            IsRightTriangle: [],
            IsIsoscelesTriangle: [],
            IsEquilateralTriangle: []
        }
        self.build_index(entity, graph)
    
    def build_index(self,
            entity: Entity, 
            graph: DeductionGraph):
        for e in entity.children:
            self.table[type(e)].append(e)
        for cond in graph.conditions:
            if type(cond) == RelationshipBased:
                r = cond.relationship
                self.table[type(r)].append(cond)

    def update_index(self, new_obj: Union[Condition, Entity]):
        if isinstance(new_obj, Entity):
            self.table[type(e)].append(new_obj)
        elif type(new_obj) == RelationshipBased:
            r = new_obj.relationship
            self.table[type(r)].append(new_obj)

    def index(self, type_):
        """Return a list of entity/relationship condition of this type."""
        return self.table[type_]
    
