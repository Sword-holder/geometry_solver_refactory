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
                if col.find(end1.id) != -1 and col.find(end2.id) != -1:
                    duplicate = True
                    break
            if not duplicate:
                self.collineation.append(end1.id + end2.id)

        # Key of _angle_alis dict is standard name, value is angle entity.
        self._angle_alis = {}
        for e in entity.children:
            if type(e) == Angle:
                std_name = self.angle_alis(e)
                self._angle_alis[std_name] = e
    
    def extend_line(self, base_point, direction_point):
        """Given two point/point's id, extend line and return line'id(str type).
        
        Return None if two point are not in the same line.
        """
        if type(base_point) == str and type(direction_point) == str:
            pass
        elif type(base_point) == Point and type(direction_point) == Point:
            base_point = base_point.id
            direction_point = direction_point.id
        
        return self._extend_line(base_point, direction_point)
            
    def index_angle_by_points(self, end1, vertex, end2):
        if type(end1) == str and type(vertex) == str and type(end2) == str:
            pass
        elif type(end1) == Point and type(vertex) == Point and type(end2) == Point:
            end1, vertex, end2 = end1.id, vertex.id, end2.id
        std_name = self.angle_alis(end1 + vertex + end2)
        return self._angle_alis[std_name]

    def _extend_line(self, base_point_str, direction_point_str):
        """Given two point's, return extended line' id.
        
        Return None if two point are not in the same line.
        """
        index_base = -1
        index_direction = -1
        for col in self.collineation:
            try:
                index_base = col.index(base_point_str)
                index_direction = col.index(direction_point_str)
            except ValueError:
                continue
            # Found the collineation, begin to extend line.
            if index_base < index_direction:
                index_direction = len(col) - 1
            else:
                index_direction = 0
            return col[index_base] + col[index_direction]
        return None

    def angle_alis(self, angle):
        """Given an angle or id of the angle, 
        return standard name of the angle.
        """
        if type(angle) == Angle:
            angle = angle.id
        vertex, end1 = self._extend_line(angle[1], angle[0])
        vertex, end2 = self._extend_line(angle[1], angle[2])
        if end1 > end2:
            end1, end2 = end2, end1
        return end1 + vertex + end2

