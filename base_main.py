from input_checker import *


def base_args(argv, nb_args):
    crossover_iterations = 1
    if len(argv) != nb_args:
        if len(argv) == nb_args + 1:
            crossover_iterations = test_arg_validity(argv[-1], int, is_positive)
        else:
            raise ValueError('Invalid argument number')
    population_size = test_arg_validity(argv[1], int, is_even)
    mutation_probability = test_arg_validity(argv[2], float, lambda x: is_in_range(x, 0, 1))
    iterations = test_arg_validity(argv[3], int, is_positive)
    return population_size, mutation_probability, iterations, crossover_iterations
