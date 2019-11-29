import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
from base_main import base_args
from input_checker import *
from problems.problem2.problem2_classes import SecretMessageProblem
from algo_gen import AlgoGen

if __name__ == '__main__':
    # Population size, mutation probability, iterations, message to find
    population_size, mutation_probability, iterations, crossover_iterations = base_args(sys.argv, 5)
    message_to_find = test_arg_validity(sys.argv[4], str, is_letters)
    problem = SecretMessageProblem(message_to_find=message_to_find)
    solver = AlgoGen(problem=problem, population_size=population_size, mutation_probability=mutation_probability,
                     crossover_iterations=crossover_iterations)
    best = solver.solve(iterations)
    print('Closest message found: {}, fitness = {}'.format(*best[1:]))
