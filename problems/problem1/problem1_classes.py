from problem_interface import Problem
from individual_interface import Individual
from math import sin, cos
from random import randint


def f(x):
    """
    This is the function we want to find the max
    :type x: int or float
    :rtype: float
    :UC: none
    """
    return x * x * sin(x) * cos(x)


class MaxFunctionProblem(Problem):
    """
    In this problem we want to find the value maximizing a given function
    We work in a given interval
    Individual's genome will be a list of bits, representing a floating value in the interval
    """
    def __init__(self, **kwargs):
        """
        Creates a problem where the goal is to find the maximum of a function in a given interval
        Uses individual with bit genes, with bit_length genes
        :type x_min: int or float
        :type x_max: int or float
        :type bit_length: int
        :type fx: function
        :UC: x_min < x_max and bit_length > 0
        """
        self.__f = kwargs.get('f', f)
        self.__x_min = kwargs['x_min']
        self.__x_max = kwargs['x_max']
        self.__bit_length = kwargs['bit_length']
        self.__biggest_int_value = 2 ** self.__bit_length - 1
        super(MaxFunctionProblem, self).__init__(maximize=True, ** kwargs)
        # By changing True by False we can aim for the minimum of the function

    def create_individual(self):
        """
        Creates an individual with genome length equals to bit_length
        :rtype: Individual
        """
        return MaxFunctionIndividual(self.__bit_length)

    def adapt(self, individual):
        """
        Returns the value corresponding to the individual genome in the problem
        Depends on x_min, x_max and bit_length
        :type individual: Individual
        :rtype: float
        """
        n = int(str(individual), 2)  # reminder: Individual.__str__() returns the genome as a string
        int_range = (self.__x_max - self.__x_min) / self.__biggest_int_value
        return self.__x_min + n * int_range

    def evaluate_fitness(self, individual):
        """
        The fitness of the individual is given by the function we want to maximize
        :type individual: Individual
        :rtype: float
        """
        return self.__f(self.adapt(individual))


class MaxFunctionIndividual(Individual):
    """
    Individuals with a list of bits as genome
    """
    @staticmethod
    def get_random_gene():
        """
        Returns a random bit value
        :rtype: int
        """
        return randint(0, 1)

    @staticmethod
    def mutate_once(gene):
        """
        Flips the bit value
        :type gene: int
        :rtype: int
        :UC: gene in {0, 1}
        """
        return 1 - gene
