from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, add_equation



def practical_test10():
    link(A, E, B)
    link(A, F, C)
    link(B, D, C)
    link(D, E)
    link(D, F)

    perpendicular('DE', 'AB')
    perpendicular('FD', 'BC')

    set_angle('AFD', 158)

    common_vertex_angles('D', ['B', 'E', 'F'])

    parser.parse_problem()
    angle_abc = parser.find_angle_by_points('A', 'B', 'C')
    angle_acb = parser.find_angle_by_points('A', 'C', 'B')
    parser.add_equation(symbol(angle_abc, 'angle') - symbol(angle_acb, 'angle'))

    assert round(get_angle('EDF'), 6) == 68

    
