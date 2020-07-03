from geometry_solver.easy_input.abc import A, B, C, D, E, F, P
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle


def practical_test26():
    link(A, B, E)
    link(A, C, F)
    link(B, C)
    link(B, D)
    link(C, D)
    link(B, P)
    link(C, P)

    set_angle('BAC', 30)

    split_angle('ABC', 'BD', 0.5)
    split_angle('ACB', 'CD', 0.5)
    split_angle('CBE', 'BP', 0.5)
    split_angle('BCF', 'CP', 0.5)

    common_vertex_angles('B', ['A', 'D', 'C', 'P'])
    common_vertex_angles('C', ['A', 'D', 'B', 'P'])
    
    result = get_angle('BPC')

    assert result['answer'] == 75


if __name__ == '__main__':
    practical_test26()
