from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, split_line



# problem idx in another docx:48
def practical_test44():
    link(A, B)
    link(A, D)
    link(D, C)
    link(C, E, B)
    link(B, D)
    link(D, E)

    set_length('AD', 1)
    set_length('AE', 1)
    set_length('CD', 1)
    split_angle('ABC', 'BD', 0.5)

    set_angle('BAD', 100)
    set_angle('ABD', 30)

    common_vertex_angles('B', ['A', 'D', 'C'])
    common_vertex_angles('D', ['A', 'B', 'E', 'C'])

    parser.parse_problem()

    line_ab = parser.find_line_by_ends('A', 'B')
    line_be = parser.find_line_by_ends('B', 'E')

    parser.add_equation(symbol(line_ab, 'length') - symbol(line_be, 'length'))

    assert round(get_angle('BCD'), 6) == 80

    