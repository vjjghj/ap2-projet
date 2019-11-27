import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
from input_checker import *
from problems.problem3.problem3_classes import LabyrinthProblem
from algo_gen import AlgoGen


if __name__ == '__main__':
    # Population size, mutation probability, iterations, maze file path
    if len(sys.argv) != 5:
        raise ValueError('Invalid argument number')
    population_size = test_arg_validity(sys.argv[1], int, is_even)
    mutation_probability = test_arg_validity(sys.argv[2], float, lambda x: is_in_range(x, 0, 1))
    iterations = test_arg_validity(sys.argv[3], int, is_positive)
    maze_file = test_arg_validity(sys.argv[4], str)  # Actually useless, only use for coherence
    problem = LabyrinthProblem(maze_file=maze_file)
    solver = AlgoGen(problem=problem, population_size=population_size, mutation_probability=mutation_probability)
    best = solver.solve(iterations)
    print('Best path found: {}, value: {}'.format(*best[1:]))
    problem.get_maze().draw_path(best[0])
