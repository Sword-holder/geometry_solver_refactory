import torch

import geometry_solver.reinforcement_learning.env_params as env_params
from geometry_solver.problem import Problem
from geometry_solver.entity import Entity
from geometry_solver.condition import RelationshipBased
import geometry_solver.theorem


def initialize_theorems():
    theorems = geometry_solver.theorem.valid_theorem
    return [th() for th in theorems]


def state_encoding(problem):
    """Extract tensor presentation of environment.
    
    Return a map encodes diffirent types of component.
    """
    state_map = {}
    state_map['entity'] = _entity_encoding(problem)
    state_map['relationship'] = _relationship_encoding(problem)
    state_map['target'] = _target_encoding(problem)
    return state_map
    
    
def _entity_encoding(problem):
    entity_type_tensor = torch.zeros(
            env_params.MAX_ENTITIES, 
            env_params.ENTITY_TYPE_NUM,
            dtype=torch.float32)
    entity_attribute_tensor = torch.zeros(
            env_params.MAX_ENTITIES, 
            env_params.ENTITY_ATTRIBUTE_NUM,
            dtype=torch.float32)
    indexer = problem.indexer
    entity_list = list(problem.entity.children)
    
    for i, e in enumerate(entity_list):
        type_index = env_params.ALL_ENTITY_TYPE.index(type(e))
        entity_type_tensor[i, type_index] = 1
        for j, attr in enumerate(env_params.ENTITY_ATTRIBUTES[type(e)]):
            cond = indexer.index_value_condition(e, attr, create_when_not_found=False)
            if cond is not None:
                entity_attribute_tensor[i, j] = 1
    
    entity_tensor = torch.cat((entity_type_tensor, entity_attribute_tensor), dim=1)
    return entity_tensor
    
    
def _relationship_encoding(problem):
    relationship_type_tensor = torch.zeros(
            env_params.MAX_RELATIONSHIPS,
            env_params.RELATIONSHIP_TYPE_NUM,
            dtype=torch.float32)
    relationship_attrbute_tensor = torch.zeros(
            env_params.MAX_RELATIONSHIPS,
            env_params.RELATIONSHIP_ATTRIBUTE_NUM,
            dtype=torch.float32)
    relationship_link_entity_tensor = torch.zeros(
            env_params.MAX_RELATIONSHIPS,
            env_params.MAX_ENTITIES,
            dtype=torch.float32)
    indexer = problem.indexer
    entity_list = list(problem.entity.children)
    
    relationships = [cond.relationship for cond in problem.conditions \
            if type(cond) == RelationshipBased]
    
    for i, r in enumerate(relationships):
        type_index = env_params.ALL_RELATIONSHIP_TYPE.index(type(r))
        relationship_type_tensor[i, type_index] = 1
        for j, attr in enumerate(env_params.RELATIONSHIP_ATTRIBUTES[type(r)]):
            cond = indexer.index_value_condition(e, attr, create_when_not_found=False)
            if cond is not None:
                entity_attribute_tensor[i, j] = 1
                
        for member_str in dir(r):
            member = getattr(r, member_str)
            if isinstance(member, Entity):
                entity_index = entity_list.index(member)
                relationship_link_entity_tensor[i, entity_index] = 1
            elif isinstance(member, list):
                for e in member:
                    if isinstance(e, Entity):
                        entity_index = entity_list.index(e)
                        relationship_link_entity_tensor[i, entity_index] = 1
    
    relationship_tensor = torch.cat(
            (relationship_type_tensor, 
             relationship_attrbute_tensor, 
             relationship_link_entity_tensor), dim=1)
    return relationship_tensor


def _target_encoding(problem):
    target_tensor = torch.zeros(
            env_params.MAX_ENTITIES 
            + env_params.ENTITY_ATTRIBUTE_NUM
            + env_params.MAX_RELATIONSHIPS 
            + env_params.RELATIONSHIP_ATTRIBUTE_NUM,
            dtype=torch.float32)
    target = problem.target
    entity_list = list(problem.entity.children)
    relationships = [cond.relationship for cond in problem.conditions \
            if type(cond) == RelationshipBased]
    
    if target.obj in entity_list:
        obj_index = entity_list.index(target.obj)
        target_tensor[obj_index] = 1
        attr_index = env_params.ENTITY_ATTRIBUTES[type(target.obj)].index(target.attr)
        target_tensor[env_params.MAX_ENTITIES + attr_index] = 1
    else:
        base = env_params.MAX_ENTITIES + env_params.ENTITY_ATTRIBUTE_NUM
        obj_index = relationships.index(target.obj)
        target_tensor[base + obj_index] = 1
        attr_index = env_params.RELATIONSHIP_ATTRIBUTES[type(target.obj)].index(target.attr)
        target_tensor[base + env_params.MAX_RELATIONSHIPS + attr_index] = 1
    
    return target_tensor
        
