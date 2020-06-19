from typing import Union

from geometry_solver.indexer.base_indexer import BaseIndexer
from geometry_solver.condition import Condition, AttributeValue, RelationshipBased
from geometry_solver.graph.deduction_graph import DeductionGraph
from geometry_solver.entity import Entity, Point, Angle, Line
from geometry_solver.relationship import Collineation


class TopologyIndexer(BaseIndexer):
    
    def __init__(self):
        pass
    
    def build_from_problem(self, 
            entity: Entity,
            graph: DeductionGraph):
        """Build indexer from entity container."""
        lines = [e for e in entity.children if type(e) == Line]
        cols = []
        for c in graph.conditions:
            if isinstance(c, RelationshipBased) and \
                    isinstance(c.relationship, Collineation):
                cols.append(c.relationship)
        
        self.collineation = []
        for col in cols:
            self.collineation.append(''.join([p.id for p in col.points]))

        for line in lines:
            end1, end2 = line.end1, line.end2
            duplicate = False
            for col in self.collineation:
                if end1 in col.points and end2 in col.points:
                    duplicate = True
                    break
            if not duplicate:
                self.collineation.append(end1.id + end2.id)
    
    def extend_line(self, base_point, direction_point):
        if type(base_point) == str and type(direction_point) == str:
            pass
        elif type(base_point) == Point and type(direction_point) == Point:
            base_point = base_point.id
            direction_point = direction_point.id
            
        return self._extend_line(base_point, direction_point)
            
    def angle_alis(self, angle):
        if type(angle) == str:
            pass
        elif type(angle) == Angle:
            angle = angle.id
        return self._angle_alis(angle)

    def line_alis(self, line):
        if type(line) ==str:
            pass
        elif type(line) == Line:
            line = line.id
        return self._line_alis(line)

    def _extend_line(self, base_point_str, direction_point_str):
        index_base = 
        index
    
    def _angle_alis(self, angle_str):
        pass
    
    def _line_alis(self, line_str):
        pass

