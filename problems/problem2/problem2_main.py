import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
from input_checker import *
from problems.problem2.problem2_classes import SecretMessageProblem
from algo_gen import AlgoGen

if __name__ == '__main__':
    # Population size, mutation probability, iterations, message to find
    if len(sys.argv) != 5:
        print(sys.argv)
        raise ValueError('Invalid argument number')
    population_size = test_arg_validity(sys.argv[1], int, is_even)
    mutation_probability = test_arg_validity(sys.argv[2], float, lambda x: is_in_range(x, 0, 1))
    iterations = test_arg_validity(sys.argv[3], int, is_positive)
    message_to_find = test_arg_validity(sys.argv[4], str, is_letters)
    crossover_rate = 0  # To change
    problem = SecretMessageProblem(message_to_find)
    solver = AlgoGen(problem, population_size, mutation_probability, crossover_rate)
    best = solver.solve(iterations)
    print('Closest message found: {}, fitness = {}'.format(*best[1:]))
