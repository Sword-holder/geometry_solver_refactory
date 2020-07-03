from geometry_solver.easy_input.abc import A, B, C, D
from geometry_solver.easy_input import link, set_length, set_angle, split_line, perpendicular, get_angle, common_vertex_angles, get_angle, get_length


# problem idx in another docx:33
def practical_test29():
    link(A, B)
    link(A, C)
    link(B, D, C)
    link(A, D)

    set_length('AB', 8)

    common_vertex_angles('A', ['B', 'D', 'C'])

    split_line('BC', 'D')

    parser.parse_problem()
    line_ab = parser.find_line_by_ends('A', 'B')
    line_ac = parser.find_line_by_ends('A', 'C')
    line_bd = parser.find_line_by_ends('B', 'D')
    line_cd = parser.find_line_by_ends('C', 'D')
    line_ad = parser.find_line_by_ends('A', 'D')

    
    parser.add_equation( \
          symbol(line_ab, 'length') \
        + symbol(line_bd, 'length') \
        + symbol(line_ad, 'length') \
        - symbol(line_ac, 'length') \
        - symbol(line_cd, 'length') \
        - symbol(line_ad, 'length') \
        - 3)

    assert round(get_length('AC'), 6) == 5


