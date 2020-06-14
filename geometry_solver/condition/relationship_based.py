from geometry_solver.relationship import Relationship
from .condition import Condition


class RelationshipBased(Condition):
    """RelationshipBased is the wrapper of a relationship.
    
    Usage
    ::
        >>> condition = RelationshipBased(parallel_AB_CD)

    """
    
    def __init__(self, relationship: Relationship):
        self.relationship = relationship

    def __hash__(self):
        return (self.relationship).__hash__()


