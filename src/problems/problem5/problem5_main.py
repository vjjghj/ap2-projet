import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
from input_checker import *
from problems.problem5.problem5_classes import TravellingSalesmanProblem
from algo_gen import AlgoGen


if __name__ == '__main__':
    # Population size, mutation probability, iterations, maze number
    population_size, mutation_probability, iterations, crossover_iterations, export = base_args(sys.argv, 5)
    graph_number = test_arg_validity(sys.argv[4], int)
    problem = TravellingSalesmanProblem(graph_file=parentdir +
                                                   '\problems\problem5\graphs\graph_file_{}.txt'.format(graph_number))
    solver = AlgoGen(problem=problem, population_size=population_size, mutation_probability=mutation_probability,
                     crossover_iterations=crossover_iterations, export=export)
    best = solver.solve(iterations)
    print('Best path found: {}, value: {}'.format(*best[1:]))
