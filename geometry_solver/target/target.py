

class Target(object):
    
    def __init__(self, obj, attr):
        self.obj = obj
        self.attr = attr
        
    def __str__(self):
        return '(Target: ' + \
            self.obj.id + \
            '.' + \
            self.attr + \
            ')'
        
