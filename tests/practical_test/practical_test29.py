from geometry_solver.easy_input.abc import A, B, C, D
from geometry_solver.easy_input import link, set_length, set_angle, split_line, perpendicular, get_angle, common_vertex_angles, get_angle, get_length


def practical_test29():
    link(A, B)
    link(A, C)
    link(B, D, C)
    link(A, D)

    set_length('AB', 8)
    set_length('BD', 4)
    common_vertex_angles('A', ['B', 'D', 'C'])
    split_line('BC', 'D')
    set_angle('ABC', 60)
    
    result = get_length('AC')

    assert result['answer'] == 8


if __name__ == '__main__':
    practical_test29()

