import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from input_checker import *
from problems.problem1_max_function import MaxFunctionProblem, f
from algo_gen import AlgoGen


if __name__ == '__main__':
    # Population size, mutation probability, iterations, x_min, x_max, bit_length(, crossover_rate)
    if len(sys.argv) != 7:
        raise ValueError('Invalid argument number')
    population_size = test_arg_validity(sys.argv[1], int, is_even)
    mutation_probability = test_arg_validity(sys.argv[2], float, lambda x: is_in_range(x, 0, 1))
    iterations = test_arg_validity(sys.argv[3], int, is_positive)
    x_min = test_arg_validity(sys.argv[4], float)
    x_max = test_arg_validity(sys.argv[5], float)
    bit_length = test_arg_validity(sys.argv[6], int, is_positive)
    crossover_rate = 0  # To change
    problem = MaxFunctionProblem(x_min, x_max, bit_length)
    solver = AlgoGen(problem, population_size, mutation_probability, crossover_rate)
    best = solver.solve(iterations)
    max_value = problem.adapt(best)
    print('Maximum found: f({}) = {}'.format(max_value, f(max_value)))
