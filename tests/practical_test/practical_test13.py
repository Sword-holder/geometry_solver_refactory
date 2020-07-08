from geometry_solver.easy_input.abc import A, B, C, D
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, parallel, get_angle


def practical_test13():
    link(A, B)
    link(A, C)
    link(B, C)
    link(C, D)

    parallel('AB', 'DC')

    set_angle('BAC', 70)
    set_angle('ABC', 40)

    result = get_angle('ACD')

    assert result['answer'] == 70


if __name__ == '__main__':
    practical_test13()

