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


def test_arg_validity(x, desired_type, condition_test=lambda x: None):
    """
    Tries to convert given variable to desired_type
    Will also check if the variable respects given condition_test function (after conversion)
    :type x: any, will be used for str
    :type desired_type: type
    :type condition_test: function of shape [desired_type] -> None
    :rtype: desired_type
    :UC: isinstance(desired_type, type)
    """
    try:
        x = desired_type(x)
    except ValueError:
        raise TypeError('Given argument {} should be of type {}'.format(x, desired_type))
    condition_test(x)
    return x


def is_even(x):
    """
    Tests if x is even
    :type x: int
    :rtype: boolean
    :UC: none
    """
    if not x % 2 == 0:
        raise ValueError('{} should be even'.format(x))


def is_in_range(x, x_min, x_max):
    """
    Tests if x_min <= x <= x_max
    :type x: int
    :type x_min: int
    :type x_max: int
    :rtype: boolean
    :UC: x_min < x_max
    """
    if not x_min <= x <= x_max:
        raise ValueError('{} should be greater than {} and smaller than {}'.format(x, x_min, x_max))


def is_positive(x):
    """
    Tests if x is positive
    :type x: int or float
    :rtype: boolean
    :UC: none
    """
    if x <= 0:
        raise ValueError('{} should be positive'.format(x))


def is_greater(x, y):
    """
    Tests if x is greater than y
    :type x: int
    :type y: int
    :rtype: boolean
    :UC: none
    """
    if x <= y:
        raise ValueError('{} should be greater than {}'.format(x, y))


def is_letters(x):
    """
    Tests if all characters in x are letters or space
    :type x: str
    :rtype: boolean
    :UC: none
    """
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [' ']
    if not all([c in letters for c in x]):
        raise ValueError('Message contains invalid characters')
