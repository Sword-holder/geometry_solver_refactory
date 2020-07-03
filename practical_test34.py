from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length



def practical_test34():
    link(A, B)
    link(A, E, C)
    link(B, D, C)
    link(A, D)
    link(D, E)

    set_angle('BAD', 40)

    common_vertex_angles('A', ['B', 'D', 'C'])
    common_vertex_angles('D', ['B', 'A', 'E'])

    parser.parse_problem()

    angle_b = parser.find_angle_by_points('A', 'B', 'C')
    angle_c = parser.find_angle_by_points('A', 'C', 'B')
    angle_ade = parser.find_angle_by_points('A', 'D', 'E')
    angle_aed = parser.find_angle_by_points('A', 'E', 'D')   
    parser.add_equation(symbol(angle_b, 'angle') - symbol(angle_c, 'angle'))
    parser.add_equation(symbol(angle_ade, 'angle') - symbol(angle_aed, 'angle'))
    
    assert round(get_angle('CDE'), 6) == 20

    