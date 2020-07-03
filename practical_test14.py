from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, parallel, get_angle, common_vertex_angles, add_equation



def practical_test14():
    link(A, B)
    link(A, D, C)
    link(B, C)
    link(B, E, D)
    link(C, E)

    set_angle('ABD', 30)
    set_angle('CBD', 30)
    set_angle('BAC', 80)

    parser.parse_problem()
    angle_bce = parser.find_angle_by_points('B', 'C', 'E')
    angle_ace = parser.find_angle_by_points('A', 'C', 'E')
    parser.add_equation(symbol(angle_bce, 'angle') - symbol(angle_ace, 'angle'))

    assert round(get_angle('BEC'), 6) == 130

    
