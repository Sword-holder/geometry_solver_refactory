import argparse
import os


parser = argparse.ArgumentParser(description='Argument of test script.')

parser.add_argument('--type', type=str, help='test type(options: basic_test, easy_input_test, ...)')
parser.add_argument('--number', type=int, help='test_script_id')

args = parser.parse_args()

root = 'tests'
test_type = args.type
number = args.number
module_name = test_type + str(number)

path = '.'.join([root, test_type, module_name])
exec('from {} import {}'.format(path, module_name))
exec('{}()'.format(module_name))
