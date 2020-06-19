from typing import List, Union

from geometry_solver.indexer.base_indexer import BaseIndexer
from geometry_solver.indexer.name_indexer import NameIndexer
from geometry_solver.indexer.ownership_indexer import OwnershipIndexer
from geometry_solver.indexer.pattern_indexer import PatternIndexer
from geometry_solver.indexer.type_indexer import TypeIndexer
from geometry_solver.indexer.value_indexer import ValueIndexer
from geometry_solver.entity import Entity, Line
from geometry_solver.pattern.pattern import Pattern
from geometry_solver.condition import Condition, AttributeValue
from geometry_solver.graph.deduction_graph import DeductionGraph


class Indexer(BaseIndexer):

    def __init__(self, 
            entity: Entity, 
            graph: DeductionGraph):
        self.build_index(entity, graph)
    
    def build_index(self,
            entity: Entity, 
            graph: DeductionGraph):
        """Build index from entites and conditions.
        
        :param entity: entity container.
        :param graph: deduction graph.
        """
        self.graph = graph
        self.pattern_indexer = PatternIndexer(entity, graph)
        self.type_indexer = TypeIndexer(entity, graph)
        self.value_indexer = ValueIndexer(entity, graph)
        self.name_indexer = NameIndexer(entity, graph)
        self.ownership_indexer = OwnershipIndexer(entity, graph)

    def update_index(self, new_obj: Union[Condition, Entity]):
        """Update index after new condition or new entity being added.
        """
        self.type_indexer.update_index(new_obj)
    
    def index_by_name(self, name, type_=None):
        """Find entities by name.
        
        :param name: name of entity.
        :param type_: type of entity. If None, it will return all type 
            of entities.
        
        return a list of entities whose name if :param name 
            and type is :param type_.
        """
        entities = self.name_indexer.index(name)
        if type_ is not None:
            entities = [e for e in entities if type(e) == type_]
        return entities
        
    def index_by_ownership(self, obj, owner_type):
        """Find entities by ownership.
        
        It will find all object whose name is 
        """
        return self.ownership_indexer.index(obj, owner_type)
        
    def index_by_pattern(self, pattern: Pattern) -> List[Condition]:
        """Find conditions by pattern."""
        return self.pattern_indexer.index(pattern)
        
    def index_by_type(self, type_):
        """Find conditions or entities by type."""
        return self.type_indexer.index(type_)
        
    def index_by_value(self, value):
        """Find AttributeValue conditions by value."""
        return self.value_indexer.index(value)
    
    def index_value_condition(self, obj, attr):
        """Find the AttrValue condition attribute of object.
        
        Return None if not found.
        """
        for cond in self.graph.attr_value_conds:
            if cond.obj == obj and cond.attr_name == attr:
                return cond
        return AttributeValue(obj, **{attr: None})
    
    def index_line_by_points(self, point1, point2):
        """Find line whose two ends are point1 and point2.
        
        Order of points is arbitary.
        Return None if line not exit.
        """
        key = ''.join(sorted([point1.id, point2.id]))
        line = self.index_by_name(key, Line)
        if not line:
            return None
        return line[0]
    
    def index_angle_by_points(self, end1, vertex, end2):
        """Find angle whose vertex is `vertex` and two ends
            are `end1` and `end2`.
        
        Order of `end1` and `end2` is arbitary.
        Firstly, this method will extend two side as far as possible.
        Then, two ends will be sorted by lexicographical order.
        Finally, indexer find angle by its name, so the name of angle 
        is supposed to follow the convention.
        """
        
        
