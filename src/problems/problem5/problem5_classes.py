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
        Creates the problem with a given secret message
        :type message_to_find: str
        :UC: all([x in LETTERS for x in message_to_find])
        """
        self.__graph = TspGraph(kwargs['graph_file'])
        super(TravellingSalesmanProblem, self).__init__(maximize=False, **kwargs)

    def create_individual(self):
        """
        Creates individual with genome equal to the length of the secret message
        :rtype: Individual
        """
        n = self.__graph.get_length() - 1
        return TravellingSalesmanIndividual(n, n)

    def evaluate_fitness(self, individual):
        """
        Returns the divergence of individual from secret message
        :type individual: Individual
        :rtype: int
        :UC: none
        """
        result = self.__graph.cross(individual.get_value())
        return result[1] + 1000 * (1 - result[0])

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
    Individual with a list of letters as genome
    """
    def __init__(self, max_value, *args):
        self.__max_value = max_value
        super(TravellingSalesmanIndividual, self).__init__(*args)

    def init_value(self):
        x = list(range(1, self.__max_value + 1))
        shuffle(x)
        return x

    def mutate(self, probability):
        genome = self.get_value()
        number_of_mutations = sum([1 for _ in range(self.get_size()) if probability > random()])
        indexes = choices(range(self.get_size()), k=number_of_mutations)
        values = [genome[i] for i in indexes]
        shuffle(indexes)
        for i in indexes:
            genome[i] = values.pop()
        self.set_value(genome)
