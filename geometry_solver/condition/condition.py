from geometry_solver.target.target import Target


class Condition(object):
    
    def __init__(self):
        self.from_conditions = []

    def match(self, target: Target) -> bool:
        raise NotImplementedError
    
