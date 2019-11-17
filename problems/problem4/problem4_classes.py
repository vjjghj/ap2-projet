from problem_interface import Problem
from individual_interface import Individual
from random import choice, random
from problems.problem4.haunted_field import HauntedField, CELLS
from enum import Enum


class PlayerState(Enum):
    """
    This is used to define the possibles states of an individual through the haunted field
    An individual has five types of value:

    * ``active``
    * ``success``
    * ``monster``
    * ``blocked``
    * ``alive``
    """
    active = 1
    success = 2
    monster = 3
    blocked = 4
    alive = 5


class HauntedFieldProblem(Problem):
    def __init__(self, height, width):
        self.haunted_field = HauntedField(height, width)
        super(HauntedFieldProblem, self).__init__(True)

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
    def __init__(self, *args, **kwargs):
        """
        Creates an individual to solve the haunted field problem
        """
        self.state = PlayerState.active
        super(HauntedFieldIndividual, self).__init__(*args, **kwargs)

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
        if probability > random():
            new_gene = gene
            while gene == new_gene:
                new_gene = HauntedFieldIndividual.get_random_gene()
            return new_gene
        return gene

    def get_state(self):
        return self.state

    def is_success(self):
        self.state = PlayerState.success

    def is_monster(self):
        self.state = PlayerState.monster

    def is_blocked(self):
        self.state = PlayerState.blocked

    def is_alive(self):
        self.state = PlayerState.alive
