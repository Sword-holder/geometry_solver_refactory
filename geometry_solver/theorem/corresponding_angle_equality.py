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
        """Find corresponding angles from parallel relationship."""
        conds = indexer.index_by_type(Parallel)
        for cond in conds:
            r = cond.relationship
            line1, line2 = r.line1, r.line2
            # col is a list of point entity.
            col1 = indexer.index_collineation_by_line(line1)
            col2 = indexer.index_collineation_by_line(line2)
            if r.reverse:
                col2 = list(reversed(col2))
            for p1 in col1:
                for p2 in col2:
                    # Link line is the line links two parallel lines.
                    link_line = indexer.index_line_by_points(p1, p2)
                    # One link line can generate four corresponding angles at most.
                    if link_line is None:
                        continue
                    link_col = indexer.index_collineation_by_line(link_line)
                    p1_index = link_col.index(p1)
                    p2_index = link_col.index(p2)
                    if p1_index > p2_index:
                        p1_index, p2_index = p2_index, p1_index
                        p1, p2 = p2, p1
                    
        
        return [([p.angle_A, p.angle_B], p.angle_C) for p in repleced_patterns]

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = 180 \
                            - sources[0].attr_value \
                            - sources[1].attr_value
        return sources, target

