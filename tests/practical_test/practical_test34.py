from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, angle_equivalence



def practical_test34():
    link(A, B)
    link(A, E, C)
    link(B, D, C)
    link(A, D)
    link(D, E)

    set_angle('ABC', 30)
    set_angle('ADE', 60)

    common_vertex_angles('A', ['B', 'D', 'C'])
    common_vertex_angles('D', ['B', 'A', 'E'])

    angle_equivalence('ABC', 'ACB')
    angle_equivalence('ADE', 'AED')
    
    result = get_angle('CDE')
    
    assert result['answer'] == 30

    
if __name__ == '__main__':
    practical_test34()
    
