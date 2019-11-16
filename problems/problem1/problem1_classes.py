from problem_interface import Problem
from individual_interface import Individual
from math import sin, cos
from random import randint, random


def f(x):
    """
    This is the function we want to find the max
    :type x: int or float
    :rtype: float
    :UC: none
    """
    return x * x * sin(x) * cos(x)


class MaxFunctionProblem(Problem):
    def __init__(self, x_min, x_max, bit_length, fx = f):
        self.f = fx
        self.x_min = x_min
        self.x_max = x_max
        self.bit_length = bit_length
        self.biggest_int_value = 2 ** bit_length - 1

    def create_individual(self):
        return MaxFunctionIndividual(self.bit_length)

    def adapt(self, individual):
        n = int(str(individual), 2)
        int_range = (self.x_max - self.x_min) / self.biggest_int_value
        return self.x_min + n * int_range

    def evaluate_fitness(self, individual):
        return f(self.adapt(individual))


class MaxFunctionIndividual(Individual):
    def get_random_gene(self):
        """
        Randomly returns 0 or 1
        :rtype: int
        """
        return randint(0, 1)

    @staticmethod
    def mutate_once(gene, probability):
        return gene if probability > random() else 1 - gene

    def evaluate(self, problem):
        self.score = problem.evaluate_fitness(self.genome)
