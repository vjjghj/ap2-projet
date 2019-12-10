from problem_interface import Problem
from individual_interface import Individual
from problems.problem5.map import TspGraph
from random import shuffle, choices, random


class TravellingSalesmanProblem(Problem):
    """
    In this problem we want to find the shortest way passing by all points through a graph
    """
    def __init__(self, **kwargs):
        """
        Creates the problem with a graph imported from given file
        :type graph_file: str
        """
        self.__graph = TspGraph(kwargs['graph_file'])
        super(TravellingSalesmanProblem, self).__init__(maximize=False, **kwargs)

    def create_individual(self):
        """
        Creates individual with genome equal to the number of towns to visit
        :rtype: Individual
        """
        n = self.__graph.get_length() - 1
        return TravellingSalesmanIndividual(n, n)

    def evaluate_fitness(self, individual):
        """
        Returns the length of the pass through all cities
        :type individual: Individual
        :rtype: int
        :UC: none
        """
        return self.__graph.cross(individual.get_value())

    def adapt(self, individual):
        """
        Returns the message corresponding to individual's genome
        :type individual: Individual
        :rtype: str
        :UC: none
        """
        return '0' + str(individual)


class TravellingSalesmanIndividual(Individual):
    """
    Individual with a list of ints as number
    """
    def __init__(self, max_value, *args):
        self.__max_value = max_value
        super(TravellingSalesmanIndividual, self).__init__(*args)

    def init_value(self):
        """
        Returns a shuffled list of ints to be the individual's genome
        :rtype: list(int)
        """
        x = list(range(1, self.__max_value + 1))
        shuffle(x)
        return x

    def mutate(self, probability):
        """
        As mutation in this problem we will swap two genes
        This way all individuals will stay solutions to the problem
        :type probability: float
        :return: none
        """
        genome = self.get_value()
        number_of_mutations = sum([1 for _ in range(self.get_size()) if probability > random()])
        indexes = choices(range(self.get_size()), k=number_of_mutations)
        values = [genome[i] for i in indexes]
        shuffle(indexes)
        for i in indexes:
            genome[i] = values.pop()
        self.set_value(genome)
