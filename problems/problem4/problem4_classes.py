from problem_interface import Problem
from individual_interface import Individual
from random import choice, random
from problems.problem4.haunted_field import HauntedField, CELLS


class HauntedFieldProblem(Problem):
    def __init__(self):
        super(HauntedFieldProblem, self).__init__(False)

    def create_individual(self):
        """
        Creates individual with genome length 243
        :rtype: Individual
        """
        return HauntedFieldIndividual(243)

    def evaluate_fitness(self, individual):
        pass

    def adapt(self, individual):
        pass


class HauntedFieldIndividual(Individual):
    """
    Individuals with list of directions as genome
    """
    @staticmethod
    def get_random_gene():
        """
        Returns a random valid direction
        :rtype: str
        """
        return choice(CELLS)

    @staticmethod
    def mutate_once(gene, probability):
        """
        Applies mutation with given probability to a gene
        If it mutates, the gene takes the value of a random different valid direction
        :type gene: str
        :type probability: int or float
        :rtype: str
        """
        if probability <= random():
            new_gene = gene
            while gene == new_gene:
                new_gene = HauntedFieldIndividual.get_random_gene()
            return new_gene
        return gene
