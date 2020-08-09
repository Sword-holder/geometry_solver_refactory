from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test89():
    link(A, E, B)
    link(A, F, C)
    link(B, D, C)
    link(D, F)
    link(D, E)
    link(A, D)

    split_line('AB', 'D')
    perpendicular('AD', 'BC')
    perpendicular('DE', 'AB')
    perpendicular('DF', 'AC')
    is_equilateral_triangle('ABC')
    set_length('AB', 8)
    common_vertex_angles('A', ['B', 'D', 'C'])
    
    get_length('BE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test89()
