from problem_interface import Problem
from individual_interface import Individual
from problems.problem5.map import TspGraph
from random import randint


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
        super(TravellingSalesmanProblem, self).__init__(maximize=False, **kwargs)

    def create_individual(self):
        """
        Creates individual with genome equal to the length of the secret message
        :rtype: Individual
        """
        pass

    def evaluate_fitness(self, individual):
        """
        Returns the divergence of individual from secret message
        :type individual: Individual
        :rtype: int
        :UC: none
        """
        pass

    def adapt(self, individual):
        """
        Returns the message corresponding to individual's genome
        :type individual: Individual
        :rtype: str
        :UC: none
        """
        pass


class TravellingSalesmanIndividual(Individual):
    """
    Individual with a list of letters as genome
    """
    @staticmethod
    def get_random_gene():
        """
        Returns a random letter from valid choices
        As we need to find an individual's score more often than printing the corresponding message,
        Using the letters' index as genes will gain us computations
        :rtype: str
        :UC: none
        """
        pass

    @staticmethod
    def mutate_once(gene):
        """
        The gene takes the value of a random different valid letter
        :type gene: str
        :rtype: str
        :UC: none
        """
        pass