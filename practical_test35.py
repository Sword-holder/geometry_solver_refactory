from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, get_angle, get_length


def practical_test35():
    link(A, B)
    link(A, E, C)
    link(B, D, E)
    link(D, C)

    set_angle('BDC', 120)
    set_angle('ABE', 30)
    set_angle('ACD', 40)
    
    result = get_angle('BAC')

    assert result['answer'] == 50
    

if __name__ == '__main__':
    practical_test35()
    
    