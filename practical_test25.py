from geometry_solver.easy_input.abc import A, B, C, O
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, get_length, common_vertex_angles


def practical_test25():
    link(A, B)
    link(A, C)
    link(B, C)
    link(A, O)
    link(B, O)
    link(C, O)

    set_angle('BAC', 60)
    set_angle('ACB', 60)
    set_angle('ABC', 60)

    split_angle('BAC', 'AO')
    split_angle('ABC', 'BO')
    split_angle('ACB', 'CO')

    common_vertex_angles('B', ['A', 'O', 'C'])
    common_vertex_angles('C', ['A', 'O', 'B'])
    common_vertex_angles('A', ['B', 'O', 'C'])

    result = get_angle('AOB')

    assert result['answer'] == 120


if __name__ == '__main__':
    practical_test25()

