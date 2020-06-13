from typing import List

from geometry_solver.indexer.base_indexer import BaseIndexer
from geometry_solver.entity import Entity, Triangle, Angle, Line
from geometry_solver.pattern.pattern import Pattern
from geometry_solver.condition.condition import Condition
from geometry_solver.graph.deduction_graph import DeductionGraph
from geometry_solver.condition.attribute_value import AttributeValue
from geometry_solver.pattern.triangle_pattern import TrianglePattern
from geometry_solver.pattern.attribute_state import AttributeState


class PatternIndexer(BaseIndexer):
    
    def __init__(self,
            entity: Entity, 
            graph: DeductionGraph):
        self.dispatch_map = {
            Angle: self._extract_angle_pattern,
            Line: self._extract_line_pattern,
            Triangle: self._extract_triangle_pattern,
        }
        self.build_index(entity, graph)

    def build_index(self,
            entity: Entity, 
            graph: DeductionGraph):
        self.entity = entity
        self.graph = graph
        self.table = {}
        for e in entity.children:
            if type(e) in self.dispatch_map.keys():
                # Extract pattern from entity.
                for p, vp in self._extract_pattern(e):
                    if p not in self.table:
                        self.table[p] = [] 
                    self.table[p].append(vp)

    def update_index(self, 
            new_condition: Condition=None,
            new_entity: Entity=None):
        # if type(new_condition) == AttributeValue:
        pass
    
    def index(self, pattern: Pattern):
        """Return a list of modified pattern whose UNKOWN attributes 
            are replaced by AttributeValue condition."""
        return self.table[pattern]
    
    def _extract_pattern(self, entity: Entity):
        """This method is responsible for dispatch pattern extraction 
        according to type of entity.
        
        Return a tuple of (pattern, (known_conditions, unknown_conditions)).
        """
        return self.dispatch_map[type(entity)](entity)
    
    def _extract_triangle_pattern(self, triangle: Triangle):
        """Extract patterns of triangle.
        
        Return a list of (pattern, (known_conditions, unknown_conditions)).
        """
        ret = []
        pattern_list = []
        value_pattern_list = []
        
        attr_map = {
            Angle: 'angle',
            Line: 'length'
        }
        
        conds = self.graph.conditions
        value_conds = [c for c in conds if type(c) == AttributeValue]
        
        def find_obj(obj, attr=None):
            for c in value_conds:
                if c.obj == obj:
                    if attr is None or attr == c.attr_name:
                        return c
            if attr is None:
                attr = attr_map[type(obj)]
            return AttributeValue(obj, **{attr: None})
        
        angle1 = find_obj(triangle.angle1)
        angle2 = find_obj(triangle.angle2)
        angle3 = find_obj(triangle.angle3)
        side1 = find_obj(triangle.side1)
        side2 = find_obj(triangle.side2)
        side3 = find_obj(triangle.side3)
        circumference = find_obj(triangle, 'circumference')
        area = find_obj(triangle, 'area')
        
        UNKNOWN = AttributeState.UNKNOWN
        KNOWN = AttributeState.KNOWN
        
        angles = [angle1, angle2, angle3]
        sides = [side1, side2, side3]
        angle_name = ['angle_A', 'angle_B', 'angle_C']
        line_name = ['line_BC', 'line_AC', 'line_AB']
        for permutation in [[0, 1, 2], [0, 2, 1], [1, 0, 2], \
                [1, 2, 0], [2, 0, 1], [2, 1, 0]]:
            pattern = TrianglePattern(init_value=UNKNOWN)
            value_pattern = TrianglePattern(init_value=UNKNOWN)
            
            def set_pattern(obj, attr_name):
                is_known = UNKNOWN if obj.attr_value is None else KNOWN
                pattern.__setattr__(attr_name, is_known)
                value_pattern.__setattr__(attr_name, obj)
                
            for i in range(3):
                angle = angles[permutation[i]]
                side = sides[permutation[i]]
                set_pattern(angle, angle_name[i])
                set_pattern(side, line_name[i])
            set_pattern(circumference, 'circumference')
            set_pattern(area, 'area')
            
            ret.append((pattern, value_pattern))

        return ret
                    
    def _extract_line_pattern(self, line: Line):
        return []
    
    def _extract_angle_pattern(self, angle: Angle):
        return []

