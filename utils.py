from typing import List

ROOT = 'tests'


def get_practical_problems(ids: List[int]):
    return [(i, get_problem(i, test_type='practical_test')) for i in ids]
    

def get_problem(number, test_type):
    module_name = test_type + str(number)
    path = '.'.join([ROOT, test_type, module_name])
    exec('from {} import {}'.format(path, module_name))
    exec('problem = {}()'.format(module_name), locals())
    return locals()['problem']

