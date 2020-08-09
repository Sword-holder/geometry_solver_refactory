from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test105():
    link(A, B)
    link(A, G, C)
    link(B, C, D, E)
    link(G, F, D)
    link(E, F)

    is_equilateral_triangle('ABC')
    set_angle('DFE', 20)
    line_equivalence('DF', 'DE')
    
    get_angle('BEF')

    return get_problem()
    

if __name__ == '__main__':
    practical_test105()
