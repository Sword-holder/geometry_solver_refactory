from typing import List

from geometry_solver.indexer.base_indexer import BaseIndexer
from geometry_solver.indexer.name_indexer import NameIndexer
from geometry_solver.indexer.ownership_indexer import OwnershipIndexer
from geometry_solver.indexer.pattern_indexer import PatternIndexer
from geometry_solver.indexer.type_indexer import TypeIndexer
from geometry_solver.indexer.value_indexer import ValueIndexer
from geometry_solver.entity.entity import Entity
from geometry_solver.pattern.pattern import Pattern
from geometry_solver.condition.condition import Condition
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
        self.pattern_indexer = PatternIndexer(entity, graph)

    def update_index(self, new_condition=None, new_entity=None) -> bool:
        """Update index after new condition or new entity being added.
        
        return whether indexer is updated successfully.
        """
        if new_condition is None and new_entity is None:
            return False
    
    def index_by_name(self, name, type_=None):
        """Find entities by name.
        
        :param name: name of entity.
        :param type_: type of entity. If None, it will return all type 
            of entities.
        
        return a list of entities whose name if :param name 
            and type is :param type_.
        """
        
    def index_by_ownership(self, obj, owner_type=None):
        """Find entities by ownership.
        
        It will find 
        
        """
        
    def index_by_pattern(self, pattern: Pattern) -> List[Condition]:
        """Find conditions by pattern."""
        return self.pattern_indexer.index(pattern)
        
    def index_by_type(self):
        """Find conditions or entities by type.
        """
        
    def index_by_value(self):
        """Find AttributeValue conditions by value.
        """
        
