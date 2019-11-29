import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
from base_main import base_args
from input_checker import *
from problems.problem1.problem1_classes import MaxFunctionProblem
from algo_gen import AlgoGen


if __name__ == '__main__':
    # Population size, mutation probability, iterations, x_min, x_max, bit_length
    population_size, mutation_probability, iterations, crossover_iterations = base_args(sys.argv, 7)
    x_min = test_arg_validity(sys.argv[4], float)
    x_max = test_arg_validity(sys.argv[5], float, lambda x: is_greater(x, x_min))
    bit_length = test_arg_validity(sys.argv[6], int, is_positive)
    problem = MaxFunctionProblem(x_min=x_min, x_max=x_max, bit_length=bit_length)
    solver = AlgoGen(problem=problem, population_size=population_size, mutation_probability=mutation_probability,
                     crossover_iterations=crossover_iterations)
    best = solver.solve(iterations)
    print('Maximum found: f({}) = {} (literal value: {})'.format(*best[1:], best[0]))
