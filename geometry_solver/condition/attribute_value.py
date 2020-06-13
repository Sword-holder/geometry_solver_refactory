from geometry_solver.condition.condition import Condition
from geometry_solver.entity import Entity
from geometry_solver.relationship import Relationship
from geometry_solver.target.target import Target


class AttributeValue(Condition):
    """This class is responsible for storing value of konwn attribute.
    
    Usage
    ::
        >>> condition = AttributeEq(line_AB, length=1)
    """
    
    def __init__(self, obj, **attr_dict):
        self.obj = obj
        if len(attr_dict) != 1:
            raise ValueError("AttributeValue condition can only keep 1 attribute's value.")
        self.attr_name = list(attr_dict.keys())[0]
        self.attr_value = list(attr_dict.values())[0]

    def match(self, target: Target) -> bool:
        return self.obj == target.obj \
                and target.attr in self.attr_value
    
