import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
from input_checker import *
from problems.problem4.problem4_classes import HauntedFieldProblem, HauntedFieldIndividual, tester
from algo_gen import AlgoGen


if __name__ == '__main__':
    # Run or test
    # Population size, mutation probability, iterations, number of field to cross,
    # width, height, number of monsters per line
    if len(sys.argv) != 9:
        raise ValueError('Invalid argument number')
    run = sys.argv[1]
    if run not in {'-t', '-r'}:
        raise ValueError('Invalid instruction')
    population_size = test_arg_validity(sys.argv[2], int, is_even)
    mutation_probability = test_arg_validity(sys.argv[3], float, lambda x: is_in_range(x, 0, 1))
    iterations = test_arg_validity(sys.argv[4], int, is_positive)
    fields_to_cross = test_arg_validity(sys.argv[5], int, is_positive)
    width = test_arg_validity(sys.argv[6], int, lambda x: is_greater(x, 2))
    height = test_arg_validity(sys.argv[7], int, lambda x: is_greater(x, 2))
    nb_monsters = test_arg_validity(sys.argv[8], int, lambda x: is_in_range(x, 1, width))
    # Note: some fields might me impossible to cross.
    # To ensure every field is crossable we could use:
    # nb_monster = test_arg_validity(sys.argv[6], int, is_in_range(1, (width - 1) // 2))
    if run == '-r':
        problem = HauntedFieldProblem(height=height, width=width, nb_monsters=nb_monsters,
                                      fields_to_cross=fields_to_cross)
        solver = AlgoGen(problem=problem, population_size=population_size, mutation_probability=mutation_probability)
        best = solver.solve(iterations)
    else:
        individual = HauntedFieldIndividual(243)
        with open(parentdir + '/problems/call_examples/HauntedFieldProblem.txt', 'r') as call_file:
            call_file.readline()  # First two lines contains unneeded problem's informations
            call_file.readline()
            individual.set_value(list(call_file.readline().split(' ')[1][:-1]))
        print('Successfully imported')
        print(str(individual))
        crossed = tester(individual, height, width, nb_monsters, fields_to_cross)
        print('{} fields crossed over {}'.format(crossed, fields_to_cross))
