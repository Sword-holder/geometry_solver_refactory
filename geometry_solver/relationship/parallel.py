from typing import List

from geometry_solver.entity.line import Line
from geometry_solver.relationship import Relationship
from geometry_solver.relationship.collineation import Collineation


class Parallel(Relationship):

    def __init__(self, 
                 id_: str, 
                 line1: Line,
                 line2: Line):
        super(Parallel, self).__init__(id_)
        self.line1 = line1
        self.line2 = line2
    
    def __str__(self):
        return '(' \
            + 'Parallel relationship ' \
            + self.id \
            + ': ' \
            + 'line1: ' \
            + str(self.line1) \
            + ', line2: ' \
            + str(self.line2) \
            + ')'
