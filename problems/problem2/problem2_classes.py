from problem_interface import Problem
from individual_interface import Individual
from random import choice, random


LETTERS = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [' ']


class SecretMessageProblem(Problem):
    """
    In this problem we want to find a given secret message
    """
    def __init__(self, message_to_find):
        """
        Creates the problem with a given secret message
        :type message_to_find: str
        :UC: all([x in LETTERS for x in message_to_find])
        """
        self.message_to_find = list(map(lambda x: LETTERS.index(x), list(message_to_find)))
        self.message_length = len(message_to_find)
        super(SecretMessageProblem, self).__init__(maximize=False)

    def create_individual(self):
        """
        Creates individual with genome equal to the length of the secret message
        :rtype: Individual
        """
        return SecretMessageIndividual(self.message_length)

    def evaluate_fitness(self, individual):
        """
        Returns the divergence of individual from secret message
        :type individual: Individual
        :rtype: int
        """
        return sum([abs(i - LETTERS.index(c)) for i, c in zip(self.message_to_find, individual.get_value())])

    def adapt(self, individual):
        """
        Returns the message corresponding to individual's genome
        :type individual: Individual
        :rtype: str
        """
        return ''.join(individual.get_value())


class SecretMessageIndividual(Individual):
    """
    Individual with a list of letters as genome
    """
    @staticmethod
    def get_random_gene():
        """
        Returns a random letter from valid choices
        :rtype: str
        """
        return choice(LETTERS)

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
