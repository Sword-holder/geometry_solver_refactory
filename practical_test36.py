from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length


def practical_test36():
    link(A, D)
    link(A, E)
    link(D, C)
    link(E, C)
    link(D, B)
    link(E, B)
    link(D, E)

    set_angle('DAE', 50)
    set_angle('DBE', 130)

    split_angle('ADB', 'DC')
    split_angle('AEB', 'EC')

    common_vertex_angles('D', ['A', 'C', 'B', 'E'])
    common_vertex_angles('E', ['A', 'C', 'B', 'D'])

    result = get_angle('DCE')

    assert result['answer'] == 90


if __name__ == '__main__':
    practical_test36()
    
