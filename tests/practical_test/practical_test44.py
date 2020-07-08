from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, split_line, line_equivalence


def practical_test44():
    link(A, B)
    link(A, D)
    link(D, C)
    link(C, E, B)
    link(B, D)
    link(D, E)

    set_length('CD', 1)
    set_length('DE', 1)
    set_length('CE', 1)
    
    split_angle('ABC', 'BD', 0.5)

    set_angle('BAD', 100)
    set_angle('BDE', 100)
    set_angle('ABD', 30)

    common_vertex_angles('B', ['A', 'D', 'C'])
    common_vertex_angles('D', ['A', 'B', 'E', 'C'])

    line_equivalence('AB', 'BE')
    
    result = get_angle('BCD')

    assert result['answer'] == 60

    
if __name__ == '__main__':
    practical_test44()

