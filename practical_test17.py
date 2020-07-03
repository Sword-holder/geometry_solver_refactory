from geometry_solver.easy_input.abc import A, B, C, D
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, add_equation



def practical_test17():
    link(A, B)
    link(A, D, C)
    link(B, D)
    link(B, C)

    set_angle('BAC', 40)

    common_vertex_angles('B', ['A', 'D', 'C'])

    # Set as unit length.
    set_length('AB', 1)
    
    parser.parse_problem()

    AB = parser.find_line_by_ends('A', 'B')
    AC = parser.find_line_by_ends('A', 'C')
    parser.add_equation(symbol(AB, 'length') - symbol(AC, 'length'))

    BD = parser.find_line_by_ends('B', 'D')
    BC = parser.find_line_by_ends('B', 'C')
    parser.add_equation(symbol(BD, 'length') - symbol(BC, 'length'))


    assert round(get_angle('ABD'), 6) == 30


if __name__ == '__main__':
    practical_test17()

