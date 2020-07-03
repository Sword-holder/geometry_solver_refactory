from geometry_solver.easy_input.abc import A, B, C, D
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, parallel, get_angle


def practical_test11():
    link(A, B)
    link(A, C)
    link(B, C)
    link(D, C)

    parallel('AB', 'DC')

    set_angle('ACD', 64)
    set_angle('ABC', 42)

    result = get_angle('ACB')

    assert result['answer'] == 74


if __name__ == '__main__':
    practical_test11()
    
