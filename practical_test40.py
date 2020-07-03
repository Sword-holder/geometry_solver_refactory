from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length



# problem idx in another docx:44
def practical_test40():
    link(A, B)
    link(A, D)
    link(B, C)
    link(C, D)
    link(A, C)
    link(B, D)

    common_vertex_angles('A', ['B', 'C', 'D'])
    common_vertex_angles('B', ['A', 'D', 'C'])
    common_vertex_angles('C', ['B', 'A', 'D'])
    common_vertex_angles('D', ['A', 'B', 'C'])

    set_angle('BAD', 60)
    set_angle('BCD', 120)
    set_length('BC', 5)
    set_length('DC', 3)

    parser.parse_problem()

    angle_abd = parser.find_angle_by_points('A', 'B', 'D')
    angle_adb = parser.find_angle_by_points('A', 'D', 'B')

    parser.add_equation(symbol(angle_abd, 'angle') - symbol(angle_adb, 'angle'))

    assert round(get_length('AC'), 6) == 8
    
    