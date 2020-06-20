from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import Parallel


class CorrespondingAngleEquality(Theorem):

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        conds = indexer.index_by_type(Parallel)
        for cond in conds:
            r = cond.relationship
            line1, line2 = r.line1, r.line2
            # col is a list of point entity.
            col1 = indexer.index_collineation_by_line(line1)
            col2 = indexer.index_collineation_by_line(line2)
            for p1 in col1:
                for p2 in col2:
                    
        
        return [([p.angle_A, p.angle_B], p.angle_C) for p in repleced_patterns]

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = 180 \
                            - sources[0].attr_value \
                            - sources[1].attr_value
        return sources, target

