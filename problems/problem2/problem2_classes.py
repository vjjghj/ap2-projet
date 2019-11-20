from problem_interface import Problem
from individual_interface import Individual
from random import randint, random


LETTERS = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [' ']


class SecretMessageProblem(Problem):
    """
    In this problem we want to find a given secret message
    """
    def __init__(self, **kwargs):
        """
        Creates the problem with a given secret message
        :type message_to_find: str
        :UC: all([x in LETTERS for x in message_to_find])
        """
        self.__message_to_find = list(map(lambda x: LETTERS.index(x), list(kwargs['message_to_find'])))
        # We don't need to store the message value, we only keep the corresponding genome
        self.__message_length = len(kwargs['message_to_find'])
        super(SecretMessageProblem, self).__init__(maximize=False, **kwargs)

    def create_individual(self):
        """
        Creates individual with genome equal to the length of the secret message
        :rtype: Individual
        """
        return SecretMessageIndividual(self.__message_length)

    def evaluate_fitness(self, individual):
        """
        Returns the divergence of individual from secret message
        :type individual: Individual
        :rtype: int
        """
        return sum([abs(i - j) for i, j in zip(self.__message_to_find, individual.get_value())])

    def adapt(self, individual):
        """
        Returns the message corresponding to individual's genome
        :type individual: Individual
        :rtype: str
        """
        return ''.join([LETTERS[i] for i in individual.get_value()])


class SecretMessageIndividual(Individual):
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
        """
        return randint(0, 26)

    @staticmethod
    def mutate_once(gene, probability):
        """
        Applies mutation with given probability to a gene
        If it mutates, the gene takes the value of a random different valid letter
        :type gene: str
        :type probability: int or float
        :rtype: str
        """
        if probability > random():
            new_gene = gene
            while gene == new_gene:
                new_gene = SecretMessageIndividual.get_random_gene()
            return new_gene
        return gene
