from geometry_solver.easy_input.abc import A, B, C, D, E, F, G, P
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, parallel, get_angle, common_vertex_angles, add_equation



def practical_test12():
    link(A, C)
    link(A, E, P)
    link(A, F, G, D)
    link(B, F, E, C)
    link(B, G, P)
    link(B, D)

    set_angle('ACB', 32)
    set_angle('ADB', 28)

    parser.parse_problem()

    angle_cap = parser.find_angle_by_points('C', 'A', 'P')
    angle_dap = parser.find_angle_by_points('D', 'A', 'P')
    parser.add_equation(symbol(angle_cap, 'angle') - symbol(angle_dap, 'angle'))

    angle_cbp = parser.find_angle_by_points('C', 'B', 'P')
    angle_dbp = parser.find_angle_by_points('D', 'B', 'P')
    parser.add_equation(symbol(angle_cbp, 'angle') - symbol(angle_dbp, 'angle'))

    assert round(get_angle('APB'), 6) == 30

    
