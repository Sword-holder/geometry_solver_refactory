from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test104():
    link(A, B)
    link(A, E, C)
    link(A, F, D)
    link(B, F, E)
    link(B, D, C)

    is_equilateral_triangle('ABC')
    set_length('AE', 1)
    set_length('CD', 1)
    set_length('AC', 4)
    set_angle('BAD', 45)
    common_vertex_angles('A', ['B', 'D', 'C'])
    common_vertex_angles('B', ['A', 'E', 'C'])
    
    get_angle('BFD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test104()
