from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, parallel, get_angle, common_vertex_angles, get_angle, get_length, split_line



def practical_test49():
    link(A, D, B)
    link(A, E, C)
    link(D, E)
    link(B, C)

    set_angle('ADE', 60)
    set_angle('ABC', 60)
    set_angle('BAC', 30)
    set_length('DE', 4)

    parser.parse_problem()
    line_ad = parser.find_line_by_ends('A', 'D')
    line_ab = parser.find_line_by_ends('A', 'B')
    parser.add_equation(3 * symbol(line_ad, 'length') - symbol(line_ab, 'length'))

    assert round(get_length('BC'), 6) == 12
    
    