import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
from input_checker import *
from problems.problem4.problem4_classes import HauntedFieldProblem
from algo_gen import AlgoGen


if __name__ == '__main__':
    # Population size, mutation probability, iterations, number of field to cross,
    # width, height, number of monsters per line
    if len(sys.argv) != 8:
        raise ValueError('Invalid argument number')
    population_size = test_arg_validity(sys.argv[1], int, is_even)
    mutation_probability = test_arg_validity(sys.argv[2], float, lambda x: is_in_range(x, 0, 1))
    iterations = test_arg_validity(sys.argv[3], int, is_positive)
    fields_to_cross = test_arg_validity(sys.argv[4], int, is_positive)
    width = test_arg_validity(sys.argv[5], int, lambda x: is_greater(x, 2))
    height = test_arg_validity(sys.argv[6], int, lambda x: is_greater(x, 2))
    nb_monsters = test_arg_validity(sys.argv[7], int, lambda x: is_in_range(x, 1, width))
    # Note: some fields might me impossible to cross.
    # To ensure every field is crossable we could use:
    # nb_monster = test_arg_validity(sys.argv[6], int, is_in_range(1, (width - 1) // 2))
    crossover_rate = 0
    problem = HauntedFieldProblem(height, width, nb_monsters)
    solver = AlgoGen(problem, population_size, mutation_probability, crossover_rate)
    best = solver.solve(iterations)
