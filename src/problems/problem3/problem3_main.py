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
    # Population size, mutation probability, iterations, maze number
    population_size, mutation_probability, iterations, crossover_iterations, export = base_args(sys.argv, 5)
    maze_number = test_arg_validity(sys.argv[4], int, lambda x: is_in_range(x, 0, 4))
    problem = LabyrinthProblem(maze_file=parentdir + '\\problems\\problem3\\mazes\\maze{}.txt'.format(maze_number))
    solver = AlgoGen(problem=problem, population_size=population_size, mutation_probability=mutation_probability,
                     crossover_iterations=crossover_iterations, export=export)
    best = solver.solve(iterations)
    print('Best path found: {}, value: {}'.format(*best[1:]))
    print(problem.get_maze().path_str(best[0]))
