from problem_interface import Problem
from individual_interface import Individual
from random import choice, random
from problems.problem4.haunted_field import PlayerState, HauntedField, CELLS


class HauntedFieldProblem(Problem):
    def __init__(self, height, width):
        self.haunted_field = HauntedField(height, width)
        super(HauntedFieldProblem, self).__init__(True)

    def create_individual(self):
        """
        Creates individual with genome length 243 = 3^5
        :rtype: Individual
        """
        return HauntedFieldIndividual(243)

    def evaluate_fitness(self, individual):
        line, used = self.haunted_field.cross(individual)
        score = used + line * self.haunted_field.get_height()
        state = individual.get_state()
        if state == PlayerState.succes:
            score += (self.haunted_field.get_width() * self.haunted_field.get_height() - used) * 10
        elif state == PlayerState.blocked:
            score += (self.haunted_field.get_height() - line) * 2
        elif state == PlayerState.monster:
            score += (self.haunted_field.get_height() - line) * 20
        return score

    def adapt(self, individual):
        """
        Considering we cant print the field and the path of individual based on the commands on each iteration,
            adapt will only return the genome of individual as a str
        :type individual: Individual
        :rtype: str
        """
        return str(individual)


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
